import os
import unittest
from ....BaseTestCase import BaseTestCase
from kombi.Crawler import Crawler
from kombi.Crawler.PathHolder import PathHolder
from kombi.Crawler.Fs.Image import DpxCrawler

class DpxCrawlerTest(BaseTestCase):
    """Test Dpx crawler."""

    __dpxFile = os.path.join(BaseTestCase.dataTestsDirectory(), "test.dpx")

    def testDpxCrawler(self):
        """
        Test that the Dpx crawler test works properly.
        """
        crawler = Crawler.create(PathHolder(self.__dpxFile))
        self.assertIsInstance(crawler, DpxCrawler)

    def testDpxVariables(self):
        """
        Test that variables are set properly.
        """
        crawler = Crawler.create(PathHolder(self.__dpxFile))
        self.assertEqual(crawler.var("type"), "dpx")
        self.assertEqual(crawler.var("category"), "image")
        self.assertEqual(crawler.var("imageType"), "single")
        self.assertEqual(crawler.var("width"), 1920)
        self.assertEqual(crawler.var("height"), 1080)


if __name__ == "__main__":
    unittest.main()
