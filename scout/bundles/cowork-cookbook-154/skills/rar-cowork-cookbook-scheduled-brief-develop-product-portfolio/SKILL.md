---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-portfolio"
description: "Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_portfolio", "rar_sha256": "925c8082658e4ea96ca2be17e2c89e03c8525bf9c37e6b4e5d440623771837f0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_product_portfolio_agent.py` and in the RCI capsule.

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

Develop product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 925c8082658e4ea9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_portfolio_agent.py` first:

```bash
python3 scheduled_brief_develop_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_product_portfolio_agent.py   # or on stdin
python3 scheduled_brief_develop_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_product_portfolio',
    "version": '2.0.1',
    "display_name": 'Develop product portfolio Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-develop-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07f780d065d8bf55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-portfolio'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-develop-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProductPortfolio'
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
    print(ScheduledBriefDevelopProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
