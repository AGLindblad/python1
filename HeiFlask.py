from flask import Flask
app = Flask(__name__)

@app.route("/")
def HeiFlask():
  return "Hei maailma"

app.run(debug=True)

#sudo apt-get update
#sudo apt-get install python3-flask
#python3 HeiFlask.py
