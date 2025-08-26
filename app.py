import streamlit as st
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
### Nagraj swój głos lub wgraj plik audio/video
                ''')