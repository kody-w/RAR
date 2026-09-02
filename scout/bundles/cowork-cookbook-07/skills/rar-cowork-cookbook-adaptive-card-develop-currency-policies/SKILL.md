---
name: "rar-cowork-cookbook-adaptive-card-develop-currency-policies"
description: "Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_currency_policies", "rar_sha256": "6f33b443888d0f2eafe0a68f2f20135b2e6057eaa0c0ac136392648a0c7e861a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_currency_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-currency-policies:b491f00e9985b913735d7bc6fcfac0fafd833ecc0da794a503f22318407268e9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_currency_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_currency_policies_agent.py` is
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

Develop currency policies Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 6f33b443888d0f2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_currency_policies_agent.py` first:

```bash
python3 adaptive_card_develop_currency_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_currency_policies_agent.py   # or on stdin
python3 adaptive_card_develop_currency_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop currency policies Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_currency_policies',
    "version": '2.0.0',
    "display_name": 'Develop currency policies Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-currency-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e024caadcec1ebd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-currency-policies'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-develop-currency-policies', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopCurrencyPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopCurrencyPolicies'
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
    print(AdaptiveCardDevelopCurrencyPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
