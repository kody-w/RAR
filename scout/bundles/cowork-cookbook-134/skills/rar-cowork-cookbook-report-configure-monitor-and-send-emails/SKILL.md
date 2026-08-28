---
name: "rar-cowork-cookbook-report-configure-monitor-and-send-emails"
description: "Builds a structured summary report of configure, monitor, and send emails activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_monitor_and_send_emails", "rar_sha256": "d17b1ff281462d18e5d60cdc8f2d5b90fdd235665cc040c28282330127cfcd9a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_monitor_and_send_emails`. The original RAPP
agent is preserved byte-for-byte in `report_configure_monitor_and_send_emails_agent.py` and in the RCI capsule.

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
