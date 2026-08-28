---
name: "rar-cowork-cookbook-adaptive-card-define-depreciation-and-amortization-policies"
description: "Produces a reusable Adaptive Card JSON snapshot of define depreciation and amortization policies status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies", "rar_sha256": "3ed9823e1921ba26b5267f12829c9535616397b6fdf6a5b83d9d0738aadbf469", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
