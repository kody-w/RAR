---
name: "rar-cowork-cookbook-ppt-exec-manage-file-storage"
description: "Generates an executive-ready PowerPoint deck on manage file storage status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_file_storage", "rar_sha256": "d07e4af7d7b3c4c5fcbce9583f31cd91fd9b35b60bf5fe47591aefad678adf88", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 d07e4af7d7b3c4c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_file_storage_agent.py` first:

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
    "version": '2.0.0',
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
