from erd import *
from table import *
from erd_converter import convert_to_table

import unittest

# Check that the `__eq__` function works correctly on the sample table
class TestEquality(unittest.TestCase):
	def test_equal_db(self):
	
		sample_db2 = Database([
	Table('A', set(['a1','a2']), set(['a1']), set()),
	Table('B', set(['a1','b1','b2']), set(['a1','b1']), 
	      set([ (('a1',), 'A', ('a1',)) ])),
        Table('C', set(['a1','b1', 'c1','c2']), set(['a1','b1', 'c1']), 
  	      set([ (('a1',), 'A', ('a1',)),
                   (('b1',), 'B', ('b1',))]))
])

		self.assertEqual( sample_db, sample_db2 )


# Check that the `convert_to_table()` function converts the sample_erd into the sample_db
class TestSample(unittest.TestCase):
	def test_converter(self):
		self.assertEqual( sample_db, convert_to_table( sample_erd ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
