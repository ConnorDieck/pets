"""Forms for our Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import AnyOf, InputRequired, NumberRange, Optional, Email, AnyOf, URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species", validators=[AnyOf(["dog", "cat", "porcupine"], message="Animal must be a dog, cat, or porcupine (please enter in lowercase).")], )
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Age must be between 0-30")])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available?")
