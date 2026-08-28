---
name: "rar-cowork-cookbook-scheduled-brief-assess-product-portfolio"
description: "Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_assess_product_portfolio", "rar_sha256": "8fefd5579244958e8a1c709429889fd8e0e20feb5825cbfb8ae22b2b72666fae", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_assess_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_assess_product_portfolio_agent.py` and in the RCI capsule.

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

Assess product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 8fefd5579244958e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_assess_product_portfolio_agent.py` first:

```bash
python3 scheduled_brief_assess_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_assess_product_portfolio_agent.py   # or on stdin
python3 scheduled_brief_assess_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_assess_product_portfolio',
    "version": '2.0.1',
    "display_name": 'Assess product portfolio Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-assess-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e206d618375e136',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/assess-product-portfolio'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-assess-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAssessProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAssessProductPortfolio'
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
    print(ScheduledBriefAssessProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
