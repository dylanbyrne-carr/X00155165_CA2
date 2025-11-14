"""
Dice Roller Application - Phase 2
Student: X00155165
DevOps CA2
"""
import random
from typing import List, Dict
class DiceRoller:
    """A dice roller with history tracking and statistics"""

    def __init__(self):
        self.history: List[int] = []

    # FEATURE 1: Basic Dice Rolling
    def roll(self, num_dice: int = 1, sides: int = 6) -> List[int]:
        """Roll one or more dice."""
        if num_dice < 1:
            raise ValueError("Must roll at least one die")
        if sides < 1:
            raise ValueError("Die must have at least one side")
        results = [random.randint(1, sides) for _ in range (num_dice)]
        self.history.extend(results)
        return results

    def roll_sum(self, num_dice: int = 2, sides: int = 6) -> int:
        """Roll mulptiple dice and return the sum."""
        return sum(self.roll(num_dice, sides))

    def get_history(self) -> List[int]:
        """Get all previous rolls."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear roll history."""
        self.history.clear()

        # Feature 2: Statistics (New)
    def get_stats(self) -> Dict[str, float]:
        """
        Get statistics for all rolls.
        
        Returns:
            Dictionary with average, min, max, count
        """
        if not self.history:
            return {'average': 0, 'min': 0, 'max': 0, 'count': 0}

        return{
            'average': sum(self.history) / len(self.history),
            'min': min(self.history),
            'max': max(self.history),
            'count': len(self.history)
        }

def main():
    """Demo the dice roller."""

    print("Demo line")
    print("=== Dice ROller Demo P2 ===\n")
    roller = DiceRoller()
    print("FEATURE 1: Basic Rolling")
    print(f"Roll 1d6: {roller.roll()}")
    print(f"Roll 2d6: {roller.roll(2, 6)}")
    print(f"Roll 3d6 sum: {roller.roll_sum(3, 6)}")
    print(f"\nHistory: {roller.get_history}")
    # New Feature 2
    print("\nFeature 2: Statistics")
    stats = roller.get_stats()
    print(f"Average: {stats['average']:.2f}")
    print(f"Min: {stats['min']}, Max: {stats['max']}")
    print(f"Total rolls: {stats['count']}")

if __name__ == "__main__":
    main()
