---
name: "rar-cowork-cookbook-ppt-exec-dispose-of-obsolete-inventory"
description: "Generates an executive-ready PowerPoint deck on dispose of obsolete inventory status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory", "rar_sha256": "55049f53e62553a3cf5f30734b220d09d43ed8915af41c82c21b10a1887bd8a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_dispose_of_obsolete_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-dispose-of-obsolete-inventory:de507a6f61bea79ce7ba9f2eac0712af7684d0b1613ecbd5cdd3e669e6dd7a3b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_dispose_of_obsolete_inventory_agent.py` is
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

Dispose of obsolete inventory Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on dispose of obsolete inventory status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-dispose-of-obsolete-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_dispose_of_obsolete_inventory_agent.py` and embedded as the fenced Python below (sha256 55049f53e62553a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_dispose_of_obsolete_inventory_agent.py` first:

```bash
python3 ppt_exec_dispose_of_obsolete_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_dispose_of_obsolete_inventory_agent.py   # or on stdin
python3 ppt_exec_dispose_of_obsolete_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispose of obsolete inventory Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on dispose of obsolete inventory status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-dispose-of-obsolete-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory',
    "version": '2.0.0',
    "display_name": 'Dispose of obsolete inventory Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on dispose of obsolete inventory status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-dispose-of-obsolete-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-dispose-of-obsolete-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4030eb51e9106e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/dispose-of-obsolete-inventory'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-dispose-of-obsolete-inventory', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDisposeOfObsoleteInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDisposeOfObsoleteInventory'
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
    print(PptExecDisposeOfObsoleteInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
