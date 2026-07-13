"""
Scheduler Dispatcher

Selects the scheduling algorithm
based on the application configuration.
"""

from ..config import (
    DEFAULT_ALGORITHM,
    ALGORITHM_ROUND_ROBIN,
    ALGORITHM_LEAST_CONNECTIONS,
    ALGORITHM_P2C,
    ALGORITHM_HYBRID,
)

from .round_robin import RoundRobin
from .least_connections import LeastConnections
from .p2c import PowerOfTwoChoices
from .hybrid import HybridScheduler


class Scheduler:
    """
    Scheduler Dispatcher
    """

    def __init__(self):

        if DEFAULT_ALGORITHM == ALGORITHM_ROUND_ROBIN:
            self.algorithm = RoundRobin()

        elif DEFAULT_ALGORITHM == ALGORITHM_LEAST_CONNECTIONS:
            self.algorithm = LeastConnections()

        elif DEFAULT_ALGORITHM == ALGORITHM_P2C:
            self.algorithm = PowerOfTwoChoices()

        elif DEFAULT_ALGORITHM == ALGORITHM_HYBRID:
            self.algorithm = HybridScheduler()

        else:
            raise ValueError(
                f"Unknown scheduling algorithm: {DEFAULT_ALGORITHM}"
            )

    def get_server(self):
        return self.algorithm.get_server()
