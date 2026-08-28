---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-offline-mode-for-apps"
description: "Generates an executive-ready PowerPoint deck on configure and manage offline mode for apps status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps", "rar_sha256": "35a70084c1263029e7dc4dfe993a4182bdd7f6f6106af2e38e1305190240d916", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` and embedded as the fenced Python below (sha256 35a70084c1263029…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` first:

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
    "version": '2.0.0',
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
