from ostoskori import Ostoskori
from varasto import varasto as default_varast
from pankki import pankki as default_pankki
from viitegeneraattori import viitegeneraattori as default_viitteet


class Kauppa:
    def __init__(self, varast=default_varast, pankki=default_pankki, viitteet=default_viitteet):
        self._varasto = varast
        self._pankki = pankki
        self._viitegeneraattori = viitteet
        self._kaupan_tili = "33333-44455"

    def aloita_asiointi(self):
        self._ostoskori = Ostoskori()

    def poista_korista(self, id):
        tuote = self._varasto.hae_tuote(id)
        self._ostoskori.poista(tuote)
        self._varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, id):
        if self._varasto.saldo(id) > 0:
            tuote = self._varasto.hae_tuote(id)
            self._ostoskori.lisaa(tuote)
            self._varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        viite = self._viitegeneraattori.uusi()
        summa = self._ostoskori.hinta()

        return self._pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)

    def return_kirjaus(self):
        return self._pankki.return_kirjaus()
