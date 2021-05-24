from flask import Flask #a class called flask is created by importing it from the library
app = Flask(__name__) #"an instance of the class" itself. "name" is a shortcut for flask to find the right resources to run the app

@app.route("/") # which path flask looks for when selecting which url to trigger the function
def HeiFlask(): # the function itself, in python the def variable seems to be used
  return "Source: Quickstart of the official Flask documentation" #the output of the function. in this case, prints out the text within quotations

app.run(debug=True) #runs out app, while enabling the debug-option within the browser


