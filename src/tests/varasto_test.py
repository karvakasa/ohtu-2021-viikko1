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

    def test_toString(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")

    def test_ottaminen_liikaa(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(3)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_yli_tilan(self):
        self.varasto.lisaa_varastoon(999)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisaa_nega(self):
        self.varasto.lisaa_varastoon(-999)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_nega(self):
        self.varasto.ota_varastosta(-899)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ylivuoto(self):
        self.varasto = Varasto(12, 50)

        self.assertAlmostEqual(self.varasto.saldo, 12)

    def test_alivuoto(self):
        self.varasto = Varasto(-50)

        self.assertAlmostEqual(self.varasto.saldo, -50)

    def test_ali_saldo(self):
        self.varasto = Varasto(12, -50)

        self.assertAlmostEqual(self.varasto.saldo, 0)
