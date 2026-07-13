from flask import Blueprint, jsonify, render_template

from loadbalancer.metrics import metrics, active_connections
from loadbalancer.health import server_health
from loadbalancer.telemetry import server_stats
from loadbalancer.config import DEFAULT_ALGORITHM

dashboard = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/dashboard/static"
)


@dashboard.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


@dashboard.route("/api/dashboard")
def dashboard_api():

    healthy_servers = sum(server_health.values())

    data = {
        "algorithm": DEFAULT_ALGORITHM,

        "total_requests": metrics["total_requests"],

        "failed_requests": metrics["failed_requests"],

        "healthy_servers": healthy_servers,

        "active_connections": active_connections,

        "server_health": server_health,

        "server_stats": server_stats
    }

    return jsonify(data)
