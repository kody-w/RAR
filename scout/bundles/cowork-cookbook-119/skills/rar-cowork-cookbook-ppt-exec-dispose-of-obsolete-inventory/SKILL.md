---
name: "rar-cowork-cookbook-ppt-exec-dispose-of-obsolete-inventory"
description: "Generates an executive-ready PowerPoint deck on dispose of obsolete inventory status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory", "rar_sha256": "19567a223be6c7baf396b82fe33497d5333972b82daf3593fbc832c34d380338", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_dispose_of_obsolete_inventory_agent.py` and embedded as the fenced Python below (sha256 19567a223be6c7ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_dispose_of_obsolete_inventory_agent.py` first:

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
    "version": '2.0.1',
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
