import time
from typing import List, Dict, Any, Optional
from database import get_mongo_db

def kg_add_entity(name: str, type: str, attributes: Dict[str, Any] = None) -> str:
    """Upsert an entity node into the MongoDB knowledge graph."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Fact could not be stored."
        
    try:
        col = db["entities"]
        now = time.time()
        col.update_one(
            {"name": name},
            {
                "$set": {
                    "type": type,
                    "attributes": attributes or {},
                    "last_seen": now
                },
                "$setOnInsert": {
                    "first_seen": now,
                    "aliases": [],
                    "source": "react_agent"
                }
            },
            upsert=True
        )
        return f"Successfully upserted entity node '{name}' of type '{type}'."
    except Exception as e:
        return f"Error adding entity: {e}"

def kg_add_relation(from_entity: str, to_entity: str, relation: str, evidence: str = "") -> str:
    """Add a directed relationship edge between two entities with supporting evidence."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Relation could not be stored."
        
    try:
        # Check or create from_entity and to_entity nodes
        col_entities = db["entities"]
        from_node = col_entities.find_one({"name": from_entity})
        if not from_node:
            kg_add_entity(from_entity, "concept")
            from_node = col_entities.find_one({"name": from_entity})
            
        to_node = col_entities.find_one({"name": to_entity})
        if not to_node:
            kg_add_entity(to_entity, "concept")
            to_node = col_entities.find_one({"name": to_entity})
            
        col_rel = db["relationships"]
        col_rel.update_one(
            {
                "from_id": str(from_node["_id"]),
                "to_id": str(to_node["_id"]),
                "relation": relation
            },
            {
                "$set": {
                    "from_name": from_entity,
                    "to_name": to_entity,
                    "strength": 1.0,
                    "created_at": time.time(),
                    "evidence_text": evidence
                }
            },
            upsert=True
        )
        return f"Successfully added relation '{from_entity} --({relation})--> {to_entity}'."
    except Exception as e:
        return f"Error adding relation: {e}"

def kg_query(entity_name: str) -> str:
    """Fetch an entity node and all its connected relationships in the graph."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col_entities = db["entities"]
        node = col_entities.find_one({"name": entity_name})
        if not node:
            return f"Entity '{entity_name}' not found in graph."
            
        node_id = str(node["_id"])
        col_rel = db["relationships"]
        
        # Outgoing
        outgoing = list(col_rel.find({"from_id": node_id}))
        # Incoming
        incoming = list(col_rel.find({"to_id": node_id}))
        
        lines = [f"Entity: {node['name']} (Type: {node['type']})"]
        if node.get("attributes"):
            lines.append("Attributes:")
            for k, v in node["attributes"].items():
                lines.append(f"  {k}: {v}")
                
        if outgoing:
            lines.append("\nOutgoing Relationships:")
            for r in outgoing:
                lines.append(f"  --({r['relation']})--> {r['to_name']} (evidence: {r.get('evidence_text','')})")
                
        if incoming:
            lines.append("\nIncoming Relationships:")
            for r in incoming:
                lines.append(f"  {r['from_name']} --({r['relation']})--> (evidence: {r.get('evidence_text','')})")
                
        return "\n".join(lines)
    except Exception as e:
        return f"Error querying graph: {e}"

def kg_search(query_text: str) -> str:
    """Search for matching entities and facts by keyword."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col_entities = db["entities"]
        col_facts = db["facts"]
        
        entities = list(col_entities.find({"name": {"$regex": query_text, "$options": "i"}}).limit(10))
        facts = list(col_facts.find({
            "$or": [
                {"subject": {"$regex": query_text, "$options": "i"}},
                {"predicate": {"$regex": query_text, "$options": "i"}},
                {"object": {"$regex": query_text, "$options": "i"}}
            ]
        }).limit(10))
        
        lines = []
        if entities:
            lines.append("Matching Entities:")
            for e in entities:
                lines.append(f"- Name: {e['name']} (Type: {e['type']})")
        if facts:
            lines.append("\nMatching Facts:")
            for f in facts:
                lines.append(f"- Fact: {f['subject']} --({f['predicate']})--> {f['object']}")
                
        if not lines:
            return f"No entities or facts matching '{query_text}' found."
            
        return "\n".join(lines)
    except Exception as e:
        return f"Error searching graph: {e}"

