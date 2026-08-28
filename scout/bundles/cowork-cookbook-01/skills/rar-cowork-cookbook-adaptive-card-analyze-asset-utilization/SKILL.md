---
name: "rar-cowork-cookbook-adaptive-card-analyze-asset-utilization"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_asset_utilization", "rar_sha256": "896cacf534050744cc02e9256885b392532422605ca0fa884a689ba9a98ce6d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_asset_utilization`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_asset_utilization_agent.py` and in the RCI capsule.

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

Analyze asset utilization Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 896cacf534050744…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_asset_utilization_agent.py` first:

```bash
python3 adaptive_card_analyze_asset_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_asset_utilization_agent.py   # or on stdin
python3 adaptive_card_analyze_asset_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset utilization Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_asset_utilization',
    "version": '2.0.1',
    "display_name": 'Analyze asset utilization Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-analyze-asset-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d0de65dc478ba4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-utilization'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-analyze-asset-utilization', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardAnalyzeAssetUtilization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeAssetUtilization'
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
    print(AdaptiveCardAnalyzeAssetUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
