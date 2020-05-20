import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('./index.tpl')



@bottle.get('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))
    
    
    
    
    
    
bottle.run(reloader=True, debug=True)