import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dataclasses import dataclass
from typing import List, Dict, Any
import time
import json

# Import modules
from modules.preprocessor import HebrewPreprocessor
from modules.tokenizer import HebrewTokenizer
from modules.analyzer import MorphologicalAnalyzer
from modules.scorer import ConfidenceScorer
from modules.exporter import DataExporter
from modules.models import ModelManager

from modules.klingon_preprocessor import KlingonPreprocessor
from modules.klingon_tokenizer import KlingonTokenizer
from modules.klingon_analyzer import KlingonAnalyzer

from modules.english_preprocessor import EnglishPreprocessor
from modules.english_tokenizer import EnglishTokenizer
from modules.english_analyzer import EnglishAnalyzer

# Page Config
st.set_page_config(
    page_title="Universal Tokenizer & Morphology Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Modules
@st.cache_resource
def get_modules(language):
    if language == "Hebrew":
        return {
            'preprocessor': HebrewPreprocessor(),
            'tokenizer': HebrewTokenizer(),
            'analyzer': MorphologicalAnalyzer(),
            'scorer': ConfidenceScorer(),
            'exporter': DataExporter(),
            'model_manager': ModelManager(),
            'direction': 'rtl',
            'font': 'Courier New'
        }
    elif language == "Klingon":
        return {
            'preprocessor': KlingonPreprocessor(),
            'tokenizer': KlingonTokenizer(),
            'analyzer': KlingonAnalyzer(),
            'scorer': ConfidenceScorer(), # Reuse generic scorer
            'exporter': DataExporter(),
            'model_manager': ModelManager(), # Reuse generic manager
            'direction': 'ltr',
            'font': 'Impact, Charcoal, sans-serif' # Klingon-esque?
        }
    elif language == "English":
        return {
            'preprocessor': EnglishPreprocessor(),
            'tokenizer': EnglishTokenizer(),
            'analyzer': EnglishAnalyzer(),
            'scorer': ConfidenceScorer(),
            'exporter': DataExporter(),
            'model_manager': ModelManager(),
            'direction': 'ltr',
            'font': 'Arial, sans-serif'
        }

# Sidebar
st.sidebar.title("Configuration")
language = st.sidebar.selectbox("Language", ["Hebrew", "Klingon", "English"])
modules = get_modules(language)

# Custom CSS for Direction and Styling
st.markdown(f"""
<style>
    .stTextInput > div > div > input {{
        direction: {modules['direction']};
        text-align: {'right' if modules['direction'] == 'rtl' else 'left'};
        font-family: {modules['font']};
    }}
    .stTextArea > div > div > textarea {{
        direction: {modules['direction']};
        text-align: {'right' if modules['direction'] == 'rtl' else 'left'};
        font-family: {modules['font']};
    }}
    .rtl-text {{
        direction: {modules['direction']};
        text-align: {'right' if modules['direction'] == 'rtl' else 'left'};
    }}
</style>
""", unsafe_allow_html=True)

model_type = st.sidebar.selectbox("Model", ["Fast", "Accurate", "Experimental"], index=1)
include_alternatives = st.sidebar.checkbox("Include Alternatives", value=True)
show_confidence = st.sidebar.checkbox("Show Confidence", value=True)
analyze_features = st.sidebar.checkbox("Analyze Features", value=True)

if language == "Hebrew":
    remove_diacritics = st.sidebar.radio("Diacritics", ["Remove Diacritics", "Keep Diacritics"]) == "Remove Diacritics"
else:
    remove_diacritics = False # Not applicable

# Data Models
@dataclass
class TokenResult:
    id: int
    original: str
    segmentation: str
    pos_tag: str
    pos_confidence: float
    morphology: Dict[str, str]
    confidence_reasoning: str

# Main Content
st.title(f"{language} Tokenizer & Morphology Explorer")
st.markdown(f"Interactive tool for {language} NLP analysis. Enter text below to begin.")

# Input Section
col1, col2 = st.columns([3, 1])
with col1:
    placeholder = "הכנס טקסט בעברית כאן..." if language == "Hebrew" else ("nuqneH..." if language == "Klingon" else "Enter text here...")
    input_text = st.text_area(f"{language} Input", height=150, placeholder=placeholder)
with col2:
    st.write("Actions")
    analyze_btn = st.button(f"ANALYZE {language.upper()} TEXT", type="primary", use_container_width=True)
    if st.button("CLEAR", use_container_width=True):
        input_text = ""
    if st.button("LOAD EXAMPLE", use_container_width=True):
        if language == "Hebrew":
            input_text = "קראתי ספר מעניין אתמול"
        elif language == "Klingon":
            input_text = "tlhIngan maH nuqneH"
        else:
            input_text = "The cats played in the garden"
        st.experimental_rerun()

# Processing Logic
if analyze_btn and input_text:
    start_time = time.time()
    
    # 1. Preprocess
    if language == "Hebrew":
        processed_text = modules['preprocessor'].normalize_hebrew_text(input_text, remove_diacritics=remove_diacritics)
        validation = modules['preprocessor'].validate_hebrew_content(processed_text)
    elif language == "Klingon":
        processed_text = modules['preprocessor'].normalize_text(input_text)
        validation = modules['preprocessor'].validate_content(processed_text)
    else:
        processed_text = modules['preprocessor'].normalize_text(input_text)
        validation = modules['preprocessor'].validate_content(processed_text)
    
    if not validation.get('is_valid', True): # Default true if no validation
        st.warning(f"Input does not appear to contain valid {language} text.")
        if validation.get('warnings'):
            for w in validation['warnings']:
                st.warning(w)
    else:
        # 2. Tokenize
        if language == "Hebrew":
            raw_tokens = modules['tokenizer'].tokenize_hebrew_text(processed_text)
        elif language == "Klingon":
            raw_tokens = modules['tokenizer'].tokenize_text(processed_text)
        else:
            raw_tokens = modules['tokenizer'].tokenize_text(processed_text)
        
        # 3. Analyze & Score
        results = []
        # Reuse model manager for POS if applicable, or fallback
        pos_tags = modules['model_manager'].predict_pos_tags(raw_tokens, model_type.lower())
        
        for i, token in enumerate(raw_tokens):
            # Segmentation
            if language == "Hebrew":
                seg_data = modules['tokenizer'].segment_word(token)
            elif language == "Klingon":
                seg_data = modules['tokenizer'].segment_word(token)
            else:
                seg_data = modules['tokenizer'].segment_word(token)
            
            # Morphology
            if language == "Hebrew":
                morph = modules['analyzer'].analyze_morphology(seg_data['best_segment'])
            elif language == "Klingon":
                morph = modules['analyzer'].analyze_morphology(token, seg_data['best_segment'])
            else:
                morph = modules['analyzer'].analyze_morphology(token, seg_data['best_segment'])
            
            # Confidence
            conf = modules['scorer'].calculate_confidence(token, morph)
            reasoning = modules['scorer'].generate_confidence_reasoning(token, conf, morph)
            
            results.append(TokenResult(
                id=i+1,
                original=token,
                segmentation=seg_data['best_segment'],
                pos_tag=morph.get('pos', pos_tags[i]), # Prefer analyzer POS if available
                pos_confidence=conf,
                morphology=morph,
                confidence_reasoning=reasoning
            ))
            
        processing_time = time.time() - start_time
        
        # Results Display
        st.divider()
        st.subheader("Analysis Results")
        
        # Info Bar
        m1, m2, m3 = st.columns(3)
        m1.metric("Tokens", len(results))
        m2.metric("Processing Time", f"{processing_time:.3f}s")
        m3.metric("Model", model_type)
        
        # Data Grid
        df_data = [{
            '#': r.id,
            'Token': r.original,
            'Segmentation': r.segmentation,
            'POS': r.pos_tag,
            'Confidence': f"{r.pos_confidence:.2f}"
        } for r in results]
        
        st.dataframe(pd.DataFrame(df_data), use_container_width=True)
        
        # Details & Visualization
        c1, c2 = st.columns([2, 1])
        
        with c1:
            st.subheader("Detailed Breakdown")
            for r in results:
                with st.expander(f"{r.id}. {r.original} ({r.pos_tag})"):
                    dc1, dc2 = st.columns(2)
                    with dc1:
                        st.markdown(f"**Segmentation:** {r.segmentation}")
                        if language == "Hebrew":
                            st.markdown(f"**Root:** {r.morphology.get('root', '-')}")
                            st.markdown(f"**Binyan:** {r.morphology.get('binyan', '-')}")
                        elif language == "Klingon":
                            st.markdown(f"**Translation:** {r.morphology.get('translation', '-')}")
                        else:
                            st.markdown(f"**Type:** {r.morphology.get('type', '-')}")
                    with dc2:
                        st.json(r.morphology)
                    st.info(r.confidence_reasoning)

        with c2:
            st.subheader("Visualizations")
            
            # POS Chart
            pos_counts = pd.DataFrame(df_data)['POS'].value_counts()
            fig_pos = px.pie(values=pos_counts.values, names=pos_counts.index, title="POS Distribution")
            st.plotly_chart(fig_pos, use_container_width=True)
            
            # Confidence Chart
            conf_values = [r.pos_confidence for r in results]
            fig_conf = px.histogram(x=conf_values, nbins=10, title="Confidence Distribution", labels={'x': 'Confidence', 'y': 'Count'})
            st.plotly_chart(fig_conf, use_container_width=True)

        # Export
        st.divider()
        st.subheader("Export")
        
        export_format = st.selectbox("Format", ["JSON", "CSV"])
        
        if export_format == "JSON":
            json_data = modules['exporter'].export_to_json({'tokens': results})
            st.download_button("Download JSON", json_data, "results.json", "application/json")
        else:
            csv_data = modules['exporter'].export_to_csv({'tokens': results})
            st.download_button("Download CSV", csv_data, "results.csv", "text/csv")

else:
    st.info(f"Enter {language} text and click Analyze to see results.")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit & Python | Universal NLP Explorer")
