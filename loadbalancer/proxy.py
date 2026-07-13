import time
import requests

from .scheduler.scheduler import Scheduler
from .metrics import active_connections, metrics
from .telemetry import server_stats

# Create one scheduler instance
scheduler = Scheduler()


def forward_request():
    """
    Forward a request to the selected backend server
    while collecting telemetry.
    """

    server = scheduler.get_server()

    metrics["total_requests"] += 1
    active_connections[server] += 1

    start_time = time.perf_counter()

    try:

        response = requests.get(server)

        end_time = time.perf_counter()

        response_time = round((end_time - start_time) * 1000, 2)

        # Update telemetry
        server_stats[server]["requests"] += 1
        server_stats[server]["response_time"] = response_time

        return response.text

    except requests.RequestException:

        metrics["failed_requests"] += 1

        return "Backend server unavailable", 503

    finally:

        active_connections[server] -= 1
