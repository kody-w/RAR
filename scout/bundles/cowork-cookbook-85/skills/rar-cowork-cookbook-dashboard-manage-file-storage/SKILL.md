---
name: "rar-cowork-cookbook-dashboard-manage-file-storage"
description: "Produces a self-contained interactive HTML dashboard for manage file storage - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_file_storage", "rar_sha256": "0d500657c54764d0701f667ba6055927547991740eb160900263b03404248741", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_file_storage_agent.py` and in the RCI capsule.

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
