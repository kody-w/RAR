---
name: "rar-cowork-cookbook-report-prioritize-notifications"
description: "Builds a structured summary report of prioritize notifications activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prioritize_notifications", "rar_sha256": "bf25815f86c2422c0582df138d488a64482d3499f95411b1551649653dd0d67a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 bf25815f86c2422c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_prioritize_notifications_agent.py` first:

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
    "version": '2.0.0',
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
