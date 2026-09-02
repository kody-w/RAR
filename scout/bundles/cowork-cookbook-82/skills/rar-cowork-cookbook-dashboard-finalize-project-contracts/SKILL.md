---
name: "rar-cowork-cookbook-dashboard-finalize-project-contracts"
description: "Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_finalize_project_contracts", "rar_sha256": "e8998828ada5baad255acc6e7f9a7c6cf3f1221c46d8a059d0bf3ff960667a6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_finalize_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-finalize-project-contracts:78c4ac48cfad07d7477ee728ee76c5dba3d31a3087c1af04c808ca7ecfab99fa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_finalize_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_finalize_project_contracts_agent.py` is
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

Finalize project contracts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 e8998828ada5baad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_finalize_project_contracts_agent.py` first:

```bash
python3 dashboard_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_finalize_project_contracts_agent.py   # or on stdin
python3 dashboard_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_finalize_project_contracts',
    "version": '2.0.0',
    "display_name": 'Finalize project contracts Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4dbeaffd4a1eff25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardFinalizeProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardFinalizeProjectContracts'
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
    print(DashboardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
