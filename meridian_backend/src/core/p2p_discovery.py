"""P2P mDNS service-discovery listener.

Split from ``src.core.p2p`` (Phase 2 god-file refactor). Pure move —
zero behavior changes. ``p2p.py`` re-exports every symbol so existing
imports keep working.
"""

import socket
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.p2p import P2PSyncNode


class MeridianZeroconfListener:
    """BK-07: Listener for mDNS zeroconf P2P service discovery."""
    def __init__(self, node: 'P2PSyncNode'):
        self.node = node

    def add_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:  # type: ignore[name-defined]  # noqa: F821
        try:
            info = zc.get_service_info(type_, name)
            if info and info.addresses:
                peer_ip = socket.inet_ntoa(info.addresses[0])
                peer_port = info.port
                # Avoid adding self
                if peer_ip not in ("127.0.0.1", self.node.host) or peer_port != self.node.port:
                    with self.node.lock:
                        if (peer_ip, peer_port) not in self.node.peers:
                            self.node.peers.add((peer_ip, peer_port))
                            self.node._save_peer_to_db(peer_ip, peer_port)
                            print(f"[P2P Zeroconf] Discovered mDNS peer: {peer_ip}:{peer_port}")
        except Exception as e:
            print(f"[P2P Zeroconf] Error parsing service info: {e}")

    def remove_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:  # type: ignore[name-defined]  # noqa: F821
        pass

    def update_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:  # type: ignore[name-defined]  # noqa: F821
        pass
