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

I used Claude Code as my AI assistant while working on this project. One suggestion that helped was when it pointed out that some of the game problems were happening because the game state wasn’t resetting when the difficulty changed. After fixing that, I tested it by switching difficulties and starting a new game, and the attempts and secret number reset correctly.

One suggestion that didn’t work at first was using st.rerun(). When I tried it, the app crashed because my version of Streamlit didn’t support that function. After I noticed the error, I told Claude and it suggested a different fix that worked.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when I tried the same thing that caused the bug before and it didn’t happen again. For example, I switched the difficulty during the game and checked that the attempts reset correctly.

I also tried running pytest to check the game logic. The tests checked different parts of the game, like guesses, score updates, and difficulty ranges. When all the tests passed, it helped confirm that the logic was working the way it should.

AI helped suggest some of the tests and what kinds of cases to check, like making sure the scoring works correctly depending on the attempt number.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number seemed like it was changing because the game didn’t properly reset when the difficulty changed. That meant the range shown to the player didn’t always match the actual secret number.

In Streamlit, the script runs again every time the user interacts with something, like clicking a button or entering text. If values aren’t stored in session state, they get recreated every time the app reruns.

I fixed this by storing the game information in session state and resetting it when the difficulty changes, so the secret number stays consistent for the game.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Next time I work with AI on a coding task, I would review the AI’s changes more carefully before accepting them. In this project I learned that AI can suggest good fixes, but sometimes the suggestions are incomplete or don’t work with my setup, so I need to check the code and test it myself.

This project changed how I think about AI-generated code because I realized AI is more like a pair programmer than an automatic solution. It can help find bugs and suggest ideas, but I still have to test the code, verify the results, and decide which suggestions to accept or reject.

There were times where i got too reliant on AI suggestions and stopped understanding what is going on. I understood that it is really important not to rush and take time to understand the code and suggestions before applying them. 