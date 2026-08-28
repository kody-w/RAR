---
name: "rar-cowork-cookbook-configure-oversee-active-campaigns"
description: "Applies a bulk configuration change to oversee active campaigns from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_oversee_active_campaigns", "rar_sha256": "cdada03edf8e1ed199b003aef35d3cb798d665e2323ce4be0af5744570a0002b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 cdada03edf8e1ed1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_oversee_active_campaigns_agent.py` first:

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
    "version": '2.0.1',
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
