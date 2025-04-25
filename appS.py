import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(api_key='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')

# Streamlit app setup
st.title("Live Audio Transcription Service")

# Audio recording section
st.header("Upload Your Audio File for Transcription")

# File uploader for audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file:
    st.write("Processing your audio file...")

    # Read the file contents
    file_contents = audio_file.read()

    # Call Groq API to transcribe the file
    try:
        transcription = client.audio.transcriptions.create(
            file=(audio_file.name, file_contents),
            model="whisper-large-v3",  # Use Whisper model for transcription
            prompt="transcribe it into text please in English",  # Optional
            response_format="json",  # Optional
            language="ur",  # Optional
            temperature=0.0  # Optional
        )

        # Display transcription result
        st.subheader("Transcription:")
        st.write(transcription.text)

    except Exception as e:
        st.error(f"An error occurred while transcribing the file: {str(e)}")

# Optionally: Add download button for audio file
if audio_file:
    st.download_button(
        label="Download the audio",
        data=file_contents,
        file_name=audio_file.name,
        mime="audio/mpeg"
    )
