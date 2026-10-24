
import streamlit as st
import re

st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ResearchMate AI")
st.subheader("AI Research Paper Reading Assistant")
st.write("Understand research papers in simple language.")


uploaded_pdf = st.file_uploader(
    "Or upload a research paper PDF",
    type=["pdf"]
)

if uploaded_pdf is not None:
    try:
        import pypdf
        pdf_reader = pypdf.PdfReader(uploaded_pdf)
        pdf_text = "\n".join(
            page.extract_text() or ""
            for page in pdf_reader.pages
        )
        st.success("PDF uploaded successfully!")
        st.text_area(
            "Extracted PDF text",
            value=pdf_text,
            height=200
        )
    except Exception as e:
        st.error(f"Could not read PDF: {e}")

paper_text = st.text_area(
    "Paste your research paper text here",
    height=250,
    placeholder="Paste the abstract or research paper text..."
)

def extract_sentences(text, keywords):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    matches = [
        sentence for sentence in sentences
        if any(word in sentence.lower() for word in keywords)
    ]
    if matches:
        return "\n\n".join(matches[:3])
    return "No clear sentence found. Please review the paper manually."

if uploaded_pdf is not None:
    paper_text = pdf_text

if st.button("Analyze Research Paper", type="primary"):
    if paper_text.strip():
        st.header("📝 Research Paper Analysis")

        sections = {
            "🎯 Research Aim": [
                "aim", "objective", "purpose", "investigate",
                "examines", "study"
            ],
            "⚙️ Methodology": [
                "method", "model", "algorithm", "dataset",
                "experiment", "approach", "used"
            ],
            "💡 Key Findings": [
                "results", "findings", "improve", "increased",
                "decreased", "suggest", "show"
            ],
            "⚠️ Limitations": [
                "limitation", "challenge", "however",
                "future work", "small dataset", "drawback"
            ]
        }

        for heading, keywords in sections.items():
            st.subheader(heading)
            st.write(extract_sentences(paper_text, keywords))

        st.info(
            "This prototype extracts relevant sentences using keywords. "
            "It does not yet use an AI language model. "
            "Verify the extracted information against the original paper."
        )
    else:
        st.warning("Please paste research paper text first.")

st.divider()
st.caption("ResearchMate AI | Undergraduate Research Support Prototype")
