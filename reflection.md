# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The hints were incorrect. The secret number was 57, but when I entered 1, the game told me to go lower. I tried 0 and -1, and it still said to go lower. When I entered 77, the game said to go higher, which was wrong.

When I tried to start a new game, I got an error message.

Sometimes I had to click the Submit Guess button twice before the hint appeared.

In Hard difficulty, the attempts left became -4 after only one attempt.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code as my AI assistant throughout this project. Claude correctly identified that the root cause of multiple bugs — wrong hints, negative attempt counts, and wrong secret ranges — was the session state never resetting when difficulty changed; I verified this by switching from Normal to Hard mid-game and confirming the attempt counter and secret both reset properly after the fix. One area where I had to push back was around the `st.rerun()` call: Claude's initial fix used `st.rerun()`, which is only available in Streamlit 1.27+, but my environment was running 1.22, so the app crashed with an AttributeError until I pointed out the error and Claude corrected it to `st.experimental_rerun()`.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when it no longer reproduced under the same conditions that originally triggered it — for example, switching difficulty mid-game and confirming attempts reset to zero, or entering blank input and confirming the attempt counter did not increment. I ran the full pytest suite (`pytest tests/test_game_logic.py -v`), which covered 17 tests including ones specifically targeting each bug, and all passed. Claude Code helped design the tests by suggesting which function signatures to call and what edge cases mattered most — for instance, it added `test_too_high_even_attempt_deducts_points` specifically to catch the even-attempt +5 scoring bug that could otherwise be missed by only testing odd attempts.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret kept appearing to change because the original code only initialized `st.session_state.secret` once, but switching difficulty silently reused the old secret from a different range — so the displayed range and the actual secret were out of sync, making hints look wrong even though the underlying logic was correct. Streamlit reruns mean every time a user interacts with a widget (clicks a button, types in a box, changes a dropdown), the entire Python script runs from top to bottom again — so any variable not stored in `session_state` is recalculated fresh each time, as if the script just started. I fixed the stable secret problem by storing the active difficulty in `session_state` and comparing it on every rerun; when it changes, all game state — including the secret — gets reset to match the new difficulty range.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

The habit I want to carry forward is separating pure logic from UI code from the start — having `logic_utils.py` made the game logic independently testable without needing to run the Streamlit app at all, which made debugging much faster. Next time I work with AI on a coding task I would check the library versions in my environment before accepting any fix, since this project showed that AI suggestions can be correct in principle but wrong for a specific version (the `st.rerun()` issue). This project changed how I think about AI-generated code by showing me that AI is good at spotting patterns across the whole codebase but can miss environment-specific constraints — so I need to be the one who tests in the actual runtime, not just reads the code.
