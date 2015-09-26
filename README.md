# clusterlogging

At this stage is just experimental project

### Motivation
Simple log messages, not provide any deep information about system. If we have a several agents, nodes,  etc. We need to get additional information.
This project provides clustering nodes by log messages

### Usage
```python

#Construct object
logg = clusterlogging.ClusterLogging()

#Initialize nodes. Nodes can have any name
for i in range(1, 6):
    logg.registerNode(i)

#Register log message. With name and unique id of the message
logg.registerMessage("A", 1)
logg.registerMessage("B", 2)
logg.registerMessage("C", 3)

#Construct matrix of nodes and log messages
logg.construct()

#Simple debug message. Where 5 - is a node name and "A" - is a message
logg.debug(5, "A")
#.. Another log messages

#At the and, apply clustering
result = logg.clustering()
# [(1, 2), (2, 1), (3, 1), (4, 1), (5, 0)]

```

### LICENCE
MIT
