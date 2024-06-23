# Audio Transcription and Summarization with FastAPI

## Project Description

This project involves developing a system that processes audio files to transcribe their content, generate summaries of the transcriptions, and extract timestamps of key events or changes in content. The system will be built using FastAPI for handling asynchronous endpoints, ensuring efficient handling of potentially large audio files

## Features

- Upload an audio file to receive a transcription.
- Obtain a summary of the transcribed text.
- Receive timestamps for each word in the transcription.

## Requirements

- Openai-whisper
- FastAPI
- Uvicorn
- tiktoken
- numba
- streamlit
- torch
- numpy

##Technologies Used

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Streamlit: An open-source app framework for Machine Learning and Data Science projects.
- Whisper: A powerful speech recognition model.
- Hugging Face Transformers: A library of state-of-the-art pre-trained models for Natural Language Processing tasks.

## Installation
    
1. Install the required packages:
    ```bash
     pip install -r requirements.txt
    ```

2. Install FFmpeg:
    - Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
    - Download the appropriate version for your operating system.
    - Follow the instructions to install FFmpeg and add it to your system's PATH.

## Usage

1. Start the FastAPI server:
    ```bash
   python fastapi_backend.py
    ```

2. Start the Streamlit Application:
    ```bash
   streamlit run frontend.py
    ```

3. Upload an audio file :
    - Use the `Browse files` endpoint to upload an audio file and receive the transcription, summary, and timestamps.

##Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

##Acknowledgments
  Whisper by OpenAI for speech recognition. Hugging Face for the BART summarization model. The Streamlit and FastAPI communities for their excellent frameworks.

Directory Structure in VSCode:


├── fastapi_backend.py             # Main FastAPI application

├── frontend.py                      #Fronend Streamlit Application

├── requirements.txt         # List of required Python packages

├── transcription.txt       # To store the transcription files generated for each audio file processed by the API

├── timestamps.txt       # To store the timestamps files generated for each audio file processed by the API

├── summary.txt         # To store the summary files generated for each audio file processed by the API
      
