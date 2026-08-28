---
name: "rar-cowork-cookbook-ppt-exec-develop-new-products"
description: "Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_new_products", "rar_sha256": "2adc96b49f2e7cccbed42f2b5cd836214897d593ebbc3819673183fa5a58defd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_new_products`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_new_products_agent.py` and in the RCI capsule.

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

Develop new products Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 2adc96b49f2e7ccc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_new_products_agent.py` first:

```bash
python3 ppt_exec_develop_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_new_products_agent.py   # or on stdin
python3 ppt_exec_develop_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new products Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_new_products',
    "version": '2.0.1',
    "display_name": 'Develop new products Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-develop-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4453f7c3748daa62',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/develop-new-products'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-develop-new-products', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopNewProducts'
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
    print(PptExecDevelopNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
