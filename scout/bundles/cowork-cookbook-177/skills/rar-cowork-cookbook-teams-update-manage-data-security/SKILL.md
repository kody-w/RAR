---
name: "rar-cowork-cookbook-teams-update-manage-data-security"
description: "Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_data_security", "rar_sha256": "10b96fc5b9d096b93d42052ec4aa61cfae319822c6db6206621efc6e5153fb84", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 10b96fc5b9d096b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_data_security_agent.py` first:

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
    "version": '2.0.1',
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
