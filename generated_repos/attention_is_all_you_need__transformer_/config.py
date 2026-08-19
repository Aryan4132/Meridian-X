"""Hyperparameter Configuration"""
from dataclasses import dataclass

@dataclass
class PaperConfig:
    batch_size: int = 32
    learning_rate: float = 1e-3
    epochs: int = 5
    hidden_dim: int = 64
    device: str = "cpu"
