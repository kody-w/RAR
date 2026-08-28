---
name: "rar-cowork-cookbook-blueprint-period-close-readiness"
description: "Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close \u2014 unposted work, subledger-to-GL differences, and FX exposure."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_period_close_readiness", "rar_sha256": "47724f88cfdbdf0210848faafe49975d7c48dcac79f357f60d9cd53ac71b7a61", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "record_to_report", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_period_close_readiness`. The original RAPP
agent is preserved byte-for-byte in `blueprint_period_close_readiness_agent.py` and in the RCI capsule.

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

Period Close Readiness Blueprint — Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close — unposted work, subledger-to-GL differences, and FX exposure.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-period-close-readiness
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
      "type": "string"
    },
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_period_close_readiness_agent.py` and embedded as the fenced Python below (sha256 47724f88cfdbdf02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_period_close_readiness_agent.py` first:

```bash
python3 blueprint_period_close_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_period_close_readiness_agent.py   # or on stdin
python3 blueprint_period_close_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Period Close Readiness Blueprint — Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close — unposted work, subledger-to-GL differences, and FX exposure.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-period-close-readiness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_period_close_readiness',
    "version": '2.0.0',
    "display_name": 'Period Close Readiness Blueprint',
    "description": 'Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close — unposted work, subledger-to-GL differences, and FX exposure.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'record_to_report', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-period-close-readiness',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-period-close-readiness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '667474295c4ede3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods', 'record-to-report/record-financial-transactions'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'record-to-report/blueprint-period-close-readiness', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.529, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintPeriodCloseReadiness(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintPeriodCloseReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BlueprintPeriodCloseReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
