# Contributing to Multi-Language Tokenizer & Morphology Explorer

Thank you for considering contributing to this project! We welcome contributions from the community for all supported languages: Hebrew, Klingon, and English.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- **Language affected** (Hebrew, Klingon, or English)
- Your environment (OS, Python version, browser version)
- Screenshots or error messages if applicable
- Sample text that causes the issue (if applicable)

### Suggesting Enhancements

For feature requests:
- Use a clear and descriptive title
- Specify which language(s) the enhancement applies to
- Provide detailed explanation of the feature
- Explain why this enhancement would be useful
- Include mockups or examples if possible

### Language-Specific Contributions

We especially welcome contributions that:
- Improve Hebrew morphological analysis accuracy
- Enhance Klingon tokenization and suffix parsing
- Add English NLP features (NER, sentiment analysis)
- Expand language-specific lexicons and dictionaries
- Add support for new languages

### Pull Requests

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Test your changes thoroughly **for all affected languages**
5. Commit with clear, descriptive messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   ```
6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. Open a Pull Request with:
   - Clear title and description
   - Language(s) affected
   - Reference to any related issues
   - List of changes made

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Add comments for complex logic, especially language-specific rules
- Keep functions focused and concise

### Testing

- Write tests for new features
- Test with sample text in **all three languages**
- Ensure all tests pass before submitting PR
- Maintain or improve code coverage
- Test edge cases for each language:
  - Hebrew: Text with and without nikud, mixed Hebrew-English
  - Klingon: Complex suffix chains, proper nouns
  - English: Contractions, punctuation, capitalization

### Language-Specific Guidelines

#### Hebrew Contributions
- Test with both modern and biblical Hebrew if applicable
- Handle nikud (diacritics) correctly
- Verify RTL text display
- Consider prefix and suffix variations

#### Klingon Contributions
- Follow canonical Klingon orthography (tlhIngan Hol)
- Reference official Klingon Language Institute resources
- Test verb and noun suffix combinations
- Verify rover suffix behavior

#### English Contributions
- Use established NLP libraries (spaCy) when possible
- Handle contractions and informal text
- Test with various text styles (formal, informal, technical)

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Start with a verb (Add, Fix, Update, Remove)
- Keep first line under 50 characters
- Mention language if language-specific: "Fix Hebrew tokenization issue"
- Add detailed description if needed

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Respect all languages and cultures equally

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Cultural insensitivity or language discrimination
- Other unprofessional conduct

## Questions?

Feel free to open an issue for any questions about contributing!

## Resources for Contributors

### Hebrew Resources
- [Hebrew Grammar Reference](https://en.wikipedia.org/wiki/Hebrew_grammar)
- Hebrew Unicode ranges: U+0590 to U+05FF

### Klingon Resources
- [Klingon Language Institute](https://www.kli.org/)
- [The Klingon Dictionary by Marc Okrand](https://en.wikipedia.org/wiki/The_Klingon_Dictionary)
- Klingon Unicode: U+F8D0 to U+F8FF (private use area)

### English Resources
- [spaCy Documentation](https://spacy.io/)
- [Penn Treebank POS Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
