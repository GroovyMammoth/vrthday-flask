from flask import Flask, render_template, url_for, request
from forms import CustomizationForm
import os
app = Flask(__name__)

app.config["SECRET_KEY"] = "73686974206f6e20796f7572206d6f74"
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),"uploads/")

@app.route("/",methods=["GET","POST"])
def hello():
    form = CustomizationForm()
    return render_template("index.html", form=form)

@app.route("/submit",methods=["POST"])
def submit():
    form = CustomizationForm()
    for file in form.photos.data:
        filename = file.filename
        destination = "/".join([UPLOAD_FOLDER,filename])
        file.save(destination)
        print(destination)
    editParadise("Hello","Goodbye",form.recipient_email)
    return render_template("index.html", form=form)

def editParadise(to,From,email):
    crimefile = open("product_template/museum.txt", 'r')
    TemplateHTML = [line for line in crimefile.readlines()]
    if ((to == "") or (From=="") or (email=="")):
        raise IndexError
        #alert("'To', 'From', and 'Recipient's Email' fields are required for this card!")
    else:
        TemplateHTML[208] = '    <a-entity text="value: Wishing you a chill birthday, '+to+'!; color:#FFFFFF; shader: msdf; font:https://raw.githubusercontent.com/etiennepinchon/aframe-fonts/master/fonts/gloriahallelujah/GloriaHallelujah.json;" position="5 5.9 -13" rotation="0 -10 0" scale="65 75" ></a-entity>'
        TemplateHTML[209] = '    <a-entity text="value: -Love, '+From+'; color:#FFFFFF; shader: msdf; font:https://raw.githubusercontent.com/etiennepinchon/aframe-fonts/master/fonts/gloriahallelujah/GloriaHallelujah.json;" position="33 1.2 -11" rotation="0 -10 0" scale="65 75" ></a-entity>'
        TemplateHTML[211] = '    <a-entity text="value: Wishing you a chill birthday, '+to+'!; color:#FFFFFF; shader: msdf; font:https://raw.githubusercontent.com/etiennepinchon/aframe-fonts/master/fonts/gloriahallelujah/GloriaHallelujah.json;" position="0 0.1 -25" rotation="-90 -10 0" scale="65 75" ></a-entity>'
        TemplateHTML[212] = '    <a-entity text="value: -Love, '+From+'; color:#FFFFFF; shader: msdf; font:https://raw.githubusercontent.com/etiennepinchon/aframe-fonts/master/fonts/gloriahallelujah/GloriaHallelujah.json;" position="30 0.1 -7" rotation="-90 -10 -5" scale="65 75" ></a-entity>'
        StringHTML = ""
        for i in TemplateHTML:
            annex = i+"\n"
            StringHTML += annex
        print(StringHTML)
        #PostFile(StringHTML);
