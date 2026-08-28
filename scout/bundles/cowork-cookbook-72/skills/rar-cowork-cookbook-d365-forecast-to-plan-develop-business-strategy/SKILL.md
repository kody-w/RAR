---
name: "rar-cowork-cookbook-d365-forecast-to-plan-develop-business-strategy"
description: "A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy", "rar_sha256": "8fe55d7da2ecfffc82ac86d5a92cdd9ab16c64fdb23570ec8478d42c84a182d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy`. The original RAPP
agent is preserved byte-for-byte in `d365_forecast_to_plan_develop_business_strategy_agent.py` and in the RCI capsule.

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

D365 Develop business strategy Expert — A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan-develop-business-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_develop_business_strategy_agent.py` and embedded as the fenced Python below (sha256 8fe55d7da2ecfffc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_develop_business_strategy_agent.py` first:

```bash
python3 d365_forecast_to_plan_develop_business_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_forecast_to_plan_develop_business_strategy_agent.py   # or on stdin
python3 d365_forecast_to_plan_develop_business_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Develop business strategy Expert — A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan-develop-business-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy',
    "version": '2.0.0',
    "display_name": 'D365 Develop business strategy Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-forecast-to-plan-develop-business-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-forecast-to-plan-develop-business-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16049eab41a04023',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'forecast-to-plan/d365-forecast-to-plan-develop-business-strategy', 'uses_skills': {'custom': ['d365-forecast-to-plan-develop-business-strategy'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365ForecastToPlanDevelopBusinessStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ForecastToPlanDevelopBusinessStrategy'
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
    print(D365ForecastToPlanDevelopBusinessStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjSLblX2HimU1lPTJCAiSWbGuzASEhgVgE2qCyLIt9X8QONfXfx5EUkVVd3T1Tb+bDKDMsBLhfv+s515349cVs6iAvX768aK6ZQZyZJGHglpCZOdAq7/IyBr/y2AI/kJ1ndRlaTZ2X1cvnF8et7DIs6jDPwHQaYofMTEO7gjB8CW3+u7YSIbcv3LKGKjsvXAeqc6gOXIh1WzfJC8hqqjBzqwqq6tKsXX+AzNI1oU8mlEwjXlGoaiwnT80wg3IP2uSla5tVPYkpEjP7EXoFGrVuWUHIHNpjUFHmNhDnVm9AObc30yJxq5cvP/38+SUE31++/PpiJ2YFbr2wQMV3ecdcAdKeSjFPnbSnSkASeOiDKcUA/JSBa2CRl5cpuOW4HvS8+lS5ifcZ+s//jDuz9Ksfv3zNoOfn68v0T22yu/F1DpYEvrDNwrTCJKyHN4hOOnOooNKtmzKrIHNySJj5b4+Z3yUBn/19evbpscib79afvr4A1wJdQRC+vvwI5SVYr2ym72+TlOLTj29J3rnlpx+/ywFujVy7noQBrd++Pa+fYsHA70ND777q34HUR7gt9+vL74ybPg+9JzvBzJe3KA+zTw/BICKtm5mZ7X768V+JtQPXjpOwqv+P5P70EBy4pgNseir+4+e7k3+G4KdBHzL/9bJTBv0VS8Dw9+U+Q09H/SvZd///g+hkSqsPj/9Tcf9sAvx36Kd/adu/m/AZ8r6+sG4SggIxrcT9Av36TVPWq59+cL7f/OHn34Do/60YLW9K+y7hW2pmoedW9bdvP/1Q3W//8PNPPzQFyDXXTL81ZfLPZP4zv97X+YMHn6M+/XEuWP+UxVneARB4z3To17z4b+Vvb9DZTELn+/3qC/T7epk+MDQZ8b7owwW/q5kK6Po7P/748hsAiwxY09j3x6DK/+M/IDG0y7zKvRrS7LypIRDgOkzdSfljEFYQ+D/VdulOaBQCxz7HgfyfIjxpDADsl/9h3wH11X4C6swBMPTNe+LQtzq/58U35wFF397x8ds7Pv7yBh3BMnkZ+mFmJpBKK8rXzPTdrJ5UKEq3cssWgIs11O4rkPs6fYEAfP7yF1f6dhf6Vgy/3IkgfGCXutpNuFU1ifs22X4J3OxpqQ24w+1duwHrJbkNlPNCgL6fgU+qPGkB7k1+quIwSSAnBGoADhnusoEvv0zCfvnlF8usgq/ZA2gx6EEu1QwM+FAHen0FVnpJ6Af118y1gxz64dfffoD+J/TvZt2FT2soAP2fkQIa8posAcrxmxQMA0EEYQewco/Ur789fQ3EZIANQVxDL3Qfk0Hmxq7z7nhtS7+iSxyy3Mm9EGCavKwBekNh/QbtPOhDX7Do9GjC9yAHNOa4hZs5bmYPQKoJzPnwZJYDygTpWXnDZ6ip3Puqv1ileVcxBRBg1r9A4koBbJInEx+WT3YBk/MsBO7/SIvHfSCk/KGCmHcRb5A05SpUmKVZBKX5XMMzH3EBLPI+HQg3ocztvmYTh7qTq+6F83APGAQ8Yz9D+jrFHHByClDCqd7Xvo8xJ8473rmv/JpVz6IAfA+8cifxAfKb0Jmo4m/PlKqCvEmcu/+AppOkZxScZ1TuOTgx+b/pKNaPBuRrg86RBfT/U48yKU9znLrm6OOahdbSUdUfTp3arMn5j84MdAgQyKxHAX3vGt4x5x16v2ZJCDKkHP72GHkPxXPMA86aEpin0updPtAXOHWSe0/TKe3Kckpw82v2jvGfQeTvgAYiBWo6fnjnfcHp6bumASjc6fo739/DWjpThYNUhIrGSkCaeK7rWKYdA63KqdSeYQE5607e64LQDv5gFQSkg9QA8iGgRAiKB/DA3XVSDswEVeaVefp9eDh1UUALp7GBtqCPdd+gC6iWKWMqUKKgFZrGAC/8cBcFpS7wMVDxw8NVYBYPZabW96mgOcUCBLl2fx+B58Pv+X3XZVIfSDUdswa+7Cb4ddz+EdkPPZ+xAspOmfOI0h/D/bQV+j0Z/e1rdtfxA/FBoScTj//OORAosLS6I+uEUxXAmtR9JhDIhDtlvz1Y90HrH7p8+VO//+mvbQnuPHr6Y+S+QEFdF9WX2ezBfe/U9wZQYgZyJCzc6k6Dr+/k9Frnr1PpvD7J6fW9BF/fS/APyzy89gX6a6r+QcQzx79AyNv8bT492oe2OyXx8wM8s3pl9NfF9PRrprrfQ/7MiwlykwHw7gf/vA8BJOSXrj8NfvBRNdFYB5jzDsAgKF+zj7R4Fg3A98yfyLPKf1fMdyIGQX7E8IMnwKOsBms7U1Pnu9PeJ5nUr9yXL1mTJJ9fAOK5f3HPM/ECSGLgmGnXBApqgsjQvV999E7TxR/3gPdSAxjh5F+mivt8x8DP0EfL+hl630Tct2hZA3ZRP03t8rQkGAp+fYz92GBa7gvYwdVDMRnx2BlNXdqze/6zElOhPWF20uW9cqcV/yQEfPF9t/yzEPn+xUye8FHV5sTc4QeTVEBPB/RBnyHgQ1CMoL4AbDZgwp+XAeuU7q0BFOlM5n7333ez8octv93dUD+2l7++vMPIMwbPVhIMB/X6Wk0kOQMpCxYE14/kAs/+b5vMpziAg6CrAfJIz10uHcIxUdf2PM8mUdMmcWdpUqjtOJRpIbiNLzzHQrElMXdtckGQzgIFv02ERB0UyHtk7LepMQgnFVETiLAJZOFQhInbLja3MNtFUMQhMHe+pDCPJN0F8NbH1BiA6NPuh52TUz/63ck/T/N/fbHwBRi5XVQ7+vFZzaizOdMJqw+2s+sc7g19I2jh8UawfiO0rpCJVIbM2YrbOo0P02G1rgf+gsqLmrfJirgtdJpU+UV3pPYeQTv8ydsbx4TzxUuvLxpCHluPNG6+v6Itpc1KUrpWaRlf0lVgXS+NsTJxs4wTJ6wv54zoavXcjNcMowIeHg2psa30EnDGkpjh7n6+USX0qrm39SotN0J7WQTLoWU0OzpGe1P05jtHQjIhl5IxOWozw060fdCEu0G1rVE0mkHdoPtTKW5VeLRKJFBv/jEO6MXWX4rXPUko12IglWvLjQk+UzwyMDiqt/H9oDWH8wK7IOfbparTodBaOpZO9aK7yMb8KJE7II7OOr4NklgMl8vmioTSsEz4trtYAnBmuAjQWcY32lox4nMxiPnNWJHlerXcC8dj5HeYsjzvQQO4W+wIMxmSNI3DpuSupFNecxhBhhY/VnHT68uxV5icls5FPmb4gVXwMTyuzpUQ2zrZHHgl52nThg+3Da4hKXEWkagdxA3d1HPN8g8bY2HB1nZVEKXGeG26359SzByN1Xyz92elqnSNaiYrKcNMBO+raoGE6HbHUTlL6i63lqodzuqOtCvPJrLUj4m6NM5RVGxhvVZ5p3QUQYuZpcsvTT4PylgWi3IW+UxSKqfZ1r2U+2Ds4+2RF7zLXqnS2uFDSblcNyvCi3Zdq6zPppPoClkvWFFGuZQ7C6xrbnZzggxbCUnzKNvPaPKWN+uOq8WrESiRKY5SWog3ASTr6bzoSet6AGjcu4tDzM+ClJ+t+pRM2O3p1OS9qSwjBDHG+obfDhWVVeTBPoJgiRvO4o79ahPvlVN+dBw5XRmbWyEcrry0vzJS+/hBSmwjpKOs5DN171+zEVPQHdsJEcEO5albw2ZL0DhqH4sZLG7RdW9zS5PG6uua0xhLr7CQvyZ7IafEvg294HbW87Ol42J7VXVL3l4uopkYu55ZdF0j8ztkRJzVEV0lx2rQZE61zPGmKyJ5PgXyhfSLa9Hv43PEFP7+gIWrnVeet+uozmp/d9g5e4FLu/O4KTRSEEwuU+OYDQ106yWKvr0uouP1iEgtj67AVjiPbxtjU+9S1xqkKiVL3ZCzQr7Nj8POzc7KHE6YfFMv5RlRrEZnyxigwoluhiguFfamNxwbpSKjmZcK5ajK1w5XxUvRNTo6H9Kb5rJB0M0th0h5PMhhAL7lPLG7Ac6XtrAu8Tlrm4ohLpcHU9XiqG1x2F/F9szxbuIgh+F+p+97xFihyT5J/GOZcZnuJc6o5WeV10/qNrpp2pBoLYILDnGqAn259mIs3Ku3/cYXCvFEHQw4WJI0ulwOY3oJddTwBYzSZ9XxLAmHVm/PqBueV7x9y8jgGNCYceZWjTM38dW+DPWYUHngWn9dB1IiX7XRWoi6NB+SFV/GK1NbjNooN4ZhaHk8D67qBR9Ynlm5Rl1s4takd95IwZfaCOcmZsx4LinQXYMuvAW8HXxqOaZdNSxGNAuUtpm7ZHvjnY3Z4lIPgINja5aQu5QS4YMDXKPpzHJu66ORJKIG0rlXsM677GA4hzFDOFnLwGX31VymODQ4szHbYadI9RliObrVzZ1VTBfq2VwVrlyO4JTHVKYnn8tWXDOn5TlDx4RcX+IdVzO0Ip840gNJsuoUzu+Ma52R9GrLn11uhsUb5AQ3FpzO1HBhez4bSze14RO1WByDs+XH2YWpupRN6GLhBMu0iKs+KAzdroN+qZdrIYn0uSyNe2MILwjapEp0MQDpr81hLJeUey1RuBFEjRY4QZsH+MzETtrJ3Fzh1i6vRo6xdD+P8tQhvdlNU1F4gQc1Im1tg9gGJAXnrU+a4nYmR+rclttMkBeHOXcMK4ynlud+dTk0doKv5X2wHCOxFrYzYXnepc7ZqIOZQhl8rYqtLm8W61LIl1u2p5SIwF0l69fyaCCqbUrabiejh10gVAia4atsw+KnnJuDUskPyak4u3GI5D111WSllm55x2CepAQ9tUKlNVmUu3O3D4swRqwbZm5CnSw5h0INLebT3f56Q4puRpyzZSUfGDVBEJ1aNw6aigxnpmIMI/2NZ/DTpqMkwy1zeMajA41VUnnbnjQA7aq6Kdn9Jqo0Cht7bI3pyuoUa61YwSoQItzwkL9ZFZ1i/S00e3TOE0uyiik1PNSLPclhaO6Z+aJbCZ2wrRoN9zP/3JpGs3H2dl4vjR0vFrs22XLSNmA7EXfI3L7aSTySrbm24y65Wsm24cXTbiXH1oLH6D0tF1VhV4BP3ZKZU8zuvNpodcz4AXFyLsWZG9Pc4cSrdtydxe1ausLNxUKM22JoFnSQXGU6564BHe6L+poqTHegMvFCOyJBBIZgpXy3nblNcT7AmlabbRCBKqW2eWKCVvHsGxc3WdThQtsRvsnSeiSP5/Ro9ShOkPSFj9wN7S8pLadkXEzodk2tT9bmaq790TcspDntL4pW7+sVzMXRee2irFsI/Wm/iU/DuVvNc3g+8Hq35limWGf9AtPbmbmud+6cnt28GRW4Fpqxdn1LWf96cbVwA8BcQDt4jpSJmTQhLkSizhrCtp1hxIDEc+PIL3kcEWhst0XR9hLYO9yhslLDTTba60vYxq8a4ampcev0i7EUCqqhNkUT9Lqp0HuTsipbjbY75EKveiwYaUfuzdW6ZdGdnAjVuk9Ep1tvUFI+NgmSZjsNZeiMOpP4fBaYt1VwNKVstd7keb/bhFp9pG3FOh2Q1a2RKedElGlIbdQImRknRUqkMaOZ4sBJPTaaZDJnRoCV2wBgJCujcn7sRqZw0NvtuglSszgeYHotWnSx3nXzdL1eFBJPrhtSjUcTNc88rdA14cvDslCY7BxtUpnYLDrizIxrNua8y0JY7OrkfDqNi+0Aeu9jehv46FTzMD+fO8wB9to+u+W7MF/gp55pTMlH1/ZCUj2xEYcuPO02ApVsWGrlM/Ch4eXoKDggnofDSrXiAi8uu3ZAE1azi+s4yre11Pd7bVbBYOdy3pACtkdV2ubsseJQNeLzQRAXAFOtKNpd6nw/xhxSV/OVBfO8IPSsskQSIVPqDRFaGa+drlYbSbVAzmyWzo1W6Hb9OfF64RoHqsxx/vV60AO9jeXbbhW2apyollA0gLZSkhDxai34twomRnXsNfQ2v8FuZ0nXYN4L2+2Qmw5Py9a8ME4qDbrcazRnpBgfVDb0jbyQRcFQRe6UX/gEQHqeRLtgJWzT7c04pYllVXOGx8jjKndJiTtksLGMlkIJTNC2wHOgXS7EOj3I1Gm5c449j8eos74cBoeYhecFr14yL0BFLUxNp+OwE7wqsLITwnOwkw8kIi/DW3bAmVsXnbizOcpZdxHJ3aJZktuYa2l53VLD/tLDlY2112CXHxA6IMosuQTuuBq5wfRxHJ7bXYgsfGNe0hLOHihcYZpVkRYbHUOZNaLvVb07aj3FX6RFxjFUOGiKhp0Su4DXkbj2c9bx92K04rzVKCqZUa1p+DCW8nlPaLyMwNJ+bRbVMqevJ29rUt31UMQqIc/sbnUz+MNVL5SowgHXDLi4yw7dLlN2lUrtDl0N64UkzFjx1lmGO/dZHpC6e4vsnR55lesWPpafQVcro1VZDNxBY3jUL2FBKzzLvJ0Gq4+uQzvbnVMkMzt56wq2ZR/YETbm8NY/EFfcubkajG8cm6xjh4gxE65kJqSwTe9R8diwdU0wY1LOMjE90DF3c2A9GI+386koGCFVUH0vzOhuSZNjRbBlUZ9m1wOVjBLiHiS+2K5OyA7hSdhNmcwJ2BPvieAq0uW9x+MkFvMY4sCrrheFdHGc9QuCApDinYracsKI2tRlr3N7widylMaiUyR15ni0JdTKlhusjNkLGpFWEFWShVE1grRbOvdUz5vFhtdxRJXv06K1SgLmW54YHETF0LYsGEBzhH7CD5SfL9drTBO2DDG3xbUYUqLYK3pS1eQhclWGRUmvQsc02a0j1hx6sGnZLrZxKnYWI8sHYpOKfdRul5LgZjJscHS62GcyITc+hYmJZZKbIycdheUxakXOG0SAO+dFaBgec93IjuUv163bJaTtuoTfqu3Bm7mGSyvpZYCbnRKlqIRddcsO5TObVoa20lU8YgkqVqyaOeoSfqF7Am/2dTD3KtLg4OUtgtGzG87g2jM7fadRORyhKyNeCRTHoVh3jdqGqGY5bgpbr740KF35fsBtUGPg+oowBxLduDfMdaSF7Etys9czC+DWpoF79sTIXlgox7myafq9U8Yit282qmjsKKY8xWcfpD5LRi7pHlyW3saSguXXKklWl3yoMraBGTkTyIPqR8su5+hBRqqD7fgax7v6JpW8dWB7+nG54Fb1YXTXdNEXu+Ws3MHyNlqIHcXAOZsftE6CmyXaCweykteMuJmvLj7oKtk9yCJSDonhxs3QJQ275aUfjGaGnru4ZuyuHMIaReoeM6+WuGnWuJcVjBQ6qdtdtppTZQlTLVx28I9NrVcRtm2OvYUTbGYgdlmPVu1v9oXaq7VLsS6O0JLFgd0mwnpR0QkGZjMp4OLZbFT7CEvCKlNTujEZzJIO6CiizNGHqQETyjQz3RqvN/FCx+dDc4zCJbbdI4Yis6nirzfLmbZfbfMtFuciizMLdktpYkAiqmhF3cleGWfqvIdTJyCVE5UbFkxLdoNhDGNvsajB4Jhj3a3cwNa+xDKFKmi5XQYYCnvEUXFPdGtV3Z4blRht0SQy0uLEykRup56r1tESqZWj1IzmzPPb2SipVJhRPSYaFaERY6VH/QZLNorPXsNbzfmZIRPXre9SZkRF0paVotYX0P0ybPtGZ3KGPzblbRE4HsGc1xTXw+sMENs21TBvVTtpqRblCaXnmxt17MAeYIx8GufqzKfZk75f2byIqUxKpEy+wg2y9a7+vPYsqz1qju3C20W9YQlmoSpORDT707oZ44W3YewYkWAAYB3pM6a9Oa1o+5r6/AizwkooZru6WyPKMRjjlV7AG9agwpzS5JS9yRd/rzh+xl27kke6Ok9n8sxY20lma+QWprjSHedz9Lpz97OjhjUbmA2y5faMEuyNJ20Sb+wqbqPK7S+bK5nTZgQPR9moqxnS8s7YNFda1xnUJpicOpxSpuC5XXHUcc3ZVYzNC56Y27E+KpSoe14ZG8GIzzm8UfYGIwUEyYzLCvOiUjjQ9Mvnl+mg+nnc/F994zwd+v0/O3t8HBO+v5S6Hza7pvPlvtaX/7KGP39+Ke0Q6Pc4fa2Sxn8eTv7D2evrX3yzMQkbHq94pzdrff1+hF+b/vSXTC9h5jRg8PCtypPmfhj8+eVD0eeh98vd5LSov91ft4PLvA7ccorOP9j6Mv2tw/S+yHVCsP7z0n+eTn9+cZ4vS79NjnLLYjL8+bJkOsWd3pa8/Pa/AN8QEyZCJgAA -->
