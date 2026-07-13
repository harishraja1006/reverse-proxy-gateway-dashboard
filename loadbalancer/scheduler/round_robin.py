from ..config import BACKEND_SERVERS
from ..health import server_health


class RoundRobin:
    """
    Round Robin scheduling algorithm
    using only healthy servers.
    """

    def __init__(self):
        self.current_index = 0

    def get_server(self):

        healthy_servers = [
            server
            for server in BACKEND_SERVERS
            if server_health.get(server, False)
        ]

        if not healthy_servers:
            raise Exception("No healthy backend servers available.")

        server = healthy_servers[
            self.current_index % len(healthy_servers)
        ]

        self.current_index += 1

        return server
