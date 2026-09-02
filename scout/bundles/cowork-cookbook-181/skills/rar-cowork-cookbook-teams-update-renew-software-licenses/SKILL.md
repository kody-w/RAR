---
name: "rar-cowork-cookbook-teams-update-renew-software-licenses"
description: "Drafts a Teams channel post on renew software licenses status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_renew_software_licenses", "rar_sha256": "63bccd67ac5773059ce33f5345d746b2bd436b7e683c603caf2c4dbc290cd78a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_renew_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-renew-software-licenses:b87590bb5344522766390943c2d28625f55077b7284f21d737f3a2018f24f74d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_renew_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_renew_software_licenses_agent.py` is
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