def kg_add_fact(subject: str, predicate: str, object: str) -> str:
    """Store an atomic subject-predicate-object fact in the knowledge graph."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["facts"]
        col.update_one(
            {"subject": subject, "predicate": predicate, "object": object},
            {
                "$set": {
                    "confidence": 1.0,
                    "created_at": time.time(),
                    "last_confirmed": time.time()
                }
            },
            upsert=True
        )
        return f"Successfully saved atomic fact: '{subject} {predicate} {object}'"
    except Exception as e:
        return f"Error adding fact: {e}"

def kg_get_facts(subject: str) -> str:
    """Retrieve all atomic facts about a given subject."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["facts"]
        facts = list(col.find({"subject": subject}, {"_id": 0}))
        if not facts:
            return f"No facts found for subject '{subject}'."
        return "\n".join(f"- {f['subject']} {f['predicate']} {f['object']}" for f in facts)
    except Exception as e:
        return f"Error getting facts: {e}"

def kg_traverse(start: str, depth: int = 2) -> str:
    """Perform a multi-hop graph walk starting from a given entity name."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col_entities = db["entities"]
        col_rel = db["relationships"]
        
        start_node = col_entities.find_one({"name": start})
        if not start_node:
            return f"Starting entity '{start}' not found in graph."
            
        visited = set()
        queue = [(str(start_node["_id"]), start, 0)]
        path_lines = []
        
        while queue:
            node_id, name, current_depth = queue.pop(0)
            if node_id in visited or current_depth > depth:
                continue
            visited.add(node_id)
            
            # Find neighbors
            outgoing = list(col_rel.find({"from_id": node_id}))
            for r in outgoing:
                to_node = col_entities.find_one({"name": r["to_name"]})
                if to_node:
                    to_id = str(to_node["_id"])
                    indent = "  " * current_depth
                    path_lines.append(f"{indent}{name} --({r['relation']})--> {r['to_name']}")
                    if to_id not in visited:
                        queue.append((to_id, r["to_name"], current_depth + 1))
                        
        if not path_lines:
            return f"No relations traversed from '{start}' within depth {depth}."
        return f"Traversal Path from '{start}':\n" + "\n".join(path_lines)
    except Exception as e:
        return f"Error traversing graph: {e}"

def suggest_cross_project_patterns(query: str) -> str:
    """Queries cross-project tech stacks and architectures to find and suggest similar design patterns (e.g. sharing API models, Tauri setups, etc.)."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col_facts = db["facts"]
        matching_facts = list(col_facts.find({
            "object": {"$regex": query, "$options": "i"},
            "predicate": {"$in": ["uses_framework", "uses_language", "uses_database"]}
        }))
        
        if not matching_facts:
            return f"No cross-project pattern matches found for tech stack: '{query}'."
            
        projects_grouped = {}
        for f in matching_facts:
            proj = f["subject"]
            pred = f["predicate"]
            tech = f["object"]
            if proj not in projects_grouped:
                projects_grouped[proj] = []
            projects_grouped[proj].append(f"{pred.replace('uses_', '')}: {tech}")
            
        result_lines = [f"Found {len(matching_facts)} patterns matching: '{query}':"]
        for proj, techs in projects_grouped.items():
            all_facts = list(col_facts.find({"subject": proj}))
            all_tech = []
            for f in all_facts:
                if f["predicate"] in ["uses_framework", "uses_language", "uses_database"]:
                    all_tech.append(f["object"])
            
            result_lines.append(f"\n- Project: {proj}")
            result_lines.append(f"  Matches search: {', '.join(techs)}")
            result_lines.append(f"  Full stack details: {', '.join(all_tech)}")
            
        if len(projects_grouped) > 1:
            projs = list(projects_grouped.keys())
            result_lines.append(f"\n💡 Reuse Suggestion: Both {', '.join(projs)} share matching tech stack requirements. You can reference code patterns (e.g., config setup, client connection setup) between them.")
            
        return "\n".join(result_lines)
    except Exception as e:
        return f"Error suggesting patterns: {e}"
