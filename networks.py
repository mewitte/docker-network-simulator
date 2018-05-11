import sys
from os import path

from actions.networkActions import convertToContainerNames, getMapKey, getNetwork, showNetworkKeys
import docker

client = docker.from_env()
containers = client.containers
couch1_container = containers.list(all=True, filters={"name": "couch1"})[0]
couch2_container = containers.list(all=True, filters={"name": "couch2"})[0]
couch3_container = containers.list(all=True, filters={"name": "couch3"})[0]

showNetworkKeys()

# network1 = getNetwork(couch1_container.name + ';' + couch2_container.name + ';')

networks = client.networks
