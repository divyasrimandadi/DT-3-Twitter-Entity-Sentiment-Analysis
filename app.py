from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    
    if request.method=="POST":
        msg=request.form.get("message")
        print(msg)
    else:
        return  render_template("index.html",methods=["GET","POST"])




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5153)