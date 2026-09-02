---
name: "rar-cowork-cookbook-ppt-exec-revoke-users-access-to-systems"
description: "Generates an executive-ready PowerPoint deck on revoke users access to systems status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_revoke_users_access_to_systems", "rar_sha256": "16e42f61e7ba300fd94b31203812ea6ac49ba4d8aa0597f552211382b94a02a2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_revoke_users_access_to_systems_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-revoke-users-access-to-systems:bda71c1431ab3d59c7ac16eda0ddcff6b70301c0047b1b5ae2d334c05db05703", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_revoke_users_access_to_systems`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_revoke_users_access_to_systems_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_revoke_users_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 16e42f61e7ba300f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_revoke_users_access_to_systems_agent.py` first:

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
    "version": '2.0.0',
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
