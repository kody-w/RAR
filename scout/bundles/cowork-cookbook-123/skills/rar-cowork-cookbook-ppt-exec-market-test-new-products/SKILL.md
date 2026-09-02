---
name: "rar-cowork-cookbook-ppt-exec-market-test-new-products"
description: "Generates an executive-ready PowerPoint deck on market test new products status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_market_test_new_products", "rar_sha256": "ebc05b63e1e4d8cd23faf22b0abaaec72f377f52253a89b0bd78d1679f524fb6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_market_test_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-market-test-new-products:20e136aee144f2f635a0854c53cbd1a077efcd21c5abf5fc7bd160658a419412", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_market_test_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_market_test_new_products_agent.py` is
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
