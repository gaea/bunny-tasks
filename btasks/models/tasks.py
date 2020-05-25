from enum import Enum
from dataclasses import dataclass


from btasks import db
from btasks.models.states import States


@dataclass
class Task(db.Model):
    id: int
    description: str
    state: str
    user_id: int

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    state = db.Column(db.String(20), nullable=False)  # db.Column(Enum(States))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', back_populates='tasks')

    def validate_states(self):
        allowed_values = ['to do', 'done']

        if self.state not in allowed_values:
            raise Exception('Invalid value for state field, allowed values: {}, given: {}'.format(
                ', '.join(allowed_values), self.state))
        else:
            return True

    def save(self):
        if self.validate_states:
            db.session.add(self)
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def list():
        return Task.query.all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def get_by_user_id(user_id):
        return Task.query.filter_by(user_id=user_id).all()
