"""
Test file for main.py - specifically testing the calculate_pi function
"""
import math
from main import calculate_pi


def test_pi_5_digits():
    """Test that pi is calculated correctly to 5 decimal places."""
    pi_calculated = calculate_pi(5)
    
    # Pi to 5 decimal places is 3.14159
    expected = 3.14159
    
    # Check if the result matches to 5 decimal places
    assert round(pi_calculated, 5) == expected, f"Expected {expected}, got {round(pi_calculated, 5)}"
    print(f"✓ Test passed: Pi calculated to 5 digits = {round(pi_calculated, 5)}")


def test_pi_accuracy():
    """Test that calculated pi is very close to math.pi."""
    pi_calculated = calculate_pi(5)
    
    # Check that the difference is very small
    difference = abs(pi_calculated - math.pi)
    assert difference < 0.00001, f"Difference from math.pi is too large: {difference}"
    print(f"✓ Test passed: Calculated pi is within 0.00001 of math.pi")
    print(f"  Calculated: {pi_calculated}")
    print(f"  math.pi:    {math.pi}")
    print(f"  Difference: {difference}")


def test_pi_more_digits():
    """Test calculating pi with different precision levels."""
    for digits in [3, 5, 10]:
        pi_calculated = calculate_pi(digits)
        difference = abs(pi_calculated - math.pi)
        assert difference < 10**(-digits), f"Pi with {digits} digits is not accurate enough"
        print(f"✓ Test passed: Pi to {digits} digits = {pi_calculated}")


def test_pi_value_range():
    """Test that calculated pi is in the reasonable range."""
    pi_calculated = calculate_pi(5)
    
    assert 3.14 < pi_calculated < 3.15, f"Pi value {pi_calculated} is out of expected range"
    print(f"✓ Test passed: Pi is in reasonable range (3.14 < {pi_calculated} < 3.15)")


if __name__ == "__main__":
    print("Running tests for calculate_pi function...\n")
    
    try:
        test_pi_5_digits()
        print()
        test_pi_accuracy()
        print()
        test_pi_more_digits()
        print()
        test_pi_value_range()
        print("\n" + "="*50)
        print("All tests passed! ✓")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
