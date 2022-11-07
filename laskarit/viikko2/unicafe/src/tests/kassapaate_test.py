import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_lounaita_oikea_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_lounaita_oikea_maara(self):
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_kateisosto_toimii_edullisilla_lounailla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 500-240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullisilla_lounailla_jos_rahaa_liian_vahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_maukkailla_lounailla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 500-400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukkailla_lounailla_jos_rahaa_liian_vahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullisilla_lounailla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 500-240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_edullisilla_lounailla_jos_rahaa_liian_vahan(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_toimii_maukkailla_lounailla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 500-400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_maukkailla_lounailla_jos_rahaa_liian_vahan(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahan_lataus_toimii(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 50)


