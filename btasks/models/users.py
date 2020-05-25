from dataclasses import dataclass


from btasks import db
from btasks.models.tasks import Task


@dataclass
class User(db.Model):
    id: int
    name: str
    tasks: Task

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    tasks = db.relationship('Task', backref=' user', lazy=True, cascade='all, delete-orphan')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def remove_task(self, task_id):
        task_to_delete = Task.query.get(task_id)
        if task_to_delete.user.id == self.id:
            db.session.delete(task_to_delete)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def list():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
