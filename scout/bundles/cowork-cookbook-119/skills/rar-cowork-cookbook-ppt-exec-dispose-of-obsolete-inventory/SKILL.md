---
name: "rar-cowork-cookbook-ppt-exec-dispose-of-obsolete-inventory"
description: "Generates an executive-ready PowerPoint deck on dispose of obsolete inventory status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory", "rar_sha256": "55049f53e62553a3cf5f30734b220d09d43ed8915af41c82c21b10a1887bd8a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_dispose_of_obsolete_inventory_agent.py` and in the RCI capsule.

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
