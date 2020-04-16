from flask import (
    Flask,
    Response,
    abort,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

app = Flask(__name__)


@app.route('/')
def home():
    """
    First Method and First Page Thats Mean Home Page on website
    """
    return render_template('index.html')



"""
Start Flask Project in This File
"""
if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)