---
name: "rar-cowork-cookbook-report-identify-background-jobs"
description: "Builds a structured summary report of identify background jobs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_background_jobs", "rar_sha256": "c43d598332189ddc8744e31a380bb55abc07689f89188205418b5443c45ec40d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_identify_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-identify-background-jobs:27683e440082005d00dec1743c3a32b3c7a692f429c157b62c131e42d9b01028", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_identify_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_identify_background_jobs_agent.py` is
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
