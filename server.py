from system.app import app
from flask_talisman import Talisman

# HEROKU DEPLOY
server = app.server
Talisman(server)