from __future__ import annotations

from typing import Any

from flox.flock import Flock, FlockNode, FlockNodeID
from flox.flock.states import FloxWorkerState, FloxAggregatorState, NodeState
from flox.strategies.base import Loss, Strategy
from flox.strategies.commons.averaging import average_state_dicts
from flox.strategies.commons.worker_selection import random_worker_selection
from flox.typing import StateDict
from flox.flock.states import FloxWorkerState


class FedSGD(Strategy):
    """Implementation of the Federated Stochastic Gradient Descent algorithm.

    In short, this algorithm randomly selects a subset of worker nodes and will
    do a simple unweighted average across the updates to the model paremeters
    (i.e., ``StateDict``).

    > **Reference:**
    >
    > McMahan, Brendan, et al. "Communication-efficient learning of deep networks
    > from decentralized data." Artificial intelligence and statistics. PMLR, 2017.
    """

    def __init__(
        self,
        participation: float = 1.0,
        probabilistic: bool = True,
        always_include_child_aggregators: bool = True,
        seed: int = None,
    ):
        """

        Args:
            participation ():
            probabilistic ():
            always_include_child_aggregators ():
            seed ():
        """
        super().__init__()
        self.participation = participation
        self.probabilistic = probabilistic
        self.always_include_child_aggregators = always_include_child_aggregators
        self.seed = seed

    def agg_worker_selection(
        self, state: FloxAggregatorState, children: list[FlockNode], **kwargs
    ) -> list[FlockNode]:
        """Performs a simple average of the model weights returned by the child nodes.

        The average is done by:

        $$
            w^{t} \\triangleq \\frac{1}{K} \\sum_{k=1}^{K} w_{k}^{t}
        $$

        where $w^{t}$ is the aggregated model weights, $K$ is the number of returned
        model updates, $t$ is the current round, and $w_{k}^{t}$ is the returned model
        updates from child $k$ at round $t$.

        Args:
            state (FloxAggregatorState): ...
            children (list[FlockNode]):
            **kwargs ():

        Returns:
            list[FlockNode]
        """
        return random_worker_selection(
            children,
            participation=self.participation,
            probabilistic=self.probabilistic,
            always_include_child_aggregators=self.always_include_child_aggregators,
            seed=self.seed,  # TODO: Change this because it will always do the same thing as is.
        )

    def agg_param_aggregation(
        self,
        state: FloxAggregatorState,
        children_states: dict[FlockNodeID, NodeState],
        children_state_dicts: dict[FlockNodeID, StateDict],
        *args,
        **kwargs,
    ):
        return average_state_dicts(children_state_dicts, weights=None)
