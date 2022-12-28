from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> HELLO WORLD  </h1>"
@app.route('/flask')
def demo():
    return "<h1> WELCOME TO PYTHON FLASK PROJECT </h1>" 

@app.route('/<name>')
def dynamic(name):
    return f"<h1> HELLO {name}!!! </h1>"

if __name__=='__main__':
    app.run()