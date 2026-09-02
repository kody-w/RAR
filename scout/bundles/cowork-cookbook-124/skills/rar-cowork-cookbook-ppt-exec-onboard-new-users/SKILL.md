---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-users"
description: "Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_users", "rar_sha256": "7703b0c030245dfc719cf7acf0a65f2a22be6e968b0f7f21fd4be2657a0995c7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_onboard_new_users_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-onboard-new-users:147e49b8805ab919c5f4c41ec0e2505388cf82b31cf2c46d203aa6fa6b6d7bd5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_onboard_new_users`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_onboard_new_users_agent.py` is
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

Onboard new users Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 7703b0c030245dfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_users_agent.py` first:

```bash
python3 ppt_exec_onboard_new_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_onboard_new_users_agent.py   # or on stdin
python3 ppt_exec_onboard_new_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new users Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_onboard_new_users',
    "version": '2.0.0',
    "display_name": 'Onboard new users Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-onboard-new-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06ae3a8717ab6ed7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/onboard-new-users'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-onboard-new-users', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecOnboardNewUsers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecOnboardNewUsers'
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
    print(PptExecOnboardNewUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
