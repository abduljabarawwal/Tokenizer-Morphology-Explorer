from typing import List, Dict, Any
import re

class HebrewTokenizer:
    def __init__(self):
        # Common prefixes in Hebrew
        self.prefixes = ['ה', 'ו', 'ב', 'ל', 'מ', 'ש', 'כ']
        # Prefixes that can be combined (e.g., "וכ" -> ו + כ)
        # For simplicity in this version, we'll handle single letter prefixes iteratively
        
    def tokenize_hebrew_text(self, text: str, model_type: str = 'accurate') -> List[str]:
        """
        Tokenize text into words/sub-words.
        """
        # Basic whitespace tokenization first
        # We also want to separate punctuation
        text = re.sub(r'([.,!?()\[\]{};:"\'])', r' \1 ', text)
        tokens = text.split()
        return tokens

    def segment_word(self, word: str) -> Dict[str, Any]:
        """
        Attempt to segment a word into prefix + stem + suffix.
        This is a rule-based approximation.
        """
        # Simple heuristic: check for common prefixes
        # In a real system, we would check against a dictionary to ensure the stem is valid
        
        best_segment = word
        segments = [word]
        confidence = 1.0
        alternatives = []
        
        # Heuristic: if word is long enough (>3 chars), try to strip prefixes
        if len(word) > 3:
            for prefix in self.prefixes:
                if word.startswith(prefix):
                    stem = word[len(prefix):]
                    # Check if stem looks valid (heuristic)
                    if len(stem) >= 2:
                        seg = f"{prefix}-{stem}"
                        segments.append(seg)
                        alternatives.append({'segment': seg, 'confidence': 0.7})
                        # If we found a likely split, we might prefer it?
                        # For now, let's keep the original as best unless we have a dictionary
                        
        return {
            'segments': segments,
            'best_segment': segments[-1] if len(segments) > 1 else word, # Prefer split if found?
            'confidence': confidence,
            'alternatives': alternatives
        }

    def extract_hebrew_morphemes(self, word: str) -> Dict[str, str]:
        """
        Extract prefix, root, suffix.
        """
        # Placeholder for more complex logic
        # This would need the segmentation result
        
        segmentation = self.segment_word(word)
        parts = segmentation['best_segment'].split('-')
        
        if len(parts) > 1:
            return {'prefix': parts[0], 'root': parts[1], 'suffix': ''}
        else:
            return {'prefix': '', 'root': word, 'suffix': ''}

    def score_segmentation(self, segmentation: str, context: str = '') -> float:
        """
        Score a segmentation based on context.
        """
        return 0.8 # Placeholder
