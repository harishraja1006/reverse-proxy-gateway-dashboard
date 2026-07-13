from flask import Flask

from .proxy import forward_request
from .health import start_health_monitor
from dashboard.routes import dashboard

app = Flask(__name__)
app.register_blueprint(dashboard)

# Start background health monitoring
start_health_monitor()


@app.route("/")
def home():
    return forward_request()


@app.route("/health-status")
def health_status():
    from .health import server_health
    return server_health


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000
    )
