import sys
import os
import json
from dataclasses import dataclass

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.preprocessor import HebrewPreprocessor
from modules.tokenizer import HebrewTokenizer
from modules.analyzer import MorphologicalAnalyzer

from modules.klingon_preprocessor import KlingonPreprocessor
from modules.klingon_tokenizer import KlingonTokenizer
from modules.klingon_analyzer import KlingonAnalyzer

from modules.english_preprocessor import EnglishPreprocessor
from modules.english_tokenizer import EnglishTokenizer
from modules.english_analyzer import EnglishAnalyzer

def run_verification():
    print("Starting Multi-Language Verification...")
    
    # --- Hebrew Test ---
    print("\n--- Hebrew Test ---")
    h_prep = HebrewPreprocessor()
    h_tok = HebrewTokenizer()
    h_anl = MorphologicalAnalyzer()
    
    text = "קראתי ספר"
    processed = h_prep.normalize_hebrew_text(text)
    tokens = h_tok.tokenize_hebrew_text(processed)
    print(f"Tokens: {tokens}")
    assert len(tokens) == 2
    print("Hebrew PASSED")
    
    # --- Klingon Test ---
    print("\n--- Klingon Test ---")
    k_prep = KlingonPreprocessor()
    k_tok = KlingonTokenizer()
    k_anl = KlingonAnalyzer()
    
    text = "tlhIngan maH"
    processed = k_prep.normalize_text(text)
    tokens = k_tok.tokenize_text(processed)
    print(f"Tokens: {tokens}")
    assert len(tokens) == 2
    
    seg = k_tok.segment_word("jIyaj")
    print(f"Segmentation (jIyaj): {seg}")
    assert seg['best_segment'] == "jI-yaj"
    
    morph = k_anl.analyze_morphology("nuqneH")
    print(f"Analysis (nuqneH): {morph}")
    assert morph['type'] == 'greeting'
    print("Klingon PASSED")
    
    # --- English Test ---
    print("\n--- English Test ---")
    e_prep = EnglishPreprocessor()
    e_tok = EnglishTokenizer()
    e_anl = EnglishAnalyzer()
    
    text = "The cats played"
    processed = e_prep.normalize_text(text)
    tokens = e_tok.tokenize_text(processed)
    print(f"Tokens: {tokens}")
    assert len(tokens) == 3
    
    seg = e_tok.segment_word("playing")
    print(f"Segmentation (playing): {seg}")
    # Note: my simple rule was for 'ing' > 4 chars. 'playing' is 7.
    # But wait, my rule was: if word.endswith('ing') and len(word) > 4: best_segment = f"{word[:-3]}-ing"
    # So 'playing' -> 'play-ing'
    
    morph = e_anl.analyze_morphology("cats")
    print(f"Analysis (cats): {morph}")
    assert morph['number'] == 'plural'
    print("English PASSED")
    
    print("\nALL LANGUAGES VERIFIED")

if __name__ == "__main__":
    run_verification()
