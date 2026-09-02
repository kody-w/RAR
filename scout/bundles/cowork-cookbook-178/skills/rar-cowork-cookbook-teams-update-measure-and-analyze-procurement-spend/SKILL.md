---
name: "rar-cowork-cookbook-teams-update-measure-and-analyze-procurement-spend"
description: "Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend", "rar_sha256": "1851943934ac7750ba5d1146caaf84bb255fab373a62b4cb5f269c34e498b151", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_measure_and_analyze_procurement_spend_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-measure-and-analyze-procurement-spend:3f414b3ca04c57d19a4f623cf8f178c44c2ec89f6903d927f7d5053fa13c78bf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_measure_and_analyze_procurement_spend_agent.py` is
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

Measure and analyze procurement spend Teams Channel Update — Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 1851943934ac7750…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_and_analyze_procurement_spend_agent.py` first:

```bash
python3 teams_update_measure_and_analyze_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_and_analyze_procurement_spend_agent.py   # or on stdin
python3 teams_update_measure_and_analyze_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure and analyze procurement spend Teams Channel Update — Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend',
    "version": '2.0.0',
    "display_name": 'Measure and analyze procurement spend Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-measure-and-analyze-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bdf27a411f8d5dca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/measure-and-analyze-procurement-spend'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-measure-and-analyze-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateMeasureAndAnalyzeProcurementSpend(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureAndAnalyzeProcurementSpend'
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
    print(TeamsUpdateMeasureAndAnalyzeProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpruX2FqPrQ9qi52EHXCEVcgJBBCK5vkdlSzJIvYd0m+/u83kVTV3WOfmXGcibjqqCoEmW++6/M+SfbvT3bbhHn19Pq0B3aGzO0kiUJQIXbmIULe51UM/+SxA38QN8+aKnLaJq/qp+cnD9RuFRVNlGdw+rSy/aZGbEQDdlojbmhnGUiQIq8bJM+QFNh1W4GbXDuzk8sVIEWVu/BeCrIGqQsAn9SN3bQ10kdNCEchUdaAynabqAPIxLOL24VgVx7i5xVStpEbI1AjOwAvUB9wttMiAfXT66+/PT9F8Prp9fcnN7FreOvpppZeeHYD1Lsuk8yb3DXZfFNkP+gBhSV2FsBZxQV6J4PfC1DBNVN4ywM+8vj2Uw0S/xn5j/+Ie7sK6p9fv2TI4/Plafi3azOkCQHS5HbdAA9x7cJ2oiRqLi/IJOntS41UoGmrbHBcDU3Jgpf7zG+S8gL5ZXj2032RlwA0P315yqEK9uD6L08/I9AZX56qdrh+GaQUP/38kuQ9qH76+ZucunVOwG0GYVDrl7fH94dYOPDb0Mi/rfoLlHoPsgO+PH1n3PC56z3YCWc+vZzyKPvpLhiGtQOZnbngp5//mVg3BG6cRHXzP5L7611wCGwP2vRQ/Ofnm5N/Q0YPgz5k/vNlCxjWv2MJHP6+3DPycNQ/k33z/38SnUQZqD88/pfi/mrC6Bfk139q23814RnxvzxNQQLrpLKdBLwiv7/tN6Lw6yfv281Pv/0BRf+3YvZ5W7k3CW+pnUU+qJu3t18/1bfbn3779VNbwFyDVfXWVslfyfwrv97W+cGDj1E//TgXrq9ncZb3GfKR6cjvefFv1R8viGEnkfftfv2KfF8vw2eEDEa8L3p3wXc1U0Ndv/Pjz09/QLzIoDWte3sMq/zf/x1RI7fK69xvkL2btw0CA9xEKRiU18KoRrRHUX/dK/Jy+ZJ6XxF4dyh3CBF2mzTIvLKjZIC5IeKDBbmPfP0/7g1WP7sPWEWbAZne2hs0vT1w8g3i5NsDJ9++w8m3G05+fUG0ECqSV1EQwUHIbrLZIBAGIZBGA/bCZKnb9HM3aAE1jO4otBPkAYHqNgH/QL7+/WXfbiu8FJfB0C8ZjJwNw+khDUiLvLKrKLkg9oBkzqUBnyEcQ7Sp8iRxbIjTw6+2eBm8Z4Yge/jUhSgPzsBtG4AkuQtN8SMI4c8wLeo8gWjfDJ6u4yhJEC+qoBvz6nJrIjAar4Owr1+/OnYdfsnuUE0i96ZUo3DAh8LI589FBfwkCsLmSwbcMEc+/f7HJ+T/Iv/VrJvwYY0NbCE3D8J0T5DFfr1CYO22g2dqZEgcCEy32P7+xz00g3YZ7KKw4iI/ArfJUNq3RLm1wVu83oMFbR5UBNVjpR/9hvQh9AsSNdBbEAXq5y/ZICKHQ6s+qsG7E++T765/j/59nSEm9cOHME5+lae3sbccHYLp5pX3gsg+8uEpaC6M662ph0Mb98CQBSBzL3Cm3XwLYZbDBg4rq/Yvz0hbQ1MHyV8dKHpwTgrhy26+IqqwgZ0wT+CvwUG35eHsPIuGwD/S934bCqk+wRzj30W8ICsAvYkUdmUXYWXX4DbOt+8ZATvg+3wo3EYy0CMDA7hl763mb5mn/o9YyJ3BCA8Gc+cMyJeWwHAK+f9McwYjJvP5TpxPNHGKiCttd7hn3EDOhhXufA4yjNvkW/l8Yx3vAPUO3V+yJIJRqi7/uI/0b0l2H3OHQ6i4B+Fld5M/lHt1kxs1MFWG2FfVkN72l+y9RzxD38BA1QPcwYqOB3zIPxYcnr5rGsKyHb5/4wvIPQsH78H8RorWSSIX8QHwbqXQhNVQaI9IwLwBQ9HBynDDH6xCoHSYE1D+EJIIhgv2kZvrVrBgIMe6Z//H8GhgYVALr3WhtrCiwAtiDgkOk7RGHACp1DAGeuHTTRSMMvQxVPHDw3VoF3dlBsL8UNAeYpGnQ/J8F4HHQ5isQzOC631UIpRqw1SDvuxhEGChne+R/dDzESuobDpUxW3Sj+F+2Ip838z+MVQj1PFbe4Acf+AB3zkHQngFs3nIWtih4xrWewoeCQQz4dbyX+5d+04LPnR5/dMu4ae/t5G49WH9x8i9ImHTFPUrit575XurfHHzFIU5EhWgvrfNz/f+9flRd5/hap8fdff5u7r7fKu7H1a6O+4V+Xva/iDikeavCP6CvWDDo2XkgiGPHx/oHOEzf/hMDU+/ZDvwLeqP1BiQD6Kxc/loQO9DYBcKKhAMg+8NqR76WA9b5w0Hbw3lIzMedTOgUTB0zzr/rp4Hm4Y438P4gdfwUTZ0Am/ghfcdVDKoX4On16xNkuenzE7B3985DQgNUxn6Zth+wSBA1tVE4Pbtg4ENX37cP94KDiKFl78OdQe7IWTLz8gH8X1G3rcit71e1sK92K8D6R6WhEPhn4+xH5tTBzzBrWBzKQY77vurges9OPiflRjKbUgbMPT7/KN+hxX/JAReBAGo/ixkfbuwkweIQLAfeihs3Y/Sr6GeHuRgzwiMJCxJWGUQPFs44c/LwHUqADsAROHB3G/++2ZWfrflj5sbmvsm9fendzAZru8U4p5FcMK/QPwGJ7837LdhKXsQeKNnN5/faO8btDcaGvN3j4KBZbzd0/TpFWITeH4aPAu7WhJdb3v2p7t+0LBvhBlKgCjzuR6IBgqrDEqC7b8YjIohQn63wHA78m7jh4vXv2bZfwsuXkmfwimHdG2McmnWwzmb8hmCdP2xj7Njl6JcArhjzmc4jPQ4gvVZj8Zo0rdx0mXHjg/VGmKd2g+1UHyIEjToIxT/C3uBp7tE2IEImoEi8TGNcxTJkZTtsiyNOTbt4TjFuLbtjynHIWjatx2SJW2GcCjXoX2C4VySAhQ3dnAaH+Q9uOddzbd3nv8etzuOvEEsTqPBCMK23bHL4pTHsTbjAhKDPgM4gXssCTCaI/3xGFBg0PQx9RG7IbR3Twx5DmknJH3dsM7vj1wYcpeh4EiJquXJ/SOgnGE7JurswuWoSkbnM1oHLW3mixWI+ZFxKdft2JIn6RQssaiWDUIw6RhCUju5WI2i2nyXn0ZBx+5HzJEA5lJRjZV7Ctx5uV9pLru+1uxSHY/q2UTjGdncNxFjxFKqoMSeQHVzkZ+2iyzFdStIHGV5pvORNo+aNX6V1kYERooxOyrohq2c0eKsHIEx8xbLxYyJ1OVhvwiBM+UWrYJnhpFcCzvAitxfKYmmFJyi7xdMXI9kTzPtY2Tr1blpnEVoh8rScEtJxtfZCWdRoB0vxzo7jU0tITiAngVlRdSJGKgeJqDQUlyxTJy2HctUZ6KpNofjxl11s4NW9ckhufJcso7opLXInF+4jE5hMr8u46AxCyCRl7Qxlpnd7nGQlzN1XCkCvayAsMR0JwVlUq8OM3+ZGMVKu+xSsBXKS6c5sdfNr52FlWzhoadUb/WLRm9zw1wo4yRn+k5lrtk2SmIowNZOFSOG9PYULxJfWKqWYUZ+lfmqbAsMWSwaId+JqUtb0+N+vLoWoDsvZSzFqMPighlcjFa8ZLeGnQiwEG2jVGr30kTJMa7iWjqfmV6uD0aH4VJlLlszdDZiwnt1Gmlo2pPJHm7yONjwqWk/1mhsd5xa+t7eG9KM5BkyLckqkZvOoSl1Kk+Na9dXsmNlnFBJThg0XdOf4UVy4ZNrxpj744lfOtdIFAjZ0oudtvYsPDqvwi4Z9+ZuRZpHXZEXrntAm9xRz3YW5jSszLN02pAzrCiE0ZUVZmHHHShcECcJW87nVMFqM8yvXKdkk4OBGyHNro59UGvdhVavc3t+Wgmzulor+xSHsmZr/2Csai/TDS7CDGKmVdV0tKvpzEVn56Y74KPFHkRsF2b+ZE1ml5OI6QWDohPV9rWKHB38fG7lHCgj1trwMc4TckEpxHnPlMqlxg5xXDZGaRxiSZJkZxbWsZdQJx0rpFIlJPLMiWulThZYoC8J2JRWWzAjMXGjj1fYxOnUvHIWmKDrpXDqJ/JaLqMiFU77ab/HLyqzmwvaSpObVG6DRNTPR2uVriWxdwF3bY0ZtUZZZWdWdqiWswW5DCPrTMlhoI98Xuzgj7RgzsYo9vZ41cVm69BMSuz2Nqk7m6QgVkSJizSOdh5aj3MyOSV6oaqj6hQ7q6PlpuZ5lPUqqkS7RdPJaXlJtxSVHcKrNSv4ZunXPsrJV3QZFEpXFtLVYkjTWBuLNI9nDdOv/WM527ETv+BCW8OJRm3yUtXmKNn0Pi4nrkFRBxxu+8cX+mivcaPT5h1BJMF+qdu6IZ3xRb6AYK8nO6WLSgNm/Give04zn8fLy7qNN5sc+LxB77Mah+zOOUWCc82tsVk1JSFSke+7zELPCabM8EmvKMJFmUuuc0KxhW9vhfM0oRdGk086vGnU04VhYbGssKgpFsuSt5n6WpzmrVccd0tFp63QYUVCdXuyMN0LJZoTfzrWjLTa+/76jGlaic4DVnVYNybo6WyZBfOdd4x2lIA6xOxqjSLzbFbEyTv3m8vWMlBHNTOPEqZz1OnplNo4eJDL2IW8ZuNVGnIU9GfRhqNmNsE8yvb7U9gU+XJib0dGtYnDpU/zfMH4EXMei6t2VmrYVQG+FY2O7XZu+Bp3jI+aSAAH+PJ+Lqy3ZjqZ0LpjrMSOmYqrk8UHhpaqvSAWh6M0046QPnUteVKn5/Rgb4NNhJXBaa9NiPmRyhtx71p8K00meKEUEgDHupyHE21l7qS1ux+5yiUqDj1z4p2y2SxPKy3zhY1cX8UxmlfLVZcV4xGwMiKc7YWUTysXRrIgkiRYbGDgKQKc83XBxx5oHDm8co68Oq+WrMBORPkolv4S4KiyHLHA8imuO45TLAKKdd5jrtpXJG66Yj3pRgtRkbzDODkmRqgsmNbbLTLDcsZW77un9WLWYLE12VflTAKt7wXw14hb0VzcnPTZVifzcIPh/CE3VDKa6ufNxFtpQZpZvBL4O0U/JztcQ0mhVxVSTVQexY7rcFapnXpqdA/fb5ayqacWfoj3FIUXO1f3VOIcrMZzy41wxwkObWmbs+4Y2leTm1fWJR7x032Eu0rEYbNkvmDHYEFFCXG40LNDfPZ5+7rFIMAlm4yS7FFLZWetAeQ1x1eyynRnWj6uA3eGHaptmCyxVi5Y+UjWXHXyNHXbKKf9EZ06rHzGlvZGXOFc7K138pXt/DBl7CV2CgQpgW2fuNa5nlZxJBiUco3KPd2sdGJbEUwLZpCXxHWg9jN9ZWFYdRLboHRSXtiZVwOXzt64mhScOjIZ1YHwBZSpbOWiyvu9fZodxjM6rceE1nD2zJ4uCjfXVlvSWZdape9q6kBe3d1xEgTLRUavOWnT4F4RN7Ihnkx1WlHZcXKVOqdmVom5F+Zi129Fau4Th8jt4Uae28xX9rY1/dok0XIJvHip2YvU3KZivrSMVI9Exjxg81gqspV7ETd1kateGa4ovSivIo5qebhgVHzZiLOjQQVejOt02GbnajI+ri/nxWmaJn3QBtZ1Vjf7ZrfbFZK6YjIuNpwjpBUTexGREOfBhZM9cVssJ5k4RdklV6dj++SUsncyrhdjcpiEBU/2KB+cM71tLGN3lPbalpcYNBlnDnqZ8fPVNupK6Ny11vKwenc9G6NRvCKuknm5ckytxMQoM06KelgfG4XlWs42zsE8ButgZXLsnGp5WaQ0Wbj0R52fop6p2GBKXWb7mJgct9OJuzMBrMPrPpqa5mIfRhNiulpCtFCuK4lnZxtdXva7UlfWJb2ebZedkxlbvSLryloxzsjYH60tpy+TPQU5/mxyEReFd6iAmfBhtF/IyjoT6Vng9Cm7W5mttI/20lI+Msc1rM6FnfJazp+KaeAn8bwa7R18qjmQ+8f1rE5Smt9pm8XRRF2ZDl1ted4neYoL03rukoIykq+JtdavU1EUVtxpGx8VQaBwzOou2ILs+4PalRpRnoSjtQ5Zmj1sdRo7g7QR7ZSN+WqKJdZyLHQ0unVtv9Ykbn+SQKAkNdNpwtkAemKzCyY02cAXFg7s9Zp/7IyhbeB6T85E/kCf4U+K5+o1WtMXE2znm4TI5Ro7plTLBTCOcTLbEZuxdywKsr0u4oZakONS7FrzjEfHEahLWQqPooNf20O4UrZ1tk1wyCN4MVthobfjMT077mfS2l/uJTlzO7rnMUGyUAA891x65niDkjvBjc5aR+GHhMSXku/ImrqyjvOtwXCKBQl2Li2MdCRrlAT2E0fjl0RK93akxItUUJgoyeeBnwbBbD2a0fsab1ugz8ho1bi7q0LggktLbREXNWEQkar1mMbkZXe2tusQQ+VUW0AaTnii00WdgcJM02VGIvimsRarq7THzZmWXJmjuD4qMmHmkhLxZ2/HOLCHLEZTZeWhPTWdA3175rYaNidcsa9Xl4pWjmOaYDrB0ZOWF3dW3dZCrR9J1MYEkpT0ETqxL5ezmJ0OiRXZUtTzPmUe053lCZeSyTrDkqYajpVj/SQf6HZ+OcVjkLQGT0+w2lX5Sy+YQq2o8rFcHqPz/KApc18+09nCoI/rFuf8PLZzdaD9+WRn+inPp75FA0poZ/JWr/fqqMnMySHvqslpeqrzsbO7mHhz2uWQ5hZWMte8BNeXlOeG3gINqnIhchtJ8sa4IUkqoax3OMFyGoYJ8mJeEF0Vs4ewTY6bMURylFqD+WYxI935mgTdFgXUGA3D05nZkJw/rbIt61ubEp9jOGH145bpctjoAbs8+9NEqy03X886y596h4srlEbpMfSO6Hz90MZrjJz2wTgd8St5khh72mS0alovJScOq4ax3YPMz7pyl2pdzMlaqaKsP9mE4qqSVnbJXoE/6082H/Fy36uYgU+J6SbDA/tcMVk1t1p7U5mStDrldC5s0B0OLp2HVQcg9eDSdOt4X+cOhVlzKkbVliNtjbNOMeF3XYcSSsfwp7lxtNFR61PpqOszUt/sAdqqi/hotYaWaOQkjmQKxPl4qRycreLNrteYn1M6RY/7417j4dbOv5R9mojT7am4XsT1QtKlRKW2hEDR08jc9R57uWp71rt0oRf1Eu/RLdvYG77n2crclwe5nLZWw54zSYFbCMiY4qm0pHguxzxfzdyxpC4ZyrbtGbdAeXfFJZhwjrQZhKrNjCZ00pelcTa+0hsK1xd0B2kcSoUsW6+kyfV4mIp+m3eidML2zuFKbHSfZdiziXId1c7XYt1OAa9yk5mfTs/mSKAYqcuk60Y77LwWF1lKuEYC6Kuq7gn8xCqw3WTrKk75GeuXkusu2ISVKn9Jc0GaT7aoZ3dZry/Gy5qxgt3UWsNtQKTRC26fmznq1j5nqInB91vZwZljs7X4jTXOKvy8VEf2xJ+r4zE1LjO4w4eb+ZYlpvlFG0+8/hpuuvWYGrk8nZtqF8wscVeNqt0JNb016rehKeV+ORmJ8zbtN8Qi9dqpMKHyureohX5yQV/X0irq58pBIbhxVyo2OwXpIrmON1qoMNWI34w8giKozmuNSGbGGrsGqZEuVHWWNyO9sn1mdN7l2oIHLXkRNtz5QsiopQN2U2XA1PxWPHtCpmyWwWGKShOpOwX+eg4bUk9lq8NavKzXxGjrTsk5qhIHyDQmeb/k6xbuJeYMRBKnsrwVm1w10t80oJiFpQSqs8VjXbHJWbee2h410TeC3SU7PmNm5AI7zPUpMd+cW09iDeWUc5KPT/IRQzNaONqDWdV4VTjfnHYkHmMuRzuNH3ohGbGVj/E4w1Zp2RtRzKPtyGf3OdB531tOM3Ta057fJqRFVbkxN9Nlw7aq441QPJaBTzqBhI4sa1crYZeOd6uEXlpncafGjifah2COTnVzZXnZJu5O/FUtM1K016ndQioubhoFnQ9tIEgXdtZFNMc1jbtVnQPOXebS8sRt6qilG49qksCruyiKbZvbHQ4FJzXTEyZTm4M6zRVxfkj3XXSdYmvWDXWMGDtuk2EEyeJYZm/SLK6NYCNgJ4GRyJVfYHQ4pcBmyhQVGMs+o3Uq3E0sSUEcW2bgXNcwO5RinK9w1Q6OGF3ya7cTwqYhKE4RUo5VzIAAdAjUOhj73tV0JXRDVro8XVLJYcU2jTO+iERryd4SPYZONmd5PEGvuAeoeSCfumSmtZAQlxdqVRv+PhRKf9yoBYdf12cu0KqxBybsVtiC5TUZ94dSK4x8P8kcVgil006GibbT6BxdE+ucGjHdNV6no6L1SDJm2jPF8Zyw6MJivc8nk8kvvzw9P93OlZ9ecWyMcc9Pw4HD49jgX3vNHFyj4u0hm2QZ7Pnpf+8N5/1t4/uh4+0YAdje6231139F7d+enyo3GlS8vaqukzZ4vOb8T+95P//9t9GDvMv9MH04Pz0376c0jR3cXp9HmdfWTXV5q/Okvb08h8Fp6+E/3NRvj0ONp5vhaTGckHxv6LdXs03+VthDAG6H0inwovvj4WvwOHt4fvIuMMiRW7+RDP0GqmKw/HEaNrwQHo7Dnv74fzg8XPNcKAAA -->
