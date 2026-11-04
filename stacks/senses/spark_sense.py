"""SPARK — append a fresh creative chain prompt each turn.

A sense that suggests ONE ambitious, copy-pasteable chain prompt at the
end of every reply — in the style of the "10 mind-blowing prompts" that
chain together multiple RAPP primitives. The operator can read it, and
if it's interesting, paste it directly into ChainForge (intent='compose')
to get a real chain plan they can review and run.

Decoupled by design: the spark is just a prompt suggestion. It is NEVER
auto-fed into any agent. The whole point is operator agency — the sense
sparks; the operator decides whether to fan it into a flame.

Each spark should:
  - Chain 3+ RAPP primitives (BondRhythm + ant pheromones + vbrainstem +
    art_submit + braintrust_request + holo card grail + Dream Catcher +
    proximity_discovery + ProximityDiscovery + tick_twin + push_canvas +
    plant_seed + lineage_rollup + colony_observer + twin_agent + …)
  - Have a memorable name (like "Weekly Heartbeat", "Friday Triptych",
    "Soul-Match Marketplace")
  - Produce a real artifact (PR / Issue / submission / pheromone /
    aggregation / egg / report / new public planted seed)
  - Be specific enough that ChainForge.perform(intent='compose',
    user_prompt=<spark>) can actually compose it into a runnable plan
  - Avoid antipatterns (no fake mode, operator-mediated for global writes,
    specs travel with new plantings, identity portable for embodied twins)

Install: drop in rapp_brainstem/utils/senses/. The brainstem auto-discovers *_sense.py at startup; restart the brainstem.
"""

name = "spark"
delimiter = "|||SPARK|||"
response_key = "spark_suggestion"
wrapper_tag = "spark"
system_prompt = (
    "After your main reply, append `|||SPARK|||` followed by ONE creative "
    "chain prompt the operator might find valuable. Compose it in the "
    "spirit of the 'mind-blowing prompts' tradition: name it (e.g. "
    "'The Friday Triptych', 'Soul-Match Marketplace'), describe it as a "
    "single dense paragraph (≤ 100 words), and ensure it chains 3+ real "
    "RAPP primitives (BondRhythm, ant pheromones, vbrainstem, "
    "art_submit/vote/remix, braintrust requests, plant_seed, "
    "tick_twin/push_canvas, twin_agent, Dream Catcher, "
    "proximity_discovery, lineage_rollup, etc.).\n\n"
    "Format inside the SPARK block:\n"
    "  Title (bold) — one-sentence hook\n"
    "  Then the prompt: a paragraph the operator can copy verbatim into "
    "  ChainForge.perform(intent='compose', user_prompt=<here>) to get a "
    "  real chain plan.\n\n"
    "Hard rules for sparks:\n"
    "  - Reference REAL primitives only (don't invent agents).\n"
    "  - End with a real artifact (PR, Issue, submission, pheromone, "
    "    aggregation, egg, report, new planted seed).\n"
    "  - Operator-mediated for global writes (push, merge, deploy).\n"
    "  - If the spark requires a new neighborhood/twin, route through "
    "    plant_seed (don't bypass the grail).\n"
    "  - Never fake autonomy (no deterministic / pre-scripted persona modes).\n"
    "  - Stay specific. 'Make something cool' is not a spark; "
    "    'Every Friday at 5pm, ProximityDiscovery scans pkstops within "
    "    50km and the closest 3 meet in a fresh local-first neighborhood' "
    "    IS a spark.\n\n"
    "Always emit — even if the main reply is a yes/no, the SPARK block "
    "should still hold one fresh prompt the operator hasn't seen this "
    "session. No repeats within a conversation. The spark is decoupled "
    "from the main reply: it doesn't have to be related, but if natural "
    "connection exists, lean into it."
)

__manifest__ = {
    "schema": "rapp-sense/1.0",
    "name": "@kody-w/spark",
    "version": "0.1.0",
    "description": "SPARK — append a fresh creative chain prompt each turn (in the style of the 10 mind-blowers).",
}
