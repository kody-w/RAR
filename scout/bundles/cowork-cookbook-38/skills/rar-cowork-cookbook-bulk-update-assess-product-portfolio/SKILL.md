---
name: "rar-cowork-cookbook-bulk-update-assess-product-portfolio"
description: "Applies a bulk field update across assess product portfolio records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_product_portfolio", "rar_sha256": "0414f6026633c7668446af1b9dd15175f3f1ee63678524790ab694b4e692184b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_assess_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_assess_product_portfolio_agent.py` and in the RCI capsule.

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

Assess product portfolio Bulk Field Update — Applies a bulk field update across assess product portfolio records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 0414f6026633c766…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_product_portfolio_agent.py` first:

```bash
python3 bulk_update_assess_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_assess_product_portfolio_agent.py   # or on stdin
python3 bulk_update_assess_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess product portfolio Bulk Field Update — Applies a bulk field update across assess product portfolio records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_assess_product_portfolio',
    "version": '2.0.1',
    "display_name": 'Assess product portfolio Bulk Field Update',
    "description": 'Applies a bulk field update across assess product portfolio records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-assess-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-assess-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd25a9ec28310280d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/assess-product-portfolio'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-assess-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAssessProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAssessProductPortfolio'
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
    print(BulkUpdateAssessProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
