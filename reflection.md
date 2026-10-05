# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first played the game, I noticed several bugs involving the guessing hints, attempt counter, and starting a new game.

**Bug Reproduction Log**
Bug 1: Guessing hints are backwards

- When I entered a number higher than the secret number, the game displayed "Go HIGHER!" However, I expected the game to tell me to guess a lower number. When I entered a number lower than the secret number, the game displayed "Go LOWER!" instead of telling me to guess higher.

- Input/Trigger: Enter a number that is higher or lower than the secret number.
Expected Behavior: If the guess is higher than the secret number, the game should say "Go LOWER!" If the guess is lower than the secret number, the game should say "Go HIGHER!"
- Actual Behavior: The game gives the opposite hint.
- Suspected Code Location: app.py, check_guess() function. The comparison logic returns the wrong hint message for guesses that are too high or too low.


Bug 2: Attempt counter starts incorrectly
- When I started the game before making any guesses, the game already showed that one attempt had been used. I also noticed that the game could say that I had run out of attempts earlier than expected.

- Input/Trigger: Start a new game without submitting a guess.
- Expected Behavior: The game should start with 0 attempts used.
- Actual Behavior: The game starts with 1 attempt already used.
- Suspected Code Location: app.py, session state initialization. The code sets st.session_state.attempts = 1 when the attempts variable does not already exist.


Bug 3: New Game does not completely reset the game status

- After I correctly guessed the secret number and won, I clicked "New Game." The secret number changed, but when I submitted another guess, the game still said, "You already won. Start a new game to play again."

- Input/Trigger: Win the game, click "New Game," and then submit another guess.
- Expected Behavior: The new game should reset the previous game and allow me to make guesses.
- Actual Behavior: The secret number changes, but the game still acts as if I already won.
- Suspected Code Location: app.py, if new_game: section. The code resets the attempts and secret number but does not reset st.session_state.status back to "playing".



Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |


---

## 2. How did you use AI as a teammate?
### 2. How did you use AI as a teammate?

**AI suggestion I accepted — Refactor and fix `check_guess()`**

* **What the AI suggested:** The AI suggested moving the `check_guess()` function from `app.py` into `logic_utils.py`, correcting the backwards HIGHER/LOWER hint logic, and updating `app.py` to import the function from `logic_utils.py`.
* **Why I accepted it:** This was a good fit for the assignment because `check_guess()` contains core game logic that could be separated from the Streamlit interface. The AI also correctly identified that a guess higher than the secret should tell the player to go LOWER, while a guess lower than the secret should tell the player to go HIGHER.
* **How I verified it:** I reviewed the AI's diff before accepting the changes. I then created pytest tests for the bug. All 5 tests passed. I also tested the game in Streamlit by entering a number higher than the secret and received "Go LOWER!", and entering a number lower than the secret and received "Go HIGHER!".

**AI suggestion I changed — Update the existing tests**

* **What the AI suggested:** After the refactor, the AI pointed out that the original starter tests were failing because they expected `check_guess()` to return only a string such as `"Win"` or `"Too High"`. The refactored function returns both an outcome and a message. The AI suggested changing the tests to check the first item of the returned result.
* **Why I changed it:** I did not want to change the application code just to make the old tests pass. Instead, I accepted the small test-only change because the existing tests no longer matched the function's intended return structure. The change was simple and kept the original purpose of each test.
* **How I verified it:** I ran `pytest` after updating the tests. The final result was **5 passed**, including the two new tests specifically created for Bug #1.


- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project, I used a combination of Chatgpt and Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed by checking both the expected behavior in the code and the actual behavior in the game. For Bug #1, I first reviewed the changes to check_guess() and then used pytest to test different guesses. I also tested the fix in the live Streamlit game. A guess higher than the secret correctly displayed "Go LOWER!", and a guess lower than the secret correctly displayed "Go HIGHER!". Since both the automated tests and the live game produced the expected results, I considered the bug fixed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

I ran pytest on tests/test_game_logic.py. I created two tests for Bug #1: one tested a guess of 60 against a secret of 50, and the other tested a guess of 40 against a secret of 50. The final test result was 5 passed. This showed me that the corrected check_guess() logic worked as expected and that the new tests passed along with the existing tests.

I also manually tested the game in Streamlit. When I entered a number higher than the secret, the game said "Go LOWER!", and when I entered a number lower than the secret, it said "Go HIGHER!". This confirmed that the fix worked in the actual game, not just in the tests.

- Did AI help you design or understand any tests? How?

Yes. I asked the AI coding assistant to create pytest tests specifically for Bug #1. The AI helped me understand that the test should check both the outcome and the hint message. It suggested testing a guess of 60 against 50 for the "Too High" case and a guess of 40 against 50 for the "Too Low" case. The AI also helped explain why the original starter tests failed after the refactoring and how to update them so they correctly checked the first value returned by check_guess().

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
