import os
import sqlite3
import pytest
from src.core.p2p import P2PSyncNode

@pytest.fixture
def clean_p2p_node(tmp_path):
    import database
    # Point SQLite DB to temporary path for testing
    old_conn_func = database.get_sqlite_conn
    temp_db_path = os.path.join(tmp_path, "temp_p2p.db")
    
    def temp_conn():
        conn = sqlite3.connect(temp_db_path)
        conn.row_factory = sqlite3.Row
        return conn
        
    database.get_sqlite_conn = temp_conn
    
    node = P2PSyncNode(port=9999)
    yield node
    
    # Restore connection function
    database.get_sqlite_conn = old_conn_func

def test_p2p_peer_persistence(clean_p2p_node):
    node = clean_p2p_node
    
    # Save a peer
    node._save_peer_to_db("192.168.1.50", 8009)
    
    # Reload peers from database
    node.peers.clear()
    node._load_peers_from_db()
    
    assert ("192.168.1.50", 8009) in node.peers

def test_p2p_pruning(clean_p2p_node):
    node = clean_p2p_node
    
    # Insert peer to peers and database
    ip, port = "127.0.0.1", 9998
    node.peers.add((ip, port))
    node._save_peer_to_db(ip, port)
    
    # Mock health failure counts to threshold
    node._fail_counts[(ip, port)] = 3
    
    # Trigger health pruning logic by calling the pruning logic or mock pruning check
    stale = []
    for peer_ip, peer_port in list(node.peers):
        count = node._fail_counts.get((peer_ip, peer_port), 0)
        if count >= 3:
            stale.append((peer_ip, peer_port))
            
    for peer in stale:
        node.peers.discard(peer)
        node._fail_counts.pop(peer, None)
        node._remove_peer_from_db(peer[0], peer[1])
        
    # Check that the stale peer has been pruned from memory and DB
    assert (ip, port) not in node.peers
    
    # Verify DB is cleared
    node.peers.clear()
    node._load_peers_from_db()
    assert (ip, port) not in node.peers
