import random

from ..metrics import active_connections
from ..health import server_health


class PowerOfTwoChoices:

    def get_server(self):

        healthy_servers = [
            server
            for server in active_connections
            if server_health.get(server, False)
        ]

        if len(healthy_servers) == 0:
            raise Exception("No healthy backend servers available.")

        if len(healthy_servers) == 1:
            return healthy_servers[0]

        server1, server2 = random.sample(
            healthy_servers,
            2
        )

        if active_connections[server1] <= active_connections[server2]:
            return server1

        return server2
