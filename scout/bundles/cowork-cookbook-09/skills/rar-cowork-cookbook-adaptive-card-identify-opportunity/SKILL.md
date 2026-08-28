---
name: "rar-cowork-cookbook-adaptive-card-identify-opportunity"
description: "Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_opportunity", "rar_sha256": "10504ef24266b33e7185d853b3f51ced8d394cec126fb73a949530d191d78398", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 10504ef24266b33e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_opportunity_agent.py` first:

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
    "version": '2.0.0',
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
