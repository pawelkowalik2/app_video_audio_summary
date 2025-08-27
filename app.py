import streamlit as st
from audiorecorder import audiorecorder
from io import BytesIO
from dotenv import dotenv_values
from openai import OpenAI
from pydub import AudioSegment

env = dotenv_values('.env')
AUDIO_TRANSCRIBE_MODEL='whisper-1'

def get_openai_client():
    return OpenAI(api_key=st.session_state['openai_open_key'])

def transcribe_audio(audio_bytes):
    openai_client = get_openai_client()
    audio_file = BytesIO(audio_bytes)
    audio_file.name = 'audio.mp3'
    transcript = openai_client.audio.transcriptions.create(
        file=audio_file,
        model=AUDIO_TRANSCRIBE_MODEL,
        response_format='verbose_json'
    )

    return transcript.text

st.markdown('''
# 🎙️ Essenza – Twój osobisty asystent do streszczania audio i wideo  

Masz godzinny podcast, wykład albo nagranie spotkania i brak czasu, by wysłuchać wszystkiego?  
**Essenza zrobi to za Ciebie.**  
''')

tab_1, tab_2 = st.tabs(['Opis aplikacji', 'Aplikacja'])

with tab_1:
    st.markdown('''
    ## ✨ Co potrafi Essenza?  
    - 🔊 **Audio & Podcasty** – szybkie streszczenia rozmów, wykładów i nagrań głosowych.  
    - 🎥 **Wideo & Spotkania** – automatyczne podsumowania webinarów, wideokonferencji i filmów.  
    - ⚡ **Szybkość i precyzja** – w kilka chwil otrzymasz klarowne notatki, które możesz przeczytać lub odsłuchać.  
    - 🌍 **Wielojęzyczność** – streszczenia w wielu językach, idealne dla globalnych treści.  

    ---

    ## 🚀 Jak to działa?  
    1. **Podaj** swój klucz OpenAI
    2. **Wgraj** plik audio lub wideo LUB **Nagraj** się.  
    3. **Otrzymaj** gotowe streszczenie w formie tekstu lub krótkiego nagrania audio.  

    ---

    👉 Zamiast tracić czas na przewijanie – poznaj sedno treści w kilka minut.  

    **Essenza – bo liczy się to, co najważniejsze.**
    ''')

with tab_2:
    if not st.session_state.get('open_api_key'):
        if "OPENAI_API_KEY" in env:
            st.session_state['open_api_key'] = env["OPENAI_API_KEY"]
        
        else: 
            st.info('Żeby korzystać z tej aplikacji potrzebujesz klucza API OpenAI')
            st.session_state['open_api_key'] = st.text_input('OpenAI API KEY', type='password')
            if st.session_state['open_api_key']:
                st.rerun()
    
    if not st.session_state.get('open_api_key'):
        st.stop()

    st.write('### Nagraj swój głos')

    if 'audio_to_transcribe' not in st.session_state:
        st.session_state['audio_to_transcribe'] = None
    if 'audio_text' not in st.session_state:
        st.session_state['audio_text'] = ''

    source_label = None
    audio_note_bytes = None
    audio_from_file = None

    audio_note = audiorecorder('Nagraj wiadomość', 'Zatrzymaj nagrywanie')

    if audio_note:
        audio = BytesIO()
        audio_note.export(audio, 'mp3')
        audio_note_bytes = audio.getvalue()
        st.audio(audio_note_bytes, format='audio/mp3')
        source_label = 'Nagranie'
        st.session_state['audio_to_transcribe'] = audio_note_bytes

    st.write('### lub prześlij plik .mp3 lub .mp4')

    uploaded_file = st.file_uploader('', ['mp3', 'mp4'], False)
    if uploaded_file:
        file_bytes = uploaded_file.read()
        source_label = 'Plik'

        if uploaded_file.type.startswith("audio"):
            st.audio(file_bytes, format=uploaded_file.type)
            audio_from_file = file_bytes

        elif uploaded_file.type.startswith("video"):
            st.video(file_bytes)
            video_file = BytesIO(file_bytes)
            audio_segment = AudioSegment.from_file(video_file, format="mp4")
            audio = BytesIO()
            audio_extracted = audio_segment.export(audio, format='mp3')
            audio_segment_bytes= audio_extracted.getvalue()
            audio_from_file = audio_segment_bytes
            
        st.session_state['audio_to_transcribe'] = audio_from_file


    if audio_note and uploaded_file:
        source_label = st.radio(
            'Wybierz z którego źródła mam wygenerować podsumowanie:',
            ['Nagranie', 'Plik']
        )

        st.session_state['audio_to_transcribe'] = audio_note_bytes if source_label == 'Nagranie' else audio_from_file

    if st.session_state['audio_to_transcribe'] is not None:
        if st.button('Podsumuj'):
            st.session_state['audio_text'] = transcribe_audio(st.session_state['audio_to_transcribe'])

    if st.session_state['audio_text']:
        st.text_area(
            'Transkrypcja audio',
            value = st.session_state['audio_text'],
            disabled = True
        )