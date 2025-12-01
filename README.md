# Hebrew Tokenizer & Morphology Explorer

![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat)
![NLP](https://img.shields.io/badge/NLP-Hebrew-orange.svg?style=flat)
![Status](https://img.shields.io/badge/status-active-success.svg?style=flat)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

---

An interactive web application for Hebrew NLP analysis. Input Hebrew text, select analysis models, and receive detailed tokenization and morphological breakdowns with confidence scores, visualizations, and export capabilities.

## Features

- 🔤 **Hebrew Preprocessing** - Normalization, diacritic handling, and language separation
- ✂️ **Advanced Tokenization** - Hebrew-aware segmentation handling prefixes and suffixes
- 📊 **Morphological Analysis** - Detailed breakdown of gender, number, person, tense, and binyanim
- 🎯 **Confidence Scoring** - Transparent confidence metrics for every analysis
- 🎨 **Interactive UI** - Built with Streamlit, supporting RTL text and dynamic visualizations
- 💾 **Export Options** - Download results in JSON or CSV formats
- 📈 **Visualizations** - Charts and graphs for morphological distribution

## Tech Stack

- **Python** 3.8+
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **Hebrew NLP Libraries** - Custom tokenization and morphology modules

## Project Structure

```
Tokenizer-Morphology-Explorer/
├── app.py                      # Main Streamlit application
├── verify_app.py               # Application verification script
├── modules/                    # Core NLP processing modules
│   ├── preprocessor.py         # Text preprocessing
│   ├── tokenizer.py            # Hebrew tokenization
│   └── morphology.py           # Morphological analysis
├── data/                       # Dictionaries and rule sets
│   ├── lexicon.json            # Hebrew word lexicon
│   └── rules.json              # Morphological rules
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

## Usage

### Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

### Using the Interface

1. **Input Text** - Enter Hebrew text in the text area
2. **Select Model** - Choose from available analysis models
3. **Analyze** - Click the analyze button to process the text
4. **View Results** - Explore tokenization, morphology, and confidence scores
5. **Export** - Download results in JSON or CSV format

### Verify Installation

Run the verification script to ensure everything is set up correctly:

```bash
python verify_app.py
```

## API Usage

You can also use the modules programmatically:

```python
from modules.tokenizer import HebrewTokenizer
from modules.morphology import MorphologyAnalyzer

# Initialize
tokenizer = HebrewTokenizer()
analyzer = MorphologyAnalyzer()

# Tokenize
text = "שלום עולם"
tokens = tokenizer.tokenize(text)

# Analyze morphology
for token in tokens:
    morphology = analyzer.analyze(token)
    print(f"{token}: {morphology}")
```

## Running Tests

To run tests (if implemented):

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

## Roadmap

- [ ] Add support for additional Hebrew NLP models
- [ ] Implement sentiment analysis
- [ ] Add named entity recognition (NER)
- [ ] Support for Aramaic and Judeo-Arabic
- [ ] RESTful API endpoint
- [ ] Docker containerization
- [ ] Batch processing mode

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hebrew NLP research community
- Streamlit framework developers
- Contributors and testers

## Contact

**the3y3-code** - [GitHub Profile](https://github.com/the3y3-code)

Project Link: [https://github.com/the3y3-code/Tokenizer-Morphology-Explorer](https://github.com/the3y3-code/Tokenizer-Morphology-Explorer)

---

⭐ If you find this project useful, please consider giving it a star!
