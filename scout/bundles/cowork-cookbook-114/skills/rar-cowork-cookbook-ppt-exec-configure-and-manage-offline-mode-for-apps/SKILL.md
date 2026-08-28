---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-offline-mode-for-apps"
description: "Generates an executive-ready PowerPoint deck on configure and manage offline mode for apps status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps", "rar_sha256": "bbef857f55d4a8497ff41fd7459c51f8f2283dfbd5ed382d9e4afac2279ee009", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` and in the RCI capsule.

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

Configure and manage offline mode for apps Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage offline mode for apps status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-offline-mode-for-apps
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` and embedded as the fenced Python below (sha256 bbef857f55d4a849…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage offline mode for apps Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage offline mode for apps status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-offline-mode-for-apps
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps',
    "version": '2.0.1',
    "display_name": 'Configure and manage offline mode for apps Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on configure and manage offline mode for apps status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-configure-and-manage-offline-mode-for-apps',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-offline-mode-for-apps',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '99d443d7f86fa8a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-offline-mode-for-apps'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-offline-mode-for-apps', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecConfigureAndManageOfflineModeForApps(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageOfflineModeForApps'
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
    print(PptExecConfigureAndManageOfflineModeForApps().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
