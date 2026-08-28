---
name: "rar-cowork-cookbook-adaptive-card-identify-opportunity"
description: "Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_opportunity", "rar_sha256": "514173bafc6db8f881f9c4148196fbcabc7b7eb2347e839a31ab0540f8727bfb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_opportunity`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_opportunity_agent.py` and in the RCI capsule.

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

Identify opportunity Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 514173bafc6db8f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_opportunity_agent.py` first:

```bash
python3 adaptive_card_identify_opportunity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_opportunity_agent.py   # or on stdin
python3 adaptive_card_identify_opportunity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify opportunity Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_opportunity',
    "version": '2.0.1',
    "display_name": 'Identify opportunity Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-opportunity',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17b202234e375ae7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/identify-opportunity'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-identify-opportunity', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardIdentifyOpportunity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyOpportunity'
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
    print(AdaptiveCardIdentifyOpportunity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
