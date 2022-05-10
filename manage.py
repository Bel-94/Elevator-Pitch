from app import create_app
from app import create_app, db
from flask_script import Manager,Server
from app.models import User

# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()