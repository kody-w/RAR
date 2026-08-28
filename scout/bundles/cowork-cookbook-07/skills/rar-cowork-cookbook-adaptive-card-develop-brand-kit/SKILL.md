---
name: "rar-cowork-cookbook-adaptive-card-develop-brand-kit"
description: "Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_brand_kit", "rar_sha256": "40b2e906c692b66e79f0f89672aa5693d6b658a5b2d808c01b9fb5aec5a7ebcd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 40b2e906c692b66e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_brand_kit_agent.py` first:

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
    "version": '2.0.0',
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
