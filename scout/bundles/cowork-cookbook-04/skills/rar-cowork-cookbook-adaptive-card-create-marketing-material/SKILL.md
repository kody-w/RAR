---
name: "rar-cowork-cookbook-adaptive-card-create-marketing-material"
description: "Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_marketing_material", "rar_sha256": "d02e6163d2b7158deb1425d132c3c266a05770ac839897a70ef3953699f6cb89", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_marketing_material`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_marketing_material_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 d02e6163d2b7158d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_marketing_material_agent.py` first:

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
    "version": '2.0.1',
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
