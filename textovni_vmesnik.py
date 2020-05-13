
def izpis_igre(igra):
    text = (
            'Število preostalih poizkusov: {stevilo_preostalih_poizkusov} \n\n'
            '{pravilni_del_gesla}\n\n'
            'Neuspeli poizkusi: {neuspeli_poizkusi} \n\n'
).format(
    stevilo_preostalih_poizkusov = model.stevilo_dovoljenih_napak - igra.stevilo_napak() + 1,
    pravilni_del_gesla = igra.pravilni_del_gesla(),
    neuspeli_poizkusi = igra.nepravilni_ugibi()
)
return text

def izpis_zmage(igra):
#geslo = igra.geslo
    pass
def izpis_poraza(igra):
    pass
def zahtevaj_vnos():
    return input('Črka: ')

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.zmaga():
            print(izpis_zmage(igra))
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
    return


