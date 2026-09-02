---
name: "rar-cowork-cookbook-dashboard-manage-compensation-changes"
description: "Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_compensation_changes", "rar_sha256": "be782da82742ab7bc94402456db057f8e41f74443489b0dd94f918bb205b8421", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_compensation_changes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-compensation-changes:0343db8402892a5385cb655437973366d6870bde2600d8c8c6d4ae158995a9a3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_compensation_changes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_compensation_changes_agent.py` is
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

Manage compensation changes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 be782da82742ab7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_compensation_changes_agent.py` first:

```bash
python3 dashboard_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_compensation_changes_agent.py   # or on stdin
python3 dashboard_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_compensation_changes',
    "version": '2.0.0',
    "display_name": 'Manage compensation changes Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a4d07e15229c459',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageCompensationChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageCompensationChanges'
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
    print(DashboardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
