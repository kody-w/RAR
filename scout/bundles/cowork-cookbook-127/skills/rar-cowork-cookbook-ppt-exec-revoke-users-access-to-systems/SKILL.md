---
name: "rar-cowork-cookbook-ppt-exec-revoke-users-access-to-systems"
description: "Generates an executive-ready PowerPoint deck on revoke users access to systems status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_revoke_users_access_to_systems", "rar_sha256": "74188d942494725b64ed4082f283113ad87256db491c6fdd9d741f7222998e29", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_revoke_users_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_revoke_users_access_to_systems_agent.py` and in the RCI capsule.

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

Revoke users access to systems Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on revoke users access to systems status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-revoke-users-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_revoke_users_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 74188d942494725b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_revoke_users_access_to_systems_agent.py` first:

```bash
python3 ppt_exec_revoke_users_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_revoke_users_access_to_systems_agent.py   # or on stdin
python3 ppt_exec_revoke_users_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revoke users access to systems Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on revoke users access to systems status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-revoke-users-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_revoke_users_access_to_systems',
    "version": '2.0.1',
    "display_name": 'Revoke users access to systems Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on revoke users access to systems status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-revoke-users-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-revoke-users-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '342800d41f3b825b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/revoke-users-access-to-systems'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-revoke-users-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecRevokeUsersAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRevokeUsersAccessToSystems'
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
    print(PptExecRevokeUsersAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
