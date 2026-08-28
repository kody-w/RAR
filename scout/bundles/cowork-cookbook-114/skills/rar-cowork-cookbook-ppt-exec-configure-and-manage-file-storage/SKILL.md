---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-file-storage"
description: "Generates an executive-ready PowerPoint deck on configure and manage file storage status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_file_storage", "rar_sha256": "5425b44185829755361b7dd445f830ddb2e108dff002ca6039d450e2834f5380", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_file_storage_agent.py` and in the RCI capsule.

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

Configure and manage file storage Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage file storage status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-file-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 5425b44185829755…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_file_storage_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_file_storage_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage file storage Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage file storage status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_file_storage',
    "version": '2.0.1',
    "display_name": 'Configure and manage file storage Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on configure and manage file storage status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58c35316401285d4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/configure-and-manage-file-storage'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConfigureAndManageFileStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageFileStorage'
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
    print(PptExecConfigureAndManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
