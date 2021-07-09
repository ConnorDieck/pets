"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

toby = Pet(name="Toby", species="dog", photo_url="https://cdn.shopify.com/s/files/1/0994/0236/articles/havanese_1200x.jpg?v=1503788710", age="8", notes="nosey")
minks = Pet(name="Minks", species="cat", photo_url="https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg", age="10", notes="regal")
pickles = Pet(name="Pickles", species="porcupine", photo_url="https://kpbs.media.clients.ellingtoncms.com/assets/img/2019/04/08/dl607_porcupines_penelope_med_wide-3df52ca121dbb5046e2ada2d3a52d73a77199ca7.jpg", age="3", notes="bushy")

db.session.add_all([toby, minks, pickles])
db.session.commit()