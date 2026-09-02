---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-offline-mode-for-apps"
description: "Generates an executive-ready PowerPoint deck on configure and manage offline mode for apps status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps", "rar_sha256": "35a70084c1263029e7dc4dfe993a4182bdd7f6f6106af2e38e1305190240d916", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-configure-and-manage-offline-mode-for-apps:757fba429c1ed248fcad4e7b1503e7b8a378b2a99d127c72bd5771295e8cf266", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` is
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
