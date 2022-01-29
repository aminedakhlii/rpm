from flask import Flask,  render_template , url_for , redirect , flash, request, abort , jsonify
from rpmqa import app, db
from rpmqa.models import Token 
from rpmqa.script import broadcast

situations = {1:"Stuck in sand",2:"Drowning",3:"Out of fuel",4:"Flat tire",5:"Overturned"}

@app.route("/broadcast" , methods = ["POST"])
def cast():
    location = {'latitude': request.form["lat"],'longitude': request.form["long"]} 
    snap = request.form['snap']
    situation = situations[int(request.form['situation'])]
    broadcast(situation,location,snap)
    return ""