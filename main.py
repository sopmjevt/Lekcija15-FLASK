

from flask import Flask, render_template, request, make_response
import datetime

#New Flask object - app
app = Flask(__name__)

# Controller or HANDLER
# Root folder
@app.route("/", methods=["GET"])                     # poševnica pomeni kje se nahaja v tem primeru root mapa
def index():
    current_year = datetime.datetime.now().year

    username = request.cookies.get ("username")
    if username:
        greating = f"Hello {"username"}!"
    else:
        greating = "Hello user!"    

    greating = "Hello, user!"
    
    return render_template("index.html", greating = greating, current_year = current_year)  #navedemop tudi vrednosti, ki jih pošiljam v index.html

@app.route("/contact" , methods=["GET", "POST"])

def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_mail = request.form.get("contact-mail")
        contact_message = request.form.get("contact-message")       

        print(contact_name)
        print(contact_mail)
        print(contact_message)

        response = make_response(render_template("feedback.html"))
        response.set_cookie( "username, contact_name")

        return response 

        # return render_template("feedback.html")    Določeno zgoraj!

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

