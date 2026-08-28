---
name: "rar-cowork-cookbook-teams-update-update-product-assortments"
description: "Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_product_assortments", "rar_sha256": "2f328a0ffef7eb749df243b1aaa4d36983c1e8af2d66e792295fd1ea62fbdef9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_product_assortments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_product_assortments_agent.py` and in the RCI capsule.

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
