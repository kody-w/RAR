---
name: "rar-cowork-cookbook-adaptive-card-define-depreciation-and-amortization-policies"
description: "Produces a reusable Adaptive Card JSON snapshot of define depreciation and amortization policies status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies", "rar_sha256": "c468838385fcb0debd4f6a94916d79401ab990c9a307a2df9f0c543456b0f850", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_depreciation_and_amortization_policies_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 c468838385fcb0de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_depreciation_and_amortization_policies_agent.py` first:

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
    "version": '2.0.1',
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
