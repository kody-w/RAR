---
name: "rar-cowork-cookbook-ppt-exec-market-test-new-products"
description: "Generates an executive-ready PowerPoint deck on market test new products status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_market_test_new_products", "rar_sha256": "111c85cce8ffee613cbef10a151ad4df052323543e987ced4c912e904b6dac95", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_market_test_new_products`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_market_test_new_products_agent.py` and in the RCI capsule.

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

Market test new products Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on market test new products status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-market-test-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 111c85cce8ffee61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_market_test_new_products_agent.py` first:

```bash
python3 ppt_exec_market_test_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_market_test_new_products_agent.py   # or on stdin
python3 ppt_exec_market_test_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Market test new products Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on market test new products status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-market-test-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_market_test_new_products',
    "version": '2.0.1',
    "display_name": 'Market test new products Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on market test new products status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-market-test-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-market-test-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21918697904feecf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/market-test-new-products'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-market-test-new-products', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecMarketTestNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMarketTestNewProducts'
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
    print(PptExecMarketTestNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
