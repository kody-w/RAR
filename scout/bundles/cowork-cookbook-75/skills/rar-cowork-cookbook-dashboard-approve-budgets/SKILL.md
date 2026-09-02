---
name: "rar-cowork-cookbook-dashboard-approve-budgets"
description: "Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_approve_budgets", "rar_sha256": "c1f22fc11f2c4a3d45a1dcc921e0eb80f25c858a0d1dc7e465484c67a9e9de5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_approve_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-approve-budgets:d990526a12c9a7232b46a77f3d078babc084ce45455fb4602ead89d4e08c0400", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_approve_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_approve_budgets_agent.py` is
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

Approve budgets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 c1f22fc11f2c4a3d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_approve_budgets_agent.py` first:

```bash
python3 dashboard_approve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_approve_budgets_agent.py   # or on stdin
python3 dashboard_approve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Approve budgets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_approve_budgets',
    "version": '2.0.0',
    "display_name": 'Approve budgets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-approve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-approve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9bb8ba26f7d41ca4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/approve-budgets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-approve-budgets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardApproveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardApproveBudgets'
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
    print(DashboardApproveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
