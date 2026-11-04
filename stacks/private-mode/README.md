# Private Mode

Say "keep my health questions private". From then on a chat that mentions a private topic is answered by a local model (Ollama) on this computer, whatever model you picked; if no local model is running, the Brainstem says so and sends nothing. The routing lives in the Grail layers `providers` layer (1.1); this pack adds the agent that keeps your list and includes Grail layers.

Proven 2026-11-04 on this kind of Brainstem: a private question made 1 local call and 0 cloud calls; a normal one 0 local calls; with no local model the private question was refused.
