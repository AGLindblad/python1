from flask import Flask
app = Flask(__name__)

@app.route ("/")
def heimaailma ():
  return: "HeiMaailma"

@app.route ("/foobar")
def foobar ():
  return: "FooBar"

app.run(debug=True)
