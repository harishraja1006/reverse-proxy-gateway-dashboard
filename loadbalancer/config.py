"""
Application configuration.
"""

# ===========================
# Backend Servers
# ===========================

BACKEND_SERVERS = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003",
]

# ===========================
# Scheduling Algorithms
# ===========================

ALGORITHM_ROUND_ROBIN = "round_robin"
ALGORITHM_LEAST_CONNECTIONS = "least_connections"
ALGORITHM_P2C = "p2c"
ALGORITHM_HYBRID = "hybrid"

# Default algorithm
DEFAULT_ALGORITHM = ALGORITHM_ROUND_ROBIN

# ===========================
# Health Check
# ===========================

HEALTH_CHECK_INTERVAL = 5

REQUEST_TIMEOUT = 3
