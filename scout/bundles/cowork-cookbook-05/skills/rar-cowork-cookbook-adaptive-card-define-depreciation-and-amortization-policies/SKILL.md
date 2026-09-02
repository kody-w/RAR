---
name: "rar-cowork-cookbook-adaptive-card-define-depreciation-and-amortization-policies"
description: "Produces a reusable Adaptive Card JSON snapshot of define depreciation and amortization policies status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies", "rar_sha256": "3ed9823e1921ba26b5267f12829c9535616397b6fdf6a5b83d9d0738aadbf469", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_depreciation_and_amortization_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-depreciation-and-amortization-policies:7268d6e06556b85eaa00dc2a3244da9c2ea5c93b91d8fd4735bc9e173b6a52ba", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_depreciation_and_amortization_policies_agent.py` is
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

Define depreciation and amortization policies Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define depreciation and amortization policies status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-depreciation-and-amortization-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 3ed9823e1921ba26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_depreciation_and_amortization_policies_agent.py` first:

```bash
python3 adaptive_card_define_depreciation_and_amortization_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_depreciation_and_amortization_policies_agent.py   # or on stdin
python3 adaptive_card_define_depreciation_and_amortization_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define depreciation and amortization policies Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define depreciation and amortization policies status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-depreciation-and-amortization-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies',
    "version": '2.0.0',
    "display_name": 'Define depreciation and amortization policies Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define depreciation and amortization policies status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-define-depreciation-and-amortization-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-depreciation-and-amortization-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6503ee5cc0e41ae8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-depreciation-and-amortization-policies'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-define-depreciation-and-amortization-policies', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDefineDepreciationAndAmortizationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineDepreciationAndAmortizationPolicies'
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
    print(AdaptiveCardDefineDepreciationAndAmortizationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
