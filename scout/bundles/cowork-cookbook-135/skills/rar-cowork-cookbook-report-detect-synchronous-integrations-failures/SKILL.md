---
name: "rar-cowork-cookbook-report-detect-synchronous-integrations-failures"
description: "Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_detect_synchronous_integrations_failures", "rar_sha256": "b3ac1bd5846d20a48b233bcdb048895f9734f295f9ef4a21d570444a7049ce1d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_detect_synchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `report_detect_synchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect synchronous integrations failures Summary Report — Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 b3ac1bd5846d20a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_detect_synchronous_integrations_failures_agent.py` first:

```bash
python3 report_detect_synchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_detect_synchronous_integrations_failures_agent.py   # or on stdin
python3 report_detect_synchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect synchronous integrations failures Summary Report — Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_detect_synchronous_integrations_failures',
    "version": '2.0.0',
    "display_name": 'Detect synchronous integrations failures Summary Report',
    "description": 'Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-detect-synchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93276d22e7a4ab66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-synchronous-integrations-failures'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-detect-synchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDetectSynchronousIntegrationsFailures(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDetectSynchronousIntegrationsFailures'
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
    print(ReportDetectSynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
