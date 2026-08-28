---
name: "rar-cowork-cookbook-adaptive-card-convert-projects-to-fixed-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of convert projects to fixed assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets", "rar_sha256": "0c7e8b85530270b6832052276f6a36c54e5de1502d1cf07617f2b1b52f9d98e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_convert_projects_to_fixed_assets_agent.py` and in the RCI capsule.

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

Convert projects to fixed assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of convert projects to fixed assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 0c7e8b85530270b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_projects_to_fixed_assets_agent.py` first:

```bash
python3 adaptive_card_convert_projects_to_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_convert_projects_to_fixed_assets_agent.py   # or on stdin
python3 adaptive_card_convert_projects_to_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert projects to fixed assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of convert projects to fixed assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Convert projects to fixed assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of convert projects to fixed assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-convert-projects-to-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac3433d127ce2f6d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/convert-projects-to-fixed-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-convert-projects-to-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardConvertProjectsToFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConvertProjectsToFixedAssets'
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
    print(AdaptiveCardConvertProjectsToFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
