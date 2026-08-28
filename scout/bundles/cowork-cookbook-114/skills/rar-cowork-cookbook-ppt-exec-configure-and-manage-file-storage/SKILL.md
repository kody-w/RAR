---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-file-storage"
description: "Generates an executive-ready PowerPoint deck on configure and manage file storage status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_file_storage", "rar_sha256": "3945dee4813c7a4eb6fcd0554c421eb6895ef70d367e994b2e2d6170b2eb657b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 3945dee4813c7a4e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_file_storage_agent.py` first:

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
    "version": '2.0.0',
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
