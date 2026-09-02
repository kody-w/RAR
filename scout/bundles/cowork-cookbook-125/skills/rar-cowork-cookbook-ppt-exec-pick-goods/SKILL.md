---
name: "rar-cowork-cookbook-ppt-exec-pick-goods"
description: "Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pick_goods", "rar_sha256": "9db7c2224f880d0fd74740a5b3722678515c3b042133b6abf8ab20a66ef5110d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_pick_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-pick-goods:ca869ab72b1e03c3f0f2094d5b80b0a982e2f3d8e14e7230278a697430a4fb43", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_pick_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_pick_goods_agent.py` is
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

Pick goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pick-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pick_goods_agent.py` and embedded as the fenced Python below (sha256 9db7c2224f880d0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pick_goods_agent.py` first:

```bash
python3 ppt_exec_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_pick_goods_agent.py   # or on stdin
python3 ppt_exec_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_pick_goods',
    "version": '2.0.0',
    "display_name": 'Pick goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed2b35a31ac857e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPickGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPickGoods'
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
    print(PptExecPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
