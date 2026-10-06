def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a difficulty level.

    Args:
        difficulty: The selected difficulty level, such as "Easy",
            "Normal", or "Hard".

    Returns:
        tuple[int, int]: A ``(low, high)`` pair giving the inclusive bounds
        the secret number is drawn from.

    Raises:
        NotImplementedError: Until this function is refactored from app.py.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def parse_guess(raw: str):
    """Parse the player's raw text input into an integer guess.

    Args:
        raw: The text the player typed into the guess box. May be ``None``
            or an empty string.

    Returns:
        tuple[bool, int | None, str | None]: A ``(ok, guess, error)`` triple.
        On success, ``ok`` is True, ``guess`` is the parsed integer, and
        ``error`` is None. On failure, ``ok`` is False, ``guess`` is None,
        and ``error`` is a message to show the player.

    Raises:
        NotImplementedError: Until this function is refactored from app.py.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def check_guess(guess, secret):
    """Compare a guess to the secret number and describe the result.

    If the two values cannot be compared directly (for example, an int
    and a str), the guess is converted to a string and compared again.

    Args:
        guess: The player's guess.
        secret: The secret number the player is trying to find.

    Returns:
        tuple[str, str]: An ``(outcome, message)`` pair. ``outcome`` is one
        of "Win", "Too High", or "Too Low", and ``message`` is the hint
        shown to the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIX: Refactored check_guess() into logic_utils.py with AI
        # assistance and corrected the backwards hints.
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate the player's new score after a guess.

    Args:
        current_score: The player's score before this guess.
        outcome: The result from ``check_guess``: "Win", "Too High",
            or "Too Low".
        attempt_number: Which attempt this guess was, used to scale
            the points awarded for a win.

    Returns:
        int: The updated score.

    Raises:
        NotImplementedError: Until this function is refactored from app.py.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )
