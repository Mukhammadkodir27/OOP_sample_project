import unittest
from main import USD, EUR, GBP


class TestCurrencyConversion(unittest.TestCase):
    def test_usd_to_base_currency(self):
        usd = USD(10)
        self.assertEqual(usd.to_base_currency(), 10)

    def test_eur_to_base_currency(self):
        eur = EUR(10)
        self.assertAlmostEqual(eur.to_base_currency(), 11.8, places=7)

    def test_gbp_to_base_currency(self):
        gbp = GBP(10)
        self.assertAlmostEqual(gbp.to_base_currency(), 13.1, places=7)

    def test_from_base_currency_usd(self):
        usd = USD.from_base_currency(10)
        self.assertAlmostEqual(usd.value, 10, places=7)

    def test_from_base_currency_eur(self):
        eur = EUR.from_base_currency(10)
        expected_value = 10 / EUR.base_rate
        self.assertAlmostEqual(eur.value, expected_value, places=7)

    def test_from_base_currency_gbp(self):
        gbp = GBP.from_base_currency(10)
        expected_value = 10 / GBP.base_rate
        self.assertAlmostEqual(gbp.value, expected_value, places=7)

    def test_add_currencies(self):
        usd = USD(10)
        eur = EUR(10)
        result = usd + eur
        self.assertIsInstance(result, USD)
        self.assertAlmostEqual(result.value, 21.8, places=7)

    def test_str_representation(self):
        usd = USD(10)
        self.assertEqual(str(usd), "10.00 USD")


if __name__ == '__main__':
    unittest.main()
