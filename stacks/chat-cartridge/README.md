# Chat cartridge (RAR stack, staging)

> Take your chat with you. Any AI wraps a chat up as one plain file you own; any other AI carries on from it.

Your chats live inside whichever AI app you used. This stack is one page, `SKILL.md`, that any AI can read. It has two
jobs: **wrap up** (write the chat as one file, the cartridge) and **carry on** (start from one).

## The two lines you say

    Go and read https://kody-w.github.io/RAR/stacks/chat-cartridge/SKILL.md and wrap up this chat.
    Go and read https://kody-w.github.io/RAR/stacks/chat-cartridge/SKILL.md and carry on from this cartridge.

## What is in here

| File | What it is |
|---|---|
| `SKILL.md` | The practice, for any AI. |
| `cartridge.py` | Optional checker and joiner for people who want proof: `check`, `next`, `join`, `grew`. Python 3, no installs. |
| `read_page_agent.py` | Optional, for an on-device Brainstem: lets it read one public page so the lines above work there. Drop it into `agents/`. |

## Nothing new was invented

The cartridge is the chat export a Brainstem already imports (`exported_at, session_id, model, turns`). The three next
jobs ride at the end of the last turn, after the line `|||NEXT|||`, the same way a Brainstem's other senses do.

## What has been seen so far (staging)

One relay, one day, one machine: a chat was wrapped up by one vendor's AI, carried on by a local open model, then by a
third vendor's AI. 9 turns, every earlier turn unchanged, checker passes. Two lessons are built into the page:

1. An AI that carries on writes only its new turns; the tool copies the old ones. A small model rewrote an earlier turn when asked to recopy it.
2. A small local model (14B) failed 3 of 3 tries by claiming work it could not have done. The checker catches a wrong shape and a wrong count. It cannot catch a false "done".

Seen in one hosted web chat: wrap up 2 of 2 and carry on 1 of 1 (its page reader only gets a summary of the page, so the tool accepts a plain 1-2-3 list). Seen on one on-device Brainstem with `read_page_agent.py`: wrap up 2 of 2. Not seen: other vendors' web chats. This stack moves down a layer only after real users on more
than one install (proven-winner rule).
