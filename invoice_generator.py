print(24 * '-', 'Factura produse', 24 * '-')


class Factura:
    from datetime import date
    seria = 'FDB'
    produse_pe_factura = []
    today = date.today()

    def __init__(self, numar):
        self.numar = numar

    def adauga_produs_pe_factura(self, *produse):
        for produs in produse:
            self.produse_pe_factura.append(produs)

    def sterge_produsul_de_pe_factura(self, produs):
        self.produse_pe_factura.remove(produs)

    def genereaza_factura(self):
        detalii_factura = f'Factura seria: {self.seria}, număr: {self.numar} \n' \
                          f'Data (zi/lună/an): {self.today.day}/{self.today.month}/{self.today.year}\n' \
                          f"{67 * '*'} \n" \
                          f"{'Produs':<18}| {'cantitate':<18}| {'preț bucată':<18}| {'Total'}\n"

        produse_factura = ''

        for produs in self.produse_pe_factura:
            produse_factura += f"{produs.nume_produs:<18}| {produs.cantitate:<18}| {produs.pret_buc:<18}| {produs.pret_buc * produs.cantitate}\n"

        return detalii_factura + produse_factura


class Produs:

    def __init__(self, nume_produs, cantitate, pret_buc):
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua

    def schimba_pretul(self, pret_nou_buc):
        self.pret_buc = pret_nou_buc

    def schimba_nume_produs(self, nume_nou_produs):
        self.nume_produs = nume_nou_produs


produs1 = Produs('Telefon', 1, 1500.00)
produs2 = Produs('Notebook Pro', 1, 3000.00)
produs3 = Produs('Casti HiFi', 1, 150.00)
produs4 = Produs('Husa telefon', 1, 100.00)

factura1 = Factura(2201)
factura1.adauga_produs_pe_factura(produs1, produs2, produs3)
factura1.adauga_produs_pe_factura(produs4)
factura1.sterge_produsul_de_pe_factura(produs2)

produs1.schimba_nume_produs('Samsung')
produs1.schimba_cantitatea(3)
produs1.schimba_pretul(2000.00)

print(factura1.genereaza_factura())
