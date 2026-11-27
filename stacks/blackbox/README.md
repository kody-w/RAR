# Blackbox (RAR stack, staging)

> Ask your Brainstem what your computer did while you were not looking.

A computer that runs AI work unattended sometimes runs out of memory. A recorder beside the Brainstem watches for
that, steps in, and writes one plain note. This agent file is the recorder's voice. Ask it:

- "What is using the most memory?"
- "Why did my computer restart?"
- "Is anything frozen?"
- "What happened overnight?"
- "Let the photo sorter carry on." / "Stop the photo sorter."

It answers from the recorder's own record, with no guessing. It never stops a job unless you name that one job.

## Install (one file)

Copy `blackbox_agent.py` into your brainstem's `agents/`. It loads on the next chat, no restart.

The agent looks for a recorder at `~/.blackbox/blackbox.py` (or the path in `BLACKBOX_PATH`) that answers
`top`, `why`, `status`, `note`, `resume <id>` and `stop <id>` in plain text. Without one it says so and does nothing.

One component is withheld: the recorder. Fingerprint (sha256): `c1e9f11d800678bda412ba7cfd6a30d636f1509fd6e9785442c40da5db26c677`

## Why it is not inside the Brainstem

A watchdog never lives inside what it watches. When memory runs out, the Brainstem may be the thing that is stuck, so
the watcher is its own always-on job and the Brainstem only speaks for it. The kernel is untouched.

## Status

Staging. One install, one day: 4 of 4 real chats (frozen, carry on, stop, nothing left frozen) on a throwaway
Brainstem. It becomes more than a stack only after real users on more than one install, time in use, and a second
independent install passing the same checks. Pairs with `night-watch` (disk, services, spend); this one is memory.
