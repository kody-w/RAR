---
name: "rar-cowork-cookbook-teams-update-renew-software-licenses"
description: "Drafts a Teams channel post on renew software licenses status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_renew_software_licenses", "rar_sha256": "a605da00f7b0a60c747306609749ff81acd3ac84f093429232ec5791e67ffcb1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 a605da00f7b0a60c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_renew_software_licenses_agent.py` first:

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
    "version": '2.0.1',
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
