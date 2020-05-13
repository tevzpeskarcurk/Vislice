import random

stevilo_dovoljenih_napak = 9
pravilna_crka = '+'
napacna_crka = '-'
ponovljena_crka = 'o'
zmaga = 'W'
poraz = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())
        
    def zmaga(self):
        for crka in self.geslo:
            if not crka in self.crke:
                return False
        return True
    
    def poraz(self):
        return self.stevilo_napak() < stevilo_dovoljenih_napak

    def pravilni_del_gesla(self):
        delni = ''
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni[-1]
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())


    def ugibaj(self, ugib):
        crka = ugib.upper()
        if crka in self.crke:
            return ponovljena_crka
        else:
            self.crke.append(crka)

            if crka in self.geslo:
                if self.zmaga():
                    return zmaga
                else:
                    return pravilna_crka
            else:
                if self.poraz():
                    return poraz
                else:
                    return napacna_crka


        
with open('besede.txt', 'r', encoding='utf8') as datoteka_z_besedami:
    bazen_besed = [vrstica.strip().upper() for vrstica in datoteka_z_besedami]


def nova_igra():
    return Igra(random.choice(bazen_besed))




