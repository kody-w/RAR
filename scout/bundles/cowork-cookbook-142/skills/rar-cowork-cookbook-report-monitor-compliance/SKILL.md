---
name: "rar-cowork-cookbook-report-monitor-compliance"
description: "Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_compliance", "rar_sha256": "4fd1ba02ab7122079038bfedcaf4bef3d6f340db93ae34d42519366adb6d43af", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_compliance`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_compliance_agent.py` and in the RCI capsule.

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

Monitor compliance Summary Report — Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-compliance
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 4fd1ba02ab712207…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_compliance_agent.py` first:

```bash
python3 report_monitor_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_compliance_agent.py   # or on stdin
python3 report_monitor_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor compliance Summary Report — Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_compliance',
    "version": '2.0.0',
    "display_name": 'Monitor compliance Summary Report',
    "description": 'Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-monitor-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '865a7b11b998fe8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/monitor-compliance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-monitor-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportMonitorCompliance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportMonitorCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
