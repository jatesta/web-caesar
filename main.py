from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;                
                }

                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                } 
            </style>
        </head>
        <body>
            <form method="post">
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="">
                <textarea type="text" name="text"></textarea>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = str(request.form['text'])
    rot = int(request.form['rot'])
    encrypted = rotate_string(text, rot)

    return '<h1>' + cgi.escape(encrypted) + '</h1>'

app.run()
