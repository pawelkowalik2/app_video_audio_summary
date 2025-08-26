import streamlit as st
from audiorecorder import audiorecorder
from io import BytesIO

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
    st.markdown('''
### Nagraj swój głos
                ''')
    
    audio_note = audiorecorder(
        'Nagraj wiadomość',
        'Zatrzymaj nagrywanie'
    )

    if audio_note:
        audio = BytesIO()
        audio_note.export(audio, 'mp3')
        audio_note_bytes = audio.getvalue()
        st.audio(audio_note_bytes, format='audio/mp3')
    
    st.markdown('''
### lub prześlij plik .mp3 lub .mp4
            ''')

    uploaded_file = st.file_uploader('', ['mp3', 'mp4'], False)
