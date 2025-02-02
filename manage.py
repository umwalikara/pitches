from flask_script import Manager,Server
from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Pitch,Comment
from flask_login import LoginManager
# from app.models import User,Pitch,Comment,Vote,PitchCategory


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
app = create_app('test')

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role )
    # return dict(app = app,db = db,User = User ,Pitch = Pitch,Comment = Comment,Vote = Vote,PitchCategory = PitchC

if __name__ == '__main__':
    manager.run()