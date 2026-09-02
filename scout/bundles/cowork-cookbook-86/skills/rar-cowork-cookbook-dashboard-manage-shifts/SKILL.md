---
name: "rar-cowork-cookbook-dashboard-manage-shifts"
description: "Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_shifts", "rar_sha256": "4905a0020e026dcbe4f24a42d96a9c402999ed9dfc9e58522134f6414728c580", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_shifts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-shifts:3011005808a5ee7299f2e84b044400f2f5007d618dde129f5bcfaf70a5963c73", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_shifts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_shifts_agent.py` is
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

Manage shifts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-shifts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 4905a0020e026dcb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_shifts_agent.py` first:

```bash
python3 dashboard_manage_shifts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_shifts_agent.py   # or on stdin
python3 dashboard_manage_shifts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage shifts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-shifts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_shifts',
    "version": '2.0.0',
    "display_name": 'Manage shifts Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-manage-shifts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-shifts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4f4f36d4a6b2d74',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-shifts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-shifts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageShifts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageShifts'
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
    print(DashboardManageShifts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
