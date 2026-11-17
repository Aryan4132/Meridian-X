"""
butler_etiquette.py — Adaptive Butler Tone & Etiquette Engine (BUTLER-31)

Controls the personality formality slider (British Butler <-> Tech Wingman <-> Minimalist)
and injects contextual etiquette directives into system prompt templates.
"""

import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class ButlerEtiquetteEngine:
    """Modulates AI persona formality, vocabulary elegance, and conversational etiquette."""

    def __init__(self, default_formality: float = 0.85):
        # 0.0 = Casual Wingman, 0.5 = Technical Colleague, 1.0 = Formal British Butler
        self._formality: float = max(0.0, min(1.0, default_formality))

    @property
    def formality(self) -> float:
        return self._formality

    def set_formality(self, level: float) -> Dict[str, Any]:
        """Sets formality level between 0.0 and 1.0."""
        self._formality = max(0.0, min(1.0, level))
        tone_label = self.get_tone_label()
        logger.info(f"[ButlerEtiquette] Formality adjusted to {self._formality:.2f} ({tone_label})")
        return {"formality": self._formality, "tone_label": tone_label}

    def get_tone_label(self) -> str:
        if self._formality >= 0.75:
            return "Formal British Butler"
        elif self._formality >= 0.40:
            return "Pragmatic Technical Advisor"
        else:
            return "Casual Silicon Valley Wingman"

    def generate_etiquette_directive(self) -> str:
        """Produces system prompt instructions conforming to the active etiquette level."""
        if self._formality >= 0.75:
            return (
                "TONE DIRECTIVE: Embody a polished, highly discreet, and impeccably courteous executive butler. "
                "Use refined British phrasing ('Very well, Sir/Madam', 'Allow me to take care of that', 'At your leisure'). "
                "Maintain utmost deference, composure, and razor-sharp competence without excessive verbosity."
            )
        elif self._formality >= 0.40:
            return (
                "TONE DIRECTIVE: Act as a sharp, pragmatic technical advisor and senior peer. "
                "Be direct, crisp, professional, and transparent about facts and tradeoffs. Zero fluff."
            )
        else:
            return (
                "TONE DIRECTIVE: Speak like an energetic, casual startup co-founder and coding wingman. "
                "Short, punchy sentences, light humor, modern dev slang when helpful, zero corporate stiffness."
            )

    def format_greeting(self, user_name: str = "Sir") -> str:
        if self._formality >= 0.75:
            return f"At your service, {user_name}."
        elif self._formality >= 0.40:
            return f"Hello {user_name}, ready to proceed."
        else:
            return f"Hey {user_name}, what are we building?"

butler_etiquette_engine = ButlerEtiquetteEngine()

def get_butler_tone_directive() -> str:
    return butler_etiquette_engine.generate_etiquette_directive()

def set_butler_formality(level: float) -> Dict[str, Any]:
    return butler_etiquette_engine.set_formality(level)

