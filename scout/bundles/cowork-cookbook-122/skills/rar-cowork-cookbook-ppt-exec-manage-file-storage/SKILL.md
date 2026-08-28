---
name: "rar-cowork-cookbook-ppt-exec-manage-file-storage"
description: "Generates an executive-ready PowerPoint deck on manage file storage status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_file_storage", "rar_sha256": "49f06bd792bb9110fec6df9792b6f9d4ca13b0f64db212ef8cc6ac72208e02ce", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_file_storage_agent.py` and in the RCI capsule.

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

Manage file storage Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage file storage status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-file-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 49f06bd792bb9110…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_file_storage_agent.py` first:

```bash
python3 ppt_exec_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_file_storage_agent.py   # or on stdin
python3 ppt_exec_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage file storage Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage file storage status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_file_storage',
    "version": '2.0.1',
    "display_name": 'Manage file storage Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage file storage status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b897b219bccfb9b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-file-storage'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageFileStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageFileStorage'
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
    print(PptExecManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
