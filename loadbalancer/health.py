"""
Health Monitoring Engine

Periodically checks backend servers and
marks them as healthy or unhealthy.
"""

import threading
import time
import requests

from .config import (
    BACKEND_SERVERS,
    HEALTH_CHECK_INTERVAL,
    REQUEST_TIMEOUT,
)

# Dictionary storing health status
server_health = {
    server: True
    for server in BACKEND_SERVERS
}


def check_server(server):
    """
    Check whether a backend server is healthy.
    """

    try:
        response = requests.get(
            f"{server}/health",
            timeout=REQUEST_TIMEOUT
        )

        return response.status_code == 200

    except requests.RequestException:
        return False


def health_monitor():
    """
    Background thread that continuously
    checks backend health.
    """

    while True:

        for server in BACKEND_SERVERS:

            healthy = check_server(server)

            server_health[server] = healthy

        time.sleep(HEALTH_CHECK_INTERVAL)


def start_health_monitor():
    """
    Start the background health thread.
    """

    thread = threading.Thread(
        target=health_monitor,
        daemon=True
    )

    thread.start()
