---
name: "rar-cowork-cookbook-adaptive-card-convert-projects-to-fixed-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of convert projects to fixed assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets", "rar_sha256": "2d09bc558d9fdbb3d6a93f8f0c3c1d90abbc5f5b50a44c09baa5bfe8ea932ffa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 2d09bc558d9fdbb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_projects_to_fixed_assets_agent.py` first:

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
    "version": '2.0.1',
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
