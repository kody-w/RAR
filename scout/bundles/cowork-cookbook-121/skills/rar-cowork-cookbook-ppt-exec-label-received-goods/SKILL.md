---
name: "rar-cowork-cookbook-ppt-exec-label-received-goods"
description: "Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_label_received_goods", "rar_sha256": "67120746e84670641df0fbe640a0be9ba71067ea7951772ff2733fdfd621796e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_label_received_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-label-received-goods:05286c3c85cf99b6678f126e827490e68df289b133d7ef12e6b48a83620033d0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_label_received_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_label_received_goods_agent.py` is
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

Label received goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 67120746e8467064…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_label_received_goods_agent.py` first:

```bash
python3 ppt_exec_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_label_received_goods_agent.py   # or on stdin
python3 ppt_exec_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_label_received_goods',
    "version": '2.0.0',
    "display_name": 'Label received goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2d2caad3af5620a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecLabelReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecLabelReceivedGoods'
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
    print(PptExecLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
