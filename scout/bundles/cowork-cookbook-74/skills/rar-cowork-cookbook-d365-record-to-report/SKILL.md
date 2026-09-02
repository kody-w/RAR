---
name: "rar-cowork-cookbook-d365-record-to-report"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Record to report end-to-end process - covers 6 L2 areas and 49 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report", "rar_sha256": "548441a5b5059922b432e45aed4fe9e9131700856c7d9627e35c572bcc691f85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_record_to_report_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-record-to-report:a40f8658e7dd6bd5b6561f376e14e5ebe1d6f798038afecbb0238a0a324993ff", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_record_to_report`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_record_to_report_agent.py` is
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

D365 Record to report Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Record to report end-to-end process - covers 6 L2 areas and 49 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_record_to_report_agent.py` and embedded as the fenced Python below (sha256 548441a5b5059922…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_record_to_report_agent.py` first:

```bash
python3 d365_record_to_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_record_to_report_agent.py   # or on stdin
python3 d365_record_to_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Record to report Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Record to report end-to-end process - covers 6 L2 areas and 49 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_record_to_report',
    "version": '2.0.0',
    "display_name": 'D365 Record to report Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Record to report end-to-end process - covers 6 L2 areas and 49 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-record-to-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-record-to-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '607f773f438fef7e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report'], 'recipe_category': 'report', 'recipe_type': 'prompt+skill', 'upstream_path': 'record-to-report/d365-record-to-report', 'uses_skills': {'custom': ['d365-record-to-report'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365RecordToReport(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecordToReport'
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
    print(D365RecordToReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
