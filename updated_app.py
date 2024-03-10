from flask import Flask, render_template, request

app = Flask(__name__)
notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:  # Ensure note is not empty
            notes.append(note)
    return render_template("updated_home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
