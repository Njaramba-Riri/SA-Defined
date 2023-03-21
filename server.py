from flask import Flask

#make package object instance
app=Flask()

#define routes and app logic
@app.route("/", method=["GET", "POST"])
def index():
    return "Hey, welcome."

@app.route("/predict")
def predict():
    return"Data Scientist, is that you?"

if __name__=="__main__":
    app.run(debug=True, Host="0.0.0.0", port=3000)