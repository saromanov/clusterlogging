import logging
import numpy as np
from sklearn.cluster import KMeans


class ClusterLogging:

    def __init__(self, logger=logging.Logger("logging")):
        '''
           By default, logger object in default configuration
        '''
        self.nodes={}
        self.messages={}
        self.nums=0
        self.logger=logger
        self.matrix=None
        self.construction = False

    def registerNode(self, title):
        '''
           register node by the name
        '''
        self.nodes[title]=len(self.nodes) + 1

    def registerMessage(self, msg, num):
        '''
           register message for clustering
        '''
        self.nums += 1
        self.messages[msg]=num

    def addLogMessage(self, nodename, msg):
        if nodename not in self.nodes:
            raise Exception("Nodename {0} is not register".format(nodename))
        if msg not in self.messages:
            raise Exception("Message {0} is not register".format(msg))
        numnode=self.nodes[nodename]
        msgnum=self.messages[msg]
        self.matrix[numnode-1, msgnum-1] += 1

    def debug(self, nodename, msg):
        self._applymsg(self.logger.debug, nodename, msg)

    def fatal(self, nodename, msg):
        self._applymsg(self.logger.fatal, nodename, msg)

    def info(self, nodename, msg):
        self._applymsg(self.logger.info, nodename, msg)

    def construct(self):
        self.construction = True
        self.matrix=np.ones((len(self.nodes), self.nums,))

    def clustering(self, numclusters=3):
        '''
          Return list of tuples with (node name, cluster)
        '''
        if self.construction is False:
            raise Exception("Clusters was not constructed")

        if self.matrix is None:
            raise Exception("Matrix object is not initialize")
        norm = self.matrix/np.max(self.matrix)
        model=KMeans(init='k-means++', n_clusters=numclusters)
        model.fit(norm)
        return list(zip(list(self.nodes.keys()), model.labels_))

    def _applymsg(self, func, nodename, msg):
        self.addLogMessage(nodename, msg)
        func(msg)
