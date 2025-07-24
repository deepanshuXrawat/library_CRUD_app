from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/data")
def show_database():
    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=True)