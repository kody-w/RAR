---
name: "rar-cowork-cookbook-workforce-headcount-report"
description: "Builds a headcount report by department, location, and worker type for the current period."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/workforce_headcount_report", "rar_sha256": "543cba672c1440abcde6a4f9ab2be85d7133eb1439866f08dc8e1255912c2419", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/workforce_headcount_report`. The original RAPP
agent is preserved byte-for-byte in `workforce_headcount_report_agent.py` and in the RCI capsule.

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

Workforce Headcount Report — Builds a headcount report by department, location, and worker type for the current period.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/workforce-headcount-report
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workforce_headcount_report_agent.py` and embedded as the fenced Python below (sha256 543cba672c1440ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workforce_headcount_report_agent.py` first:

```bash
python3 workforce_headcount_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 workforce_headcount_report_agent.py   # or on stdin
python3 workforce_headcount_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Workforce Headcount Report — Builds a headcount report by department, location, and worker type for the current period.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/workforce-headcount-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/workforce_headcount_report',
    "version": '2.0.1',
    "display_name": 'Workforce Headcount Report',
    "description": 'Builds a headcount report by department, location, and worker type for the current period.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'workforce-headcount-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/workforce-headcount-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '208d7a75d7b4f12b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/workforce-headcount-report', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'verified'},
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


class WorkforceHeadcountReport(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkforceHeadcountReport'
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
    print(WorkforceHeadcountReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
