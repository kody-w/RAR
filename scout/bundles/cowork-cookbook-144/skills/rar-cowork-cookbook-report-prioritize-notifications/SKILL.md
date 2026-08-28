---
name: "rar-cowork-cookbook-report-prioritize-notifications"
description: "Builds a structured summary report of prioritize notifications activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prioritize_notifications", "rar_sha256": "d49b96a24aca2d7a5bf8638bf16a2cf85530d8cc2dd67f6373b331af28549c25", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_prioritize_notifications`. The original RAPP
agent is preserved byte-for-byte in `report_prioritize_notifications_agent.py` and in the RCI capsule.

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

Prioritize notifications Summary Report — Builds a structured summary report of prioritize notifications activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-prioritize-notifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 d49b96a24aca2d7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_prioritize_notifications_agent.py` first:

```bash
python3 report_prioritize_notifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_prioritize_notifications_agent.py   # or on stdin
python3 report_prioritize_notifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prioritize notifications Summary Report — Builds a structured summary report of prioritize notifications activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-prioritize-notifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_prioritize_notifications',
    "version": '2.0.1',
    "display_name": 'Prioritize notifications Summary Report',
    "description": 'Builds a structured summary report of prioritize notifications activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-prioritize-notifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-prioritize-notifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bde0ae864da8ced8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/prioritize-notifications'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-prioritize-notifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPrioritizeNotifications(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPrioritizeNotifications'
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
    print(ReportPrioritizeNotifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
