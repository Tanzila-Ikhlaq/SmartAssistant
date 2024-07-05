# SmartAssistant Streamlit Application

This Streamlit application integrates Google's Generative AI models for various functionalities, including image captioning, question answering, and YouTube video summarization.

## Features

- **Image Captioning:** Upload an image and generate a caption using Google Gemini Vision model.
- **Ask Bot:** Ask questions and receive responses using Google Gemini model.
- **YouTube Video Summariser:** Enter a YouTube URL to summarize its transcript using Google Gemini model.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/smartassistant-streamlit.git
   cd smartassistant-streamlit
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   - Create a `.env` file in the project root.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## Technologies Used

- **Streamlit:** Web framework for building interactive web applications.
- **Google Generative AI:** API for generating text and captions.
- **PIL (Pillow):** Python Imaging Library for handling images.
- **youtube-transcript-api:** Python library to fetch YouTube video transcripts.

## Screenshots

![Screenshot 1](https://github.com/Tanzila-Ikhlaq/SmartAssistant/assets/141930681/6716c353-4cca-4ab3-bbae-69c5bb668c97)

![Screenshot 2](https://github.com/Tanzila-Ikhlaq/SmartAssistant/assets/141930681/bdc40d06-71d7-40d1-89c6-857f5b61a6c2)

![Screenshot 3](https://github.com/Tanzila-Ikhlaq/SmartAssistant/assets/141930681/39a4e2a9-e544-4cfd-9bb3-e5b5d951c873)
