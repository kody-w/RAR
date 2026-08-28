---
name: "rar-cowork-cookbook-ppt-exec-revoke-users-access-to-systems"
description: "Generates an executive-ready PowerPoint deck on revoke users access to systems status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_revoke_users_access_to_systems", "rar_sha256": "16e42f61e7ba300fd94b31203812ea6ac49ba4d8aa0597f552211382b94a02a2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
