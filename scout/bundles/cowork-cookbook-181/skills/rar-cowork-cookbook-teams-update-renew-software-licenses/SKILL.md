---
name: "rar-cowork-cookbook-teams-update-renew-software-licenses"
description: "Drafts a Teams channel post on renew software licenses status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_renew_software_licenses", "rar_sha256": "63bccd67ac5773059ce33f5345d746b2bd436b7e683c603caf2c4dbc290cd78a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_renew_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `teams_update_renew_software_licenses_agent.py` and in the RCI capsule.

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

Renew software licenses Teams Channel Update — Drafts a Teams channel post on renew software licenses status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-renew-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 63bccd67ac577305…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_renew_software_licenses_agent.py` first:

```bash
python3 teams_update_renew_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_renew_software_licenses_agent.py   # or on stdin
python3 teams_update_renew_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Renew software licenses Teams Channel Update — Drafts a Teams channel post on renew software licenses status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-renew-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_renew_software_licenses',
    "version": '2.0.0',
    "display_name": 'Renew software licenses Teams Channel Update',
    "description": 'Drafts a Teams channel post on renew software licenses status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-renew-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-renew-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1bb21523fba91cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/renew-software-licenses'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-renew-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateRenewSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRenewSoftwareLicenses'
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
    print(TeamsUpdateRenewSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
