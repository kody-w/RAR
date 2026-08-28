---
name: "rar-cowork-cookbook-teams-update-pay-taxes"
description: "Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pay_taxes", "rar_sha256": "55a22403ae8b90cca37e79b6db165c8afe1f6101e9467cb9bfaa82f63248704d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_pay_taxes`. The original RAPP
agent is preserved byte-for-byte in `teams_update_pay_taxes_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Pay taxes Teams Channel Update — Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 55a22403ae8b90cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pay_taxes_agent.py` first:

```bash
python3 teams_update_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pay_taxes_agent.py   # or on stdin
python3 teams_update_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Teams Channel Update — Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pay_taxes',
    "version": '2.0.1',
    "display_name": 'Pay taxes Teams Channel Update',
    "description": 'Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2eecc6126be717c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePayTaxes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePayTaxes'
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
    print(TeamsUpdatePayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjyLLlX2Hyfajqp6oUO6KuXbNBCEkgCSTEJrraqtlB7KuAnv7vE0jKrOrX3e++azY2qiUFRHi4H3c/7hHkby9W24R59fLl5exZGbSxkiQKvQqyMhdi81texeBHHtvgH+TkWVNFdtvkVf3y6cX1aqeKiibKMzB9VVl+U0MWpHhWWkNOaGWZl0BFXjdQnkGFNUCN1Xs1VDdW09bQLWpCsAoUZY1XWU4TdR7EuFZx/8JalQv5eQWVbeTEEFjVCrxXsKbXW2mRePXLl59/+fQSge8vX357cRKrBrde7kurhWs13tEalGk5MCexsgA8LAZgaAauC68ColNwy/V86Hn1sfYS/xP0n/8Z36wqqH/68jWDnp+vL9Mfuc2gJvSgJrfqxnMhxyosO0qiZniFmORmDTVUeU1bZRMGNdA4C14fM79Lygvon9Ozj49FXgOv+fj1JQcqWBOKX19+goDNX1+qdvr+OkkpPv70muQ3r/r403c5dWtfPaeZhAGtX789r59iwcDvQyP/vuo/gdSHv2zv68sPxk2fh96TnWDmy+s1j7KPD8FFlXdeZmWO9/GnvxPrhJ4TJ1Hd/I/k/vwQHHqWC2x6Kv7TpzvIv0Czp0HvMv9+2QK49d+xBAx/W+4T9ATq72Tf8f8vopMoA8H7hvhfivurCbN/Qj//rW3/3YRPkP/1ZeUlIB0qy068L9Bv385Hjv35g/v95odffgei/6WYc95Wzl3Ct9TKIt+rm2/ffv5Q329/+OXnD20BYg0kz7e2Sv5K5l/hel/nDwg+R33841ywvprFWX7LoPdIh37Li/9V/f4KaVYSud/v11+gH/Nl+sygyYi3RR8Q/JAzNdD1Bxx/evkd0EIGrGmd+2OQ5f/xH9Ahcqq8zv0GOjt520DAwU2UepPyShjVEPg75XblAVzrCAD7HAfif/LwpHHuQ7/+b+fOiJ+dJyPOm4lwvrV3xvkGKO7bneJ+fYUUIC2voiDKrASSmePxawYYLGumlYrKq72qAxxiD433GbDP5+kLYELo178W+O0+97UYfr3zcvRgIpnlJxaq28R7nSzRQy976u0AYvV6z2mB2CR3gA5+BFjzE7CwzhNAsM1kdR1HSQK5UQVMzKvhLhsg82US9uuvv9pWHX7NHrSJQQ+ur+dgwLs60OfPwBg/iYKw+Zp5TphDH377/QP0f6D/btZd+LTGEbD2E3egoXCWRAjkUZuCYcAlwImAJO64//b7E1IgJgPFCXgp8iPvMRnEYey5b/iet8xnlCAh2wO4AkzTIq8awMVQ1LxCvA+96wsWnR5NbB1ONcr1Ci9zvcwBdSq0gDnvSGZ5A9Ug2Gp/+AS1tXdf9Ve7su4qpiChreZX6MAeQW3IE/DfpOZ9EJicZxGA/937j/tASPWhhpZvIl4hcYo8UCQrqwgr67mGbz38AmrC23Qg3IIy7/Y1m2qfN0F1T4MHPGAQQMZ5uvTz5HNQtFOQ8279tvZ9jDVVMOVeyaqvWf0McauaXOEAygeLBm3kTsT/j2dI1WHeJu4dP6DpJOnpBffpldeHS9/K/KMNYJ9twKMoQ19bFEZw6P9DrzApw2w2MrdhFG4FcaIiXx4gTV3MBOaj8QH1+z75nhDfa/obI7wR49csiYDHq+Efj5F3aJ9jHmTTVgAJmZHv8oFfAUiT3HvYTWFUVVPAWl+zNwb+BOy/0w2wGOQoiOEpdN4WnJ6+aRqCRJyuv1fju5uA2cCxILSgorUT4Hbf81zbmjAIqyl1nmiDGPSmNLqFkRP+wSoISAeuBvIn2CPgEsDSd+jEHJgJssav8vT78GjqcYAWbusAbUGb6L1COoj+KQJqkHKgUZnGABQ+3EVBqQcwBiq+I1yHVvFQZuosnwpaky/ydAqQHzzwfPg9Xu+6TOoDqRYIJ4DlbWJN1+sfnn3X8+kroGw6Zdh90h/d/bQV+rFU/ONrdtfxnahB4iZTlf0BHAgEIIjYiSkn3qkBd6TeM4BAJNwL6uujJj6K7rsuX/7UTn/89zrue5VT/+i5L1DYNEX9ZT5/VKa3wvQKsn4OYiQqvPpRpD4/aspnkFuf77n1B2kPcL5A/55GfxDxDOUvEPIKv8LTo33keFOsPj8AAPbz8vIZn55+zWTvu2ef7p+YMhlAVXwvG29DQO0IKi+YBj/KSD1VnxsoeHfeBNh/zd69/8yNiVWCqebV+Q85e6+fwJcPV73TO3iUNWBtd+qsHluNZFK/9l6+ZG2SfHrJrNT72y3GRNwgKgEE03YEZAhoT5rIu1+9tyrTxR/3TPfcAUnv5l+mFPoETW3lJ+i9Q/wEvfXs971P1oJNy89TdzotCYaCH+9j3zdktvcCtkbNUEzqPjYiU1P0bFb/rMSUOUBjx5uKcf6eitOKfxICvgSBV/1ZiHT/YiVPPgC8PZXWqHnL4hro6YJG5RMEHAayCyQM4MEWTPjzMmCdygNkDgh1Mvc7ft/Nyh+2/H6HoXns5n57eeOFpw+enRsYDhLwcz1VsTkITrAguH6EEXj2P+zpnrMAf4HuAkwjCAtFcRizvIVNw45jYZRH0Tbp2ghJOAvL9xCfRGDEo3GScmza9i1rgfokhuILCsZdIO8Rgt+mAh1Nmniw72E0gjouRqIEgdMIhVq0a+GUZbnwAkyjfBdQ/PepMSC/p3kPcybs3tvLCYanlb+92CQORm7xmmceH3ZOaxalU7Yc2nRFehfTmPN2pJaDR6LBXvCQre7YPJOu5B6LFryGshwRl1Z65s0V2nDWsstPvsPPBpOgzHlQ9GlKoYyKnpet3W3FjGo8YAQF6hoVX91hr1aEISe3slWOkc12isYaEToOeiHv5vNu2Htrm3f1lHOXOzleBKOK5/XaSK838zxU/IAjnqYPayVv1uf1lSvofCEX++1xhqs3vdbCLDRCg/RCK+F1fTPTjkLpdEYyON0Y0cftIh0T2jeysYsWbcMl3Garx4W51toa3hkeQlj2VZd442CS+dnDbed8S7R2CIRtxp7I/ebc+2i+RsZCbk4BV5ZRzYb6PqIPey2ikTIo9BJu/I4dwpYN4ErYKJk6InqRDMum6bQNB1ccOpDLshrI0bw2lE7Q/a4mDX8x7CjVSg78oO7WOjDGsvvlYVYdxI2ss8AyYn/AYGE1rgmpRs6CzSJtM1YW3d5keD3WZ8Uj9OGgojq8SyhMuqxnJOfVEUoZbL2XT+hq1vJFP5a3KolmM7QO5XUi53IZnSlBTi9HVFtfSj9AsSvowM3a1IljHBqGv5KFeU2jCbNwK1qyr5f9uFgNaEgulROBcGR9Ffb24PVtSV91eTyGjrPd8lsEKEYfjtX+IJebgcQxZXAXYnrazZlBHmnB5K9ME+LysLJioR/EoytUPGWbSpUsTt55LPMghy8yPowLdImkuxrvxaPTDmS/mkeWhLFtRjFJk8/4BbKK1RznVQk3bXbLHTOQ4Je9o6P7rTQa7C0ywohwDVKlZJtnBbiqh6jIpIu2pnNHU5Rs1+ZljRFm1NBYVuKbhDL3CzecE6s5m5I0UrBBg8mLiz/ac7LrCGO+HJxya3n7krewPWzkMnWxBJYgNRNhd0tsc9s1520YHMRovh2O1EGrbC6fZeOpd0eNGfZr2czNwOVKZdxxJzQIwhr054mzDzStiMg+ylV5yXkcW53llSrLMYfHiqM4AT/Csm0KErZe4+ECG6UeyZhLSqcY6Q7FfInOSl3sq5sU3pDlhTuceOa0DNFVmVyzDAZl2xHn11mW1opJMO3apg78BS0JGcndI36EVxrYTNhypRQU3MZeBhfiDfSspJUTtzzETk56HvLBXOUKTDFDsF5emXwphdt5sTEohzgbNHJUb3OdUPhzNDJspK3P40poEbUS4MPcJpbXKhbxK+xU54MyP4JEvFnlsHMql8T5RdHWqCAmmWKIrUtrccGUO5BZJLJetEO1jkGGqcelkatDAIf14Ig6t0s8prrK7JZcZVjhqRrenDYhZppHzyFZP1JOR6TrrjJ94QKkvo6L2Iml5W42MK1TNbOrwcUL4iIsZ9cmkWYh6/sKqTVrXTCsy0hsK1jR1DOBXDJ9k8REOAgRQKaT3bPBILjPovLm5olLfU8Q7rrQ7UYaap8UA7JMnBSGJULq1C2pHCJdVgVWIZmQRtaNsWBj5GTrV0eKS3F/rCjltgiosjqvmNMQGtaGq0X5cqRPudTtPFeKkG0nkteNJRzWu0tRqTDM0WLu79gV3ZxYVGFRM8PJrF0qdgg8NKbz7RVZNEImJiKmSSS5GHqRjpt43THXE16ujP5EJQdpHkgIEqEXpK4UZBUdioXJiq5dmkV1QDHXHEK7MgPkBJcBaGSCqt45HSZzZV3i6ppJgyLemUXGXq8qnBlNJMQwTPFisjyH8q1kSMWSdksrO2pse4qU/Xo4VZe2MwjS7TCCsnNuDdgqJOfk0dL1W9zORlGsXWsZCoIikKrTUcc+YRADzuotHOTMIGRDoMnmYu53AlHuCXzOGTFXq80iLHLCNLozjAv4crU4M/oeHgcj0jguxEoaSTYac7D0kI7M817ZSC3HZpu8MHLRxGu03UVpzpjoIh+Iba7HZwtboqticLkFYfGse1iBOrRboKqXM+sqS81RRplqLCKETTaFbLfMiZHVXZIcosU+lYsCddGocjYaJW/5zGI39CxmlqXVnPfZsdVssPM9qHZE7fc2TEqHdBuFdLVy+2uV6ed4ucbgWyAPhqnYQR+xwYyzxda0z6KM6SPXiN62OqGiTs7bojF37nW92C6Y7UEppMFChdU2wNnOGRcXZqeo7izB+kN/K6ziemmofbw6D80lLUI+s1H/sK633TlZCpiZ2kumEPzgQgoEXgWNMkZSnO0MlxoKjWLizIxZuy319dq6FIf9oNYHNi90pJ1tm/1M4HKkv8rpSkmO/dnUMUa5IrPVii8NvlhrmxR1j5G8CDNSIW+neqEjZq/kSkRUm/1BsVn2Go/u7UI41gxFQRVbXs7mJRcz1mwJTrbQkbtpAk/o52B/ZQaVdYgUTy4yiPS00RvesGUEs+1+TUuxRhRcjakFfpyn1dHi5TXVCsRBSFiC2OtSwdOMG0Rb+FoJms/pR6XNBHmPHrU1udP6a8PlRkhh8UZewR0b3/jqEG/yBL3ZEpNraS0vl5Uq3CLpylU6u2Ss2W5YUjNRTzryFHGLcy5e4XG23S879wjahe5QbQUVtRmePy8yWd3y5BIprWw47tbLdNjDmEJLexpdjElwvsDWti3WS0RF4DNPefmqqsbdPtzG7bw7UNHc79Gbxh0oId4RdLu6aFqgc7oUbFjaDlzqpEQHHl6Zl90eIO7kpqHdjtzZkbVog7TuMajcbqzpXCqyHZMOzbJMyGhnWqYsZLnPO+Yp6RIW1AlMr7ltSJGXzZlM5S5xBYqnnTL3UqLZGRvKPxFn5uSEneIOYS1isX5mQcJI4YVYFCU8ItcQzfNoOG98c20c2JiQGap2ejU0tmy01Y/ikbwioF26oKPbw2aqGupqNLQjxUq5vSYvEQZfWWzpBJnImW0k7FQk4YblmTOqxMdXwuFkbJoIbU8hx46lPZRhfJkdeHLmxk2poqpDxyhfSTcYEet9v+lXzUaOKRNxSGlcHwO9qwfDkkP1oonkKJAcXHKzWkbN3tBp+JiZGXnaUaV0OVCGqVkLQSs4OuDs9iiEqjdTxVTimRrepnhdBMVcTdYCcd1aeovApaZkrDSPK3bX21jYJnxKDbc1vh6M/kC0AirIg8Nebl4k9iq7QrEVjqwwmXET/uRETsMfQnGYV8wm38w6faAtMjuZTeqCGsE65aB1MBsPC0qgDBt0xGO7rqOqwdW2PIenhiyExTI7SXDOoGeWb5YjtzzqbV2MVTHbnKwlTuZxGQXUcCidWUNTI+NZp+Jqb2ra0QoP1FzLtWM2ulD2wTq00oniEfbMVeTqgKqqZtclb1acR83OCJyfxn032JtSqUY2rpwduUvggXduyYyBDYbSu3hZHkt1JS/XA9gs1fLxcBmjkqsK1AsO6Gok8QNZ5Q0GtkqWqknspt+GldrvDGpMLEJIc6/ByCuWarDELZckupSpbT4YAdV5Z5uTDDOv2n2D0AyO+jRbr/PhIopNxy+qFV8lmhX0/HbF2DpzummyEiw1xDog2I0bwmxwzF2ygY/6trGMcrkqwzXJLNGlrul4FHjwBcbqPc4Vy/OSG4jIpdjBa2tGOOyGou+3y4ueHPchx2+SeW42umIf5zHZN5TTCVvqPNttZBQ5uhfsvKB6svQwtybtCjUIabfmjyh+3BBzcY2koU1VSmgHrXct+kLqktORoirX60iq7GRx1s63TZ+43tyourzTFpLW+W19c/ZSO+PIPt6sb1eJRvEsPdravq2rvSQoHrVm2JOqucnRHIgSXxO71E3Nstk5/CHBw1nGwoWOupztb+fL0szywCyUZKdpVecvZw3iUr6Y3TZY6HsrfLzxNO5ZaAC6QCk9uvlZvnrE1peGtk93s3maL45Mn5ozjU4JRuv5mTTXiBKlx0qYdX2/2vYGNic2Br2s5F0tSpQxx9t5pgqoCrY+sy7XVWJfrFeKjKRdsAmskF/MhUtMLXFhPt6kvVlfivmtPp28kyj5kaRENcOclHYYMpTfwtvkcDGMBU7QUerOXLG3i8ZFCZ8PemallfG1QRdZcDnNwiauNuwuQgYCXTjjdaNfy4uvSlvdaOanhURfemIhnlYJYmDiXJLm3kKkEYSko+WadC9zjkANDDtJxI7gj55cdmy1OnH42FxoEtsgweXQEKVknIzIRJ2INTchQV7nhmaVPt36u5vZ1WOx73I+y7lyEXh7DOu2J5o2ZxfSZvcdqcpNv840mg41wwzFaj0ztFyTGmMJswU6Px8cd0e3aN9iw8ZW+t1iJVFemzb9xo+sFhack7eXuCucW2ulNovF5ZjaXrzjgpAzkdLvfGO9HQ9ZgSjHLW4x7uYwq3EnSphOtE5Cg2Mr7pJ0q0wVL8p23GfcKtxuGtvy4OPhVsbkzFqTtHQVOHqOUae5uoT3Yri/UHNDoDiR5A+FtNpfdmffXjHzA2dqtajivoixZNXa8UHH23PXiRJPhRTOoDDVZmbkDlPGEYOf46Sgg+VdvUwJRewHdXvdeXy8Juhty816LXCLto0pQqKwqigSKjjh4eiuGMVpFMrbnmaOeBoDe3DQANcqihzpWhi7XWGKvVhQjDxKm+FGWbkfmfE6U1rcbw1N9FDfoIf9SpW8TdRu87Lw89FpZXG3WA77NqBu85O8ABg7AVPG/ryAh0zG0TM+Owoy2E/Da7UDPf6+J6hmlfn8kpTRGcYpqxV9Qbr5xXfjmsTwlJZYchaK6MEJjrN5fyP9VbzNsNstnOELTtPnWF34G5plZqVkdz4O9zIVznVVJpIZtsfmi2V9nicrX7wFdkVq3ekWmHkLdr4EI3pCbiIuybYevblubI3Xedg9IB4+03n/nM1sNLBY9pKUXrvPMIKEl0yfuTq2QQ9GavlC5d5sordBrgv+rFmfNBJwaHzwYGl7SgI6uG2CIjDBDmJxNqV+tOIyJTHajuuWxDCvTCiVKr1zrzIL4Xygcl9NvExLQQeB01tEUWlcP5J9Ea8uPEeFu8NeuRxMDAdblXSxEAnJYkzYRNRY2qad3ajNVjTQU3MZrUWwArnZHdGsO6y7iEqImklofbVpb0Zimit7v0+kBHZvzViC/B7mOdllh5XMLUeFJJRT4SQXx/QTfwCF7YgXXI9i4wIZglXmui2Dn9iurrRijsuMopiOv5RGWJEpLsJH1ZJZPD9uDCGnNnYKyMAu+c1MzRrQ5gjzxabQgoQQDznDMP98+fQynSw/z4f/xQvc6ezu/9kR4uO07+2d0P1o2LPcL/e1vvwrRX759FI5EVDjcSRaJ23wPEr8Lwein//6/cE0Z3i8/5xeU/XN20F5YwXTr+e8RJnb1k01fKvzpL0fxH56sdt6+q2B+tvzwPnlbkBaTKfXPyo8nbbeT/G/Nfm3x4val+m9/vT2xXOjx4jpMngeDX96cQfggcipv2Ek8c2risnA5zsJYBf6Cr8iL7//X7rkciHvJAAA -->
