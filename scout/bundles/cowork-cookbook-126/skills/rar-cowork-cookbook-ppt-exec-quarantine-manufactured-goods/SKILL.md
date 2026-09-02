---
name: "rar-cowork-cookbook-ppt-exec-quarantine-manufactured-goods"
description: "Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_quarantine_manufactured_goods", "rar_sha256": "a34a42d27a5acd9f03a7d9cdfc10ca89a124d9d7b65399e94993ed67f973da16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_quarantine_manufactured_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-quarantine-manufactured-goods:f185658ae0f0b9a42904caa9b75eedeb93aee42d964a6d268eb1e394a3edc256", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_quarantine_manufactured_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_quarantine_manufactured_goods_agent.py` is
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

Quarantine manufactured goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 a34a42d27a5acd9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_quarantine_manufactured_goods_agent.py` first:

```bash
python3 ppt_exec_quarantine_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_quarantine_manufactured_goods_agent.py   # or on stdin
python3 ppt_exec_quarantine_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine manufactured goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_quarantine_manufactured_goods',
    "version": '2.0.0',
    "display_name": 'Quarantine manufactured goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-quarantine-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37479011b49685be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/quarantine-manufactured-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-quarantine-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecQuarantineManufacturedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecQuarantineManufacturedGoods'
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
    print(PptExecQuarantineManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
