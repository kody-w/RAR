---
name: "rar-cowork-cookbook-report-identify-background-jobs"
description: "Builds a structured summary report of identify background jobs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_background_jobs", "rar_sha256": "c43d598332189ddc8744e31a380bb55abc07689f89188205418b5443c45ec40d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `report_identify_background_jobs_agent.py` and in the RCI capsule.

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

Identify background jobs Summary Report — Builds a structured summary report of identify background jobs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 c43d598332189ddc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_background_jobs_agent.py` first:

```bash
python3 report_identify_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_background_jobs_agent.py   # or on stdin
python3 report_identify_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify background jobs Summary Report — Builds a structured summary report of identify background jobs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_background_jobs',
    "version": '2.0.0',
    "display_name": 'Identify background jobs Summary Report',
    "description": 'Builds a structured summary report of identify background jobs activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-identify-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9621e776f1aacc7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/identify-background-jobs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-identify-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportIdentifyBackgroundJobs(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyBackgroundJobs'
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
    print(ReportIdentifyBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
