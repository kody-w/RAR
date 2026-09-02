---
name: "rar-cowork-cookbook-report-prioritize-notifications"
description: "Builds a structured summary report of prioritize notifications activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prioritize_notifications", "rar_sha256": "bf25815f86c2422c0582df138d488a64482d3499f95411b1551649653dd0d67a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_prioritize_notifications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-prioritize-notifications:caab19513df59574f772682308242dde8cc28eb58a64e7a52537e2afc1a3e257", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_prioritize_notifications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_prioritize_notifications_agent.py` is
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
