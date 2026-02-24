import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="KontextWerk",
    page_icon="🧭",
    layout="centered",
)

# --- Header ---
st.title("KontextWerk")
st.caption("AI prototypes • RAG systems • Knowledge interfaces")
st.write("")

st.markdown(
    """
I build practical Retrieval-Augmented Generation (RAG) demos and knowledge-based AI prototypes.
This page is a small portfolio hub with links to selected projects.
"""
)

st.write("---")

# --- Projects ---
st.subheader("Demos")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Mietrecht (DE)**")
    st.write("Prototype for structured Q&A and first orientation on common rental law questions.")
    st.link_button("Open demo", "https://mietrecht-uhxkybmnijgv8kk4t72pru.streamlit.app/")

with col2:
    st.markdown("**Politik Chatbot (DE)**")
    st.write("RAG demo for exploring political documents and answering questions with sources.")
    st.link_button("Open demo", "https://rag-politik-demo-9hvadctrythe3q9v5f9qlf.streamlit.app/")

st.write("---")

# --- About / services ---
st.subheader("What I do")
st.markdown(
    """
- **RAG prototyping** (chunking, metadata, retrieval, evaluation)
- **Document pipelines** (PDF extraction, cleaning, indexing)
- **Demo apps** (Streamlit) for non-technical stakeholders
"""
)

st.subheader("Contact")
st.markdown(
    """
- **Name:** Lena Geller  
- **Email:** _lena.geller@gmx.de_  
- **LinkedIn:** _https://www.linkedin.com/in/lena--geller/_
"""
)

st.write("")
st.caption("© KontextWerk")