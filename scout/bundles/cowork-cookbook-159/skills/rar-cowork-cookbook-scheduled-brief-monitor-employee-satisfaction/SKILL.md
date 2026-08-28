---
name: "rar-cowork-cookbook-scheduled-brief-monitor-employee-satisfaction"
description: "Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction", "rar_sha256": "dc4cdc85c1b960d406aea8d3b7017ab63adffad4c5d0ad632018a8998072774b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_employee_satisfaction_agent.py` and in the RCI capsule.

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

Monitor employee satisfaction Scheduled Email Brief — Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_employee_satisfaction_agent.py` and embedded as the fenced Python below (sha256 dc4cdc85c1b960d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_employee_satisfaction_agent.py` first:

```bash
python3 scheduled_brief_monitor_employee_satisfaction_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_employee_satisfaction_agent.py   # or on stdin
python3 scheduled_brief_monitor_employee_satisfaction_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor employee satisfaction Scheduled Email Brief — Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction',
    "version": '2.0.1',
    "display_name": 'Monitor employee satisfaction Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-employee-satisfaction',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7f06e76a84c3c9a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-employee-satisfaction'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-monitor-employee-satisfaction', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMonitorEmployeeSatisfaction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorEmployeeSatisfaction'
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
    print(ScheduledBriefMonitorEmployeeSatisfaction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjSLbmX9HEfcisS2aIfcm2NhskoQUEQggkoLIsix3EKnaoW/99HEkRmdXV3TN1Zx5GEWEBuPvZz3eOO/rtxWrqMC9fvrycPCubbawkiUKvnFmZO1vmXV7G4F8e2+Bv5uRZXUZ2U+dl9fLpxfUqp4yKOsqzabkTem6TWHbizdK8zKIs+GyXkefPvNSKklnVpKlVRiN4DsazCBABI0WSD543q6w6qnzLmWjNfDBSh96s9Koiz6pooph3mVf+bQZYRkHmubM6n5VNNnMB5WEG5neeFyfDK5DK6y1A1atevvz8y6eXCFy/fPntxUmsqvoupecuJtHEhxzcU4zTD1IASomVBWBJMQADTfeFVwLRUvDIBVo97z5WXuJ/mv3nf8adVQbVT1++ZrPn5+vL9KMAMSdt6tyqaiC5YxWWHSVRPbzO2KSzhgooWjdlVs2sWQXsmwWvj5XfKeXF7O/T2McHk9fAqz9+fcmBCNYk69eXnyYbfH0BJgHXrxOV4uNPr0neeeXHn77TqRr76jn1RAxI/frtef8kCyZ+nxr5d65/B1Qffra9ry8/KDd9HnJPeoKVL6/XPMo+PggXZd56mZU53sef/hVZ4AknTqKq/j+i+/ODcOhZLtDpKfhPn+5G/mUGPRV6p/mv2RbArX9FEzD9jd2n2dNQ/4r23f7/QDqJMq96t/g/JffPFkB/n/38L3X7dws+zfyvLysviVoQHSB1vsx++3aSueXPH9zvDz/88jsg/b8lc8qb0rlT+JZaWeR7Vf3t288fqvvjD7/8/KEpQKx5VvqtKZN/RvOf2fXO5w8WfM76+Me1gL+WxRnI/Nl7pM9+y4v/Uf7+OjtbSeR+f159mf2YL9MHmk1KvDF9mOCHnKmArD/Y8aeX3wFYZECb5p7+E1b8x3/MxMgp8yr369nJyZt6wpw6Sr1JeDWMqhn4fSAVsOsDqB7zQPxPHp4kzv3Zr//TuSPpZ+eJpPPqDYa+3SHy2xMQv70B4rcfAfHX15kKmORlFESZlcwUVpa/ZlbgZfUkQAFw0itbAC32UHufASh9ni5mUTb79S/x+XYn+VoMv97RP3rglrLcTZhVASqvk96X0MueWjqgYHi95zSAW5I7QDQ/Asj7aULuPGkB5k02quIoSWZuVAKD5OVwpw3s+GUi9uuvv9pWFX7NHiCLzR4VpZqDCe/izD5/Bjr6SRSE9dfMc8J89uG33z/M/mv271bdiU88ZID8Ty8BCfnTQZqBrGtSMA04ELgcQMrdS7/9/rQ0IAOqzQz4NPIj77EYRG3suW9mP23ZzyhBzmwPmBuYOi3ysp4qW1S/znb+7F1ewHQamrA9zKsaFLDCy1wvcwZA1QLqvFsyy+tnGRw+zZrKu3P91S6tu4gpSH+r/nUmLmVQSfLkrQBOk8Bi4FZg/vegeDwHRMoP1WzxRuJ1Jk1xOius0irC0nrymLw/+QVUkLflgLg1y7zuazbVT28y1T1pHuYBk4BlnKdLP08+B60BqO6ZW73xvs+xpnqn3ute+TWrnglhlZMrHFAgANOgidypTPztGVJVmDeJe7ef9+gCnl5wn165x6D4b/uH9xo/4+6dx73Uz742KIzgs/8v2pRJB3azUbgNq3KrGSepivGw7dRiTT54dGWgSXiyAXn0vXF4g5039P2aJREIlHL422Pm3SPPOQ9Ea0ogjMIqd/ogHIBtJ7r3aJ2iryynOLe+Zm8w/wkEwB3TgKIgteOHLm8Mp9E3SUOQv9P995J/927pTokOInJWNHYCosX3PNe2nBhIVU4Z9/QHCF1vyr4ujJzwD1rNAHUQIYD+DAgRgRwC1r2bTsqBmsA/fpmn36dHUyMFpHAbB0gLeljvdXYBSTN5oAKZCrqhaQ6wwoc7qVnqARsDEd8tXIVW8RBmanufAlqTL/IUxPKPHngOfg/zuyyT+ICq5Vo1sGU3YbDr9Q/Pvsv59BUQNp0S877oj+5+6jr7sR797Wt2l/Ed9kG+P6L4u3FmIM/S6g6wE1xVAHJS7z1OH1X79VF4H5X9XZYvf+r1P/617cC9lGp/9NyXWVjXRfVlPn+Uv7fq9wrAYg5iJCq86nslfGTh52fOfX7Luc8/5twfmDxs9mX21wT9A4lnhH+ZIa/wKzwN7SPHm0L4+QF2WX5eGJ/xafRrpnjfHf6Migl3QW7bw3sRepsCKlFQesE0+VGUqqmWdaB83lEYuORr9h4Uz5QBIJ8FUwWt8h9S+V6NgYsfHnwvFmAoqwFvd+rqAm/a/CST+JX38iVrkuTTS2al3l/c9EzFAYQwMMy0bQLpBBqmOvLud+/N03Tzx93fPdEAQrj5lynfPs2mRvfT7L1n/TR720Xc92hZA7ZRP0/98sQSTAX/3ue+by1t7wVs4eqhmJR4bI2mNu3ZPv9ZiCnNgMSONxX8/D1vJ45/IgIugsAr/0zkcL+wkid4VLU1le+ofkv5t4D9NANuBKkIsguAZgMW/JkN4FN6twbUSXdS97v9vquVP3T5/W6G+rG//O3lDUSePnj2kmA6yNbP1VQp5yBkAUNw/wguMPZ/12U+iQEMBI3NtMd1cMd1aMJBbIaEXRwmLc+iXcymYISybBKzXN+3XNwhXNhySQwYh7ZohqFhCqUo3Ab0HvH6beoNoklAD/Y9jEFQx8VIlCBwBqFQi3EtnLIsF6ZpCqZ8F5SJ70tjAKBPrR9aTiZ9b3gn6zyV/+3FJnEwc4tXO/bxWc6Zs0WilK2ENlSSnmHq850dabf2MpA3stPdc5dtyAUfDCdK8TgBW3JEfLPSAztsa0G0Fm1+9J0dNOhUNspsdMq4Juou6NEtDYKPR5OmkgNDm8IxWsLng0rSN+2YosK4Gc5cYl7QiEi0NFUjwucvtzNSJHzfFhzJdcy+NO2IQZi5xVC7w1qKDLpwCLIuxg19PjEFWRGbZB7oMu2TjWyauEaiZ4HXanWDI5aq6s0p96O1YrbOrffQM3cBcAr2xnUgD4hW+KYUDpIa0nM/20KQrJ4h24/mUlquR2iDh2eNP1nteY3zl7NbalBxI0dfOUenId5vD+QigXIMK7vESuKiVopGOiV1tVWzZWEYjh5oS/e8BSQQ0mnTFaJV0vJ8a0ptNRT5/srRFnrMcUxkznvTioS4WQtJoUkpXyYwgUZoTnlSdqkLZK5QmpmXiVPRuwsdF/GwHiVRyWq3L8JDf17eJFPf8SnJhoR6jfnco5KGJ0tTRsYs5iTeteEICQIBrzxFazzU7ORYSS5mIfH4oCZBSRWYtjww3u0sbHHjBJd0WZ1BtouSkwXQRrrwK0NoY2RbXuT6EtoHLpG8Kk1P8w2NVgnPlMzBToz9SK96RClWZ6C6enEyRbIHr4BuUoQqZdbRhyunkMQJrxpoi/C0clsPJI6puFFdkEE5Uym5cRpTbeSIu503cHPoQ4oolHNZIetaSwo1wdMlgitAaggNq3GdeptrFibjxhPnjq+chnNH96FhzdODdOw5wROSayNc4J5ZESODGKNzIW9BTmU0fNKLK+5e1pF0leJwSWqZm6Z8gjKqjiCq2d7S1ipvFLR1GNfx+cj0jzCUQn5EzxeexzJtWx/4PB0RH1qqFZSttqTr456eg/K6pBbSIp5D2K7GhZQ4kbfDUHFGFlvJ5bY+JtvtErbXSRVLZ+KqdeX6xsFrvS/5S2OU5snbaRYTkWqgXRQHX6xGWT1pld5o5zrGEUSAjzC7MiT8FgEwvJ74YZf2nLuL2K2NHrs1zBURuheIqu/wdBVhjTvk8wU638F7uDzxWuiZ0VJUISfk1Msp8lN1oxctJpwymk0opt2mYAdYx05YIQ0Gc9reuyXbA4ZB9pwtcxtF+lOVxH7C2xIU35r92vSvLGdJCh9vkFRFHGphhKO+voa1fVTi05xtZecgp6QQZZ3d57Fb6tYtF5NNIbQ9p2LKgRXWp6vbV35Ch6YPH0jFWMB5KrXlOCfg6Nzr13ClVUE77pMkpy4XRrTm5e0S7lylUDR/O1ygm7et7JN0vNUAi/dLZbjN83BXoWmuLY8Hg28CmFlRZCjx2BpuSg7RqEBRaWVkmg2XF3MIxdVCKRJtDtuMsScFozohDYIeEyZcUVdI4xAPPVqktsEpzN5WUdhRquB31nbHI0aEwn2mH+KKt2vptCfb47kPdB7vsbXnnPKjxspb5oyk5anV5SHWSDfHrJtddi1CqOJuSx9OkpkoOY/lG2KueQd/2NhIVJsMtzj6iKw07IgLTDBvEE20+gYC8pisXWD6JgjmNE/ApKBBa0HUVkq/KMjlYYMmbNkXK+JYQUe4xuKVm5nQPrx2gu0IXMY358pry/jsBOINyoaRPaV8BaEOdAw9PlwcjdWYLCptHBg2wQ20WhTmQb+yu1MixUBJp76hKOWInbzRw3zJkvvTrbzqHrJZwEUdnBZlvlvuHDu5slXZirA2GjG7uR6iODp4xNo5arHrdMc62GCJc0HQOpTDizmYHmdmmY5hxGGkUacetSCOzKhbu/O6v8TJlnchA9uMqLQYd+KqhEuek33K3GVM7RlbNwzGfUxCFwaCyhKa71p9OPt8Bp0ZDI0g7ryI6BNNx9haOG61IISKdrOVdkRiKt6ySODGRRYJa1OkXPMJp6P4aZ/zZ2fOifbCbaXsvD4a2I4uSJJNL8XJ6tfEKTl62i2ntkv/Ei+0TSKboq2JbFsXpmV41MJhdpe8XKBKKoKaw4QOopuuGrF7VcJM1B205iAsteN5q3IV6BtW26YQirrTdJWxUjQIarNUU6OBTWa3Utjc0EdK0A/itYxHNVy0Yp+OHAIsu/FTcX447/bxiPTtKeu2l7nC+Do3MnnJU124C/fkKU+TMyZhubj1tkRmRFSyDAd3r6N2De+FRUJt9+uLkpgFF9YX+6YNZMGTGoOX7HK8xQtPau1jv1Z4kTseNXm9S0BbwlfhSuohukwuBO8vDXYnWGV41elVjJswzhqu7jCaT7cn8ziYalt6YZ3m+TJqOgTiMLaE13KvHJRBLWQkwf1btQxMRSNZlGEu7qWQ0v1FEzgzWpCBYF5xz5nLBeOWMcNduPKyX9ldSgQ8l1M1IZ2NExMHytDz2jXcsxmRGjq7p0CH06+sZI+URFjPiejWnrWYDM1zsIcAqCF8uJ83CiopCUsSlCZWPHVixkiA+XaZ8Gf8tGMOpJPsWi3RNCPNwmxnalB+ZYmA2cOtuBdGfmHxtriheyE4Y9eTIJU7KNqRzcAfd9zquihEH8VjUpvzC+G04IL53JbnVQpveAaJD+GNIIRYDNg4BI2h1VnjTd+UZV5dcyVnI0YU52oCBO8um3R/bNbu0U2FgLlp5kBxoxYz1HG7gXqGr/cxSmbIeDgYjVIJJdIypHmrNpRYKzGOlnKziHfHgyhywqIR59chvlALBqm2oGImfMWOjLjo13sC8jNmQ0u8keSCsyg3tlWA7mzbBEdm0SfLC6PdbqsrGZ5yUxrrFXe7JRRscE1gHU/EWUkliNBukgd1V3zBOmGruMNQSWRsnZb7W8paEqsXMro81c4h4eKDdxw10qvwxRFhVwtN3l+C7XovyWSM3bhER7EjcVwZZY2vosZShzWN93sOT/W43TOLK5ySRt2cBE+7JttBGRy9DS7clRePoB+LrAG0eUtQh9PiujOPh7AnKFPViLjn0yg2Lz23PZowauLq9QytbtxYVskaK8YhFthOGApb3HNIfdbBfjAtkZi4dtEFaxAYQ/XxqM7DS7FZH3O/3MqBMBcBVmZOX4nyirB6m0BPTbTFOKTdymQT543Yo9eyltgcPTg7CjofFFR26Az0W/qYg3xuhBPf7hVp7vMx72qeEBz50d2pmsxwCKqFymgMcDhsDx6Nc6DVKIlWPjQ47JWeDml5fzgaBEYv4RNJJllT38RFkuLUILR6YZG5sF5itxjrli5LDceVaexQeLvp1oxFiJ2vq1xcwSsCOfImF6rI/ubQVb2fs56ltVdNsjb4VfVPhO7U+3SJK0tb1FDQzvF7AlvhId8VMal6hiy08tZlhAg67/grRrjZhU+g22ntrdWzTpqcYAg4quUXEMChPkJraFV3Ke5UqC7pkWj2ykoH25ygvrF4NMfIMiiwMrMtmJeWF4ILJWe4wfs+jpgGzS8QBmJks+PqWx7QFJvT6hG6gLTejeIg2K2j6faONCpW3cuI0IGuIaAr9JAlTho3Z4lccawjLtJutYkiwQk0UDbTCg10YePzg+mD7qiWWwRsTrjDTdRxljNcQvO1fpBRJGbPXbGMiqDPBkI8cJJrAHQwzmp68oSuFq3D0tHEfQWPVpU2PmVgig5qxgY6j1dE9aX4GsWuW8z1WuyipXLbliR/QNdU3qjM9aTKm5UbXofQbRdmjZRji23kLdGeaO9az/UmJbADVo9Obdeim9ByWY9kjYt6M9B6R2iUhA6r0EawDruI6bFYW5nTHJkSQ9Zlsav5Dt3JfBscTyxo2Ru7CdKOpHuUyq3SS+3NIlcsKzZj0pRPnHWVIdBD4MrKWozHW0NjWW8s0cgIlqKwEgkXNCcjQVOXSoAKsjep9EqiXj8apGyx1zki6eINsy10G9LbqrTHmiuFDSSt+4aXu33rovH8jBPrjKKoOROVUGCALcqlnZdbiG9LqmeQFay31LhRNmfK1HCN6XdGJGwLQV4O6SZeZopDY6zSLA4HX1zDcWcs5zqdVnwesvCOdOhwFSnIglCBk4LmcMST2Nl6dAXDDeaUuG4Ei0737Ia6XDuH9TAkvqVLIaASyqPNfryKYZZiBdsP0KK1RBwb+bhdBEuo2aBpKKttp69802Ur46r42HLfe25SY8Ni3s93qApJ56VjkkGVQbHsu4uA3IAe1VgxyNqInCzPMaVt3NwnMJ3MaHuLeaK2MGFGh7kRZs+QIa9tXL7mHuT4IiOFa5TS1DbYb3Y7atk048q+yNVt71sO2ZwMTq+h3O27rNErr6brDF1awWLFjDfIXxyzLt0X1oJbOTh39Hg5yBAhtK710M+xeFC17YINAVSgyMrhxHbwWp2jRyRf0MbYjdfh5rDORmJTuaHdzdIPVWbj8AyBZlsskKVll1Tr0YjWHuIkMmMjlI51SnjbUoFfsCWf0UzkJnZARwcQNet0eck3TLu3F50hSlG6LCqfgoK0wVFiaXrzaIerXuQFVyhxUanZY4YOaDdcM8+KtRupV97YywWP6jhZ0d5qCNSidqrrfOek0RyBtx5GEhszw+xQ1tmwv97wDdsSI2t31PYalhtxhfGjtQqdNijlasNKTDlKzQ60KztxiRv7VXtbNCF6vEApdr0QDoxgLeWXimGFWApfOma7Vm8Ctu+g2DtKbHdsSS1QGE4i3Q3oIxnlCtlbBUKWOSGHJJMjK1T3L5zcql0mlbWzk+jjpsAylArxbbt3S2YvbiCdUZmyySSXnsOs6AQyg/Vz0gXqrUgCRH4FSXzJAAzzRXfZQWCnEOwJvA8xbH5hQWVzG9afE64DdbcNRPUcqse1TyvsoNSwUkSsTUuKgbioAZ0YeisON99RctAiUHRUHSGw/TcugbVcGsnNg/YZRpJIz/bVqGE7w2lkDRotKkWwCL0oAPp3gqKUyDqMMtiDD/LxGjBBdwjyoxmZFrQX5SNVD2tVtft6QH3V9lv95Ea+JC+skr2si42EyI3FqAW13Ha0s0Vs0GyeMXJ1Fbcdy2NLjtbRwBy91SESGqaQiIPFmjBx40XHF8JaGnAG1PW6POjBxaOCg9gGKEQdqk6G5rGWd5tzX3Q2RlktwfG10xi4Do1LrJGaVbmfZ8LAdBKrbuerXeZu4vFcDwYe08lSusxNwVapMnVX4zLDOpxeQBEXwHq274Mezo7JsVocMFhatofoeMjpaDuq0LWyFYiZO9udK1m2a2dlEB16ilnMtQs8zhHhyLIvn16mI+vnwfN/7/XzdPz3/+wU8nFg+PZq6n7o7FnulzuvL/9N+X759FI6EZDucQZbJU3wPKT8hxPYz3/p7cZEani8653erfX12zF+bQXT15leosxtqrocvlV50jxX2E01fZ+i+vY8+H65q5sW0yn6P6gHnoRR6X2r82+lV4Orl+krD9M7I8+NrPrtNnieUX96cQfgx8ipvgGs+eaVxaT485UJ0Bd9hV+Rl9//Fy0PkK9CJgAA -->
