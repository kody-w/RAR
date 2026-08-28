---
name: "rar-cowork-cookbook-teams-update-develop-product-catalogs"
description: "Drafts a Teams channel post on develop product catalogs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_catalogs", "rar_sha256": "92161951efad82f238164a1e8e2eeb14d2741764c28f3df7f90e5a31b3317140", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_catalogs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_catalogs_agent.py` and in the RCI capsule.

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

Develop product catalogs Teams Channel Update — Drafts a Teams channel post on develop product catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 92161951efad82f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_catalogs_agent.py` first:

```bash
python3 teams_update_develop_product_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_catalogs_agent.py   # or on stdin
python3 teams_update_develop_product_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product catalogs Teams Channel Update — Drafts a Teams channel post on develop product catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop product catalogs Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop product catalogs status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-develop-product-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae2cd1f749fb9454',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-develop-product-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopProductCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductCatalogs'
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
    print(TeamsUpdateDevelopProductCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
