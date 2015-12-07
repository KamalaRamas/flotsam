#!/usr/bin/env python

"""
This class holds the information necessary to run a complete test.
"""

class FlotsamTest(object):
  def __init__(self, test_gen, runners, comparator, seed):
    self.test_gen = test_gen
    self.runners = runners
    self.comparator = comparator
    self.seed = seed

  def run(self):
    t = self.test_gen.gen_tests()
    outputs = {}
    for r in self.runners:
      print r.name + "\n"
      outputs[r.name] = r.run_test(t, self.seed)
    self.comparator.compare(outputs)
