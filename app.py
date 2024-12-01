from flask import Flask , render_template,jsonify,request
from controller import predict , cleanText
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) 
def prediction():
   data = request.json
   text = data.get('text','')
   if not text:
        return jsonify({"error": "Text input is required"}), 400
   cleanData = cleanText(text)
   return jsonify({'prediction':predict(cleanData)})

if __name__  == "__main__":
    app.run()
