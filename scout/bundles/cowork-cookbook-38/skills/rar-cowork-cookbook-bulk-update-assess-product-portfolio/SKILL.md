---
name: "rar-cowork-cookbook-bulk-update-assess-product-portfolio"
description: "Applies a bulk field update across assess product portfolio records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_product_portfolio", "rar_sha256": "ad868b05a0f42ecc6db5c4aa7bd55458c4e78a592f6f2f613a8e8ce39c134f17", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_assess_product_portfolio_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-assess-product-portfolio:46e3501b48bc89ec7ef2dc930ba2f87ef01d286e79e1de861ec76c572b9ad233", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_assess_product_portfolio`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_assess_product_portfolio_agent.py` is
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
