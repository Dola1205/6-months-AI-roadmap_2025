import streamlit as st
from gtts import gTTS
from googletrans import Translator

# Streamlit App
st.title("🌐 Text Translator and Speech Generator")

# Step 1: Input text
text_input = st.text_area("Enter your text:", height=150)

# Step 2: Language selection
lang_dict = {
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "English": "en",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Urdu": "ur",
    "Punjabi": "pa"
}

language = st.selectbox("Choose the language you want to convert to:", list(lang_dict.keys()))
target_lang = lang_dict[language]

# Step 3: Translate and Convert to Speech
if st.button("Translate and Speak"):
    if text_input.strip() != "":
        try:
            translator = Translator()
            translated = translator.translate(text_input, dest=target_lang)
            st.success(f"Translated Text ({language}):")
            st.write(translated.text)

            # Convert to speech
            tts = gTTS(text=translated.text, lang=target_lang)
            tts.save("translated_speech.mp3")

            # Play audio
            audio_file = open("translated_speech.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter some text.")
