---
name: "rar-cowork-cookbook-report-manage-data-security"
description: "Builds a structured summary report of manage data security activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_data_security", "rar_sha256": "f7bd1c353fd18ff90776dcd6926188354081d912785fc77bc82c7c638428f885", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_data_security_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-data-security:348281c8e19583c943ce56b9b222320b81d9f2416a852975e602b1b987e1ad53", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_data_security`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_data_security_agent.py` is
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

Manage data security Summary Report — Builds a structured summary report of manage data security activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-data-security
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 f7bd1c353fd18ff9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_data_security_agent.py` first:

```bash
python3 report_manage_data_security_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_data_security_agent.py   # or on stdin
python3 report_manage_data_security_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data security Summary Report — Builds a structured summary report of manage data security activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-data-security
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_data_security',
    "version": '2.0.0',
    "display_name": 'Manage data security Summary Report',
    "description": 'Builds a structured summary report of manage data security activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-data-security',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-data-security',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97cb62000c7814d5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-data-security'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-data-security', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageDataSecurity(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageDataSecurity'
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
    print(ReportManageDataSecurity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
