---
name: "rar-cowork-cookbook-d365-record-to-report"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Record to report end-to-end process - covers 6 L2 areas and 49 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report", "rar_sha256": "20e2d17e3d55702aa65502a78b59b4121458869df475961c746b854fdbdaa0a4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_record_to_report_agent.py` and embedded as the fenced Python below (sha256 20e2d17e3d55702a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_record_to_report_agent.py` first:

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
    "version": '2.0.1',
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
