from typing import List, Dict

class ConfidenceScorer:
    def __init__(self):
        pass

    def calculate_confidence(self, token: str, analysis: Dict, context: str = '') -> float:
        """
        Return score 0.0-1.0 based on analysis quality.
        """
        score = 0.5 # Base score
        
        # If we have specific features identified, confidence goes up
        if analysis.get('gender') != 'unknown':
            score += 0.2
        if analysis.get('binyan') != 'unknown':
            score += 0.1
            
        # Length heuristic - very short words are ambiguous
        if len(token) < 2:
            score -= 0.1
            
        return min(1.0, max(0.0, score))

    def ensemble_confidence(self, scores: List[float], weights: List[float] = None) -> float:
        if not scores:
            return 0.0
        if weights and len(weights) == len(scores):
            return sum(s * w for s, w in zip(scores, weights)) / sum(weights)
        return sum(scores) / len(scores)

    def generate_confidence_reasoning(self, token: str, confidence: float, analysis: Dict) -> str:
        if confidence > 0.8:
            return "High confidence: Clear morphological markers found."
        elif confidence > 0.5:
            return "Medium confidence: Some ambiguity in suffix."
        else:
            return "Low confidence: Word not in dictionary and no clear patterns."

    def identify_ambiguous_tokens(self, tokens: List[Dict]) -> List[Dict]:
        ambiguous = []
        for t in tokens:
            if t.get('confidence', 1.0) < 0.6:
                ambiguous.append(t)
        return ambiguous
