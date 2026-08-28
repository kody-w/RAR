---
name: "rar-cowork-cookbook-dashboard-establish-banking-relationships"
description: "Produces a self-contained interactive HTML dashboard for establish banking relationships - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_banking_relationships", "rar_sha256": "5e9bca325c8a48c27a6d25bf95a238522b36e413c2f0811eb7e190ff8e9be34b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_establish_banking_relationships`. The original RAPP
agent is preserved byte-for-byte in `dashboard_establish_banking_relationships_agent.py` and in the RCI capsule.

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

Establish banking relationships Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for establish banking relationships - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 5e9bca325c8a48c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_banking_relationships_agent.py` first:

```bash
python3 dashboard_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_establish_banking_relationships_agent.py   # or on stdin
python3 dashboard_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for establish banking relationships - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_establish_banking_relationships',
    "version": '2.0.1',
    "display_name": 'Establish banking relationships Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for establish banking relationships - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06c64c14ca6ea5d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardEstablishBankingRelationships(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEstablishBankingRelationships'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(DashboardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
