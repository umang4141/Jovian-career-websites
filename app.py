from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,world"

@app.route("/products")
def welcome():
    return "welcome to the API"

if __name__ =="__main__":
    # print("I am inside the if now")
    app.run(host='0.0.0.0',debug=True)
