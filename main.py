from flask import Flask, request
from caesar import rotate_string
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>       
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans serif;
                border-radius: 10px
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>
    <body>
        <form method="post">
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label>

            <br>

            <label>
                <textarea name="text">{0}</textarea>
            </label>

            <br>

            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(...)

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    x = rotate_string(text, rot)
    y = "<h1>" + x + "</h1>"
    return y.format(...)
   
app.run()