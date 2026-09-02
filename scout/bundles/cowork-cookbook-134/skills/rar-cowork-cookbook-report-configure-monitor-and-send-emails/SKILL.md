---
name: "rar-cowork-cookbook-report-configure-monitor-and-send-emails"
description: "Builds a structured summary report of configure, monitor, and send emails activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_monitor_and_send_emails", "rar_sha256": "d17b1ff281462d18e5d60cdc8f2d5b90fdd235665cc040c28282330127cfcd9a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_configure_monitor_and_send_emails_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-configure-monitor-and-send-emails:4c536f8bb6a328e537d6af02dc7c36e19d7cc9176c445dd53d7680832feb0480", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_configure_monitor_and_send_emails`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_configure_monitor_and_send_emails_agent.py` is
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

Configure, monitor, and send emails Summary Report — Builds a structured summary report of configure, monitor, and send emails activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-monitor-and-send-emails
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_monitor_and_send_emails_agent.py` and embedded as the fenced Python below (sha256 d17b1ff281462d18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_monitor_and_send_emails_agent.py` first:

```bash
python3 report_configure_monitor_and_send_emails_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_monitor_and_send_emails_agent.py   # or on stdin
python3 report_configure_monitor_and_send_emails_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure, monitor, and send emails Summary Report — Builds a structured summary report of configure, monitor, and send emails activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-monitor-and-send-emails
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_monitor_and_send_emails',
    "version": '2.0.0',
    "display_name": 'Configure, monitor, and send emails Summary Report',
    "description": 'Builds a structured summary report of configure, monitor, and send emails activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-configure-monitor-and-send-emails',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-monitor-and-send-emails',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc9aafb36d67f1c6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-monitor-and-send-emails'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-monitor-and-send-emails', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConfigureMonitorAndSendEmails(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureMonitorAndSendEmails'
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
    print(ReportConfigureMonitorAndSendEmails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
