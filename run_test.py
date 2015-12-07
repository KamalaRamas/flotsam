#!/usr/bin/env python

import sys
sys.path.append('./util/')
import tests_file

def main(args):
  try:
    tests_filename = sys.argv[1]
  except Exception,e:
    sys.stderr.write("Error: %s\n" % str(e))
    try:
      sys.stderr.write("Usage: %s test_file.json\n" % args[0])
    except:
      sys.stderr.write("Usage: run_test.py test_file.json\n")

  seeds = [ 3,27,387 ] # seeds 3, 387, 27 
  for i in range(1,10):
     for seed in seeds:
        tests = tests_file.read_tests(tests_filename, seed=seed, num_nodes=3 )
        for t in tests:
           t.run()

if __name__=="__main__":
  main(sys.argv)
