from ..metrics import active_connections
from ..health import server_health


class LeastConnections:
    """
    Least Connections scheduling algorithm.
    """

    def get_server(self):

        healthy_servers = {
            server: connections
            for server, connections in active_connections.items()
            if server_health.get(server, False)
        }

        if not healthy_servers:
            raise Exception("No healthy backend servers available.")

        return min(
            healthy_servers,
            key=healthy_servers.get
        )
