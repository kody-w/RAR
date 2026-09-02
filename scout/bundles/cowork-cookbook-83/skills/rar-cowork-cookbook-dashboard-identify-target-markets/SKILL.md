---
name: "rar-cowork-cookbook-dashboard-identify-target-markets"
description: "Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_target_markets", "rar_sha256": "d331aede0c5e83de1de4c98d74151e38b34bda5520451e110e0f4782a2c7d13a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_identify_target_markets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-identify-target-markets:f37418bc311079c3ac72fc2ebdbc71c7821efe0e5e70cd4b4e1ea13158d8474c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_identify_target_markets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_identify_target_markets_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Identify target markets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 d331aede0c5e83de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_target_markets_agent.py` first:

```bash
python3 dashboard_identify_target_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_target_markets_agent.py   # or on stdin
python3 dashboard_identify_target_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify target markets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_target_markets',
    "version": '2.0.0',
    "display_name": 'Identify target markets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-identify-target-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-target-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e22838d4d5320f15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/identify-target-markets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-identify-target-markets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardIdentifyTargetMarkets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyTargetMarkets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(DashboardIdentifyTargetMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZPiRrruX9Gt88H2obrRLuiJibhIIAmQEEgIEO6JspbUvu/C1//9poCqbo/HZ8YR98Oloigtme/yvGtm1q8vZlP7Wfny5UUDZooIZhwHPigRM3UQLuuyMoJ/ssiCv4idpXUZWE2dldXL64sDKrsM8jrIUjh9X2ZOY4MKMZEKxO6ncbAZpMBBgrQGpWnXQQsQ8ShLiGNWvpWZpYO4WYkEDkjrwB2Q2iw9UCOJWUagrpBPSJaDtILToTADYpVZV4HyFUkzZEnQFGLakFuFpAA4kIkF5/sAaQPQgfIzlA70ZpLHoHr58vM/Xl8CeP3y5dcXOzYr+Ohl+S7C+sn9eGcuP3jD6bGZenBcPkB0UnifgxIKm8BHDnCR592Po6avyH//d9TB6dVPX76myPPz9WX8UZv0LladmVUNpbTN3LSCOKiHz8gi7syhQkpQN2V6hw2Cm3qfHzO/Ucpy5O/jux8fTD5DMX/8+gKxKc0R+q8vPyEQxa8vZTNefx6p5D/+9DnOIBA//vSNTtVYIbDrkRiU+vPb8/5JFg78NjRw71z/Dqk+jGyBry/fKTd+HnKPesKZL5/DLEh/fBDOy6wFqZna4Mef/oys7QM7ioOq/o/o/vwg7APTgTo9Bf/p9Q7yP5DJU6EPmn/ONodm/SuawOHv7F6RJ1B/RvuO/z+RjmEAVB+I/0ty/2rC5O/Iz3+q2/804RVxv74sQQxDrTStGHxBfn3T9ivu5x+cbw9/+MdvkPS/JaNlTWnfKbwlZhq4oKrf3n7+obo//uEfP//Q5NDXgJm8NWX8r2j+K1zvfH6H4HPUj7+fC/nraZRmXYp8eDrya5b/r/K3z8jJjAPn2/PqC/J9vIyfCTIq8c70AcF3MVNBWb/D8aeX32CGSKE2jX1/DaP8v/4LkQO7zKrMrRHNzpoagQaugwSMwh/9oEKOz6D+RduuJelz4vyCwKdjuMMUYTZxjQilGcQIjIfR4qMGmYv88r/te1qFCfKRVqcf6fDtPRW+PVLh2zMV/vIZOfqQb1YGXpCaMaIu9nvE9ODgkePdN6om+dSOTO8J9y6Fyq3HhFM1Mfgb8su/5fJ2J/g5H0Y1vqbQLo/0XYMkz0qzDOIBMcc8ZQ01+ATTK8wlZRbHlmlHyPjV5J9HbM4+SJ+I2bCigB7YTQ2QOLOh5G4AU/IrNHqVxbAc1COOVRTEMeIEJQQpK4d76YFYfxmJ/fLLLxYU/Gv6SMQE8ig51RQO+BAY+fQpL4EbB55ff02B7WfID7/+9gPyf5D/adad+MhjD0vCHTDozDGy0ZQdAoFpEjhsrD7QxqZzt9yvvz0sMUqXwhoJ4ylwA3CfDKl9c4NRg4d53m0DdR5FBOWT0+9xQzof4oIENUQLxnj1+jUdSWRwaNkFFXgH8TH5Af27sR98RptUTwyhndwyS+5j7x44GtPOSuczsnaRD6SgutCu9WhRP6tq6LSw3ELXsMdKatbfTJhmNVLBuKnc4RVpKqjqSPkXC5IewUlgcjLrXxCZ28M6l8XwawTozh7OztJgNPzTWx+PIZHyB+hj7DuJz8gOQDSR3CzN3C/NCtzHuebDI2B9e58PiZuw5nfIWNHBaKN7RN89b/0nncT6nxuQj+qPfG1wFCOR/6+al1GVhSCoK2FxXC2R1e6oGg+/G8UaYXj0bLCLuMtwD6JvncV7EnpPz1/TOIC2Koe/PUa6d1d7jHmkvKaEMqgLFXlXu3zoVkOHGT2gLEcnN7+m73XgFeIEzVWNKQ3GdTRmieyD4fj2XVIfojXef+sJkIcvjjECvRzJGysObMSFQNwDovbLMdyedoHeA8bQg/Fh+7/TCoHUoWdA+ggUIoCQw1pxh24Hwwb2UY8Y+BgejJ1W/jCzg8C4Ap+R8+jm0FUrxAKwXRrHQBR+uJNCEgAxhiJ+IFz5Zv4QZmyKnwKaoy2yxKzB9xZ4voQuOxYcyO8jHiFV0zFriGUHjQDDrX9Y9kPOp62gsMkYG/dJvzf3U1fk+4L1tzEmoYzfagLs48da/x04MJGXSXXPTbAKRxWM+gQ8HQh6wr2sf35U5kfp/5Dlyx9WAj/+tcXCvdbqv7fcF8Sv67z6Mp0+6uF7OfxsZ8kU+kiQg+pbafz0HmifHoH26RlovyP8wOkL8teE+x2Jp1d/QbDP6Gd0fCUFNhjd9vmBWHCfWOMTOb79mqrgm5GfnjCmO5iCYUy/V533IbD0eCXwxsGPKlSNxauD9fKe/O5V5MMRnmECc2vqjSWzyr4L31Gn0awPq30kafgqHdO/M7Z6HhiXQfEofgVevqRNHL++pGYC/pPlz5iIoa9CNMZVE4wb2DrVAbjffbRR483vF4H3iIKpwMm+jIEFix5seV+Rj+71FXlfT9yXaGkDF1Q/j53zyBIOhX8+xn6sMC3wAldw9ZCPkj8WSWPD9myk/yjEGE9Q4nuCHcvFM0BHjn8gAi88D5R/JKLcL8z4mSUq6HZjN1C/x3YF5XRgZ/WKQNvBmINhBLNjAyf8kQ3kU4KigcXZGdX9ht83tbKHLr/dYagfK81fX96zxXj96BQefjOuQv/jdm7E9L0Mv42UzXH+vem6Q3xvVd+gesFYbr975Y29w9vDD1++wFwDXl9GIMsA9t+3+8r65SEO1ONbkwspwKzxqRrbhykMI0gJFvV81CGCGe87BuPjwLmPHy++/Hln/Gfh/8UlGBKbWTaBYSgztwnTZnDXxoHlWDaD2cwMx2DXhQIKMKjtkBYJMGBiBEbNnBnJkDaUYrRkYj6lmGKjDaD8H0D/9Xb95UEA1gucokdTEQRmwjqP2hSYEQ7AHEDa85kDJacwQMwsgrQck6JwlIT3UBGAuiSU3MRtxsEIc6T37BcfUr299+bvVnmkgTeYOZNglBk3TXsG9SedOWPSNiBQi7ABhmMOQwCUmhPubAZIOP9j6tMyo+Eeio9OC1tF2LS0I59fn5YeHZEm4UiRrNaLx4ebzk8mc2Ys1bfmJQ2M62W6tgKd1pyaz8zu4qhounS4yAN7J0sXvBMFSr6N8mW4W+L1ymTb7ODa68lwJRlxUPlBZ8z+sGW8636dbiLGmTBiA2yF1y8qLejNEGfNrrglIIiLurFordaEVuvL7BKfB7xl2xIj5yrG9BVanE63lNk7rovv2lourCMbCokq8kZewJWROfDL5NiRJ6ohOH+32RPM0okLfxt3F0kYOkyqraw/RHOjcILbbTqlN0C+OqFS8ZwkboL0XHYaEzcbgRY9VEnTnmxvVW+nPH7c4fO2DKYyMC5nzojlTRMuXUxL4qtFd8Jcz8y4FbY5s/Wu02B3XZ5PhXXxaGzl6zPooEViNRuO53i5y+y0UCOFnVG7G1/RFWGLRSLh1frkl9rFuJaXKOdnkr6ah9k58cKTHW3jE+Y7JgHt4qG0lHA5CAmtqEvdXQ8rdJCOMj+0ci+CHR359s1YhNc1uBh8qi3ZibnT8zNbdGfqLMd1nRoOW9X0wVoY/GY11FZUGIx04SZ2Fp/xAGMCK8z5XL+VEXXuotporWVQO/KOYJWtl2MHYtdNpdWp3xlcXWFieRZ3QewoK/rclkJhM9vpuWWv82K+X+sVS4INyWx0vwwUmSqnacbGRmtPRQAs6XS7VaJWUD5owNlyXXqFbzG7d2Urp5VSoGbaycSJYLZNq22f6rqRpdd62C2NjOkGa3s5d5Ut7bczMz3ERmgJxDxRymE9ONu01XX63OhtH7P4jJfmkWRxvL8f6l5Z63aZ6NsK92/cJp3ie+sUbomiCbe3jN7LUnWbNaF/pIfdyt8OK+VcHk0/18zm/nssguklOYfCNPcL9xBNvMStbLfL3ExTGfyQbFfSXJyHvrMvd+FcbuWlR/MUVrauHOOXfhmcq0EyW1Nc6zl3mjX1KdQoWaUH+XhiM0E2zv2W8icY07p5tMXIRlWTRTlFq1xTDnMKvWXb44BB7AQuKyUeW0Ya54KNyu48a6On69ug+v2kx9U1WB+lK2es9BufxOB0UsqbzyviCmYPOb0sin1YUliYV6tbegQauSZWQNv3hO8znEMrG+WwOR/Xsxt9zrmS2nQeNRU3jqXZmyuuTIc9edEPun0J6SMQyXZdSUyikftTjO88db03cE4V+APqgGPvk8yhV7aLnjM42dny6UQKGrMtdKe7hkYX7lVeT2t3q2SZe5aFRtVmajQR8Y2+vwSzDrc3S+VIStoG3Z1IprxsZXGSz9eWgp3ao9niDWmoc03D+f2x1YCD64BdJ+ZeaKJTYaib48WReorGNoaoMGudTzPgHjBY8dUhI+SLTK3cJktPm3g+M8LrjaGHjRSvmvowXaOTw44pNVSgGbpNZZCUt2WcRr6J+hye4KdDjMXzm2Ecc35I1MtKxmLyrCWh1g9efbUHVHcms2HQDml8MU1qK3hHcTZrHU5OiCsMNLwf/Lrc1q3YtJsF7k2WV5nZq6yOzRaCyATkZr6KZVTDSuLghE4zLZcJQaKlMjkRqHLqb5heXeXtIinDkpVhazkjh+tCauzZRTGyIV21ikC6V483er/ybwXhSIa6cHParZJ+dt2V4jXdprZa4WXcg/6q475dt8U+PsXVNfKJiqv5xdpdb6WLttlMF8eI4y02AAraLdYgslea7AcL1Dqc2oIpw82a1z1pQLOEjFS/6Hb8qQ72HVncZHGZc8HK6uOL5x11eitWsw1DUgwR+0st311LtgmwucJijlTGmKmguhKpqXvJGgqkV3rqpjm/jrg63sg0PbnsNE23dgRda+XFjph1VCgtDBR2OjU81nNuhGhV8lI1fHLWaOWNmW7bWTCd7m+bbHYJJQJCvTqpHOPglNuavnc8cBcz2q0N/AYlYtdCdOH6CPMPi3oeNZlv2M7RXl0W2/radJjA9QIWYbtjhK1nFE1yTZSap0JqY8VjqOMBI1cMeRmCWN9yOk90zZKuY3tmeeKBCGelOE3SNfRA90pXeZbQpkeu9CIvClgn6Tiqbw4/124F1m6vgaYvLkKFCvUM7LG83F5R7BztMrS8FFNBZq5iaUwWrO318magoujE5kzlXKfc6ZzN6/WZD3HOxHyCuTFSclPLZU4B3DjTUnXaUpQXFuqGOexPWqvN8dWFWBHGYlhHpntuJhtOVkxNvuh9VCdkwhbiQVjW1gz69KG1j3i/XUjO2duem1s5r/s6XPVgoLHCtK9khfUTAuxQtuI4sIbtexEvTxlORvKKXVnyRSKWtw5n1YGflbpWR/5xthLUxTX2Ix9d3XC9Ps+2lnyKSZDFuM/y52Gxn8/ON0CdlC6bbbJwHhpLdqUfCbqliHaT5IfS9IKdWBnC5SpUDAqEBkM7viRTOT8NoTTAvHOTj9dZ47VUJKAUR1qKLtlC1Q5UDbRrUfChHg7+FXW0TEuZyAp146CUu1K6srRZM6G4GpotfSrnHjpXilW6ngqAzM35ooGVblnKVJd3oDAw4M3K4ZgE5xtbVpp34SgjWiVdph3odSFv2EJJjnxZ7RsmRX3aWu0W+yh1GUs89+yUCcttZIf8bcAW3pKlTthSabxbqsc7HdN5x91HmTqZ7K20i7v1WZ1uBI4MLbQjmNoX2crRd0ci21lMyaLFpD1J9JXw+6s0XJXNBKubuazKxHEVsHxX1q7DHFbham1sV8trhuP40jLUTi666XlLDtJCUXpzHzHX5qZPcqb3VHydsBq9O9Q77QoofDkshWhjzrUga2TOAyzpMAoXKzlvYXutUVaSfuKkS1nrFXNBFdVbLddWd3H5ktNyQZ7wKE7GeiA02r5ccTxOFp5/u3HzS3SqFhs7YZ21muaid8mjVctoVi8ey9LOK9iCs9dm4ca3A0j3qSBWDi/1vl9LDiqkHJ4f4pkqmomdXbJtKGOz1PCaYyJ5HioT60PCXk67fnWw0Ug06MqJNoGGVvNDCaTS8Mv1aroUziJJXSV6w/a4GRH5bRYVrLntM0u+xeb21JSmFvLDuRUXZ9LEJ2gVTzQBcJOoWGHZ3mYnqD3Zbwfn3LHVPE761JSKy+LkwdByystyp0TtumhzwF7r9KLRzSHrjdQdcnqTE/PmHPXupPNCrzxXwXUgtUpLeXKt+Tm36SKOVRgq2EIDh7vTVsOLIped1Xkn2EunC3WGT6YrbTcfjL6Zs/2kvNS00gjrQ1FEWGYQ59rUF5WvoYZ1Y/nA4Q9sZq94E7YqHMOaRVWnGhqddS6PVSJntcvZUQ6KpBCDxbV+sMP1hFr1YRZHuyiTLstrbs2w1jC13OgYUpV9jKbPR5uXtS0zH+rJRg3YJpoKO39fnw4+oajOgK5tJeVziV0E/N4/l7FcyKa9FITVQFWxXYF1n1JLwd3L08VJX9r8rb4K2AajWhMKn3ACEPe8Nh17ZwwbiPoQT51ebGi54CQ2Do38ogCmw0gXPxkFd3G6LqGXqY52e9OdcxW1xhYrHqvRWayVW2wlcNJa6TphucB2rBhQi4A88TA/c/3hdm14WFPSo0mc+2B56h10wRX7PD+R12qfsth8UhtcslmrUnE4k0azW3QTV/Uic4XxJBY6ci6J4d5M+KjlZK7kyrhB+WMXzDi0bi4hXPvNoYrYzM8Gb6vHNzUtj/HNPw1eNj2Axay4JLe2b60ziTFzxnHBzN4Xoe4SGDhapZE5Vn010eu+Jm0RO++nOJNuGHtJ2c1Fd3YQC6FvmgrzsmhNJfR8G4gm0DQV8EOYkUlzU7xto0rWmamYtD6IaZUUV9ycbhlfv63ULZXwsnzMSpesyUvBHeqFpe8usUzQIcozxZ5TFnx4YDR2olKouL7ML3ps805wnONm0V1phdkfLXyHm1Srnkrp2KPXZBpfVHBYmoYryldLB1Rg3WpjiQIQutMJTk/JhYUW1U4iL9NZ66YZxVhEo7jWaQnXDXNxaxVKdUIXzA5diRFFby4H4Li4acR2gZ+mhtasjUpo94PJd4S/yHucXB/FRCQXkeFGRODRoZy4mC36WLilbK5OlYEUsKVJO1sl7Gy5rvhsk1aKz8DGaEZRA5/xG/nocEMwBC29kgksa9xlsqDb2DH2U4qg936bVZkkbcm9NV+Suzp2CJyfssTGvVpCtDCOe/1KtNWUtjxZPAymeSOtJEtSsadvGGoysSnOr7tmO6X7ORFu/IuzOs0Xcr3gd+nyWE6kZQZwe7pjroFU4a1lioms8gyHV3l6ndQ5AyyqPC3ttpGXkjA9KyR+bdKZW8/8BA+0cHGcE8X5qKYpI0qqfTQknYpSXW03DL6egABQ5zkXdx4LJlcDuOvmWrormPVtBVppWW/Z2fUqiXv/UAndBZUNMO9oOZoHxEUmtXmPpfwtJPhtz8PenPR9B5vy+xu9E44bYmU33VxnsU1ununpgrFiTz8x/ibaiuxmxTjkKuhs+rYGvtFe2g2mZVa048jGcdXAvhLHqbGbgMYFBMXk0g4/EwlzHZvf2y5UrJsbc7iF8fiwniornrH28nZKbMLWb+oMH2DYTloBrpG4QNx1+2voMVO9d0Kvw2qOFdF5xXrVBT2nxKlmwGnWmyFxIhbYohGCjqHZMnQioT3NqXNz3O0cfEJYui4dGMzaerUYYw1LeEzDufLisFtR7klgLzBtblC48loyQgsbCrFUuaU3F0U00C8nZZ5v7HMaBYx4JtVlF9ZMgOrLkr5Z+3Y+LXoHS2fTucLRsz0NlkBa7p25o9SHWRba7TzDpda+mVNvK7fHxq/T025H3HDHKJieyAuB6usWdafkye7JQpgxkxXeUObEqXgyKLvwuF0Rt5yNVdE+UuVkVR1B4fhCmJ/bZltMOAZvcRfdHw/LRa6JmDPdH4+psV2rAVw3goG5LbvcakMBSHvDmU4bMpvSzcByJ6uaZTLwRXW+8Oa86pX+YTeDTUJ/MyMzPlidQi33ZzxlcJS4iFmPrfs1N7Coi+mTsMcWaUW6kn+58NVxH6jtnpAX0s7bkiDmzvgSt9CrTml7rC7U5CC4+BAclszQWp2pMhuHkM6tCaiDoFRkAJwLuIrukpBuHiu1srix/FaVcQFXjppzvLm+lVJdb6KztMFnvqz4DWtc8vNKSohVFdenqX5e6nv8yN+kNs3b60Lc05TN3jyBGnbKtGK1kxA1FMvtwhygUsf3mBZHaZCezalGiJ13bMzuFkY20+4ru6m6uQDXTjdcSQp+e1gsXl5f7me8L18wlMbnry/jOcBzN/8v7QV7tyB/e5IiGAJ/ffl/t1H52DR8P+m7b+0D0/ly5/7lL0j5j9eX0g6gRI/t4ypuvOfm5D9txn76tzvE4/ThcUo9Hkn29ftJSG169x3sIHWaqi6HtyqLm/v+NUS6qcb/U6nenscIL3e1kvx+JvHOcdxXz6Caef1WZ08dXsb/IxnP2YATmDV43nrP7X44eYAmC+zqjaCpN1Dmo6bPI6dx23Y8c3r57f8CURrB0pQnAAA= -->
