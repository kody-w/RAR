---
name: "rar-cowork-cookbook-ppt-exec-define-product-attributes"
description: "Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_attributes", "rar_sha256": "61717a143586ce7e255f25ab13a5d928076d5f9dd4e7d18252329af65692ffd6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_product_attributes`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_product_attributes_agent.py` and in the RCI capsule.

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

Define product attributes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 61717a143586ce7e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_attributes_agent.py` first:

```bash
python3 ppt_exec_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_attributes_agent.py   # or on stdin
python3 ppt_exec_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_attributes',
    "version": '2.0.1',
    "display_name": 'Define product attributes Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6265b2a16e5b4e48',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineProductAttributes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductAttributes'
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
    print(PptExecDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
