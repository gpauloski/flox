from __future__ import annotations

import torch


class FloxModule(torch.nn.Module):
    """
    The ``FloxModule`` is a wrapper for the standard ``torch.nn.Module`` class from PyTorch, with
    a lot of inspiration from the ``lightning.LightningModule`` class from PyTorch Lightning.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def training_step(
        self, batch: torch.Tensor | tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> torch.Tensor:
        """
        A single training step to calculate loss before performing backpropagation.

        Args:
            batch (torch.Tensor | tuple[torch.Tensor, torch.Tensor]): The training data batch.
            batch_idx (int): Index of the batch.

        Returns:
            Loss from the training step.
        """

    def configure_optimizers(self) -> torch.optim.Optimizer:
        """Configures, initializes, and returns the optimizer used to train the model.

        Returns:
            The optimizer used to train the model.
        """

    def validation_step(
        self, batch: torch.Tensor | tuple[torch.Tensor, ...], batch_idx: int
    ):
        """

        Args:
            batch (torch.Tensor | tuple[torch.Tensor, ...]):
            batch_idx (int):

        Returns:

        """

    def test_step(self, batch: torch.Tensor | tuple[torch.Tensor, ...], batch_idx: int):
        """

        Args:
            batch (torch.Tensor | tuple[torch.Tensor, ...]):
            batch_idx (int):

        Returns:

        """

    def predict_step(
        self,
        batch: torch.Tensor | tuple[torch.Tensor, ...],
        batch_idx: int,
        dataloader_idx: int = 0,
    ):
        """

        Args:
            batch (torch.Tensor | tuple[torch.Tensor, ...]):
            batch_idx (int):
            dataloader_idx (int):

        Returns:

        """
