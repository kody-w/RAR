---
name: "rar-cowork-cookbook-scheduled-brief-end-product-sales"
description: "Schedulable morning-brief email summarizing end product sales for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_end_product_sales", "rar_sha256": "bfd993d64eafe1774a9bc102fd3505c47e0c0ed510fdb44bedf6b07428ecff26", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_end_product_sales`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_end_product_sales_agent.py` and in the RCI capsule.

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
