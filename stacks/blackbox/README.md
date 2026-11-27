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

## Install (two files)

1. The recorder, once per Mac:

```
python3 blackbox.py install
```

   It copies itself to `~/.blackbox/`, starts, and starts by itself from then on. `python3 ~/.blackbox/blackbox.py uninstall` switches it off.
2. Copy `blackbox_agent.py` into your brainstem's `agents/`. It loads on the next chat, no restart.

## What the recorder does on its own

When memory runs short it blames the job that grew most over ten minutes. It closes what is safe to close without
asking (a leftover whose folder is gone, git's own housekeeping, anything you list as `disposable`), freezes anything
else, never touches what you list as `precious`, and lets a frozen job go once memory is back. It writes one plain
note each morning. Settings live in `~/.blackbox/blackbox.json`; `"guard": "watch"` makes it only say what it would do.
macOS only. Standard library only.

One component is withheld. Fingerprint (sha256): `398a242a5934707e8d3dc1e64004aeac95783046bae4817400a71589de7187a1`

## Why it is not inside the Brainstem

A watchdog never lives inside what it watches. When memory runs out, the Brainstem may be the thing that is stuck, so
the watcher is its own always-on job and the Brainstem only speaks for it. The kernel is untouched.

## Status

Staging. One install, one day, plus one clean second Mac where install, the record, the answers and uninstall all worked: 4 of 4 real chats (frozen, carry on, stop, nothing left frozen) on a throwaway
Brainstem. It becomes more than a stack only after real users on more than one install, time in use, and a second
independent install passing the same checks. Pairs with `night-watch` (disk, services, spend); this one is memory.
