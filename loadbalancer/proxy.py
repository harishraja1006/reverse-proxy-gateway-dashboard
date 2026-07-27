import time
import requests
from flask import request

from .scheduler.scheduler import Scheduler
from .metrics import active_connections, metrics
from .telemetry import server_stats
from .logger import logger

# Create one scheduler instance
scheduler = Scheduler()


def forward_request():
    """
    Forward a request to the selected backend server
    while collecting telemetry and request logs.
    """

    server = scheduler.get_server()

    metrics["total_requests"] += 1
    active_connections[server] += 1

    start_time = time.perf_counter()

    try:

        print(f"Forwarding request to: {server}")

        response = requests.get(server)

        end_time = time.perf_counter()

        response_time = round((end_time - start_time) * 1000, 2)

        # Update telemetry
        server_stats[server]["requests"] += 1
        server_stats[server]["response_time"] = response_time

        # Log request
        logger.info(
            "Client=%s | Backend=%s | Algorithm=%s | Status=%s | ResponseTime=%sms",
            request.remote_addr,
            server,
            type(scheduler.algorithm).__name__,
            response.status_code,
            response_time
        )

        return response.text, response.status_code

    except requests.RequestException:

        metrics["failed_requests"] += 1

        logger.error(
            "Client=%s | Backend=%s | Status=503 | Backend Unavailable",
            request.remote_addr,
            server
        )

        return "Backend server unavailable", 503

    finally:

        active_connections[server] -= 1
