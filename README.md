# 📚 ResearchMate AI
### AI Research Paper Reading Assistant for Undergraduates

ResearchMate AI is a web-based prototype designed to help undergraduate students understand research papers more easily. It extracts text from uploaded PDF documents and identifies relevant sentences related to research aims, methodology, key findings, and limitations.

## 🎯 Project Objective

To make academic research papers easier to explore and understand by organizing important information into simple sections.

## ✨ Features

- 📄 **PDF Upload:** Upload a research paper in PDF format.
- 📝 **Text Extraction:** Extract readable text from PDF documents.
- 🎯 **Research Aim:** Identify sentences related to the research objective.
- ⚙️ **Methodology:** Find sentences describing methods, models, and datasets.
- 💡 **Key Findings:** Identify sentences related to results and findings.
- ⚠️ **Limitations:** Find sentences mentioning limitations and future work.
- 📖 **Basic Glossary:** Explain selected AI and machine learning terms.
- 🌐 **Web Interface:** Use the application through a browser.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Regular Expressions
- GitHub

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yogalakshmij267/AI-Research-Paper-Reading-Assistant.git
   ```

2. Open the project folder:

   ```bash
   cd AI-Research-Paper-Reading-Assistant
   ```

3. Install the required packages:

   ```bash
   py -m pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   py -m streamlit run app.py
   ```

5. Open the local URL displayed in the terminal.

## 🚀 How to Use

1. Open ResearchMate AI.
2. Upload a research paper PDF.
3. Review the extracted text.
4. Click **Analyze Research Paper**.
5. Explore the research aim, methodology, key findings, limitations, and available glossary terms.

## 🔄 Project Workflow

PDF Upload → Text Extraction → Keyword-Based Analysis → Results Display

## ⚠️ Current Limitations

- The current prototype uses keyword-based sentence extraction.
- It does not use a connected AI language model.
- Extracted sentences may appear in the wrong section or may miss relevant information.
- Scanned PDFs without an extractable text layer may not work correctly.
- The glossary covers only predefined terms.

Users should verify all extracted information against the original research paper.

## 🔮 Future Enhancements

- AI-powered summarization using a language model.
- Comparison of multiple research papers.
- Automatic glossary generation.
- Downloadable analysis reports.
- Improved handling of scanned PDFs.

## 🎓 Expected Outcome

A beginner-friendly research assistant prototype that helps undergraduate students navigate research papers and locate important information efficiently.

## 👩‍💻 Project Repository

[AI Research Paper Reading Assistant on GitHub](https://github.com/yogalakshmij267/AI-Research-Paper-Reading-Assistant)

---

**Note:** ResearchMate AI is an educational prototype and should not replace reading and verifying the original research paper.
