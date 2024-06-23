import os
import requests
import streamlit as st
from io import BytesIO
from transformers import pipeline 
from pydub import AudioSegment 


def transcribe_audio(file):
    try:
        response = requests.post("http://localhost:8000/transcribe/", files={'file': file})
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to summarize text using Hugging Face transformers
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function convert audio to WAV format
def convert_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    wav_io = BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)
    return wav_io

st.title("Audio Transcription, Summarization and Timestamps App")

# uploader the audio file to user
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a", "flac"])

if uploaded_file is not None:
    wav_file = convert_to_wav(uploaded_file)
    
    with st.spinner('Transcribing...'):
        data = transcribe_audio(wav_file)
        
        if data:
            transcription = data.get("transcription")
            segments = data.get("segments")

            st.subheader("Transcription")
            st.write(transcription)

       
            transcription_file = "transcription.txt"
            with open(transcription_file, "w", encoding="utf-8") as file:
                file.write(transcription)

            st.success(f"Transcription saved as {transcription_file}")

     
            summarized_text = summarize_text(transcription)
            
            st.subheader("Summary")
            st.write(summarized_text)
            
            summary_file = "summary.txt"
            with open(summary_file, "w", encoding="utf-8") as file:
                file.write(summarized_text)
            
            st.success(f"Summary saved as {summary_file}")
            st.subheader("Timestamps")
            for segment in segments:
                start = segment['start']
                end = segment['end']
                text = segment['text']
                st.write(f"[{start:.2f}s - {end:.2f}s]: {text}")
          
            timestamps_file = "timestamps.txt"
            with open(timestamps_file, "w", encoding="utf-8") as file:
                for segment in segments:
                    start = segment['start']
                    end = segment['end']
                    text = segment['text']
                    file.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
            
            st.success(f"Timestamps saved as {timestamps_file}")             

else:
    st.write("Please upload an audio file.")
