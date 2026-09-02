---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-file-storage"
description: "Generates an executive-ready PowerPoint deck on configure and manage file storage status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_file_storage", "rar_sha256": "3945dee4813c7a4eb6fcd0554c421eb6895ef70d367e994b2e2d6170b2eb657b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_configure_and_manage_file_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-configure-and-manage-file-storage:718ce7176345fb74827a84ced269095c7812dfc4464aa188aa7eb8bf2e9dedf4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_configure_and_manage_file_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_configure_and_manage_file_storage_agent.py` is
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
