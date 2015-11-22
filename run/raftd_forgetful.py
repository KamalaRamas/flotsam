#!/usr/bin/env python

"""
Run the "forgetful" version of the raftd service from goraft/raftd.
Everything is the same as the actual raftd service, except for the Docker image
and the name.
"""

import raftd

class RaftdForgetfulCandidate(raftd.RaftdCandidate):
  def __init__(self, num_nodes=5 ):
    super(RaftdForgetfulCandidate,self).__init__()
    self.name = "connorg/raftd-forgetful"
    self.docker_image = "raftd-forgetful"
    self.num_containers = num_nodes
    port = 5001
    self.ports = []
    for ind in range( 1, num_nodes+1 ):
	self.ports.append(port)
	port += 1
