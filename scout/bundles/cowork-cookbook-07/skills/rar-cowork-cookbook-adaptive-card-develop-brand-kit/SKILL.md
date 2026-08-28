---
name: "rar-cowork-cookbook-adaptive-card-develop-brand-kit"
description: "Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_brand_kit", "rar_sha256": "3f98ea2fcd162d1d032b38c0bc397a4524ca40f00b963276a568ca20d48a3e54", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_brand_kit`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_brand_kit_agent.py` and in the RCI capsule.

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

Develop brand kit Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 3f98ea2fcd162d1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_brand_kit_agent.py` first:

```bash
python3 adaptive_card_develop_brand_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_brand_kit_agent.py   # or on stdin
python3 adaptive_card_develop_brand_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop brand kit Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_brand_kit',
    "version": '2.0.1',
    "display_name": 'Develop brand kit Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-develop-brand-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '137fe3fa21cf8525',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-brand-kit'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-develop-brand-kit', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopBrandKit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopBrandKit'
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
    print(AdaptiveCardDevelopBrandKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
