from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        message = request.form.get("message")  # Get input text from form
        return redirect(url_for("result", sentiment="Positive", user_input=message))  # Redirect to result page
    return render_template("predict.html")

@app.route("/result")
def result():
    sentiment = request.args.get("sentiment", "Neutral")  # Default sentiment
    user_input = request.args.get("user_input", "No input provided")
    return render_template("result.html", sentiment=sentiment, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
