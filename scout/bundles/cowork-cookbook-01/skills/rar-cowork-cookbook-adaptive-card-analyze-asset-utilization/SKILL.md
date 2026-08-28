---
name: "rar-cowork-cookbook-adaptive-card-analyze-asset-utilization"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze asset utilization status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_asset_utilization", "rar_sha256": "63d18793cb053871d1cf33e04ece4f7e1476323e7c17f552f701c9bba3fd4f5d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 63d18793cb053871…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_asset_utilization_agent.py` first:

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
    "version": '2.0.0',
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
