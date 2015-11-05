from app import app
from flask import render_template, flash, redirect, session, g, request, url_for, abort
from monkey import *
from forms import CrunchForm
    
@app.route('/')
@app.route('/home/')
@app.route('/index/')
def home():
    return render_template("home.html", homeclass="active")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", homeclass="active", errortext="Sorry, the page does not exist.")

@app.errorhandler(403)
def not_permitted(e):
    return render_template("error.html", homeclass="active", errortext="Sorry, you are not permitted to see this.")

@app.route('/crunchresult/')
def crunchresult():
    reslist = getAllAnalysis(["this is awesome. i am loving this! though the time is running out. though the time is running out. though the time is running out","no","haha","never"])
    return render_template("crunch.html", homeclass="active", temptext="See command line",
        reslist=reslist)

@app.route('/crunch/',methods=["GET","POST"])
def crunch():
    form = CrunchForm()
    if form.validate_on_submit():
        try:
            hashtag = form.hashtag.data
            flash('Successfully got the hash tag '+hashtag)
            return redirect('home')
        except:
            flash('Error in your form submission')
    else:
        form_error_helper(form)
    return render_template("crunchnow.html", crunchclass="active",signincss=False,form=form)

@app.route('/temp/')
def temp():
    return render_template("temp.html", homeclass="active", temptext="See command line")

def form_error_helper(form):
    for field, errors in form.errors.items():
           for error in errors:
               flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error))