---
name: "rar-cowork-cookbook-teams-update-develop-product-catalogs"
description: "Drafts a Teams channel post on develop product catalogs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_catalogs", "rar_sha256": "92161951efad82f238164a1e8e2eeb14d2741764c28f3df7f90e5a31b3317140", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_product_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-product-catalogs:d412cf2c29e7d4e25d52df45df925ec685be7192c3605daf805af7663103502c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_product_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_product_catalogs_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
