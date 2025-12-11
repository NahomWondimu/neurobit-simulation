"""Simple test script for the Neurobit class.

Demonstrates basic functionality including pattern matching and adaptation.
"""

from src.neurobit_walker import Neurobit


def main():
    """Test basic Neurobit functionality."""
    # Create a Neurobit with specific pattern and mask
    neurobit = Neurobit(id=1, pattern=0b10110010, mask=0b11110000)
    print(f"Initial state: {neurobit}")
    
    # Test pattern matching
    input_byte = 0b10110111
    if neurobit.trigger(input_byte):
        print("Pattern matched - Triggered!")
    else:
        print("No pattern match.")
    
    # Test adaptation with reward
    neurobit.adapt(reward=0b00000011)
    print(f"After adaptation: {neurobit}")


if __name__ == "__main__":
    main()
