

from flask import Flask, render_template
import datetime

#New Flask object - app
app = Flask(__name__)

# Controller or HANDLER
# Root folder
@app.route("/")                     # poševnica pomeni kje se nahaja v tem primeru root mapa
def index():
    current_year = datetime.datetime.now().year
    greating = "Hello, user!"
    
    return render_template("index.html", greating = greating, current_year = current_year)  #navedemop tudi vrednosti, ki jih pošiljam v index.html

@app.route("/contact")

def contact():
    return render_template("contact.html")

@app.route("/galerie")
def galerie():
    return render_template("galerie.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/location")
def location():
    return render_template("location.html")


if   __name__== "__main__":
    app.run(use_reloader=True)   # (use_reloader=True) : pomeni avtomatski reload strni . če se main.py spremeni

