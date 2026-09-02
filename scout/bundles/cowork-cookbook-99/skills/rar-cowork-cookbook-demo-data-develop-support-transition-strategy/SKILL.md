---
name: "rar-cowork-cookbook-demo-data-develop-support-transition-strategy"
description: "Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_support_transition_strategy", "rar_sha256": "cabfe29b2be8d0477d26830dc86952274222d4a4d0cc87c56d1c2eafc1e6e117", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_support_transition_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-support-transition-strategy:d1ac48ecab85bfcbf863929f4aadd0400b09a7ac173601d63982fa50c1f698e9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_support_transition_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_support_transition_strategy_agent.py` is
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

Develop support transition strategy Demo Data Generator — Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 cabfe29b2be8d047…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_support_transition_strategy_agent.py` first:

```bash
python3 demo_data_develop_support_transition_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_support_transition_strategy_agent.py   # or on stdin
python3 demo_data_develop_support_transition_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop support transition strategy Demo Data Generator — Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_support_transition_strategy',
    "version": '2.0.0',
    "display_name": 'Develop support transition strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop support transition strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-support-transition-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0764a5b90b0e472e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/develop-support-transition-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-develop-support-transition-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopSupportTransitionStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSupportTransitionStrategy'
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
    print(DemoDataDevelopSupportTransitionStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZejVrbmX6HjPti+ZKaYQVGr1mpAMyCEBJLAWSvMcBjEKAYxuP3f+yApItPXrtvl6n5oxYoQwzl73t/eG+LXF7upw7x8eX05ADtDlnaSRCEoETvzEDFv8zKGX3nswF/EzbO6jJymzsvq5dOLByq3jIo6yjO4fQkyUNo1qO5b3RLcj+FXElV15CIeSHN46ualVyF+XsILN5DkBVI1RZGXNVKXdlZFIzWkqkdKQY9EGWIjFSTo5B1Sg8zO6vteeD/Koiy48yqiJK+RyoW3yyivvkDRQGenRQKql9ef//HpJYLHL6+/vriJXcFLLzMoysyu7dlDgsNDAP2D/+HJHhJK7CyAO4oeGimD5wUoIf8UXvKAjzzPfqxA4n9C/vM/49Yug+qn168Z8vx8fRl/9k2G1CFA6tyuagCtYxe2EyVR3X9B+KS1+9FQdVNm1agutHEWfHns/EYJWurv470fH0y+BKD+8etLXoxGhzJ/ffkJgYb5+lI24/GXkUrx409fkrwF5Y8/faNTNc4FuPVIDEr95e15/iQLF35bGvl3rn+HVB++dsDXl++UGz8PuUc94c6XL5c8yn58EC7K/DZ6zAU//vTPyLohcOMxQP4luj8/CIfA9qBOT8F/+nQ38j8Q9KnQB81/zraAbv0rmsDl7+w+IU9D/TPad/v/F9JJlMFceLf4n5L7sw3o35Gf/6lu/92GT4j/FUZ5Et1gdDgJeEV+fTvs5uLPP3jfLv7wj98g6f8jmUPelO6dwltqZ5EPqvrt7ecfqvvlH/7x8w9NAWMN2OlbUyZ/RvPP7Hrn8zsLPlf9+Pu9kL+RxVneZshHpCO/5sX/KH/7ghwhtHjfrlevyPf5Mn5QZFTinenDBN/lTAVl/c6OP738BrEig9o07v02zPL/+A9Eidwyr3K/Rg5u3tQIdHAdpWAUXg+jCtGfSf3LQVrL8pfU+wWBV8d0hxBhN0mNLCFaJQjMh9Hjowa5j/zyP907un52n+g6GQHyzYOw9PZExrcnMr59Q8a3d2T85Quih1CGvIyCKLMTZM/vdogdAAiQkPs9Tqom/XwbBYDCRQ8A2ovrEXyqJgF/Q375Sxzf7sS/FP2o3tcM+gtCMKRcgxRugcib9Ig94pfT1+AzBGCIMWWeJI7txsj4pym+jDY7hSB7WtKFBQd0wG1qgCS5C7XwIwjan2AwVHlyg3g52reKoyRBvAjWDlh4+jvkQx+8jsR++eUXx67Cr9kDoEnkUZGqCVzwITDy+XNRAj+JgrD+mgE3zJEffv3tB+R/If/drjvxkccOFo278cZahmwO6haBGdukcFmFjOEC4eju0V9/e3hllA7WQgTmWeRH4L4ZUvsWHqMGD1e9+wnqPIoIyien39sNaUNoFySqobVg7lefvmYjiRwuLduoAu9GfGx+mP7d8Q8+o0+qpw2hn/wyT+9r75E5OnMsy1+QtY98WAqqO4bC6NEwr2oYzAXIPJC5Pdxp199cmI3FF+ZT5fefkKaCqo6Uf3HGEg2Nk0LQsutfEEXcwfqXJ/DPaKA7e7g7z6LR8c/IfVyGRMofYIwJ7yS+IFsYoCVS2KVdhKVdgfs6335EBKx77/shcRvJQIuMNR+MPrpn+j3yZv9CwzG2BsjYGyDPfmasqQ2B4RTy/0+DMyrDL5f7+ZLX5zNkvtX35iPyxg5tNMSjqYP9xYPYmEbfeo53eHoH7q9ZEkFvlf3fHiv9e7A91jzAsClhJO35/Z3+mPblnW5Uw5AZY6AsxzC3v2bvFeIT1Ao6rBp1hZkdjziRfzAc775LGsL0Hc+/dQtPG46awzhHisZJoHV9ALx7StRhOSbc0ykwfsCYfDBD3PB3WiGQOowNSB+BQkQwkGEVuZtuCxNnNO09Cz6WR6MvoRRe40JpYWaBL8hpDHQYrBXiQE+24xpohR/upJAUQBtDET8sXIV28RBm7JqfAtqjL/IUevt7DzxvBs+Q8r5lJKRqj5D8NWuhE2DCdQ/Pfsj59BUUNh2z477p9+5+6op8X8r+NmYllPFbhYCN/tgFfGccGH9l+ohuWJ/jCuZ9Cp4BBCPhXvC/PGr2oyn4kOX1D6PCj39tmrhXYeP3nntFwrouqtfJ5FEp3wvlFzdPJzBGogJU96L5ebTX52e2fX5m2+dv2fb5Pdt+x+Rhs1fkrwn6OxLPCH9F8C/YF2y8JUcwSaFhnh9oF/GzYH6mxrtfsz345vBnVIzgBwHZ6T9q0PsSWIiCEgTj4kdNqsZS1sLqeYfCe035CIpnykCkzYKxgFb5d6k86jS6+OHBD8iGt7KxGHhjQxiAcWxKRvEr8PKaNUny6SWzU/DXxqURoGEEQ7uM8xbMJthq1RG4n320XePJ72fHe55BgPDy1zHdYDGELfIn5KPb/YS8zx/34S5r4AD289hpjyzhUvj1sfZjMHXAC5z96r4YdXgMVWOD92y8/yjEmGVQYheM5T7/SNuR4x+IwIMgAOUfiaj3Azt5YkdV22MJhZX7mfEVlNOD3dcnBBoTZiJMLoiZDdzwRzaQTwmuDSza3qjuN/t9Uyt/6PLb3Qz1YzL99eUdQ8bjRwfxiKD71PrvtHyjfd9L9dvIxR5p3Ruzu7nvbe4bVDUaS/J3t4Kxv3h7ROfLK0Qj8OllNGoZwao53Ofzl4doUKdvDTKkAHHlczW2GBOYXJASLPzFqE8MMfE7BuPlyLuvHw9e/7Sr/pcB4tXDbZfigGs7HO34ruNzDDklpj5l256HURjmYFObtV2cJRkM9+BNjvBtGnNxn5lyYAolGj2c2k+JJvjoG6jLhwP+79r+lwcxWGkImoHUoKA+IKYO4QAOyseyHsFwJOa5HDOlCYKlCILwKJvyMNflWJdmPNwlgO27OGAAjrMjvWev+ZDw7b2vf/fWAzTeIOam0Sg/Ydsu57I45U1Zm3EBiTmkC3AC91gSYPSU9DkOUHD/x9anx0aHPowwBjZsM2GTdxv5/PqMgDFYGQquXFHVmn98xMn0aDME6+xDBy0ZYFrnydqJjOvg2+JRt+UmZ/SZJ8aBRXp5xi/YgncPx62+2lgzop7bwi3XfHeN9mc2G3Z8dKjounJ5wl02lkLu0kFOOHqoZ4Ixb8FVao4nUzJBEylLI7kmcnpMoHsVCOvM8XSaLOaO2VHrqCqya+JS9rzoADqZ1A5X2L0GDteDcVtkE+WKlWctMpLifK0OxnV/lOV56ZuD6ol9XAmKk17s0JBvqoQTG5ceCp87MoshbhNnLYdGWDmX2MwG6K5swFhwJon9pp/6KxI1e1il6ONa56l9Ygl4rdtJWVoqviic2A3F7nK9WJOobJsDEwgbyYlt6xLXlhOidGQ03hXqt6n3m6PlXhfAzei+BadreuhAfl0oXCmKtKzrpuWcDk3CFac5PeSn4nQaitSi+WspTbfNnlG3WVoX+GRPGlZRqtk1uu3IHBchAVRRwgSD1jH7xtyo8UbsFVLSJWJ5omDmx5OzCjQtTvDmINsiX95m5Sb3N+fw6s5ay0tSR9c9J9ZA7+NBhp2l+hACaVXb3fwEvFO3m/kzlxQ4160Oy9ZwNo16qnZ2fejdzdXmzNqICW9aUVsUxU9JTB+U3DOuGh7ymcHpNsNbpwHf4V2W9jhMCQErGnNVZklCkmi4jeqzch6WlH85BmRzWJfVBAy6YrXO0t0Li4Z27aXL+IMUlWdLErgbJ/dFj+mCHW9cTvFOsRNT2/NgGITamLc2u0SMMSjG4EiLcEebVDZfqzJpKBWtE8uZPKlAUzbH8Hw8rbIKz0SxUydyPChWbq+x9alXsOtNspIrc9vef4nmfKyVtJyErHpe7TrzVBIbHw6x+W3Xtn7IUx1X0EtZWZcTgW5cvZxMXT9fCLGfXTN1mLX77bRGJbCuXDk77oljPGwsqTzayWk7g/3cNG0JUcoVs9v2+9NlG+45O9pDxEeNzBVWN7NPKFqA8+0u4GZt1iuCdk5X5XG+c8WA2vJr6SIti35rlnOTnLN5rMy3SXzp1xItzgtrsdieLMrUhU4hs6rZts2FWqIgtoGSTONunuUpZ/XyLbUvg77dU1bTJ8BqDu3ai3Fg0deU2Pcn0mB39j7aEpLBsbF/vU1WbXdbrPT9wSmmp1VLMH1DV0k4VTWLwRdCscRTHbf1AIjy0j1hArG1loEczG9obO1SRoouDH65KhNLvgpwvG3nCyNVgrMTaRamJ2Jo1CQLqKNww04MLOyYCdf6k2NSKAWMfdHenDTPINjCkTEcdmQTfCNpin3FqJtyIXQPv0T+NlzIU6OpD4RxSXBSn+/BTdeC+ZVr93hIUysSn/FDuik8IPXSTtB33fJG1OtDlE3oJlSTZZAYE62xAqy9Rp1ss541X7XSThXU/RFnTaGUNDCr8aoZDiu9VgosimDORoXLuIN8OZ2Mkk9pizmZBooP4TZ3Bnm3dzfyXg9Q0PTHYtsMCrHz1Fypre2EmuC07q8Vvrnwg1wqtrpxOBlMrvJiZ8lbZg8qVNxou0N2JflweuR5tsFd1R3IxmxppQ8yvSy3No+aiy6+Ls9oIe6MYt+rG8JVUzrlKf24FOUdqrU1Z6zcbMNIDskZhKKFsRHTaUJxfof1OFFed2dVvLrpwO67TlTa7sBHbUZKM3oXk4e4m60XkVIKLUpteKPIL95Rqylo9ltjChclwI48OBZ7D88vWz3wro45zyh61gar1UY4rK+XYbtQ5+Z1PZWGlmazpBcOC3wQGEyT7aPAOhZjMiuLXKRUmHqe73jcVB2Szss2ggTzWwz5NbqLsbyXbtmSXtrDBl3w4XYZWhzJcUtXNuVbqZ7N8zYKxVU2TPG93/eT4DZD1ysmb26rPvelFb3H5uuuJDvdNQK+PgmrQzrNOXyfHsMFxTTHw4Y0ltjmdlsTWGrYSydYNwF+7DlBnSx6yW56KVZvKyzm6xTWhyKtbZ4TDuFOtDSPTZRNNC8u0qVJ43ohTEqtx1qnX7AEfVyQTTYU5bwWGsWRwsUKJ82INW/dXjOOSthlWLw8+xfccQJWja/H4iaF9nDarvZm2aJzsYpwRbKnWJIsOxbzNhPRJ8yeZtZBNxPsYeGyYCMWg5AWin+O2STuGXQvzIOwL7Xt8lqtp/3G99Bu2tbsZSaoerrPonJzLU2uoXX5mmcLnQ0GfpZeNZEipslMN7BU262ENXc8nOsiT0VxtvJWTHF00qTccLxKF/0CNsXkQorkQWyP5+2Z2AmDRkSadOQMw9Kwva7MiX3VxpS4avXZwqVXsGhNTueQFXFmdlIlazC8U7FN5VO8iaxmHvGSu5rXRI92TmelVE/E84BxVD5x9/NsU/d4NlsqUamuTxsr17lQn1QDNKucOwzY2kboVjf7WJfGOWYgdF5t2zocgwlunYt+vU/Y297mDyHsMOVeDS1gTl1RxkPpFtQ7/RpuenXRiMGV0za1JTmaPaPwVgFDFetOa0nums0XXGe5RmkYhqlpQmhMqqhw2niek4VyuqxRtvEPuyLXMJ7tPb/BdnV0QZtl1ex75bzbGEJezZLzkWPgwOcdDokFy821N5TJZEfGsNVxzMV+zeAbgVwvU2IFduKa8YrscmDI20W2LNQlzgfW36ddwijZnElqFAdmP2hLcbvUJBp4hbsOEv4oxTMzX92yXV1d6dOh3WH76zyCuazVK8w9lRW+vcJWvBcW25KXrIIQk3Pq8jQ2q2enam0nhzJvhGtuhCHZmpLBxMdb5qlUYjRHw/ZAc9Qv1C0wEp5fapOooR1jSTOS5c6KaHnBBKq4xjp+CbAYX8TLLWo1V0Ow2kAYzEVcLOzZdT9jinw31UyaOUsOmt0OJyde0AqXFM60DZtVUajStla6srWqgYnx837GX60+sgKqlS+TPFx3bQqht3PktcYIMil2GR6fNaqq803kEtZhOGzl0oy4nOccl1q3zJSvIg8jxNTBiqm+4B3FNOps0dvEtezSw9G+uUVMR1x4OqN4fMPwrE3TpY9SXb8itSFf3obFbWUUk+wUTq4isfXZk1ZsW5Zy9uSk3EjSpfJyhtF14Wjqa7aHdea4RWnGOdAZDXqV9/B4T5DSPppjhRC5oqdFQtDuYYvoX1SGhr2MltPhxjQj6SwS7sxrQ4PapQHFbFbJ4iIP276dpPvTdlK5/pVmYJ+/nW9OyzK6rYsLSODsnMTy6ToD3Kaa3Tb8Fs7SrOZu+J1VxoNAeLteszQ1g6gd752dwRRt32M3bmflc3SrDXAC2Gw5Odn2WGxKYFZUXcOQlBeXmbIDc11M9WLLGsvjHJC3ZnFbSKK2pTKLbiwfAhU0P6GCZCYaTLPlpaWRL6Uj1iXd1A5OrZSe/W0tduxlec60zVTR58K85dAjWFxAoZIeq9tB3JpDy+JFejwEDarayRlEZXa+zobaiELuIsolqU+XvIhubvNBGnIQs3vZTi+C11FYMYkva9gfL6JLzIGkOW5oHssqRehb9yRWvaJYQJpG9dI8Sktn3RXZ5khbakNPvTy3S6XLeRETz9esIwNHvWje1OIXitTmqTnXJ/DKrLP3p5DDRasg9Vkn5Owq1OCUo++uosgycXrerfQV1aNzOYQDxZTsG63e0RTDKE1dWh0/v+jdeYi8en3WkiwXE8bBVrU+i0VWnSVOcU79+gj8Ho1yejWdnmuCJq5k0nO1VSte7q62hDPtWVIm3dXCVc8q7YWBeZpWzZrtjGixYF1qu7/UqmWdm7mGsTvrUg3UjI2h1xpOpGE3w7Kza+KljSSY1rGbJ1c61M9zRubRFSfT3W4fzNJVxZXlYPqCzyniap4EpspK7YZinB6TUVpiDuU8Y05K2VHLLRuwJrFA/eLcLfCkoBhlAH0JRVrWym7IVQ+Vvc6jm0pgdrvlbjJxPJ/TFClJl8n0PEHXZ5oh4LTNZhmFawQjeTfZvUrkkYKDLMWJu86fzrblNAgbp5WP/oRPvf1+rTS7Bh+WBSxPl7rn453iY+t1PtncjEW72qwnEbO7ZKcjwxwddQrRHJWg3daEKgRT0lw2tcVfV022pYfzTVIOV91MmXkCEcvHYBVOT6g/S3mWO3pYv4z9tlmiPTOzwsUFBWs1cCcye8sl1Gz2aN9v8/2mmuorm8V2J6+rqKUsC+aFwhYYzk4WESwGV3KlEjcOL6fOhLxcwpUUNEx5IXgrEjcstzuw1CrM1QFMrN4Ry4S4rXT+xGkqsTh5KUPcbrR7Qg2P4LrgCMhrSK5m3jAdOjhPoq1u8ILfFKeBUhfovHPlQAmdbB55oTTtd1q0uG7ZpJxe1TheqzNxRYOUNbbtoZvAAdg9DDsjWHUXdaLupLDlWxMTTZTtMHODLs+mQh2mHZ6thmC3kLqEW+dUJPg4KvlMa6qrGae0noDms+pgX0/o5IA6/Xq9nrVpK5yDrPdSVAw1xVtUW830SVb0jkbdz3HOV24Brc7Z6EJtnLp0zw3adJrsWjWl9mC6WClDwJ2iFa3XEm1Ml4mWitLUWzUr3xMHoiVPmE3vnOx8vuyyedjNUmYVD20yiU21o0wbvfDT3iUC6ixT8p4N3Cm5vO1O5pSc8pYmC1WjNo1Nn71ZWZDekY0HnQRkfSoW4XUFYKYKWLPf5SwQBWXJ8dIsythB1wA6NN064PvKby0GRjjurDl/la/MtHeYMptKjmjAtG17MuLtlXezZLH1wYk9U0dzSzUMywWgaRj6dkKXymEFWGbiSSGtSVMHnRnymbzUfgKWLA7yxCM1+SBONHJBnk2UYrwMBxPB99PqslJKdpWycLG2nR0WF1rAQ/G6FnQKP5Inwpqw7LK1L/ae6k9lmZW3QEJLTvPDqy2YC0lDy5JibI8V9vP6RCo7t7mIXH9gYbkvh5NEV8CRNVBiyxD2I6or7DS2RnnevqypQ7hJ6bUL0WYqqvrsjNfR8qw7ZG3103rKXoqOWONrsd3mk6qYktlV2FktuouCRjbT2/wGTGDyJ5WXKJCIJ4JXHcwyaJ3ErWQ95DNlZVmSMKPPdXfVVhuPlE8BA+gD5lpdzDGAYlV0djtTa/EsWLcEiOhuZvhmsZVxmGwr1Dw5rBv0KEylmKOW+ebiF4belNpeIugtZ7uHUL36Sr0tptNBFeiLLrcA8ORBhyNNJvdBh2XaRasE9dyr4g2NNDXnIuh71KzOezCdOKu1t7VKl91lJu1dBmaGzsxMjjhJ4/mXTy/398IvrzjGcNSnl/FtwfOZ/7/9nDgYouLtSZZkCebTy/+7h5WPB4fv7wnvrwCA7b3eub/+mxL/49NL6UZQusdj5ippgufDyv/yoPbzX3qSPJLqH2+/xxedXf3+TqW2g/tT7yjzGri4f6vypLk/84beaKrx/2Kqt+driJe7umnxeKfxVA8e214aZRGkXr7V+dvjvQB4Gf93ZXyDB7zo22nwfGUACfTQtZFbvZEM/QbKYtT8+QJrfKw7vsF6+e1/A9h8BAMPKAAA -->
