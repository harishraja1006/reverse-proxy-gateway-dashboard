"""
Telemetry Module

Stores per-server statistics for the dashboard.
"""

from .config import BACKEND_SERVERS

server_stats = {
    server: {
        "requests": 0,
        "response_time": 0,
    }
    for server in BACKEND_SERVERS
}
