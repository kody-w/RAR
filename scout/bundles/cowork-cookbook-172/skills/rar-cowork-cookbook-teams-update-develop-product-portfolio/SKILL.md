---
name: "rar-cowork-cookbook-teams-update-develop-product-portfolio"
description: "Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_portfolio", "rar_sha256": "df7ab03785e875c83eb62d629df360cd1d4f44340dbde06a8976d26ae8cab3a7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 df7ab03785e875c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_portfolio_agent.py` first:

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
    "version": '2.0.0',
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
