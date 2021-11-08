import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_konstruktori_nollaa_tilavuuden(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_konstruktori_nollaa_alkusaldon(self):
        self.varasto = Varasto(10, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktorin_alkusaldo_ei_ylita_tilavuutta(self):
        self.varasto = Varasto(10, 12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_maaran_lisaaminen_varastoon_ei_onnistu(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tilavuuden_ylittaminen_varastoon_lisaamisessa_ei_onnistu(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_maaran_ottaminen_varastosta_ei_onnistu(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_tilavuuden_ylittaminen_varastosta_ottamisessa_toimii(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(12), 8)

    def test_str_palauttaa_oikein(self):
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
