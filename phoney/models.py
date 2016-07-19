from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def get_or_create(cls, **query):
        created = False
        commit = query.pop('_commit', True)
        try:
            p = cls.query.filter_by(**query).one()
        except NoResultFound:
            p = cls(**query)
            db.session.add(p)
            if commit:
                db.session.commit()
            created = True
        return p, created

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<{}({})>".format(
                self.__class__.__name__,
                ', '.join(["{}={}".format(k, repr(self.__dict__[k]))
                           for k in self.__dict__ if k[0] != '_'])
            )


class Number(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(250), unique=True)
    name = db.Column(db.String(250), default='Unknown')
    called = db.Column(db.DateTime, default=datetime.utcnow)
