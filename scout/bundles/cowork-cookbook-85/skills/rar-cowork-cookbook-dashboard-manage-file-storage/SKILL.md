---
name: "rar-cowork-cookbook-dashboard-manage-file-storage"
description: "Produces a self-contained interactive HTML dashboard for manage file storage - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_file_storage", "rar_sha256": "8fd433d773e4cdf6dbd894d291d5909d610ddb5ae677cc12642468f14910dda2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 8fd433d773e4cdf6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_file_storage_agent.py` first:

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
    "version": '2.0.1',
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
