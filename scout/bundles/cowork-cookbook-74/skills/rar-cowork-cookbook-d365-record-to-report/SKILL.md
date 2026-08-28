---
name: "rar-cowork-cookbook-d365-record-to-report"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Record to report end-to-end process - covers 6 L2 areas and 49 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report", "rar_sha256": "548441a5b5059922b432e45aed4fe9e9131700856c7d9627e35c572bcc691f85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_record_to_report`. The original RAPP
agent is preserved byte-for-byte in `d365_record_to_report_agent.py` and in the RCI capsule.

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
