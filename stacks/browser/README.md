# Browser

Lets a Brainstem use your own browser, signed in as you, by reading pages and pressing buttons by their labels.

- Ask in plain words: "open github.com/me and name my pinned repos", "find the cheapest nonstop to New York on Friday".
- It never presses Pay, Buy, Delete, Allow, Confirm or sign-in buttons, and never types passwords. Those it hands back to you.
- Every step is written to a receipts file (`~/.openrappter/receipts/browser.jsonl`) in plain words.

Needs the browser link from [rapp-copilot-in-chrome](https://github.com/kody-w/rapp-copilot-in-chrome) installed and paired once.

Status: **staging**. Proven on one Mac (9 of 9 rerunnable jobs); it moves out of staging after a second install passes the same jobs.
