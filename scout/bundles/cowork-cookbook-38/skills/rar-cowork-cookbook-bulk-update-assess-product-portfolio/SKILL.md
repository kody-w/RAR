---
name: "rar-cowork-cookbook-bulk-update-assess-product-portfolio"
description: "Applies a bulk field update across assess product portfolio records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_product_portfolio", "rar_sha256": "ad868b05a0f42ecc6db5c4aa7bd55458c4e78a592f6f2f613a8e8ce39c134f17", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 ad868b05a0f42ecc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_product_portfolio_agent.py` first:

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
    "version": '2.0.0',
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
