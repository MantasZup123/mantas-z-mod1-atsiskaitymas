import unittest
from mantas_z_mod1_atsiskaitymas.crawler import crawl

class TestCrawl(unittest.TestCase):

    def test_crawl_gintarine(self):
        source = "gintarine"
        result = crawl(source, data_format="list")
        self.assertEqual(list(result[0].keys()), ["Title", "Price"])

    def test_crawl_benu(self):
        source = "benu"
        result = crawl(source, data_format="list")
        self.assertEqual(list(result[0].keys()), ["Title", "Price"])



if __name__ == "__main__":
    unittest.main()