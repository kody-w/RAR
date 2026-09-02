---
name: "rar-cowork-cookbook-ppt-exec-handle-quarantine-goods"
description: "Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_quarantine_goods", "rar_sha256": "e15f9c6193e8a3375002313e7c9dc28b2c42d58a879922cdf26f10ffbcb0d011", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_handle_quarantine_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-handle-quarantine-goods:3383553f07442087ed033f898e9f2a33e50af1b35421d9b0502accbe1d9e8f09", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_handle_quarantine_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_handle_quarantine_goods_agent.py` is
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

Handle quarantine goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 e15f9c6193e8a337…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_quarantine_goods_agent.py` first:

```bash
python3 ppt_exec_handle_quarantine_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_handle_quarantine_goods_agent.py   # or on stdin
python3 ppt_exec_handle_quarantine_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle quarantine goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_handle_quarantine_goods',
    "version": '2.0.0',
    "display_name": 'Handle quarantine goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-handle-quarantine-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7dcaac7889ce705',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/handle-quarantine-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-handle-quarantine-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecHandleQuarantineGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecHandleQuarantineGoods'
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
    print(PptExecHandleQuarantineGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
