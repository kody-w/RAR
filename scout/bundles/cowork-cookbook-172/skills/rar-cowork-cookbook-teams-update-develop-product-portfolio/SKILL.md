---
name: "rar-cowork-cookbook-teams-update-develop-product-portfolio"
description: "Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_portfolio", "rar_sha256": "9290300502a6f0f18ba8c00d65cb6a1b3665be26938370d9f617d571fc4d3c43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_portfolio_agent.py` and in the RCI capsule.

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

Develop product portfolio Teams Channel Update — Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 9290300502a6f0f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_portfolio_agent.py` first:

```bash
python3 teams_update_develop_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_portfolio_agent.py   # or on stdin
python3 teams_update_develop_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product portfolio Teams Channel Update — Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_portfolio',
    "version": '2.0.1',
    "display_name": 'Develop product portfolio Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8addd5522920dd9a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-portfolio'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-develop-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductPortfolio'
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
    print(TeamsUpdateDevelopProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
