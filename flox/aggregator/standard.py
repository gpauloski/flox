import lightning as L

from flox.aggregator.base import AbstractAggregatorLogic


class SimpleAggregatorLogic(AbstractAggregatorLogic):
    def __init__(self):
        super().__init__()

    def on_model_broadcast(self):
        pass

    def on_model_receive(self):
        pass

    def on_model_aggregate(self, updates: list):
        pass

    def on_model_evaluate(self):
        pass
