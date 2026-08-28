---
name: "rar-cowork-cookbook-adaptive-card-define-routing-rules"
description: "Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_routing_rules", "rar_sha256": "5f6abf489a021ab84659af4e284a27eea7a8e737695aa458ad03c3c56bd75816", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_routing_rules`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_routing_rules_agent.py` and in the RCI capsule.

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

Define routing rules Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_routing_rules_agent.py` and embedded as the fenced Python below (sha256 5f6abf489a021ab8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_routing_rules_agent.py` first:

```bash
python3 adaptive_card_define_routing_rules_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_routing_rules_agent.py   # or on stdin
python3 adaptive_card_define_routing_rules_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define routing rules Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_routing_rules',
    "version": '2.0.0',
    "display_name": 'Define routing rules Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-routing-rules',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c722f1d95b5e5ca5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-routing-rules'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-define-routing-rules', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineRoutingRules(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineRoutingRules'
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
    print(AdaptiveCardDefineRoutingRules().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
