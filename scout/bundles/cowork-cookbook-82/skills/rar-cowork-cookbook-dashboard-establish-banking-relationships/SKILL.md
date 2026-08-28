---
name: "rar-cowork-cookbook-dashboard-establish-banking-relationships"
description: "Produces a self-contained interactive HTML dashboard for establish banking relationships - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_banking_relationships", "rar_sha256": "cce0ea496fcc6f22f0fec574cd3b9536b6b709a3904f9816e4a02e571a6a7eee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 cce0ea496fcc6f22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_banking_relationships_agent.py` first:

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
    "version": '2.0.0',
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
