"""Dataset & DataLoader"""
import random

class SyntheticDataset:
    """Generates synthetic benchmark dataset for paper model."""
    def __init__(self, num_samples: int = 100, feature_dim: int = 10):
        self.data = [[random.random() for _ in range(feature_dim)] for _ in range(num_samples)]
        self.labels = [random.randint(0, 1) for _ in range(num_samples)]

    def __getitem__(self, idx: int):
        return self.data[idx], self.labels[idx]

    def __len__(self):
        return len(self.data)
