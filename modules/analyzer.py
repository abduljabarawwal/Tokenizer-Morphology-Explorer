from typing import Dict, List, Optional
import json
import os

class MorphologicalAnalyzer:
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.dictionary = self._load_dictionary()
        self.rules = self._load_rules()

    def _load_dictionary(self) -> Dict:
        path = os.path.join(self.data_dir, 'hebrew_dictionary.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _load_rules(self) -> Dict:
        path = os.path.join(self.data_dir, 'morphological_rules.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def analyze_morphology(self, token: str, pos_tag: Optional[str] = None) -> Dict[str, str]:
        """
        Analyze morphological features of a token.
        """
        # 1. Dictionary Lookup
        if token in self.dictionary:
            return self.dictionary[token]
        
        # 2. Rule-based Fallback (simplified)
        features = {
            'gender': 'unknown',
            'number': 'singular', # default
            'person': 'unknown',
            'tense': 'unknown',
            'binyan': 'unknown',
            'state': 'absolute',
            'definiteness': 'indefinite'
        }
        
        # Simple heuristics
        if token.endswith('ים'):
            features['gender'] = 'masculine'
            features['number'] = 'plural'
        elif token.endswith('ות'):
            features['gender'] = 'feminine'
            features['number'] = 'plural'
        elif token.endswith('ה'):
            features['gender'] = 'feminine'
            
        if token.startswith('ה'):
            features['definiteness'] = 'definite'
            
        features['binyan'] = self.detect_binyan(token)
            
        return features

    def detect_binyan(self, word: str) -> str:
        """
        Recognize Hebrew verb patterns.
        """
        # Very basic pattern matching
        if word.startswith('הת'):
            return 'hitpael'
        elif word.startswith('נ'):
            return 'nifal'
        elif word.startswith('מ'):
            return 'piel' # Often participles
        # ... add more rules
        return 'pahal' # Default assumption

    def extract_features(self, word: str) -> Dict[str, str]:
        return self.analyze_morphology(word)

    def validate_feature_agreement(self, tokens: List[Dict]) -> List[Dict]:
        """
        Check agreement between tokens (placeholder).
        """
        return []
