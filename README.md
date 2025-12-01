# Multi-Language Tokenizer & Morphology Explorer

![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat)
![Languages](https://img.shields.io/badge/languages-Hebrew%20%7C%20Klingon%20%7C%20English-orange.svg?style=flat)
![NLP](https://img.shields.io/badge/NLP-Multi--Language-brightgreen.svg?style=flat)
![Status](https://img.shields.io/badge/status-active-success.svg?style=flat)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

---

An interactive web application for multi-language NLP analysis supporting **Hebrew**, **Klingon**, and **English**. Input text in any of these languages, select analysis models, and receive detailed tokenization and morphological breakdowns with confidence scores, visualizations, and export capabilities.

## Supported Languages

- 🇮🇱 **Hebrew** - Full morphological analysis with gender, number, person, tense, and binyanim
- 🖖 **Klingon (tlhIngan Hol)** - Advanced tokenization with agglutinative morphology support
- 🇬🇧 **English** - Part-of-speech tagging, lemmatization, and dependency parsing

## Features

- 🌐 **Multi-Language Support** - Process Hebrew, Klingon, and English text
- 🔤 **Advanced Preprocessing** - Normalization, diacritic handling, and language separation
- ✂️ **Language-Aware Tokenization** - Specialized segmentation for each language's unique structure
- 📊 **Morphological Analysis** - Detailed breakdown adapted to each language's grammar
  - Hebrew: gender, number, person, tense, binyanim
  - Klingon: noun/verb prefixes, suffixes, aspect markers
  - English: POS tags, lemmas, morphological features
- 🎯 **Confidence Scoring** - Transparent confidence metrics for every analysis
- 🎨 **Interactive UI** - Built with Streamlit, supporting RTL text (Hebrew) and LTR text (Klingon, English)
- 💾 **Export Options** - Download results in JSON or CSV formats
- 📈 **Visualizations** - Charts and graphs for morphological distribution across languages

## Tech Stack

- **Python** 3.8+
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **spaCy** - English NLP processing
- **Custom NLP Modules** - Hebrew and Klingon tokenization and morphology

## Project Structure

```
Tokenizer-Morphology-Explorer/
├── app.py                      # Main Streamlit application
├── verify_app.py               # Application verification script
├── modules/                    # Core NLP processing modules
│   ├── preprocessor.py         # Multi-language text preprocessing
│   ├── tokenizer.py            # Hebrew, Klingon, English tokenization
│   ├── morphology.py           # Morphological analysis for all languages
│   ├── hebrew_analyzer.py      # Hebrew-specific analysis
│   ├── klingon_analyzer.py     # Klingon-specific analysis
│   └── english_analyzer.py     # English-specific analysis
├── data/                       # Dictionaries and rule sets
│   ├── hebrew_lexicon.json     # Hebrew word lexicon
│   ├── klingon_lexicon.json    # Klingon word database
│   ├── english_lexicon.json    # English word database
│   └── rules.json              # Language-specific morphological rules
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/the3y3-code/Tokenizer-Morphology-Explorer.git
cd Tokenizer-Morphology-Explorer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download Language Models (if using spaCy for English)

```bash
python -m spacy download en_core_web_sm
```

## Usage

### Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

### Using the Interface

1. **Select Language** - Choose Hebrew, Klingon, or English
2. **Input Text** - Enter text in the selected language
3. **Select Model** - Choose from available analysis models
4. **Analyze** - Click the analyze button to process the text
5. **View Results** - Explore tokenization, morphology, and confidence scores
6. **Export** - Download results in JSON or CSV format

### Example Inputs

**Hebrew:**
```
שלום עולם
```

**Klingon:**
```
nuqneH, qaleghpu'
```

**English:**
```
Hello world, how are you?
```

### Verify Installation

Run the verification script to ensure everything is set up correctly:

```bash
python verify_app.py
```

## API Usage

You can also use the modules programmatically:

```python
from modules.tokenizer import MultiLanguageTokenizer
from modules.morphology import MorphologyAnalyzer

# Initialize
tokenizer = MultiLanguageTokenizer()
analyzer = MorphologyAnalyzer()

# Hebrew example
hebrew_text = "שלום עולם"
hebrew_tokens = tokenizer.tokenize(hebrew_text, language="hebrew")
for token in hebrew_tokens:
    morphology = analyzer.analyze(token, language="hebrew")
    print(f"{token}: {morphology}")

# Klingon example
klingon_text = "nuqneH"
klingon_tokens = tokenizer.tokenize(klingon_text, language="klingon")
for token in klingon_tokens:
    morphology = analyzer.analyze(token, language="klingon")
    print(f"{token}: {morphology}")

# English example
english_text = "Hello world"
english_tokens = tokenizer.tokenize(english_text, language="english")
for token in english_tokens:
    morphology = analyzer.analyze(token, language="english")
    print(f"{token}: {morphology}")
```

## Running Tests

To run tests (if implemented):

```bash
pytest tests/
```

## Language-Specific Features

### Hebrew Analysis
- Root extraction (shoresh)
- Binyan identification
- Gender and number agreement
- Prefix and suffix handling
- Nikud (diacritics) processing

### Klingon Analysis
- Verb prefix recognition (pronominal prefixes)
- Noun suffix types (1-5)
- Verb suffix types (1-9)
- Rover suffixes
- Aspect and mood markers

### English Analysis
- Part-of-speech tagging
- Lemmatization
- Named entity recognition
- Dependency parsing
- Morphological features (tense, number, person)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

## Roadmap

- [ ] Add support for additional languages (Arabic, Esperanto)
- [ ] Implement sentiment analysis for all languages
- [ ] Add named entity recognition (NER) for Hebrew and Klingon
- [ ] Cross-language comparison tools
- [ ] Translation suggestions between supported languages
- [ ] RESTful API endpoint
- [ ] Docker containerization
- [ ] Batch processing mode
- [ ] Mobile-responsive UI improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hebrew NLP research community
- Klingon Language Institute (KLI)
- spaCy and English NLP communities
- Streamlit framework developers
- Contributors and testers

## Contact

**the3y3-code** - [GitHub Profile](https://github.com/the3y3-code)

Project Link: [https://github.com/the3y3-code/Tokenizer-Morphology-Explorer](https://github.com/the3y3-code/Tokenizer-Morphology-Explorer)

## Resources

- [Hebrew Morphology Reference](https://en.wikipedia.org/wiki/Hebrew_grammar)
- [Klingon Language Institute](https://www.kli.org/)
- [The Klingon Dictionary](https://en.wikipedia.org/wiki/The_Klingon_Dictionary)
- [English NLP with spaCy](https://spacy.io/)

---

⭐ If you find this project useful, please consider giving it a star!
