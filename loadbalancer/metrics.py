from .config import BACKEND_SERVERS

# ==========================================================
# Active Connections
# ==========================================================

active_connections = {
    server: 0
    for server in BACKEND_SERVERS
}

# ==========================================================
# Global Metrics
# ==========================================================

metrics = {
    "total_requests": 0,
    "failed_requests": 0
}


# ==========================================================
# Prometheus Metrics Generator
# ==========================================================

def generate_metrics(server_stats, server_health):
    """
    Returns metrics in Prometheus text format.
    """

    lines = []

    lines.append(f"total_requests {metrics['total_requests']}")
    lines.append(f"failed_requests {metrics['failed_requests']}")

    healthy = sum(
        1
        for status in server_health.values()
        if status
    )

    lines.append(f"healthy_servers {healthy}")

    for server, stats in server_stats.items():

        name = server.split("//")[1].replace(":", "_")

        lines.append(
            f"{name}_requests {stats['requests']}"
        )

        lines.append(
            f"{name}_response_time {stats['response_time']}"
        )

        lines.append(
            f"{name}_active_connections {active_connections[server]}"
        )

    return "\n".join(lines)
