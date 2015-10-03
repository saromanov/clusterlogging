import clusterlogging
import unittest


class TestBasic(unittest.TestCase):

    def test_num_clusters(self):
        logg = clusterlogging.ClusterLogging()
        for i in range(1, 6):
            logg.registerNode(i)
        logg.registerMessage("A", 1)
        logg.registerMessage("B", 2)
        logg.registerMessage("C", 3)
        logg.construct()
        logg.debug(5, "A")
        logg.debug(2, "A")
        logg.debug(2, "B")
        logg.debug(5, "C")
        logg.debug(4, "A")
        logg.debug(3, "C")
        logg.debug(1, "B")
        logg.debug(2, "A")
        logg.debug(2, "A")
        logg.debug(3, "A")
        logg.debug(4, "A")
        logg.debug(5, "B")
        logg.debug(5, "C")
        logg.debug(4, "B")
        logg.debug(3, "A")
        logg.debug(2, "A")
        logg.debug(1, "B")
        logg.debug(3, "A")
        logg.debug(2, "C")
        logg.debug(5, "B")
        logg.debug(4, "A")
        logg.debug(1, "B")
        logg.debug(2, "C")
        logg.debug(1, "A")
        self.assertEqual(len(logg.clustering()), 5)

    def test_empty_clusters(self):
        logg = clusterlogging.ClusterLogging()
        try:
            logg.clustering()
        except:
            self.assertTrue(True)
            return
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
