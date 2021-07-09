from forms import AddPetForm
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_homepage():
    """Renders template for home page"""

    pets = db.session.query(Pet).all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    "Pet add form; handle adding"

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}!")

        return redirect('/')
    
    else:
        return render_template("add_pet_form.html", form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_and_edit(pet_id):
    "Show pet information and form; handle edit"

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        availabile = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = availabile
        db.session.commit()

        flash(f"Edited {pet.name}!")

        return redirect('/')
    
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
