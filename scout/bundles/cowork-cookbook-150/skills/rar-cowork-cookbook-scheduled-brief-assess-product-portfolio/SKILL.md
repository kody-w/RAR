---
name: "rar-cowork-cookbook-scheduled-brief-assess-product-portfolio"
description: "Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_assess_product_portfolio", "rar_sha256": "1efab3ca9c5ce687ad4eac577122e12a7a1ddccf8b067776bfd556fc695c618a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 1efab3ca9c5ce687…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_assess_product_portfolio_agent.py` first:

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
    "version": '2.0.0',
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
