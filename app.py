from flask import Flask, render_template, request
from test import TextToNum
import pickle
import traceback
import os

app = Flask(__name__)

# Function to load pickled objects safely
def load_pickle(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found!")
        return None
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None

# Load vectorizer and model at the start to avoid repeated loading
vectorizer = load_pickle("vectorizer.pickle")
model = load_pickle("model.pickle")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    msg = request.form.get("message")
    if not msg:
        # If message is empty, display a friendly error on the prediction page.
        return render_template("predict.html", sentiment="No message provided", user_input=""), 400

    try:
        # Text preprocessing using TextToNum
        ob = TextToNum(msg)
        ob.cleaner()
        ob.token()
        ob.removeStop()
        processed_tokens = ob.stemme()

        if not vectorizer or not model:
            return render_template("predict.html", sentiment="Model or Vectorizer is missing", user_input=msg), 500

        # Join the processed tokens and transform the input
        processed_text = ' '.join(processed_tokens)
        data = vectorizer.transform([processed_text])

        # Predict sentiment
        pred = model.predict(data)
        sentiment_result = str(pred[0])

        return render_template("predict.html", sentiment=sentiment_result, user_input=msg)

    except Exception as e:
        print("Error:", str(e))
        print(traceback.format_exc())
        return render_template("predict.html", sentiment="Internal Server Error", user_input=msg), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5153, debug=True)
