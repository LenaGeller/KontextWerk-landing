import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="KontextWerk",
    page_icon="🧭",
    layout="centered",
)

# HERO
st.title("KontextWerk")
st.markdown(
    "<h3 style='color: grey;'>AI • RAG • Knowledge Systems</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
Designing structured AI interfaces for complex documents and knowledge domains.
"""
)

st.write("")

colA, colB = st.columns([1,1])
with colA:
    st.link_button("Explore Mietrecht Demo",
                   "https://mietrecht-uhxkybmnijgv8kk4t72pru.streamlit.app/")
with colB:
    st.link_button("Explore Politik Demo",
                   "https://rag-politik-demo-9hvadctrythe3q9v5f9qlf.streamlit.app/")

st.write("---")

# ABOUT
st.subheader("What I build")

st.markdown("""
- Retrieval-Augmented Generation (RAG) prototypes  
- Structured document pipelines (PDF → cleaned → indexed)  
- AI demos for public sector and complex domains  
""")

st.write("---")

# CONTACT
st.subheader("Contact")

st.markdown("""
**Lena Geller**  
Berlin  

📩 lena.geller@gmx.de  
🔗 https://www.linkedin.com/in/lena--geller/
""")

st.write("")
st.caption("© KontextWerk")
