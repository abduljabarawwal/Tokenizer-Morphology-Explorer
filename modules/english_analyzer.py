from typing import Dict, List, Optional
import json
import os

class EnglishAnalyzer:
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.dictionary = self._load_dictionary()

    def _load_dictionary(self) -> Dict:
        path = os.path.join(self.data_dir, 'english_dictionary.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def analyze_morphology(self, token: str, segmentation: str = None) -> Dict[str, str]:
        """
        Analyze morphological features of an English token.
        """
        lower_token = token.lower()
        
        # 1. Dictionary Lookup
        if lower_token in self.dictionary:
            return self.dictionary[lower_token]
            
        # 2. Rule-based
        features = {'pos': 'UNKNOWN', 'type': 'unknown'}
        
        if token.endswith('ing'):
            features.update({'pos': 'VERB', 'tense': 'present participle'})
        elif token.endswith('ed'):
            features.update({'pos': 'VERB', 'tense': 'past'})
        elif token.endswith('ly'):
            features.update({'pos': 'ADV'})
            
        return features
