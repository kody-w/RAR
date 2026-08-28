---
name: "rar-cowork-cookbook-report-identify-background-jobs"
description: "Builds a structured summary report of identify background jobs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_background_jobs", "rar_sha256": "1a0b2b2fa4c9cd51416ebc5f91826e659809abb833031d355f4a076500cce757", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 1a0b2b2fa4c9cd51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
