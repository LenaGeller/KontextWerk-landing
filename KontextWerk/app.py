import streamlit as st

st.set_page_config(
    page_title="KontextWerk",
    page_icon="🧠",
    layout="centered",
)

# ---- Custom Color Styling ----
st.markdown("""
    <style>
        h1 {
            color: #0B3D91;   /* dunkles Blau */
        }
        h3 {
            color: #4A6FA5;   /* helleres Blau */
        }
        .stLinkButton > a {
            background-color: #0B3D91;
            color: white !important;
            border-radius: 8px;
            padding: 0.6em 1em;
            text-decoration: none;
        }
        .stLinkButton > a:hover {
            background-color: #092C6C;
        }
    </style>
""", unsafe_allow_html=True)

# HERO
st.title("Kontext Vert")
st.markdown("<h3>AI • RAG • Knowledge Systems</h3>", unsafe_allow_html=True)

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
