from logic_utils import check_guess
from app import parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_bug1_high_guess_says_go_lower():
    # Bug #1: hints were backwards. A guess above the secret must tell the player to go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER!" in message

def test_bug1_low_guess_says_go_higher():
    # Bug #1: hints were backwards. A guess below the secret must tell the player to go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER!" in message

def test_parse_guess_empty_string():
    # Edge case: an empty input should be rejected with a prompt to enter a guess.
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."

def test_parse_guess_non_numeric():
    # Edge case: non-numeric text should be rejected instead of crashing.
    ok, value, error = parse_guess("hello")
    assert ok is False
    assert value is None
    assert error == "That is not a number."

def test_parse_guess_negative_number():
    # Edge case: a negative number is still valid input; parse_guess only converts, it does not range-check.
    ok, value, error = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert error is None
