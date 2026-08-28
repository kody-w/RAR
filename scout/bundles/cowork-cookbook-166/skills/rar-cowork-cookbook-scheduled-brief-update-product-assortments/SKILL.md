---
name: "rar-cowork-cookbook-scheduled-brief-update-product-assortments"
description: "Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_product_assortments", "rar_sha256": "719d1435448b882a0b118936ff186200b7525f98ccf1250b9aa6a14d338fb105", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 719d1435448b882a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_product_assortments_agent.py` first:

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
    "version": '2.0.0',
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
