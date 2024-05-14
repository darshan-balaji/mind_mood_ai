import gradio as gr
import whisper_app

from openai import OpenAI
import gradio as gr

from typing import Optional
import gradio as gr
import joblib

# Load the saved pipeline
pipeline_file = open("emotion_classifier_pipe_lr.pkl", "rb")
loaded_pipe_lr = joblib.load(pipeline_file)
pipeline_file.close()

with open('conversation.txt','w') as fp:
    pass

def predict_emotion(text):
    pred = loaded_pipe_lr.predict([text])
    return pred[0]

client = OpenAI(
    api_key="",
)

class Chat:

    def __init__(self, system: Optional[str] = None):
        self.system = system
        self.messages = []

        if system is not None:
            self.messages.append({
                "role": "system",
                "content": system
            })

    def prompt(self, content: str) -> str:
          self.messages.append({
              "role": "user",
              "content": content
          })
          response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=self.messages,
                temperature=0
            )
        #   print(response)
          response_content = response.choices[0].message.content
          self.messages.append({
              "role": "assistant",
              "content": response_content
          })
          return response_content
      
      
system_prompt = "You are a helpful assistant. You need to act as a psychologist and provide appropriate diagnosis while you keep your answers short and precise. You have to detect user's emotion from text and your role is to analyze the emotion conveyed in the user's text and offer suitable activities and uplifting quotes accordingly to brighten their mood. You should also prompt for follow up questions based on your answers to further analyse the user's feelings. While reponding, any response must be preceeded by the following text 'Predicted motion: <enter the detected emotion of the user here>', the detected emotion can be one of the following: neutral, joy, surprise, fear, anger, sadness, shame, anxiety, lonliness "
      
chat = Chat(system=system_prompt)

with gr.Blocks() as demo:
    header = gr.Markdown(
    """
    # Welcome to MIND-MOOD AI
    How are you feeling today?
    """)
    
    chatbot = gr.Chatbot(value=[[None, "You can open up about your feelings here.."]])
    download_button = gr.DownloadButton(value='conversation.txt')
    with gr.Row():
        msg = gr.Textbox(label="Write your query here..")
        audio = gr.Audio(sources="microphone", type="filepath")
    submit_btn = gr.Button(value='submit')
    clear = gr.ClearButton([msg,chatbot,audio])
    

    def respond(message, audio , chat_history):
        if audio:
            message = whisper_app.transcribe(audio)
        bot_message = chat.prompt(content=message)
        # print(len(chat_history))
        if len(chat_history) == 1:
            pred = predict_emotion(message)
            s = f'Predicted emotion: {pred}\n\n' 
            bot_message = s + bot_message
        chat_history.append((message, bot_message))

        with open('conversation.txt','a+') as fp:
            fp.write(f'user: {message}\n\nbot: {bot_message}\n\n')
        
        return "", gr.Audio(sources="microphone", type="filepath",value=None), chat_history, gr.DownloadButton(value='conversation.txt')
    
    submit_btn.click(respond, [msg, audio, chatbot], [msg, audio, chatbot, download_button])

# demo.launch(allowed_paths=["."])
demo.launch(allowed_paths=["."])
