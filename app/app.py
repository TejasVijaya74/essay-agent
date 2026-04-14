import streamlit as st
import requests

st.set_page_config(page_title="Essay Agent", layout="centered")

st.title("🎓 College Essay Agent")

# Form
with st.form("essay_form"):
    interests = st.text_area("Interests")
    achievements = st.text_area("Achievements")
    challenges = st.text_area("Challenges")
    goals = st.text_area("Goals")

    tone = st.selectbox("Tone", ["storytelling", "formal", "bold"])

    submit = st.form_submit_button("Generate Essay")

if submit:
    with st.spinner("Generating your essay..."):

        response = requests.post(
            "http://127.0.0.1:8000/api/generate-essay",
            json={
                "student_profile": {
                    "interests": interests,
                    "achievements": achievements,
                    "challenges": challenges,
                    "goals": goals
                },
                "tone": tone
            }
        )

        result = response.json()

        st.subheader("📄 Generated Essay")
        st.write(result["essay"])

        # Download DOCX
        with open(result["docx_path"], "rb") as file:
            st.download_button(
                label="📥 Download DOCX",
                data=file,
                file_name="essay.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )