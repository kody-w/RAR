---
name: "rar-cowork-cookbook-adaptive-card-define-routing-rules"
description: "Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_routing_rules", "rar_sha256": "5f6abf489a021ab84659af4e284a27eea7a8e737695aa458ad03c3c56bd75816", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_routing_rules_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-routing-rules:5e268eda6d1b2815b02919b42374af36a0e12523b638452aa2f393de1c324e7c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_routing_rules`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_routing_rules_agent.py` is
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
