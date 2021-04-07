from flask.cli import FlaskGroup

from app import app, db
from app.models import *
from app.routes import *

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("update_chals")
def update_chals():
    from app.chals import create_update_chals
    create_update_chals()


if __name__ == "__main__":
    cli()