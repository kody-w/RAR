---
name: "rar-cowork-cookbook-teams-update-update-product-assortments"
description: "Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_product_assortments", "rar_sha256": "2f328a0ffef7eb749df243b1aaa4d36983c1e8af2d66e792295fd1ea62fbdef9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_update_product_assortments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-update-product-assortments:e20b8f364fc75fdb503a0e10bb35549d193ac2aded30ea9971ff8ef238f427a7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_update_product_assortments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_update_product_assortments_agent.py` is
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

Update product assortments Teams Channel Update — Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 2f328a0ffef7eb74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_product_assortments_agent.py` first:

```bash
python3 teams_update_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_product_assortments_agent.py   # or on stdin
python3 teams_update_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Teams Channel Update — Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_product_assortments',
    "version": '2.0.0',
    "display_name": 'Update product assortments Teams Channel Update',
    "description": 'Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a99ee589b7c31dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateUpdateProductAssortments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateProductAssortments'
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
    print(TeamsUpdateUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
