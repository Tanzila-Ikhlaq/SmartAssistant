import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as gen
from PIL import Image
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# Load environment variables from a .env file
load_dotenv()

# Configure Google Generative AI with API key from environment variables
gen.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate a response from Google Gemini model based on a user question
def gemini_response(question):
    try:
        # Load the generative model
        model = gen.GenerativeModel("gemini-pro")
        # Generate content based on the input question
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}."

# Function to generate a caption for an image using Google Gemini Vision model
def gemini_vision_response(image, prompt):
    try:
        # Load the vision model
        model = gen.GenerativeModel("gemini-1.5-pro")
        # Generate content based on the image and prompt
        response = model.generate_content([image, prompt])
        return response.text
    except Exception as e:
        return f"Error: {e}."

# Function to get transcript text from a YouTube video
def get_transcript(video_url):
    try:
        # Parse the YouTube video URL
        url_data = urlparse(video_url)
        
        # Extract video ID from different formats of YouTube URLs
        if url_data.netloc == 'youtu.be':
            video_id = url_data.path[1:]
        elif url_data.netloc == 'www.youtube.com':
            query = parse_qs(url_data.query)
            video_id = query['v'][0]
        else:
            raise ValueError("Invalid YouTube URL format")
        
        # Get the transcript list for the video
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine transcript parts into a single string
        transcripts = ''
        for item in transcript_list:
            transcripts += item['text']
        
        return transcripts
    except Exception as e:
        return f"Error: {e}."

# Function to get a summary from Google Gemini model based on a video transcript and a prompt
def get_summary(video, prompt):
    try:
        # Load the generative model
        model = gen.GenerativeModel("gemini-pro")
        # Generate content based on the prompt and video transcript
        response = model.generate_content([prompt, video])
        return response.text
    except Exception as e:
        return f"Error: {e}."

# Prompt for summarizing YouTube videos
yt_prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points within 250 words."""

image_prompt = "Generate a caption for this image."

# Set Streamlit page configuration
st.set_page_config(
    page_title="SmartAssistant",
    page_icon="🤖",
)

# Main application logic
def main():
    # Set the main title of the app
    st.title(":rainbow[SmartAssistant]")

    # Sidebar selection box for different operations
    ans = st.sidebar.selectbox("Select Operation", ["Image Captioning", "Ask Bot", "YT Summariser"])

    # Ask Bot section
    if ans == "Ask Bot":
        st.header(":blue[Gemini Ask Bot 🤖]")

        # Input box for user to enter their question
        user_input = st.text_input("Enter your message: ")

        # Button to submit the question
        if st.button("Submit"):
            st.write("Generating...")
            if user_input:
                response = gemini_response(user_input)
                st.write(response)
            else:
                st.error("Please enter your message and click submit")

    # Image Captioning section
    if ans == "Image Captioning":
        st.header(":blue[Gemini Vision Image Captioning 🖼️]")

        # File uploader for user to upload an image
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            try:
                # Open and display the uploaded image
                image = Image.open(uploaded_file)
                st.image(uploaded_file, caption='Uploaded Image.', use_column_width=False)
                st.write("")
                st.write("Generated caption: ")
                caption = gemini_vision_response(image,image_prompt)
                st.write(caption)
            except Exception as e:
                st.error(f"Error: {e}")

    # YouTube Summariser section
    if ans == "YT Summariser":
        st.header(":blue[YouTube Video Summariser 📹]")
        
        # Input box for user to enter the YouTube URL
        link = st.text_input("Provide the YouTube URL: ")
        
        # Button to trigger summarization
        if st.button("Summarise") and link:
            try:
                # Get the transcript of the video
                video_transcript = get_transcript(link)
                # Extract the video ID for the thumbnail
                url_data = urlparse(link)
                if url_data.netloc == 'youtu.be':
                    video_id = url_data.path[1:]
                elif url_data.netloc == 'www.youtube.com':
                    query = parse_qs(url_data.query)
                    video_id = query['v'][0]
                else:
                    raise ValueError("Invalid YouTube URL format")
                # Get the summary of the video
                summary = get_summary(video_transcript, yt_prompt)
                # Display the thumbnail and summary
                st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")

# Run the main application
if __name__ == "__main__":
    main()
