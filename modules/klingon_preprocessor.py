from typing import Dict, List, Tuple
import re

class KlingonPreprocessor:
    def __init__(self):
        # Klingon characters: a, b, ch, D, e, gh, H, I, j, l, m, n, ng, o, p, q, Q, r, S, t, tlh, u, v, w, y, '
        self.valid_chars_pattern = re.compile(r"[a-zA-Z'\s]+")

    def normalize_text(self, text: str) -> str:
        """
        Normalize Klingon text. 
        Note: Klingon is case-sensitive (q vs Q), so we do NOT lowercase.
        """
        if not text:
            return ""
        return text.strip()

    def validate_content(self, text: str) -> Dict:
        """
        Check if text looks like valid Klingon.
        """
        if not text:
            return {'is_valid': False, 'ratio': 0.0, 'warnings': ['Empty text']}

        # Simple check: mostly valid latin chars + apostrophe
        # In a real app, we'd check for specific Klingon digraphs/trigraphs
        match = self.valid_chars_pattern.fullmatch(text)
        is_valid = match is not None
        
        return {
            'is_valid': is_valid,
            'ratio': 1.0 if is_valid else 0.0,
            'warnings': [] if is_valid else ['Contains invalid characters for Klingon transcription']
        }
