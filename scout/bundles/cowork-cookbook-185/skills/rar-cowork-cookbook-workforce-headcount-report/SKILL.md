---
name: "rar-cowork-cookbook-workforce-headcount-report"
description: "Builds a headcount report by department, location, and worker type for the current period."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/workforce_headcount_report", "rar_sha256": "6bbec9cfc5c3d27f5aceecb3d0519217f4ac491024db1147940da486949d8c0d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "workforce_headcount_report_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/workforce-headcount-report:d98fa64a78cfebe9edf0ed451912d5edc6a6428e4982aeba82d814b3b606380d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/workforce_headcount_report`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `workforce_headcount_report_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workforce_headcount_report_agent.py` and embedded as the fenced Python below (sha256 6bbec9cfc5c3d27f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workforce_headcount_report_agent.py` first:

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
    "version": '2.0.0',
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
