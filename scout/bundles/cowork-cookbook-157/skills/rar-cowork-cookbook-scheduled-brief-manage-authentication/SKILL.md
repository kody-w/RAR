---
name: "rar-cowork-cookbook-scheduled-brief-manage-authentication"
description: "Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_authentication", "rar_sha256": "e0272533965f4f4ab1e42fffaa68f7a394a7990c99d80d0d89f9f1ceefeab3dd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_authentication_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-authentication:198f6c9fc10d15999e83f88dc603fa66824368c03a097b02a79670aa8552e5c1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_authentication`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_authentication_agent.py` is
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

Manage authentication Scheduled Email Brief — Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 e0272533965f4f4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_authentication_agent.py` first:

```bash
python3 scheduled_brief_manage_authentication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_authentication_agent.py   # or on stdin
python3 scheduled_brief_manage_authentication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage authentication Scheduled Email Brief — Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_authentication',
    "version": '2.0.0',
    "display_name": 'Manage authentication Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-authentication',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '629151c481143ee4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-authentication'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-authentication', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageAuthentication(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageAuthentication'
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
    print(ScheduledBriefManageAuthentication().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
