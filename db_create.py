from project import db
from project.models import BlogPost

# create the database tables based on the schema defined in models.py
db.create_all()

# insert changes
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("postgres", "I\'m postgres."))

# commit changes
db.session.commit()
