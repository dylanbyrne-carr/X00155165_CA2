"""
Dice Roller Application
Student: X00155165
CA2 - DevOps Project
"""

import random
from typing import List


class DiceRoller:
    """A simple dice roller with history tracking."""
    
    def __init__(self):
        """Initialize the dice roller."""
        self.history: List[int] = []
    
    def roll(self, num_dice: int = 1, sides: int = 6) -> List[int]:
        """
        Roll one or more dice.
        
        Args:
            num_dice: Number of dice to roll
            sides: Number of sides on each die
        
        Returns:
            List of roll results
        
        Raises:
            ValueError: If num_dice or sides is less than 1
        """
        if num_dice < 1:
            raise ValueError("Must roll at least 1 die")
        if sides < 1:
            raise ValueError("Die must have at least 1 side")
        
        results = [random.randint(1, sides) for _ in range(num_dice)]
        self.history.extend(results)
        return results
    
    def roll_sum(self, num_dice: int = 2, sides: int = 6) -> int:
        """
        Roll multiple dice and return the sum.
        
        Args:
            num_dice: Number of dice to roll
            sides: Number of sides on each die
        
        Returns:
            Sum of all rolls
        """
        return sum(self.roll(num_dice, sides))
    
    def get_history(self) -> List[int]:
        """Get all previous rolls."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear roll history."""
        self.history.clear()


def main():
    """Demo the dice roller."""
    print("=== Dice Roller Demo ===\n")
    
    roller = DiceRoller()
    
    print("FEATURE 1: Basic Rolling")
    print(f"Roll 1d6: {roller.roll()}")
    print(f"Roll 2d6: {roller.roll(2, 6)}")
    print(f"Roll 3d6 sum: {roller.roll_sum(3, 6)}")
    print(f"Roll 1d20: {roller.roll(1, 20)}")
    
    print(f"\nHistory: {roller.get_history()}")


if __name__ == "__main__":
    main()