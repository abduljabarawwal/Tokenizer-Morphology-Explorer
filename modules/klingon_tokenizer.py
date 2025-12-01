from typing import List, Dict, Any
import re

class KlingonTokenizer:
    def __init__(self):
        # Common prefixes (Type 1: Pronominal)
        self.prefixes = [
            'jI', 'qa', 'vI', 'Da', 'wI', 'bo', 'lu', # Subject/Object markers
            'ma', 'cho', 'ju', 'nu', 'Sa', 'pI', 'HI', 'gho', 'yI', 'pe', 'tI'
        ]
        # Common suffixes (Type 1-9) - Simplified list
        self.suffixes = [
            "be'", "qu'", "Ha'", # Type 1: Negation/Emphatic
            "pu'", "taH", "lI'", # Type 7: Aspect
            "Daq", "vo'", "mo'"  # Noun suffixes (Locative, etc)
        ]

    def tokenize_text(self, text: str) -> List[str]:
        """
        Tokenize Klingon text (whitespace split).
        """
        # Remove punctuation for simple tokenization
        text = re.sub(r'([.,!?])', r' \1 ', text)
        return text.split()

    def segment_word(self, word: str) -> Dict[str, Any]:
        """
        Attempt to segment a Klingon word into prefix-root-suffix.
        """
        best_segment = word
        segments = [word]
        alternatives = []
        
        current_word = word
        found_prefix = ""
        found_suffix = ""
        
        # 1. Check Prefix
        for prefix in self.prefixes:
            if current_word.startswith(prefix):
                # Heuristic: Root must be at least 2 chars usually
                if len(current_word) > len(prefix) + 1:
                    found_prefix = prefix
                    current_word = current_word[len(prefix):]
                    break
        
        # 2. Check Suffix
        for suffix in self.suffixes:
            if current_word.endswith(suffix):
                if len(current_word) > len(suffix) + 1:
                    found_suffix = suffix
                    current_word = current_word[:-len(suffix)]
                    break
                    
        if found_prefix or found_suffix:
            root = current_word
            seg_parts = []
            if found_prefix: seg_parts.append(found_prefix)
            seg_parts.append(root)
            if found_suffix: seg_parts.append(found_suffix)
            
            best_segment = "-".join(seg_parts)
            segments.append(best_segment)
            
        return {
            'segments': segments,
            'best_segment': best_segment,
            'confidence': 0.8 if found_prefix or found_suffix else 0.5,
            'alternatives': alternatives
        }
