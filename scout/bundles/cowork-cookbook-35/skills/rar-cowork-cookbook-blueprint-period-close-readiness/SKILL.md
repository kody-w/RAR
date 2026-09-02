---
name: "rar-cowork-cookbook-blueprint-period-close-readiness"
description: "Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close \u2014 unposted work, subledger-to-GL differences, and FX exposure."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_period_close_readiness", "rar_sha256": "47724f88cfdbdf0210848faafe49975d7c48dcac79f357f60d9cd53ac71b7a61", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "blueprint_period_close_readiness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/blueprint-period-close-readiness:f654cd154a195d8dcfc5a941555010632db68fc9cf1583ee2f9adb39e7cd2fde", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "record_to_report", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/blueprint_period_close_readiness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `blueprint_period_close_readiness_agent.py` is
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
