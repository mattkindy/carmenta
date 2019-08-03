from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Candidate(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30))
    title = db.Column(db.String(50))
    schools = db.Column(db.String(300)) # json - possibly convert to this https://www.michaelcho.me/article/json-field-type-in-sqlalchemy-flask-python
    workplaces = db.Column(db.String(500)) # json
    locations = db.Column(db.String(500)) # json
    label = db.Column(db.String(20)) # could be enum
    # lived in texas or DC?
    # time at current job?
    # time since education?

    def __init__(self, id, name, title, schools, workplaces, locations, label):
        self.id = str(id)
        self.name = str(name)
        self.title = str(title)
        self.schools = str(schools)
        self.workplaces = str(workplaces)
        self.locations = str(locations)
        self.label = str(label)

    def update_label(self, label):
        self.label = label
        db.session.commit()

    def commit(self):
        # if db.app is None:
        #     raise Error("DB not linked to app!")

        if Candidate.query.filter_by(id=id).first() is None:
            db.session.add(self)
        db.session.commit()

    def serialize(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Edge(db.Model):
    id1 = db.Column(db.String(30), primary_key=True)
    id2 = db.Column(db.String(30), primary_key=True)
