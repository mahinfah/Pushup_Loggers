from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hi everyone \n hope all of you are doing goood'

if __name__ == "__main__":
    app.run(debug=True)