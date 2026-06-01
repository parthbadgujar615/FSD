from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Welcome to Flask Template Example"
    return render_template('index.html', msg=message)

if __name__ == '__main__':
    app.run(debug=True)