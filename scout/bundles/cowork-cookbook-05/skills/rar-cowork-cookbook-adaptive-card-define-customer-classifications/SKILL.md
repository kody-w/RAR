---
name: "rar-cowork-cookbook-adaptive-card-define-customer-classifications"
description: "Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_classifications", "rar_sha256": "038571f43c7a346e443d651320441fc5dc93257d81f6280cb1c13e6532bea0eb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_customer_classifications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-customer-classifications:62a1bb3bd7c26970002a2580b7a37ccb0c213ff37ef83a68ac978da7e5d05e54", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_customer_classifications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_customer_classifications_agent.py` is
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

Define customer classifications Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 038571f43c7a346e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_classifications_agent.py` first:

```bash
python3 adaptive_card_define_customer_classifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_customer_classifications_agent.py   # or on stdin
python3 adaptive_card_define_customer_classifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer classifications Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_customer_classifications',
    "version": '2.0.0',
    "display_name": 'Define customer classifications Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-customer-classifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bb499a17f02b974',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-customer-classifications'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-define-customer-classifications', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineCustomerClassifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineCustomerClassifications'
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
    print(AdaptiveCardDefineCustomerClassifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
