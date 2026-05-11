"""Embedding generator using sentence-transformers."""
from __future__ import annotations

from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIM = 384  # Hardcoded for our model; verify if you swap models


class Embedder:
    """Wraps SentenceTransformer with our preferred defaults."""

    def __init__(self, model_name: str = DEFAULT_MODEL) -> None:
        self.model_name = model_name
        self.model = SentenceTransformer(model_name, device="cpu")

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Convert a batch of texts into embeddings.

        Returns a list of vectors (each vector is a list of floats).
        Batching is handled internally by sentence-transformers.
        """
        vectors = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
            normalize_embeddings=True,
        )
        return vectors.tolist()

    def embed_one(self, text: str) -> list[float]:
        """Convenience method for embedding a single text."""
        return self.embed([text])[0]