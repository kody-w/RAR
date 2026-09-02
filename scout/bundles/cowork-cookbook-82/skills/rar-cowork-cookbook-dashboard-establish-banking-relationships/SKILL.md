---
name: "rar-cowork-cookbook-dashboard-establish-banking-relationships"
description: "Produces a self-contained interactive HTML dashboard for establish banking relationships - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_banking_relationships", "rar_sha256": "cce0ea496fcc6f22f0fec574cd3b9536b6b709a3904f9816e4a02e571a6a7eee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_establish_banking_relationships_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-establish-banking-relationships:223e0ba82e38b45b1165b9171c5ec2deb8d0b2e0ae02ed010da9943adead34c3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_establish_banking_relationships`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_establish_banking_relationships_agent.py` is
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
