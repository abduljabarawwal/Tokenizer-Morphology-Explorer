from typing import Dict, List, Tuple
import re

class EnglishPreprocessor:
    def __init__(self):
        pass

    def normalize_text(self, text: str) -> str:
        """
        Normalize English text (trim).
        We might keep case for proper nouns, or offer an option.
        For now, just trim.
        """
        if not text:
            return ""
        return text.strip()

    def validate_content(self, text: str) -> Dict:
        """
        Check if text looks like valid English (Latin chars).
        """
        if not text:
            return {'is_valid': False, 'ratio': 0.0, 'warnings': ['Empty text']}

        # Count latin chars
        latin_count = len(re.findall(r'[a-zA-Z]', text))
        total_chars = len(text.replace(" ", ""))
        
        if total_chars == 0:
             return {'is_valid': False, 'ratio': 0.0, 'warnings': ['Only whitespace']}

        ratio = latin_count / total_chars
        
        return {
            'is_valid': ratio > 0.5,
            'ratio': ratio,
            'warnings': [] if ratio > 0.5 else ['Text does not appear to be English']
        }
