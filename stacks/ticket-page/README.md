# Ticket page

Adds one read-only page to any Brainstem: `GET /api/ticket`. It tells a visiting AI what this Brainstem is, how to
talk to it (`POST /chat`, reply in `response`), which agent files are present, and how to add one. Save the `.py`
into the agents folder, check for successful hot-loading, then exercise the tool. Hot-loads like every page;
remove the pack and it is gone.

`agent_files_present` is a filesystem listing, never an import or a claim that the tools work. The retained
`agents_loaded` list is empty because this page cannot query an authoritative runtime loader registry;
`agents_loaded_status` is `unknown`. That does not mean the host has no loaded tools. Broken files remain
listed only as files present.
