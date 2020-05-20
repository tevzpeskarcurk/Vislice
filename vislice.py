import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('C:\\UVP\\Github_in_Git\\Repozitoriji\\Vislice\\views\\index.tpl')

bottle.run(reloader=True, debug=True)