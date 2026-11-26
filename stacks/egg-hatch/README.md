# Egg hatch (staging)

Your Brainstem in one file you carry anywhere. Hatch it on your computer, take the same file to any AI, bring
the conversation home.

1. **Hatch it here.** `python3 hatch_app.py` opens one page. Drop your `.egg`; it is checked and your
   Brainstem starts on this computer.
2. **Take it to any AI.** Attach the egg in claude.ai (or any AI that can run Python) and say: *Open this egg
   and follow its skill.md. You are my Brainstem's model.*
3. **Bring it home.** Ask the AI for `chat.json`, open your Brainstem, click **Import**. The chat carries on.

Make an egg from your own Brainstem: freeze and pack it with rapp-brainfreeze, then
`python3 lay_egg.py <your.brainstem.py> <github-login> <name>`.

What is inside an egg: a rapp/1 organism egg (§9) holding `rappid.json`, `soul.md`, `brainstem.py` (the packed
Brainstem with `host` mode) and `skill.md` (how an AI wakes it and uses rapp/1). No sign-in or key is ever packed.

Not yet: the chat comes home, the memory does not (use a frozen snapshot for that). Unsigned eggs.

Learned from others: Docker's save/load and a browser's bookmark export work because one file goes out and the
same file comes back, checked by fingerprint; this keeps that shape and reuses the egg and the page's Import
instead of a new format.
