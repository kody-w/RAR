---
name: "rar-cowork-cookbook-ppt-exec-manage-file-storage"
description: "Generates an executive-ready PowerPoint deck on manage file storage status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_file_storage", "rar_sha256": "d07e4af7d7b3c4c5fcbce9583f31cd91fd9b35b60bf5fe47591aefad678adf88", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_file_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-file-storage:eb3a2aa0e90206b97cf0304df16e79a88636d7d92cbe47957afde52c48e1b5bc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_file_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_file_storage_agent.py` is
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
