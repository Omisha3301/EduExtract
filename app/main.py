import streamlit as st
from pipeline import process_syllabus

st.set_page_config(page_title="EduMapr", layout="wide")
st.title("EduMapr: AI-Powered Syllabus Analyzer")

uploaded_file = st.file_uploader("Upload your Syllabus PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing the syllabus..."):
        summary, sequence, prerequisites, books = process_syllabus(uploaded_file)

    if isinstance(summary, str) and summary.startswith("The uploaded PDF does not appear"):
        st.error(summary)
    else:
        st.subheader("📘 Course Summary")
        st.markdown(summary)

        st.subheader("🔗 Learning Sequence")
        for i, topic in enumerate(sequence, 1):
            st.markdown(f"**{i}. {topic}**")

        st.subheader("⚙️ Prerequisites")
        st.markdown(", ".join(prerequisites) if prerequisites else "No specific prerequisites found.")
        st.subheader("📚 Recommended Books")
        for book in books:
            st.markdown(f"### [{book['title']}]({book['url']})")
            st.image(book["image"], width=150)
            st.markdown(f"**Author**: {book['author']}")
            st.markdown(f"**Price**: {book['price']}")
            st.markdown("---")
