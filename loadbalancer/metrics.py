from .config import BACKEND_SERVERS

# Number of active requests on each backend server
active_connections = {
    server: 0
    for server in BACKEND_SERVERS
}

# Application metrics
metrics = {
    "total_requests": 0,
    "failed_requests": 0
}
