from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    #return "Hi there, how ya doing?"
    return render_template("index.html", title="Epic Tutorial", paragraph="wow I am learning so much great stuff!")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')