---
name: "rar-cowork-cookbook-scheduled-brief-end-product-sales"
description: "Schedulable morning-brief email summarizing end product sales for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_end_product_sales", "rar_sha256": "bfd993d64eafe1774a9bc102fd3505c47e0c0ed510fdb44bedf6b07428ecff26", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_end_product_sales_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-end-product-sales:ae815051e1c9cf922972de1eceae387355f747b415b2380e693a2cc1edaa3704", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_end_product_sales`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_end_product_sales_agent.py` is
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

End product sales Scheduled Email Brief — Schedulable morning-brief email summarizing end product sales for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-end-product-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 bfd993d64eafe177…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_end_product_sales_agent.py` first:

```bash
python3 scheduled_brief_end_product_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_end_product_sales_agent.py   # or on stdin
python3 scheduled_brief_end_product_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
End product sales Scheduled Email Brief — Schedulable morning-brief email summarizing end product sales for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-end-product-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_end_product_sales',
    "version": '2.0.0',
    "display_name": 'End product sales Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing end product sales for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-end-product-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-end-product-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8380bba8933623f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/end-product-sales'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-end-product-sales', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefEndProductSales(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefEndProductSales'
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
    print(ScheduledBriefEndProductSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
