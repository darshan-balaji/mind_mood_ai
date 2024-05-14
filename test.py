import joblib

# Load the saved pipeline
pipeline_file = open("emotion_classifier_pipe_lr.pkl", "rb")
loaded_pipe_lr = joblib.load(pipeline_file)
pipeline_file.close()

pred = loaded_pipe_lr.predict(['i am happy'])
print(pred)