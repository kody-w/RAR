# Ticket page

Adds one read-only page to any Brainstem: `GET /api/ticket`. It tells a visiting AI what this Brainstem is, how to
talk to it (`POST /chat`, reply in `response`), which agents are loaded, and how to add one (save the `.py` into the
agents folder; the next message can use it). Hot-loads like every page; remove the pack and it is gone.
