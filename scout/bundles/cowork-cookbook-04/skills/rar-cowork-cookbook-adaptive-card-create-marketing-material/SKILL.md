---
name: "rar-cowork-cookbook-adaptive-card-create-marketing-material"
description: "Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_marketing_material", "rar_sha256": "e32199e231c02cecae17031321249b03eaae7badbadb006cb1775ff9a9dd7b28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_create_marketing_material_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-create-marketing-material:10bee63915fc3acbd523a2f7c87f491abf4740fdacd645cac91fc0a71c63afe6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_create_marketing_material`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_create_marketing_material_agent.py` is
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

Create marketing material Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 e32199e231c02cec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_marketing_material_agent.py` first:

```bash
python3 adaptive_card_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_marketing_material_agent.py   # or on stdin
python3 adaptive_card_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_marketing_material',
    "version": '2.0.0',
    "display_name": 'Create marketing material Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '83092695e8192eea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCreateMarketingMaterial(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateMarketingMaterial'
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
    print(AdaptiveCardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
