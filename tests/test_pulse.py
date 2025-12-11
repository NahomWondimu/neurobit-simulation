"""Unit tests for NeuroPulse functionality.

This module tests the basic operations of NeuroPulse objects including
initialization, step progression, TTL management, and history tracking.
"""

import unittest
from src.neurobit_walker import Neurobit, NeuroPulse

class TestNeuroPulse(unittest.TestCase):
    def setUp(self):
        """Set up a simple 2x2 maze graph and initialize test instances."""
        self.graph = {
            (0, 0): [(0, 1), (1, 0)],
            (0, 1): [(0, 0), (1, 1)],
            (1, 0): [(0, 0), (1, 1)],
            (1, 1): [(0, 1), (1, 0)]
        }
        self.neurobit = Neurobit(id=1, pattern=0b11110000)  # Basic pattern
        self.pulse = NeuroPulse(pos=(0, 0), neurobit=self.neurobit, graph=self.graph, ttl=3)

    def test_initial_state(self):
        """Test initial state of the NeuroPulse object."""
        self.assertEqual(self.pulse.pos, (0, 0))
        self.assertEqual(self.pulse.ttl, 3)
        self.assertEqual(len(self.pulse.history), 1)
        self.assertTrue(self.pulse.is_alive())

    def test_step_progression_and_ttl(self):
        """Test pulse step progression and TTL reduction."""
        result = self.pulse.step()
        self.assertLess(self.pulse.ttl, 3)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(p, NeuroPulse) for p in result))

    def test_no_revisit_same_node(self):
        """Test pulse does not revisit the same node during its path."""
        self.pulse.step()
        self.assertEqual(len(set(self.pulse.history)), len(self.pulse.history))  # no duplicates

    def test_lifespan_expiration(self):
        """Test that the pulse lifespan expires after steps run out."""
        for _ in range(3):
            self.pulse.step()
        self.assertEqual(self.pulse.ttl, 0)
        self.assertFalse(self.pulse.is_alive())

if __name__ == "__main__":
    unittest.main()
