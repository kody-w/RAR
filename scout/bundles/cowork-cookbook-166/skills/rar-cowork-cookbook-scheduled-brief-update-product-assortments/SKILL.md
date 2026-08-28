---
name: "rar-cowork-cookbook-scheduled-brief-update-product-assortments"
description: "Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_product_assortments", "rar_sha256": "41c6a0add260d31a4e79153297a9a773b2d948892874c0619a11f5835675a219", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_update_product_assortments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_update_product_assortments_agent.py` and in the RCI capsule.

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

Update product assortments Scheduled Email Brief — Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 41c6a0add260d31a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_product_assortments_agent.py` first:

```bash
python3 scheduled_brief_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_product_assortments_agent.py   # or on stdin
python3 scheduled_brief_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Scheduled Email Brief — Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_product_assortments',
    "version": '2.0.1',
    "display_name": 'Update product assortments Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '644a6f20dfcedd34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefUpdateProductAssortments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateProductAssortments'
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
    print(ScheduledBriefUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
