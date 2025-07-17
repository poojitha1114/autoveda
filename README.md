# AutoVeda 🎬📚

AutoVeda is an AI-powered content generator designed for automating YouTube video production in the educational domain. Perfect for platforms like Vedantu that scale with 1000+ videos monthly.

## 🔥 Features
- AI-generated scripts based on subject/topic
- Metadata generation (title, description, tags)
- Download-ready output for YouTube upload
- Streamlit UI for easy use

## 📦 Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Dependencies
- OpenAI GPT (for script + metadata)
- Streamlit

Create a `.streamlit/secrets.toml` file:
```
[general]
OPENAI_API_KEY = "your_openai_api_key"
```

## 🚀 Example Input
- Subject: Class 10 Physics
- Topic: Light – Reflection and Refraction

## 🎯 Outputs
- 📜 Educational script (3-min)
- 📝 YouTube metadata (JSON)

---
