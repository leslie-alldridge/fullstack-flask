from app import db
from models import BlogPost

# create the database tables based on the schema defined in models.py
db.create_all()

# insert changes
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

# commit changes
db.session.commit()