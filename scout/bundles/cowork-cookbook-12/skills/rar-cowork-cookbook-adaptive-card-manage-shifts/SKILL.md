---
name: "rar-cowork-cookbook-adaptive-card-manage-shifts"
description: "Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_shifts", "rar_sha256": "387b33ee9553fed500d5a5e21ffcf356c1d2e291872201fb43bb430ba41a85fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_shifts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-shifts:e8050587104d9f64993c2bca8a37fc66ed3a4a28dfd10d1118cb84cacf58197e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_shifts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_shifts_agent.py` is
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

Manage shifts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-shifts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 387b33ee9553fed5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_shifts_agent.py` first:

```bash
python3 adaptive_card_manage_shifts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_shifts_agent.py   # or on stdin
python3 adaptive_card_manage_shifts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage shifts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-shifts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_shifts',
    "version": '2.0.0',
    "display_name": 'Manage shifts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-shifts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-shifts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5ef494ef30dca259',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-shifts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-shifts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageShifts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageShifts'
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
    print(AdaptiveCardManageShifts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyJLtX2FyPnT3kJUSILHUtWv2tCAESEICia2rLYsl2DexiKWn//sEUmZW1/Ty7jV7Zk9lmYkgwt3juPtxj6B+fbKaOsjLp89PCrAyhLOSJAxAiViZi6zyNi9j+CePbfiDOHlWl6Hd1HlZPT0/uaByyrCowzyD049l7jYOqBALKUFTWXYCkIVrwcc3gKys0kUERTogVWYVVZDXSO4hqZVZPkCqIPTqCqlqq24qxMtLBKQ2cN0w85EwQ1yrCuwcCqie4QMrTOBfOOYMrLR6gWaAzkqLBFRPn3/+5fkphNdPn399chKrgree3k0YLdjf9Sl3dXBiYmU+HFH0EIAMfi9ACZWn8JYLPOTt248VSLxn5L/+K26t0q9++vwlQ94+X57Gf3KTIXUAkDq3qhq4iGMVlh0mYd2/IIuktfoK4lE3ZTYiU0H8Mv/lMfObpLxA/jk++/Gh5MUH9Y9fnnJogjWi++Xpp3HFX57KZrx+GaUUP/70kuQtKH/86ZucqrEj4NSjMGj1y+vb9zexcOC3oaF31/pPKPXhRxt8efrd4sbPw+5xnXDm00uUh9mPD8FFmd9AZmUO+PGnvxLrBMCJk7Cq/yW5Pz8EB8By4ZreDP/p+Q7yLwj6tqAPmX+ttoBu/XdWAoe/q3tG3oD6K9l3/P+X6CTMYNC/I/6n4v5sAvpP5Oe/XNvfTXhGvC9Pa5DAmC7HJPuM/PqqHNnVzz+4327+8MtvUPT/VYySN6Vzl/AKczH0QFW/vv78Q3W//cMvP//QFDDWYKK9NmXyZzL/DNe7nu8QfBv14/dzof5LFmd5myEfkY78mhf/Uf72gqhWErrf7lefkd/ny/hBkXER70ofEPwuZypo6+9w/OnpN8gNGVxN49wfwyz/z/9E9qFT5lXu1Yji5E2NQAfXYQpG489BWCHnt6T+qoj8bveSul8ReHdMd0gRVpPUCFdCRkJgPoweH1cAee3r/3HuzPnJeWPOifXGQq8OpKHXB++9Pnjv6wtyDqDGvAz9MLMSRF4cjwh8ntWjrntUVE366Taqg6aED7qRV/xINVWTgH8gX/9G/utd1EvRj6Z/yaAvLOggF6lBWuSlVYZJj1gjN9l9DT5BMoX8UeZJYltOjIy/muJlxEMLQPaGkgMLBeiA09QASXIH2uyFkICfoaOrPIF0X4/YVXGYJIgblhCYvOzvFQXi+3kU9vXrVxvS+pfsQb4E8qgk1QQO+DAY+fSpKIGXhH5Qf8mAE+TID7/+9gPy38jfzboLH3UcYQG4QwUDOHkUH5iNTQqHVcgYCpBq7t769beHD0brMlj6YA6FXgjuk6G0b64fV/BwzLtX4JpHE0H5pul73JA2gLggYQ3RgnldPX/JRhE5HFq2YQXeQXxMfkD/7uaHntEn1RuG0E9emaf3sfeoG53p5KX7gvAe8oEUXC70az16NMirGgZqATIXZE4PZ1r1NxdmsAhXMFcqr39GmgoudZT81YaiR3BSSEhW/RXZr46wtuUJ/DUCdFcPZ+dZODr+LU4ft6GQ8gcYY8t3ES/IAUA0kcIqrSIorQrcx3nWIyJgTXufD4VbSAZaZKzfYPTRPYvvkbf/rk1QHm3C963FlwafYjPk/08PMtq44DiZ5RZndo2wh7NsPAJqbJjG9T16LNgS3CXfs+Nbm/DOKO9c+yVLQuiEsv/HY6R3j6HHmAd/NSUMEHkh3+WP2Vze5YY1jITRtWU5Rq/1JXsn9WcICPRDNfITTNh4TP/8Q+H49N3SAC50/P6twCOPIBuDH4YvUjR2EjqIB4B7j/Q6KMc8enMADAswogoD3wm+WxUCpUOXQ/kINCKEWEPiv0N3gPkwwnwP7o/h4dg2FQ9/ughMGPCCaGP8whisEBvA3mccA1H44S4KSQHEGJr4gXAVWMXDmLGJfTPQGn2Rp1YNfu+Bt4cwFsfqAfV9JBqUCrm1hli20Akwj7qHZz/sfPMVNDYdg/4+6Xt3v60V+X31+ceYbNDGbzQP++57uH4DBzJ0mVZ30oElNa5gOqfgLYBgJNxr9MujzD7q+Ictn//Quf/47zX398J5+d5zn5Ggrovq82TyKG7vte3FydMJjJGwANVHnfs01qFPj9z69Mit70Q+EPqM/HtmfSfiLZ4/I9jL9GU6PtqFDhgD9u0DUVh9WhqfZuPTL5kMvrn3LQZGBoOsavcfheR9CKwmfgn8cfCjsFRjPWphCbzz2b0wfITAW4JAusz8sQpW+e8Sd1zT6NCHvz54Fz7KRkZ3x47NB+M+JhnNr8DT56xJkuenzErB3+9fRlaF8QlxGDc8MFdg71OH4P7tow8av3y/UbtnEUx/N/88JhOsYLBnfUY+2s9n5H1DcN9dZQ3cEf08tr6jSjgU/vkY+7ELtMET3HzVfTHa/NjljB3XWyf8RyPGHIIWQ66uRlvek3LU+Ach8ML3QflHIdL9wkremAGS91j3YLl9y+cK2unCBgly9m3MM5g6MCQbOOGPaqCeElwbWGndcbnf8Pu2rPyxlt/uMNSPreKvT+8MMV4/yv4jYuCEf6UrG9F8r6avo0xrnHnvne7g3rvMV7iwcKyav3vkjy3A6yP2nj5DZgHPTyOEZQhb5+G+HX56GAJX8K0/hRIgR3yqxi5gAlMHSoK1uRitjyG//U7BeDt07+PHi89/2dT+SbJ/BvR0Pp3TFDaduYxHzhiGcHDbsWiLoDyHJIFLWDMLp13PxaYuhmG0Y9Mzx3K8OY0xFID6R++l1pv+CTbiDi3/APff6bGfHlNhRcDnJJxL0JRNEAAw8znhAXc+nbpzaw5wzPMcj5iTDubiAGcwmsJhIHn2jLDhz9S2ZphFzz1nlPfW6j3seX1vq9898Uj3V8iNaThai1uWQzsUBtGgLNIBUBjhAAzHXIoA0zlDeDQNZnD+x9Q3b4zOeix5DFHY5cEe6zbq+fXNu2PYkTM4cjur+MXjs5owqkXiM7vrdHQggWFn85OSBV0myotUvPJ5FTYh43fCzl3my7WNu9NAcje9SeGDOI/VpXQK6FyexxmVDVKvJkIfi3xuVDFRD0I7d3rKQ51Z5fcL42Yqpr6qgwNRqFq2MftS7GeRIsOu+5asw7OsCCgKkoy281aRL6VInnKVU5NELJfljvG8Wy3i7JC66UE0VDPE54cqA4oqGmdLDgvB3RmaFEhCLdz4E79yDXZ93RyZaAiqpCYMnCumKHRaN7kN08HL9NltUNPZ7Waiu4OcZ4Yp6qIScqWT7kUdzA27zGS1OvXJfCORcoKKAzfvU8w8HdocU9kgZKa63QjirA3QVWheHDVWxYDVi86p9KbYb5ROS4Zjl+dnP6+Xsb9kpSLxxCTYG7OpoapFvS9WFto1pXI43GRLJLJlDmJiclwRYrA3S2610fbrKx1XHNjMN9aF3IRNEscRhzELgS2GYD/fw62dXcsVsIksZoWlQ8Uh7vu8dRi0KRdT015aovumL/d1ge/jzri62HzfsYZqhRaK04Gy2aipbMmKM60H59h2q06wl26V5rTVuuFhKGZxUSYxpngGoWHptazVwhQx/7jujtlSjA/OWZAFs3cXTWnOEnI+DCYpAXfRX+SlkAwKgzKTXDYot91UTHWTr6098zvNbNBMdNzU6jbyNRXK3l0bPNXgRirhfeXsjhx65ROrTYOVPtltZHO1ldbLCTYIUbnaTjZTS1NSPZR253PVdeL2QkdBYMz9pOLBCTUmaDm3QhYz55nRZTSg90e7NMutOQSsLCUuvssw6yxvut6Vkyn8uagg3NPz1WRtJU0g0NSKYjtqn1W9Y6AXexumu/Nkxm6Gq+l55wmz4aVoxVxIzK7dmFIJvs4FrnPIHUQ1C3YiYxcna547VTqpdgc6CNbc/uxkbU7b3THYhpEzaKsquZ0VZ0Keo1hGnbRZe7vFaqadMAiILBlXNVp7J+5kLxXO1SwOhpLs9ntS5tbR+sJfNT70422MmrqeSlu2dYBkEqvrPiqZ6a7ItGOa0azAe6cGbKfHJKAOLrlidn2Bn9doloa2SYm6Gu28aMIfwkatSE1Hb+iSUHNzg4txh9O7KisY0XW0KznhlKMvUjW5wa4nNdOmNAukvKqWhjWVfDaf56Qco/ZNUo43rTq3NN4ky8ByhFXiBeyZkLmrNVWic1h6GB1NdgNtLryBZEIumwzzCluoqB4VmJF3Ho6LWxmvKtKUUXyarJxsdQkr9CgIg4ars0tM59ihEqU6OJlnd3pL9ei2aZd4yRuuIYIlxij9fhpZul7R4bq9DKjvN8UOXtA9A4T9YcP7nuCFWyI+Faw+FedeS/S4t+fmwX5o29I6LU8eTialLIQdnrKkvLyxmCxIN00zL+T5FORsC7O03JttlXGFTODguMrZJD1umbPKlUpUZvP8Qjq5npuHA+mpvcfy21waxF5MVgbqF54r2ypzKmrNwkpixftAP3oopc82xyV6IfYcHw2V0ZoHZZEM5W4jrClj08XXjY4Wa4ady6oknJzDdZ4t+p3KrfibJklcsFqkQ0WxKkPv7D1fbIWG5VEdFntnmEcYRgGdPK5Vs0kqv8sXwbJiJSERqliOJrLP5eGQ7mJL3XnLXjkFy047AWBrRXuZO+6VDIoFCLY8WmgGeVoNw24exWsRV6uZvFuw54RTBSsOwXJ30ABHOI57s9qw4G+WvtSU+qjtDgNRohkLihCYU+wWEzuaknQMB/E0OvH4HhvKkvJUQZDDzEudrmL6kxOuHBKGLThObvKiPDfSjKpPrbDpOffKgCzLyFIVpqiirSmG2u49cTuXp9yiKolOd2J/EWvLrZJgOT3tUzVgW7JWxQ67iKfNrcpx/3o5T0p/0QTwFr3wvU2/M669FQeWO5OT/pgcWKxkt47YCVNlFhWsQCyOK1w68ZvTfrUPs8JMSH7D4EKyXUKSyqhSqrBNhclOcGB1fqH5uyM408sE7barom/lW9axC4KjzK5PCCmtOS1T3NpJghtubNCzTO29vicqg2SwtObnVGV0OifiBjmTDb89y9ue1v2E0CJXu+1yW+ktwt5whhSfMGWzvCrXuVAct5Fcol7Iuqy12bW2l6PcpeY5u8rDXUwG+VygpW5VVjmprRmf81H8MhMiW8KD9VW7zDjYTkuiuUvbeSRvgihHJ6WqdDwWGgvIglpgqtZur8zCqA2Ty05l9BbWkDZWCo9VOfnAX6jlIbEdQVwEU/bUnRq5D6+7AzYDs7rxp9KJXJ5RcifWLDdwN9KpHX1vLDJtHaL9zVsz8+bMFrbCnZLDbaU0PH+ONYJqp5EQV4EpLOrT7iZSx2Evl0FE4nhScwGv20Rv2mDYMFKYFNckVU+lcWO26hUSyFyfwaK4zf3a6d1toRAaq51SZrjMz6FIFFMlZjgywSs6Eeklr+43drkyW2MBktmFXBZGnB3YBl/LOYuGasjvD+fgyC3nZmJRPr85N4px1DoUc9D4cDaj0xr2IijeMZVxJGPqJG/5zqGL0zZuJbVmhyxfm5hgm3om6ro/F7e3SWaTXeT16+VMSDPAS8x6iSbGsXW3pbECrhDplgFSHett86xNMmqvn0hVnuHoHKtOsAXieHaQChWfsDs/wfMFx63VorGNawMpc4uyfCrAlka1I0PcYaiXYdvtvjA21uZ6UDKVONuZSO2xYDZkClsbuXqhtpiRrmYMVq824pWlMFVuDlqZyKKt68Ulx8v5cGiXgb+f2Y186K5siNsr0ogKWVJ4a86jhsGWh05dRre0uMq85vC5g0smL8M8P63zOI3QwqUDIWFul0g4Sn049eFOIJ8Yl2HN0tlGQxNT5XfTolMsKk6XCU+e6Hh/3gyzWbSM0v2ZTRRLPMvGKiOFvkiE6wJNWnOnwvCpOtyKKJXrNtRCmGsFLQcJujYuk7za7PHijGb9As87g5J2cRer+nYdXztgDgK2KbjDrS4FL+6y0w1zsNOUa04TS/JWqgaOxoazoyTXqBvt67Ka+hzY98b1lsudprvrjtN64NrF7cpJnDsRE4iU55yq8qJP+MWNbxRSCHcy14l7I9KombFatlnICHOZviw7cyVtWNeTFoE0r6PYbljJv6xQkpLtQsHNKayQrcVk8rRNtjDdSV1Z2ERgkcVSXiTXPM1W3oKMwrphtWSuLdyemycOLO5BuApVKTTo3LqAYnNS1VsNeHbizfd8gAtTISaHm7Pmz8u9OVvqRiQlTa+6Wyk/zAX8RHKOp9bxVVhMtmCHahjrn6/HILXPkrxbS0lfVvPldiha6xrL/PJMqmIbipGEL260spc0bjf1Wm4/4Y1hPr/5pr1QVY/S1Dqz8l3NAFZJ1lLkdVzRqHv9KGwU+3hSBw9bp/hV8PLliqqn50JcLwDsUlRxKMpqkFVgMIa2Ot8SyPXmgVW7auqkUQvNge2A7wa+pK2r9tKcgw0rG/vzdVgFp8GUjheTq3cFQxxH3saU+JBL10hQNZTQ15dy5yyKQGFXHRt5u2KYSduzyJ7ghm53RGeWcNhatIDz+dVk5IVuq1VqwgQYnNKZJTGFRnU+kHjgsyebAAmohQsaOCvF86/LW3mycJvWCa29lM7VHtxrVKPKbtuRIkt6B1BObxdGWx2m04AGOpdgFHNt0Py4mzklSFzTNzS3aniqO/fsxgY0mQdpto8zHeSWy8UDbtIrphfWCuHYTn1Z0O4Vk6tBn6cpqzjmylg6eh2s/HqSEj5QhKsjma2qpthEw1o9cTF1cjKtTW0Q2DG7mJGXMKdwMidjAquEddpNPXrNTcJZNfOapoO3TMLUiNJZatqWnHpctWHohrmVSxAN/frY6xkxWa37QA0LXZtMrltUSuJqAsg5o+s1Gkr2ajyPmIMFuj0tltONF1IkOzkT0tm5+lqTocs9GZx9wzmydqpa7Gq7tmJ5j7aTUwTbu5Rp7SVtDHQq0y4zt4tEbeb4dt/NdhfYDDskBxup1pW5/nSSXOD1kFsvBnNKOrflRXsvTvKdAmiPZiBlDvSNSm9s5rU4h5LkCgSbiPF44DuTHVVWImo2p6DvD/lpV9Ht+YAq27Jpp876kPiNHFohabkZH3HypNHyCYap12xS6hNnrxl9Qd8yHoNNVuWD43GKSkvKGirilvJpe0VRbEFbIVqh+KzqKk/CmduhJa5FrTf0escRmjTDbXxADzh6iuzl8uybOIXxCUwx+gz3nutwHbq9PRx5+UKxzu28oGsXM1t/uUSt9ridTljCY3O7c47eplrX4pJ2Wi+CW5L9fr+p+fQotR6neKELQ5w90Z65pGfrpVapt5UlzS6aO9ksGODtpqTW4k6H5utYsa4aTpCo3vM8Dz3RSoQf9Ey6Wg0ng9zxIGhvBcGS18aO99dZ43pLy+mIc9ZyOKVXmUm7vabNQgp38xklAjNdVnVy6EOb6Q9ULUJ2UufMttl4Wj8QLaFfajpxbQafKVjLO8a8WQZHmjoTXOR7HBeVLdZJdusIqnOw0CNwqDDWo8oz0MU+3/i4urXPR2cnRdOOwFWNkaYuoTLiwO9djUw5nmxAvgWw/vJ0d134/o08+RyjpvNjtAjhlmFgLLgxwRb+/BiQjIBt8bOnrfQYm60aDG/YPc3vzjYzrWbogewn2W0m21KFTqhsqsMulzC6cDEhvO2kuBylBXGdtKDT0FYqJhdDvylkoBKuWG9Leurorq4Ty/N04lL0hkFNjceTo1MTe7MkQSWfYpuXaP4iLyTAXW8W3k8mppGuL7Z25BaY6zAuIemdF0b0/nw6LovVGnO97Xo9cUQ+uU7RgoqmCz219Lx0Gcvu9F00CC6DHTKVj3t0aPfk9lB2i/PJ2CmaUQBLk7bS9jRUsCR4dpoMGmNb9s0+u4qLH2WtWGhcwTHTY0ozJ4GS1i192XTnCzbLqGE9LLi2Xeqr6UxL2+UAIjESS0axFQdfDEF/UU4Gqu7MMu7IC7NalpIeavIQSeItJG82U/k2Q11PSaudZ9dWxwbrvGWFAjQz9IIOq6lX9+sdxUTiefAtPz3gmcyRhyVbUvGAFi0k1oLusUtGEasZlx729XI+g/2ZtDa16iaut4q7OKxalvLInJuQwoJcTY+3w5HUugO3Zobdthqu57TDJJ2dudFkti5EI4xOi2KxWPzz6fnp/gr26TM2nTHk89N4pv92Mv8vnu76Q1i8vgkhKGz6/PT/7hjycST4/qbufkwPLPfzXfvnf8m+X56fSieEtjyOgquk8d8OHf/X8eqnvzntHSf2j1fG42vErn5/h1Fb/v0cOszcpqrL/rXKk+Z+Cg1xbarxP4pUr2+vAZ7uS0mL8Z3Cd6bD70FYgtc6H09Z4dXT+D85xpdjwA2t+v2r/3Ze//zk9tBDoVO9EuT8FZTFuMi3t0XjSez4uujpt/8Bxcurt/kmAAA= -->
