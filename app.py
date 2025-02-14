from flask import Flask,render_template,request,jsonify
from test import TextToNum
import pickle 
app=Flask(__name__)
@app.route("/")
def home():

    if request.method=="POST":
        msg=request.form.get("message")
        print(msg)
        ob=TextToNum(msg)
        ob.cleaner()
        ob.token()
        ob.removeStop()
        st=ob.stemme()
        with open("vectorizer.pickle","rb") as vcfile:
            cv=pickle.load(vcfile)
        stvc=" ".join(st)
        data=cv.trasform([stvc])
        print(data)
        with open("model.pickle","rb") as mbfile:
            model=pickle.load(mbfile)
        pred=model.predict(data)
        return jsonify({"result":str(pred[0])})


    else:
        return render_template("index.html",methods=["GET","POST"])

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)