import streamlit as st
import json
import os

st.set_page_config(
    page_title="Portfolio – Ben Cheick",
    layout="wide",
    page_icon="💻"
)

st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stButton > button {
        background-color: #4A90E2;
        color: white;
    }
    .css-1v0mbdj {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)


data_path = os.path.join(os.path.dirname(__file__), './data/projects.json')
with open(data_path) as f:
    projects = json.load(f)

col1, col2 = st.columns([1, 4])
img_path = os.path.join(os.path.dirname(__file__), 'assets/flox.jpg')
with col1:
    st.image(img_path, width=200)  
with col2:
    st.title("Ben Cheick")
    st.markdown(
        "<span style='font-size:20px; font-family: Monteserrat;'>👨‍💻 Software engineer passionate about AI, Machine Learning, data engineering, and mobile development, " \
        "which I have made my core focus..</span>",
        unsafe_allow_html=True
    )


with open("assets/KANAZOE_Ben-Cheick-Oumarou.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Télécharger mon CV",
    data=PDFbyte,
    file_name="Ben_Cheick_CV.pdf",
    mime='application/pdf',
    use_container_width=True
)

st.markdown("---")

st.subheader("📁 Projets")
for project in projects:
    with st.container():
        st.markdown(f"### {project['title']}")
        st.write(project['description'])
        st.markdown("**Technos :** " + ", ".join(project['technologies']))
        st.markdown(f"[🔗 Voir sur GitHub]({project['link']})")
        st.markdown("---")

st.subheader("📬 Me contacter")

with st.form("contact_form"):
    name = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    subject = st.text_input("Sujet")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Envoyer")
    if submitted:
        st.success("Merci pour ton message ! Je te reviens vite.")

# Footer
st.markdown("---")
st.write("📧 Email direct : [bencheickoumarouk@gmail.com](mailto:bencheickoumarouk@gmail.com)")
st.write("🔗 LinkedIn : [linkedin.com/in/bencheick](https://www.linkedin.com/in/ben-cheick-kanazoe)")
