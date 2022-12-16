from app import change


def test_change():
    # Fix this broken test
    # There should be 5 quarters
    assert [{4: 'quarters'}, {1: 'nickels'}, {4: 'pennies'}] == change(1.34)

# Write another test