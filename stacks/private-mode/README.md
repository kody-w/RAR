# Private Mode

Say "keep my health questions private". With the Grail layers `providers` layer active, a chat matching a private topic substring is answered by local Ollama or refused if unavailable. Matching is case-insensitive, not semantic: synonyms and indirect references may not match. This pack edits the list and includes Grail layers; the editor cannot verify that enforcement is active.

An absent `private-topics.json` leaves ordinary routing unchanged. An unreadable, corrupt or invalid policy refuses chat with a clear error until repaired; the editor never replaces it with an empty policy. Local dispatch errors never retry the cloud.

Verify the supervisor log lists `providers_1_1` as applied, then test a matching chat with Ollama stopped: it must refuse. Installing files or seeing a healthy server alone does not prove enforcement.

Proven 2026-11-04 on this kind of Brainstem: a private question made 1 local call and 0 cloud calls; a normal one 0 local calls; with no local model the private question was refused.
