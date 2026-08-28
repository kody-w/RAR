---
name: "rar-cowork-cookbook-teams-update-develop-product-catalogs"
description: "Drafts a Teams channel post on develop product catalogs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_catalogs", "rar_sha256": "f464115e84226817875fd4bd484ddcf68871a51a82ae752f23a987cb6a848d21", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 f464115e84226817…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_catalogs_agent.py` first:

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
    "version": '2.0.1',
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
