---
name: "rar-cowork-cookbook-report-configure-monitor-and-send-emails"
description: "Builds a structured summary report of configure, monitor, and send emails activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_monitor_and_send_emails", "rar_sha256": "e14fbe3bad8e7a50c96a01d6b309bc61cd2f877fcc544ab248928a1066d5e760", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_monitor_and_send_emails_agent.py` and embedded as the fenced Python below (sha256 e14fbe3bad8e7a50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_monitor_and_send_emails_agent.py` first:

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
    "version": '2.0.1',
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
