from fastapi import FastAPI 
from pydantic import BaseModel 
import joblib 
nb = joblib.load('nb.pkl')

vectorizer = joblib.load('cv.pkl')  


app=FastAPI(title='Spam Classifier') 

class SMSRequest(BaseModel):
    message:str 


@app.get('/home')
def home():
    return {"Spam Classifier"}

# Define prediction endpoint
@app.post("/predict/")
def predict_spam(request: SMSRequest):
    # Transform the input message
    message_vectorized = vectorizer.transform([request.message])
    
    # Predict
    prediction = nb.predict(message_vectorized)
    
    # Return response
    return {"message": request.message, "prediction": "Spam" if prediction[0] == 1 else "Not Spam"}

# Run using: uvicorn filename:app --reload      