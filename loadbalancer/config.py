"""
Application configuration.
"""

import os

# ===========================
# Environment
# ===========================

RUNNING_IN_DOCKER = os.getenv("DOCKER_ENV", "false").lower() == "true"

# ===========================
# Backend Servers
# ===========================

if RUNNING_IN_DOCKER:

    BACKEND_SERVERS = [
        "http://server1:5001",
        "http://server2:5002",
        "http://server3:5003",
    ]

else:

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

DEFAULT_ALGORITHM = ALGORITHM_ROUND_ROBIN

# ===========================
# Health Check
# ===========================

HEALTH_CHECK_INTERVAL = 5

# ===========================
# Request Configuration
# ===========================

REQUEST_TIMEOUT = 2

MAX_RETRIES = 3
