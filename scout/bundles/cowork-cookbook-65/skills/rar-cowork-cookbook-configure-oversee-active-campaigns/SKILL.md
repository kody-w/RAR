---
name: "rar-cowork-cookbook-configure-oversee-active-campaigns"
description: "Applies a bulk configuration change to oversee active campaigns from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_oversee_active_campaigns", "rar_sha256": "c51be291157daa3067b9f1abf2d0a43003e97d27a9400c9e83c80c1169136e1c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_oversee_active_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-oversee-active-campaigns:8871655e2e9f96929cd93042cfe2819c6ae48843c55f13001f1f80c522571255", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_oversee_active_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_oversee_active_campaigns_agent.py` is
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
