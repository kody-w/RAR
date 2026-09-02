---
name: "rar-cowork-cookbook-report-renew-software-licenses"
description: "Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_renew_software_licenses", "rar_sha256": "ccaed08910fb69c86bb9741767eb705dc0f82460a2fbe96dd37c8b8a40752017", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_renew_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-renew-software-licenses:e18e50bd449808ac94eb566bb885e98f6d1ada2f10fd9184dd21424837e7b288", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_renew_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_renew_software_licenses_agent.py` is
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

Renew software licenses Summary Report — Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-renew-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 ccaed08910fb69c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_renew_software_licenses_agent.py` first:

```bash
python3 report_renew_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_renew_software_licenses_agent.py   # or on stdin
python3 report_renew_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Renew software licenses Summary Report — Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-renew-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_renew_software_licenses',
    "version": '2.0.0',
    "display_name": 'Renew software licenses Summary Report',
    "description": 'Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-renew-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-renew-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdec36c9821cf7fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/renew-software-licenses'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-renew-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRenewSoftwareLicenses(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRenewSoftwareLicenses'
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
    print(ReportRenewSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
