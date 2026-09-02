---
name: "rar-cowork-cookbook-dashboard-manage-file-storage"
description: "Produces a self-contained interactive HTML dashboard for manage file storage - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_file_storage", "rar_sha256": "0d500657c54764d0701f667ba6055927547991740eb160900263b03404248741", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_file_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-file-storage:b897ae08aea09b9b7aceb404612e35dcbc08e206f34496bd25458a2da4907034", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_file_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_file_storage_agent.py` is
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

Manage file storage Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage file storage - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-file-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 0d500657c54764d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_file_storage_agent.py` first:

```bash
python3 dashboard_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_file_storage_agent.py   # or on stdin
python3 dashboard_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage file storage Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage file storage - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_file_storage',
    "version": '2.0.0',
    "display_name": 'Manage file storage Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage file storage - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1851d7fa7c310d38',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-file-storage'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageFileStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageFileStorage'
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
    print(DashboardManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
