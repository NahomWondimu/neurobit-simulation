"""Neural processing units and pulse propagation classes.

This module implements simple neural-like processing units (Neurobits) that can
pattern match on binary inputs and neural pulses that can propagate through graphs.
"""

import random


class Neurobit:
    """A simple neural unit that performs pattern matching on binary inputs.
    
    Attributes:
        id: Unique identifier for the neurobit
        pattern: Binary pattern to match against inputs
        mask: Mask to apply during pattern matching
        state: Internal state counter
        action_code: Code for action to perform when triggered
        memory_ref: Reference to external memory (optional)
    """
    
    def __init__(self, id, pattern, mask=0xFF, action_code=0, memory_ref=None):
        """Initialize a new Neurobit.
        
        Args:
            id: Unique identifier
            pattern: 8-bit pattern to match
            mask: Bit mask for pattern matching (default: 0xFF)
            action_code: Action code when triggered (default: 0)
            memory_ref: Optional memory reference
        """
        self.id = id
        self.pattern = pattern
        self.mask = mask
        self.state = 0
        self.action_code = action_code
        self.memory_ref = memory_ref

    def trigger(self, input_byte):
        """Check if input matches pattern and update state.
        
        Args:
            input_byte: 8-bit input to check against pattern
            
        Returns:
            bool: True if pattern matches, False otherwise
        """
        if (input_byte & self.mask) == (self.pattern & self.mask):
            self.state += 1
            return True
        return False

    def adapt(self, reward):
        """Adapt the pattern based on reward feedback.
        
        Args:
            reward: Reward signal (positive for reinforcement, 0 for reset)
        """
        if reward > 0:
            self.pattern ^= reward & 0xFF  # Simple learning mechanism
        elif reward == 0:
            self.state = 0

    def __repr__(self):
        return (f"Neurobit(id={self.id}, pattern=0b{self.pattern:08b}, "
                f"mask=0b{self.mask:08b}, state={self.state})")

class NeuroPulse:
    """
    Represents an action potential traveling through a fixed neuron graph.
    Each pulse moves, fades, or replicates based on its neurobit's logic.
    """
    
    def __init__(self, pos, neurobit, graph, ttl=20, exploration_rate=0.1):
        self.pos = pos
        self.nb = neurobit
        self.graph = graph
        self.ttl = ttl
        self.history = [pos]
        self.exploration_rate = exploration_rate

    def is_alive(self):
        """Check if the pulse is still active."""
        return self.ttl > 0

    def step(self, blocked_positions=None):
        if self.ttl <= 0:
            return []

        self.ttl -= 1
        new_pulses = []
        neighbors = self.graph.get(self.pos, [])
        random.shuffle(neighbors)

        blocked_positions = blocked_positions or set()

        for neighbor in neighbors:
            if neighbor in self.history or neighbor in blocked_positions:
                continue

            byte = self.encode(neighbor)
            if self.nb.trigger(byte) or random.random() < self.exploration_rate:
                self.pos = neighbor
                self.history.append(neighbor)
                new_pulses.append(self)
                break  # One move per tick

        return new_pulses


    def encode(self, pos):
        """Convert position to 8-bit binary input for pattern match."""
        r, c = pos
        return ((r << 4) ^ c) & 0xFF

    def __repr__(self):
        return f"Pulse@{self.pos}, ttl={self.ttl}, nb={self.nb}"
