---
name: "rar-cowork-cookbook-configure-oversee-active-campaigns"
description: "Applies a bulk configuration change to oversee active campaigns from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_oversee_active_campaigns", "rar_sha256": "c51be291157daa3067b9f1abf2d0a43003e97d27a9400c9e83c80c1169136e1c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_oversee_active_campaigns`. The original RAPP
agent is preserved byte-for-byte in `configure_oversee_active_campaigns_agent.py` and in the RCI capsule.

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

Oversee active campaigns Configuration Bulk Setup — Applies a bulk configuration change to oversee active campaigns from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-oversee-active-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 c51be291157daa30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_oversee_active_campaigns_agent.py` first:

```bash
python3 configure_oversee_active_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_oversee_active_campaigns_agent.py   # or on stdin
python3 configure_oversee_active_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Oversee active campaigns Configuration Bulk Setup — Applies a bulk configuration change to oversee active campaigns from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-oversee-active-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_oversee_active_campaigns',
    "version": '2.0.0',
    "display_name": 'Oversee active campaigns Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to oversee active campaigns from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-oversee-active-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-oversee-active-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63f0a84984ef4973',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-oversee-active-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureOverseeActiveCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureOverseeActiveCampaigns'
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
    print(ConfigureOverseeActiveCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
