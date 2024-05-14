# Mind-Mood AI

Welcome to Mind-Mood AI, an NLP-based AI chatbot designed to analyze user sentiments and act as an aid to therapists in better understanding their patients. This project utilizes cutting-edge technologies such as BERT for sentiment analysis, the OpenAI API for accessing GPT-based models to generate responses, Gradio for the front-end user interface, and Whisper for voice-to-text conversion.

## Features
- **Sentiment Analysis:** Mind-Mood AI employs BERT, a state-of-the-art NLP model, to classify user sentiments.
- **Therapist Assistance:** The chatbot assists therapists in understanding their patients' emotions and concerns through natural conversation.
- **GPT-based Responses:** Utilizing the OpenAI API, Mind-Mood AI generates responses using GPT-based models, providing human-like interactions.
- **User-friendly Interface:** Gradio powers the intuitive front-end UI, enabling seamless interaction with the chatbot.
- **Voice Input:** With Whisper, users can conveniently input text via voice, enhancing accessibility.

## Setup
To run the Mind-Mood AI project, follow these steps:

1. **Clone the Repository:** Clone the Mind-Mood AI repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/username/Mind-Mood-AI.git
   ```

2. **Install Dependencies:** Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate API Key:** Obtain your API key from OpenAI. Visit [OpenAI API](https://beta.openai.com/signup/) to sign up and generate your API key.

4. **Configure API Key:** Open the `chatbot.py` script and enter your API key in the designated placeholder:
   ```python
   # Replace 'YOUR_API_KEY' with your actual OpenAI API key
   openai.api_key = 'YOUR_API_KEY'
   ```

5. **Run the Application:** Execute the `main.py` script to start the Mind-Mood AI chatbot:
   ```bash
   python main.py
   ```

6. **Interact:** Access the chatbot interface through your web browser and start interacting with Mind-Mood AI!

---

Feel free to reach out if you have any questions or need assistance in setting up Mind-Mood AI. Happy chatting!
