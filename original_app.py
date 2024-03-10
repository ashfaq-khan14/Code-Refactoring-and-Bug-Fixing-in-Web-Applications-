from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["POST"])
def index():
    note = request.args.get("note")
    notes.append(note)
    return render_template("original_home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
