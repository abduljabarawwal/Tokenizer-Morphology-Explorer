from typing import Dict, List, Optional
import json
import os

class KlingonAnalyzer:
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.dictionary = self._load_dictionary()

    def _load_dictionary(self) -> Dict:
        path = os.path.join(self.data_dir, 'klingon_dictionary.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def analyze_morphology(self, token: str, segmentation: str = None) -> Dict[str, str]:
        """
        Analyze morphological features of a Klingon token.
        """
        # 1. Dictionary Lookup
        # Try full token first
        if token in self.dictionary:
            return self.dictionary[token]
            
        # Try root if segmented
        if segmentation and '-' in segmentation:
            parts = segmentation.split('-')
            # Assuming middle part is root if 3 parts, or checking logic
            root = parts[1] if len(parts) == 3 else (parts[1] if parts[0] in ['jI','qa'] else parts[0]) 
            # Simplified logic above, better to rely on tokenizer output structure if passed explicitly
            
            # Let's just try to find the root in the dictionary from the parts
            for part in parts:
                if part in self.dictionary:
                    base_analysis = self.dictionary[part].copy()
                    base_analysis['notes'] = 'Root found in complex word'
                    return base_analysis

        return {
            'pos': 'UNKNOWN',
            'translation': '?',
            'type': 'unknown'
        }
