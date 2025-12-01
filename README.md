# Hebrew Tokenizer & Morphology Explorer

An interactive web application for Hebrew NLP analysis. Users can input Hebrew text, select analysis models, and get detailed tokenization and morphological breakdown with confidence scores, charts, and export options.

## Features

- **Hebrew Preprocessing**: Normalization, diacritic handling, and language separation.
- **Advanced Tokenization**: Hebrew-aware segmentation handling prefixes and suffixes.
- **Morphological Analysis**: Detailed breakdown of gender, number, person, tense, and binyanim.
- **Confidence Scoring**: Transparent confidence metrics for every analysis.
- **Interactive UI**: Built with Streamlit, supporting RTL text and dynamic visualizations.
- **Export**: Download results in JSON or CSV formats.

## Installation

1. Clone the repository or download the source code.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main application entry point.
- `modules/`: Core NLP processing modules.
- `data/`: Dictionaries and rule sets.
