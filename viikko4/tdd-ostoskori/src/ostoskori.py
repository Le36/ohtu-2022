from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        total = 0
        for x in self._ostokset:
            total += x.lukumaara()
        return total
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        total = 0
        for x in self._ostokset:
            total += x.hinta()
        return total
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        for x in self._ostokset:
            if x.tuotteen_nimi() == lisattava.nimi():
                x.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for i, x in enumerate(self._ostokset):
            if x.tuotteen_nimi() == poistettava.nimi():
                if x.lukumaara() == 1:
                    del self._ostokset[i]
                    return
                x.muuta_lukumaaraa(-1)
                return

    def tyhjenna(self):
        self._ostokset = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
