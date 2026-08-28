---
name: "rar-cowork-cookbook-teams-update-manage-data-security"
description: "Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_data_security", "rar_sha256": "e06fb55f5be5f8488822c2ea9944713a26f31d55a64d1623c0b7f3a9336ce299", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_data_security`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_data_security_agent.py` and in the RCI capsule.

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

Manage data security Teams Channel Update — Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-data-security
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 e06fb55f5be5f848…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_data_security_agent.py` first:

```bash
python3 teams_update_manage_data_security_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_data_security_agent.py   # or on stdin
python3 teams_update_manage_data_security_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data security Teams Channel Update — Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-data-security
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_data_security',
    "version": '2.0.0',
    "display_name": 'Manage data security Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-manage-data-security',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-data-security',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9681baadfe006e8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-data-security'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-manage-data-security', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageDataSecurity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageDataSecurity'
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
    print(TeamsUpdateManageDataSecurity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
