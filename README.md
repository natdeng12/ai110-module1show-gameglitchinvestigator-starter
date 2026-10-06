# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x ] Describe the game's purpose.
      The game is a number-guessing game where the player tries to guess a randomly generated secret number. The game gives the player hints, tracks attempts and score, and allows the player to start a new game.
- [x] Detail which bugs you found.
      The HIGHER and LOWER hints were backwards. A guess higher than the secret number said "Go HIGHER!" instead of "Go LOWER!", and a guess lower than the secret number said "Go LOWER!" instead of "Go HIGHER!"
      The attempt counter started at 1 instead of 0 when a new game began.
      The "New Game" button did not reset the game status after the player won, so the new game could still display "You already won. Start a new game to play again."
- [x] Explain what fixes you applied.
      I fixed the backwards hints by correcting the check_guess() logic and moving the function from app.py into logic_utils.py with AI assistance. I also added pytest tests to verify the correct HIGHER and LOWER hints. For the "New Game" bug, I reset the game status to "playing" and cleared the game history when a new game starts. The final pytest results were 5 passed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

## Demo Walkthrough

1. The game generates a secret number within the selected difficulty range.
2. User enters a guess that is lower than the secret number.
3. The game returns **"Too Low"** and displays **"Go HIGHER!"**
4. User enters a guess that is higher than the secret number.
5. The game returns **"Too High"** and displays **"Go LOWER!"**
6. User continues guessing until the correct number is entered.
7. When the correct number is guessed, the game displays **"Correct!"** and the player wins.
8. User can click **"New Game"** to start a fresh game with a new secret number.


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

### Advanced Edge-Case Testing

I added three pytest cases to test edge cases in the `parse_guess()` function:

* An empty input
* A non-numeric input
* A negative number

The tests verify that the game handles these inputs correctly without crashing.

The final pytest run passed all 8 tests:

      
tests/test_game_logic.py::test_winning_guess PASSED                         [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                        [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                         [ 37%]
tests/test_game_logic.py::test_bug1_high_guess_says_go_lower PASSED         [ 50%]
tests/test_game_logic.py::test_bug1_low_guess_says_go_higher PASSED         [ 62%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED              [ 75%]
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED               [ 87%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED           [100%]

=============================== 8 passed in 1.63s ================================



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
