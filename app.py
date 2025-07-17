import streamlit as st
import openai
import json
from datetime import datetime

# Set your API key (you can use secrets for production)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else ""

st.set_page_config(page_title="AutoVeda - YouTube Content Generator", layout="centered")
st.title("📺 AutoVeda: AI-Powered YouTube Content Generator")

st.markdown("""
Welcome to AutoVeda! Generate educational scripts, metadata, and content ideas with a single click. Perfect for scaling YouTube education content at Vedantu.
""")

subject = st.text_input("Enter Subject (e.g., Class 10 Physics)")
topic = st.text_input("Enter Topic (e.g., Light – Reflection and Refraction)")
language = st.selectbox("Select Language", ["English", "Hindi"])
tone = st.selectbox("Select Script Tone", ["Energetic", "Conversational", "Professional"])

if st.button("🚀 Generate Content"):
    if subject and topic:
        with st.spinner("Thinking and generating..."):
            prompt = f"""
You are an expert YouTube scriptwriter for educational content.
Generate a 3-minute script in {language} in a {tone} tone for the topic: '{topic}' under the subject '{subject}'.
Make it suitable for school students, with examples and engaging language. Add a call to action at the end.
"""

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}]
                )
                script = response['choices'][0]['message']['content']

                # Metadata
                title = f"{topic} | {subject} Explained with Animations"
                description = f"Learn about {topic} in this quick and engaging video, specially designed for {subject} students. 🔔 Subscribe for more lessons!"
                tags = [topic, subject, "Vedantu", "Educational", "YouTube", "CBSE"]
                metadata = {
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "language": language,
                    "category": "Education"
                }

                # Display and download
                st.subheader("📜 Generated Script")
                st.text_area("Script", script, height=300)
                st.download_button("📥 Download Script", script, file_name="script.txt")

                st.subheader("📦 Video Metadata")
                st.json(metadata)
                st.download_button("📥 Download Metadata", json.dumps(metadata, indent=4), file_name="metadata.json")

            except Exception as e:
                st.error(f"Error generating content: {e}")
    else:
        st.warning("Please fill in both Subject and Topic.")
