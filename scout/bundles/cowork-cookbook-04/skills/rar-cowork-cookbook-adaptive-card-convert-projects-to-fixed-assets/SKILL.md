---
name: "rar-cowork-cookbook-adaptive-card-convert-projects-to-fixed-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of convert projects to fixed assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets", "rar_sha256": "0c7e8b85530270b6832052276f6a36c54e5de1502d1cf07617f2b1b52f9d98e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_convert_projects_to_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-convert-projects-to-fixed-assets:c9f2f0aab1a362ff3e003bd59078698a10e30776b03e01d18776fee45f4f0074", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_convert_projects_to_fixed_assets_agent.py` is
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
