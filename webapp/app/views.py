from app import app
from flask import render_template, flash, redirect, session, g, request, url_for, abort
from forms import RegisterationForm, LoginForm

    
@app.route('/')
@app.route('/home/')
@app.route('/index/')
def home():
    return render_template("home.html", homeclass="active")

@app.route('/login/',methods=["GET","POST"])
def login():
    if session.get('userid')>=1:
        return render_template("temp.html", loginclass="active", signincss=False, temptext="Already logged in!")
    form = LoginForm()
    if form.validate_on_submit():
        try:
            someobj = Users.get(Users.userid == form.emailid.data, Users.password == 
                hashlib.md5(form.password.data).hexdigest())
            session['userid']=someobj.userid
            session['role']=someobj.role
            flash('Successfully logged in')
            print session
            return redirect('home')
        except:
            flash('Details do not match')
    else:
        form_error_helper(form) 
    return render_template("login2.html", loginclass="active", signincss=False, form = form)

@app.route('/logout/',methods=["GET","POST"])
def logout():
    if not session.get('userid'):
            return render_template("temp.html", loginclass="active", signincss=False, temptext="Please log in first!")
    session.clear()
    return render_template("temp.html", loginclass="active", signincss=False, temptext="Successfully logged out!")

#get to land first on signup page, post to actually sign up
@app.route('/signup/', methods=["GET","POST"]) 
def signup():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash('Signup details valid')
        return redirect('home')
    else:
        form_error_helper(form)
    return render_template("signup.html", signupclass="active", signincss=True, form=form) 

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", homeclass="active", errortext="Sorry, the page does not exist.")

@app.errorhandler(403)
def not_permitted(e):
    return render_template("error.html", homeclass="active", errortext="Sorry, you are not permitted to see this.")

@app.route('/temp/')
def temp():
    nayaperson = Person.create(name='nayaperson')
    naya_kitty = Pet.create(ownerid=nayaperson, type='cat')
    toflash = ''
    for person in Person.select():
        toflash = toflash + (str(person.id)+" "+person.name) + "\n\r"
    flash(toflash)
    return render_template("temp.html", homeclass="active", temptext=str(nayaperson.id)+" "
        +str(naya_kitty.id))


def get_current_user_role():
    return 'admin'

def form_error_helper(form):
    for field, errors in form.errors.items():
           for error in errors:
               flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error))