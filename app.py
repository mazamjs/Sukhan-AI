
import streamlit as st
# Backend integration
from backend.poetry_generator import generate_poetry

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Sukhan AI | Urdu Poetry",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
    
@import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background: #121212;
    color: #F5F0E8;
    font-family: 'Poppins', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1A1A1A;
    border-right: 1px solid #383027;
}

/* Hero */
.hero {
    text-align: center;
    padding: 35px 10px 25px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 700;
    background: linear-gradient(90deg, #D6AD60, #F5D99B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #B5AA98;
    font-size: 16px;
}

/* Poetry Card */
.poetry-card {
    background: #1E1E1E;
    border: 1px solid #705A35;
    border-radius: 18px;
    padding: 30px;
    margin-top: 25px;
    text-align: center;
}

.poetry-title {
    color: #D6AD60;
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 20px;
}

/* Urdu Poetry */
.poetry-text {
    font-family: 'Noto Nastaliq Urdu', serif;
    direction: rtl;
    text-align: center;
    color: #F5EBDD;
    font-size: 23px;
    line-height: 2.5;
    white-space: pre-wrap;
}

/* Input Fields */
.stSelectbox > div > div,
.stTextArea textarea {
    background-color: #292929;
    color: #F5F0E8;
    border: 1px solid #454039;
    border-radius: 10px;
}

.stSelectbox > div > div:focus-within,
.stTextArea textarea:focus {
    border-color: #C49A52;
    box-shadow: 0 0 0 1px #C49A52;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #B68A43, #D6AD60);
    color: #17130D;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    width: 100%;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #D6AD60, #E8C995);
    color: #17130D;
    border: 1px solid #F0D49C;
}

/* Download Button */
.stDownloadButton > button {
    background: #292929;
    color: #D6AD60;
    border: 1px solid #A98549;
    border-radius: 10px;
}

.stDownloadButton > button:hover {
    background: #383027;
    color: #F5D99B;
    border-color: #D6AD60;
}

/* Footer */
.footer {
    text-align: center;
    color: #898175;
    padding: 35px 0 10px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## ✍️ Sukhan AI")

    st.caption("Your Personal Urdu Poetry Companion")

    st.divider()

    st.markdown("### About")

    st.write(
        "Sukhan AI is an AI-powered Urdu poetry "
        "generator that creates meaningful poetry "
        "based on your emotions and imagination."
    )

    st.divider()

    st.markdown("### Poetry Types")

    st.write("• Ghazal")
    st.write("• Nazm")
    st.write("• Sher")
    st.write("• Short Poetry")

    st.divider()

    st.caption("Powered by Groq & LangChain")


# ---------------- MAIN HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>Sukhan AI</h1>
    <p>Alfaaz ko ehsaas mein badalne ka aik safar</p>
    <p>Express your emotions through Urdu poetry.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- POETRY INPUT SECTION ----------------

st.markdown("### Create Your Poetry")

col1, col2 = st.columns(2)

with col1:

    poetry_type = st.selectbox(
        "Select Poetry Type",
        ["Ghazal", "Nazm", "Sher", "Short Poetry"]
    )

with col2:

    theme = st.selectbox(
        "Select Poetry Theme",
        [
            "Love",
            "Sadness",
            "Separation",
            "Loneliness",
            "Hope",
            "Friendship"
        ]
    )

instructions = st.text_area(
    "Additional Instructions",
    placeholder="Describe your feelings or the topic you want poetry about...",
    height=120
)

# ---------------- GENERATION ----------------

if st.button("✦ Generate Poetry"):

    with st.spinner("Sukhan AI is composing your poetry..."):

        try:

            poetry = generate_poetry(
                poetry_type=poetry_type,
                theme=theme,
                instructions=instructions
            )

            if not poetry or not str(poetry).strip():
                st.warning("No poetry was generated. Please try again.")

            else:

                st.session_state["poetry"] = str(poetry)
                st.session_state["poetry_type"] = poetry_type
                st.session_state["theme"] = theme

        except Exception as e:

            st.error(f"Something went wrong: {str(e)}")


# ---------------- OUTPUT SECTION ----------------

if "poetry" in st.session_state:

    st.markdown("---")

    st.markdown(
        f"""
        <div class="poetry-card">
            <div class="poetry-title">
                Your {st.session_state["poetry_type"]}
            </div>
            <div class="poetry-text">
                {st.session_state["poetry"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.download_button(
        label="Download Poetry",
        data=st.session_state["poetry"],
        file_name="sukhan_ai_poetry.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button("Generate Another Poetry"):
        del st.session_state["poetry"]
        st.rerun()


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    Made with AI and Poetry | Sukhan AI © 2026
</div>
""", unsafe_allow_html=True)
