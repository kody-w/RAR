# Rooms (test distro)

Summon it and you get your own Brainstem whose job is group chat between AI seats.

- Each seat has its own personality and its own private notebook (SeatNotes).
- One helper Brainstem (same pinned kernel, fingerprint-checked) plays every seat by swapping
  three links before each answer, so ten seats cost one process.
- The room is an append-only log with a bookmark: stop any time, "run" picks up where it stopped.
- Turn budget, hop limit, DONE: and ASK_OWNER: stop AI-to-AI storms and hand control back.

Try: "add a seat alice who is a cautious planner", "add bob who is a bold builder",
"start room plan with alice and bob, goal: pick a weekend project", "run plan".
