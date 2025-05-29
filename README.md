# Multimodal AI Clinical Assistant (Ongoing Project)

**Smart Medical Chatbot with Vision and Voice**

---

## Project Overview

This project aims to build a **Multimodal AI Clinical Assistant** — an intelligent medical chatbot that understands and responds through **text, images, and voice**. It leverages the latest AI models to provide personalized healthcare assistance, combining medical knowledge with seamless multimodal interaction.

---

## Current Progress

- Integrated the **meta-llama/llama-4-maverick-17b-128e-instruct** multimodal LLM for advanced image and text understanding.
- Set up **OpenAI Whisper** for speech-to-text conversion enabling voice queries.
- Implemented initial **text-to-speech** functionality using **gTTS** and **ElevenLabs** for dynamic and realistic audio responses.
- Developed a basic **Gradio** app interface supporting multimodal inputs (text, image, and voice).

---

## What’s Next

- Improve and optimize multimodal interaction workflows.
- Enhance the clinical knowledge base for more accurate medical advice.
- Add real-time voice conversation capabilities with continuous speech recognition.
- Implement better error handling and context awareness for more natural dialogue.
- Explore deployment options for scalable and secure cloud hosting.
- Extend language support and accessibility features.

---

## Technologies

- **Meta LLaMA 4 Maverick 17B Multimodal Model** (text + image understanding)
- **OpenAI Whisper** (speech-to-text)
- **gTTS & ElevenLabs** (text-to-speech)
- **Gradio** (UI for multimodal interaction)

---

## Installation & Running

```bash
git clone https://github.com/yourusername/multimodal-ai-clinical-assistant.git
cd multimodal-ai-clinical-assistant
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
