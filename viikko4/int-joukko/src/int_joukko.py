KAPASITEETTI = 5
OLETUSKASVATUS = 5


def kopioi_taulukko(a, b):
    for i in range(0, len(a)):
        b[i] = a[i]


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not (isinstance(kapasiteetti, int) and not (kapasiteetti < 0)):
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not (isinstance(kapasiteetti, int) and not (kapasiteetti < 0)):
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        on = 0
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                on = on + 1
        return on > 0

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        return self.lisaa_apu(n)

    def lisaa_apu(self, n):
        if self.kuuluu(n):
            return False
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm % len(self.ljono) == 0:
            taulukko_old = self.ljono
            kopioi_taulukko(self.ljono, taulukko_old)
            self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            kopioi_taulukko(taulukko_old, self.ljono)
        return True

    def poista(self, n):
        kohta = -1
        kohta = self.poista_apu(kohta, n)
        if kohta == -1:
            return False
        self.poista_loop(kohta)
        return True

    def poista_loop(self, kohta):
        for j in range(kohta, self.alkioiden_lkm - 1):
            apu = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def poista_apu(self, kohta, n):
        for i in range(0, self.alkioiden_lkm):
            if n != self.ljono[i]:
                continue
            kohta = i  # siis luku löytyy tuosta kohdasta :D
            self.ljono[kohta] = 0
            break
        return kohta

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        a_taulu, b_taulu, x = IntJoukko.taulut(a, b)
        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])
        return x

    @staticmethod
    def leikkaus(a, b):
        a_taulu, b_taulu, y = IntJoukko.taulut(a, b)
        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])
        return y

    @staticmethod
    def erotus(a, b):
        a_taulu, b_taulu, z = IntJoukko.taulut(a, b)

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])
        return z

    @staticmethod
    def taulut(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        return a_taulu, b_taulu, z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i]) + ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1]) + "}"
            return tuotos
