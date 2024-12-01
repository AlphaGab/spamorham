import joblib
import re

model = joblib.load('models/random_forest_model2.pkl')
vectorizer = joblib.load('models/vectorizer2.pkl')


def predict(text,threshold=0.7):
   input_vector = vectorizer.transform([text])
   probabilities = model.predict_proba(input_vector)
   spam_probability = probabilities[0, 1]
   print(spam_probability)
   if spam_probability >= threshold:
     return "spam"
   else:
     return "ham"
def cleanText(text):
  txt = re.sub(r'[^a-zA-Z\s]', '', text).lower()
  return txt