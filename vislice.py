import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

botlle.run(reloader=True, debug=True)