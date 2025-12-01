import re
import unicodedata
from typing import Dict, List, Tuple

class HebrewPreprocessor:
    def __init__(self):
        self.hebrew_pattern = re.compile(r'[\u0590-\u05FF]+')
        self.niqqud_pattern = re.compile(r'[\u0591-\u05C7]')

    def normalize_hebrew_text(self, text: str, remove_diacritics: bool = True) -> str:
        """
        Normalize Hebrew text by handling unicode variants and optionally removing niqqud.
        """
        if not text:
            return ""
        
        # Normalize unicode characters
        text = unicodedata.normalize('NFKC', text)
        
        if remove_diacritics:
            text = self.remove_diacritics(text)
            
        return text.strip()

    def remove_diacritics(self, text: str) -> str:
        """
        Strip all diacritical marks (niqqud) from the text.
        """
        return self.niqqud_pattern.sub('', text)

    def validate_hebrew_content(self, text: str) -> Dict:
        """
        Check if text contains Hebrew and return statistics.
        """
        if not text:
            return {'is_valid': False, 'hebrew_ratio': 0.0, 'warnings': ['Empty text']}

        total_chars = len(text.replace(" ", ""))
        if total_chars == 0:
            return {'is_valid': False, 'hebrew_ratio': 0.0, 'warnings': ['Only whitespace']}

        hebrew_chars = len(self.hebrew_pattern.findall(text))
        # Note: findall returns list of strings, need to sum lengths
        hebrew_char_count = sum(len(match) for match in self.hebrew_pattern.findall(text))
        
        ratio = hebrew_char_count / total_chars
        
        warnings = []
        if ratio < 0.5:
            warnings.append("Text contains mostly non-Hebrew characters")
            
        return {
            'is_valid': hebrew_char_count > 0,
            'hebrew_ratio': ratio,
            'warnings': warnings
        }

    def separate_hebrew_english(self, text: str) -> List[Tuple[str, str]]:
        """
        Split text into tokens with language detection.
        Returns list of (token, language) tuples.
        """
        tokens = []
        # Split by whitespace but keep punctuation attached for now, 
        # or better: use regex to find words
        
        # Simple whitespace split for initial separation
        raw_tokens = text.split()
        
        for token in raw_tokens:
            if self.hebrew_pattern.search(token):
                tokens.append((token, 'HE'))
            elif re.search(r'[a-zA-Z]', token):
                tokens.append((token, 'EN'))
            else:
                tokens.append((token, 'OTHER')) # Numbers, punctuation only
                
        return tokens
