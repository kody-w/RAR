---
name: "rar-cowork-cookbook-scheduled-brief-end-product-sales"
description: "Schedulable morning-brief email summarizing end product sales for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_end_product_sales", "rar_sha256": "1b15301e5dd5b46cda3937d83a6a2c56dc84327f50fd856d88e59ab098150ce8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 1b15301e5dd5b46c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_end_product_sales_agent.py` first:

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
    "version": '2.0.1',
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
