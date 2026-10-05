import os
import shutil
import tempfile
from typing import Optional, Dict, Any, List
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel, field_validator

from database import (
    ingest_into_knowledge_base,
    search_knowledge_base,
    add_knowledge_fact,
    get_knowledge_facts,
    get_mongo_db,
    add_to_task_log
)
from src.core.memory_consolidation import ConsolidationRequest


router = APIRouter(tags=["rag"])

class IngestRequest(BaseModel):
    source: str
    text: str
    metadata: Optional[Dict[str, Any]] = None

class IngestFileRequest(BaseModel):
    file_path: str

class IngestFilesRequest(BaseModel):
    file_paths: List[str]
    
    @field_validator('file_paths')
    @classmethod
    def file_paths_must_not_be_empty(cls, v):
        if not v or len(v) == 0:
            raise ValueError('At least one file path must be provided')
        return v

class SearchRequest(BaseModel):
    query: str
    limit: Optional[int] = 2

class FactRequest(BaseModel):
    entity: str
    relation: str
    target: str

class MemoryUpdateReq(BaseModel):
    id: str
    new_value: Any

class MemoryForgetReq(BaseModel):
    entity_id: str

@router.post("/api/rag/ingest")
def rag_ingest(request: IngestRequest):
    try:
        ingest_into_knowledge_base(request.source, request.text, request.metadata or {})
        add_to_task_log("ingest_file", 1, "success")
        return {"status": "success", "message": f"Successfully ingested '{request.source}' into Turbovec RAG."}
    except Exception as e:
        add_to_task_log("ingest_file", 1, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/rag/ingest-file")
def rag_ingest_file(request: IngestFileRequest):
    try:
        from database import extract_text_from_file
        abs_path = os.path.abspath(request.file_path)
        if not os.path.exists(abs_path):
            raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")
            
        text = extract_text_from_file(abs_path)
        if not text or not text.strip():
            raise ValueError("No extractable text content found. The file may be empty, scanned, or password-protected.")
        ingest_into_knowledge_base(os.path.basename(abs_path), text)
        add_to_task_log("ingest_file", 1, "success")
        return {"status": "success", "message": f"Successfully parsed and ingested '{os.path.basename(abs_path)}' into Turbovec RAG."}
    except Exception as e:
        add_to_task_log("ingest_file", 1, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/rag/ingest-files")
def rag_ingest_files(request: IngestFilesRequest):
    """Batch ingest multiple files into the knowledge base."""
    try:
        from database import extract_text_from_file
        
        results = []
        failed_files = []
        
        for file_path in request.file_paths:
            try:
                abs_path = os.path.abspath(file_path)
                if not os.path.exists(abs_path):
                    failed_files.append({
                        "file": file_path,
                        "error": "File not found"
                    })
                    continue
                    
                text = extract_text_from_file(abs_path)
                if not text or not text.strip():
                    failed_files.append({
                        "file": file_path,
                        "error": "No extractable text content found"
                    })
                    continue
                
                ingest_into_knowledge_base(os.path.basename(abs_path), text)
                add_to_task_log("ingest_file", 1, "success")
                results.append({
                    "file": file_path,
                    "status": "success",
                    "message": f"Successfully parsed and ingested '{os.path.basename(abs_path)}'"
                })
            except Exception as e:
                failed_files.append({
                    "file": file_path,
                    "error": str(e)
                })
                add_to_task_log("ingest_file", 1, "failed", str(e))
        
        return {
            "status": "partial_success" if failed_files else "success",
            "results": results,
            "failed_files": failed_files,
            "summary": {
                "total": len(request.file_paths),
                "successful": len(results),
                "failed": len(failed_files)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/rag/ingest-file-upload")
async def rag_ingest_file_upload(file: UploadFile = File(...)):
    try:
        from database import extract_text_from_file
        
        fname = file.filename or "uploaded_file"
        await file.seek(0)
        suffix = os.path.splitext(fname)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
            
        try:
            text = extract_text_from_file(tmp_path)
            if not text or not text.strip():
                raise ValueError("No extractable text content found. The file may be empty, scanned, or password-protected.")
            ingest_into_knowledge_base(fname, text)
            add_to_task_log("ingest_file", 1, "success")
            return {"status": "success", "filename": fname, "name": fname, "message": f"Successfully parsed and ingested '{fname}' into Turbovec RAG."}
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    except Exception as e:
        add_to_task_log("ingest_file", 1, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/rag/search")
def rag_search(request: SearchRequest):
    try:
        results = search_knowledge_base(request.query, request.limit or 2)
        add_to_task_log("search_knowledge", 0, "success")
        return {"results": results}
    except Exception as e:
        add_to_task_log("search_knowledge", 0, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/facts/add")
def facts_add(request: FactRequest):
    try:
        add_knowledge_fact(request.entity, request.relation, request.target)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/facts/get")
def facts_get(entity: str):
    try:
        facts = get_knowledge_facts(entity)
        return {"entity": entity, "facts": facts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/graph/all")
def graph_all():
    db_conn = get_mongo_db()
    nodes = []
    edges = []
    if db_conn is not None:
        try:
            node_map = {}
            entities_col = db_conn["entities"]
            relationships_col = db_conn["relationships"]
            
            for ent in entities_col.find({}, {"_id": 0}):
                name = ent.get("name")
                if name:
                    node_map[name] = {
                        "id": name,
                        "label": name,
                        "type": ent.get("type", "entity")
                    }
                    
            for rel in relationships_col.find({}, {"_id": 0}):
                src = rel.get("source")
                tgt = rel.get("target")
                if src and tgt:
                    if src not in node_map:
                        node_map[src] = {"id": src, "label": src, "type": "entity"}
                    if tgt not in node_map:
                        node_map[tgt] = {"id": tgt, "label": tgt, "type": "entity"}
                    edges.append({
                        "source": src,
                        "target": tgt,
                        "relation": rel.get("relation", "connected_to")
                    })
            nodes = list(node_map.values())
        except Exception as e:
            print("Failed to query full graph:", e)
    return {"nodes": nodes, "edges": edges}

@router.get("/api/codebase/graph")
def get_codebase_graph():
    try:
        from src.core.code_graph import get_codebase_graph_json
        return get_codebase_graph_json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/docs/search")
def search_docs(query: str, limit: int = 5):
    try:
        from src.core.doc_indexer import search_offline_docs
        results = search_offline_docs(query, limit)
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/kg/graph")
def api_kg_graph():
    db = get_mongo_db()
    if db is None:
        raise HTTPException(status_code=503, detail="MongoDB is offline.")
        
    try:
        entities_col = db["entities"]
        entities = list(entities_col.find({}, {"_id": 0}))
        
        relations_col = db["relations"]
        relations = list(relations_col.find({}, {"_id": 0}))
        
        facts_col = db["facts"]
        facts = list(facts_col.find({}, {"_id": 0}))
        
        nodes = []
        links = []
        node_ids = set()
        
        for e in entities:
            name = e.get("name")
            if name and name not in node_ids:
                nodes.append({
                    "id": name,
                    "label": name,
                    "type": e.get("type", "concept"),
                    "attributes": e.get("attributes", {})
                })
                node_ids.add(name)
                
        for r in relations:
            source = r.get("from_entity") or r.get("source")
            target = r.get("to_entity") or r.get("target")
            rel = r.get("relation")
            if source and target:
                links.append({
                    "source": source,
                    "target": target,
                    "relation": rel or "related_to"
                })
                for node_name in [source, target]:
                    if node_name not in node_ids:
                        nodes.append({"id": node_name, "label": node_name, "type": "concept"})
                        node_ids.add(node_name)
                        
        for f in facts:
            source = f.get("subject")
            target = f.get("object")
            rel = f.get("predicate")
            if source and target:
                links.append({
                    "source": source,
                    "target": target,
                    "relation": rel or "has_fact"
                })
                for node_name in [source, target]:
                    if node_name not in node_ids:
                        nodes.append({"id": node_name, "label": node_name, "type": "concept"})
                        node_ids.add(node_name)
                        
        return {"status": "success", "nodes": nodes, "links": links}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/neural-rag/intent-graph")
async def get_neural_rag_intent_graph_api():
    """JARVIS-09: Subconscious Codebase Memory & Neural RAG Intent Knowledge Graph."""
    from src.core.neural_rag import get_neural_rag_synthesizer
    synth = get_neural_rag_synthesizer()
    graph = synth.get_intent_graph()
    return {"status": "success", "intent_graph": graph}

@router.get("/api/memory/list")
def list_memories_api(query: Optional[str] = None, category: Optional[str] = None):
    """TRUST-01: Fetch all agent memory entries with optional query/category filter."""
    from src.core.memory_editor import MemoryEditor
    editor = MemoryEditor()
    memories = editor.get_all_memories(query=query, category=category)
    return {"status": "success", "count": len(memories), "memories": memories}

@router.post("/api/memory/update")
def update_memory_api(req: MemoryUpdateReq):
    """TRUST-01: Update specific memory entry or preference value."""
    from src.core.memory_editor import MemoryEditor
    editor = MemoryEditor()
    success = editor.update_memory_entry(req.id, req.new_value)
    return {"status": "success" if success else "error", "updated": success}

@router.post("/api/memory/forget")
def forget_memory_api(req: MemoryForgetReq):
    """TRUST-01: Forget all memory records associated with entity_id."""
    from src.core.memory_editor import MemoryEditor
    editor = MemoryEditor()
    count = editor.forget_entity(req.entity_id)
    return {"status": "success", "forgotten_count": count}

@router.get("/api/memory/export")
def export_memory_api():
    """TRUST-01: Export JSON bundle of all agent memories, preferences, and graphs."""
    from src.core.memory_editor import MemoryEditor
    editor = MemoryEditor()
    return editor.export_memory_json()

class SummarizeRequest(BaseModel):
    messages: List[Dict[str, Any]] = []

@router.post("/api/memory/summarize")
async def summarize_conversation(payload: SummarizeRequest):
    """Summarize messages into key topics, decisions, and user facts."""
    from src.core.memory_consolidation import memory_consolidation_engine
    return memory_consolidation_engine.summarize_messages(payload.messages)

@router.post("/api/memory/consolidate")
async def consolidate_memory(payload: ConsolidationRequest):
    """Consolidate conversation session into long-term semantic memory graph."""
    from src.core.memory_consolidation import memory_consolidation_engine
    from src.core.agent_status_stream import agent_status_stream_manager
    result = await memory_consolidation_engine.consolidate(payload)
    agent_status_stream_manager.broadcast_event(
        status="idle",
        message=f"Consolidated memory: extracted {len(result.extracted_nodes)} memory nodes.",
        details={"nodes_count": len(result.extracted_nodes)}
    )
    return result


@router.get("/api/memory/consolidation-status")
async def get_consolidation_status():
    """Get status metrics for memory consolidation runs."""
    from src.core.memory_consolidation import memory_consolidation_engine
    return memory_consolidation_engine.get_status()
