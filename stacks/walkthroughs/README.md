# Walkthroughs (staging)

A walkthrough is a simulated Windows 11 click-through that shows an agent, stack or distro working, so people
follow along instead of reading. It is optional: publish one beside your thing if you want a visual guide.

- **Play one:** `player.html?w=brainstem-skill` (the first one: "Give your AI a Brainstem").
- **Make one:** `python3 walkthrough.py new <name> <path of the file it shows>`, edit the steps, then
  `python3 walkthrough.py check`.
- **Data only.** A walkthrough is one JSON file in `walkthroughs/`. The one shared player shows its words as
  text, so a walkthrough can never run code, and every walkthrough looks the same.
- **Pinned.** Each walkthrough names the file it shows and that file's fingerprint. If the file changes, the
  check says "may be out of date"; re-check the steps, then `walkthrough.py repin`.
- **Always marked simulated.** The screens are drawn, never a recording.

Learned from others: app-store previews beat descriptions; interactive tutorial sites went stale when the
real screens changed, so every walkthrough is pinned to what it shows.
