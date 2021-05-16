from system.app import app
#from flask_talisman import Talisman

#csp = {
#       'default-src': '\'self\'',
#       'script-src': '\'self\'',
#       'style-src': '\'self\''
#      }

# HEROKU DEPLOY
server = app.server
#Talisman(server, content_security_policy=csp)