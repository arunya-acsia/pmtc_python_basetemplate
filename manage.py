import os
from app import create_app
from flask.cli import FlaskGroup


env = os.getenv("FLASK_ENV") or "dev"
print(f"Active environment: * {env} *")

app = create_app(env) # Creating flask app

cli = FlaskGroup(create_app=create_app)
if __name__ == "__main__":
    cli()