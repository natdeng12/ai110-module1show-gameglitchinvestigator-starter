# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude to come up with three pytests for the existing parse_guess() function in tests/test_game_logic.py. I also make sure Claude to not change the application code or any existing tests.

**What did the agent do?**

Claude added three more tests to my existing 5 tests. And run it and all 8 tests passed.

**What did you have to verify or fix manually?**

I reviewed the lines before continuing to let Claude edit the code.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case         | Prompt Used                                                                                                           | AI-Suggested Test                                                                   | Did It Pass? | Your Reasoning                                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------- |
| Empty input       | Asked the AI to add a pytest test for an empty string input to `parse_guess()` without changing the application code. | `parse_guess("")` should return `False`, `None`, and `"Enter a guess."`             | Yes          | A player might submit the form without entering a guess, so the game should handle empty input without crashing. |
| Non-numeric input | Asked the AI to add a pytest test for a non-numeric string such as `"hello"` to `parse_guess()`.                      | `parse_guess("hello")` should return `False`, `None`, and `"That is not a number."` | Yes          | A player might type letters instead of a number, so the game should reject invalid input correctly.              |
| Negative number   | Asked the AI to add a pytest test for a negative number such as `"-5"` to `parse_guess()`.                            | `parse_guess("-5")` should return `True`, `-5`, and `None` for the error.           | Yes          | This tests how the parser handles a valid numeric value that is outside the normal positive guessing range.      |


> I want to complete the Advanced Edge-Case Testing bonus.
>
> Please add exactly three pytest tests for the existing `parse_guess()` function in `tests/test_game_logic.py`.
>
> Test these three edge cases:
> 1. An empty string `""`
> 2. A non-numeric string such as `"hello"`
> 3. A negative number such as `"-5"`
>
> Do not change the application code or any existing tests. Only add these three new tests.
>
> Please explain briefly what each test checks before making the changes.

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

The PEP 8 checker found four E501 line-too-long errors in `logic_utils.py`: - line 15: 87 characters - line 34: 87 characters - line 56: 113 characters - line 86: 87 characters Please fix only these PEP 8 line-length issues. Do not change any program logic, return values, function names, parameters, or behavior. Only reformat the long lines so they are 79 characters or fewer. After making the changes, briefly explain what formatting changes you made.

**Linting output before:**

logic_utils.py:15:80: E501 line too long (87 > 79 characters) logic_utils.py:34:80: E501 line too long (87 > 79 characters) logic_utils.py:56:80: E501 line too long (113 > 79 characters) logic_utils.py:86:80: E501 line too long (87 > 79 characters)

**Changes applied:**

The AI reformatted the four lines that were longer than the PEP 8 limit. Three of the errors were long raise NotImplementedError(...) lines, so the error message was moved onto its own indented line. The fourth error was a long # FIX: comment in check_guess(), which was split into two comment lines.

The wording and behavior of the code were not changed.

After the formatting changes, I ran python -m pycodestyle logic_utils.py again and received no errors. I also ran the pytest test suite and all 8 tests passed.
---
### Docstrings

I also used AI to improve the professional docstrings for all four functions in `logic_utils.py`. I instructed the AI to only improve documentation and not change the functions' logic or behavior. I reviewed the changes before accepting them.

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
