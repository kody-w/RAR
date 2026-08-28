---
name: "rar-cowork-cookbook-ppt-exec-market-test-new-products"
description: "Generates an executive-ready PowerPoint deck on market test new products status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_market_test_new_products", "rar_sha256": "ebc05b63e1e4d8cd23faf22b0abaaec72f377f52253a89b0bd78d1679f524fb6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 ebc05b63e1e4d8cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_market_test_new_products_agent.py` first:

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
    "version": '2.0.0',
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
