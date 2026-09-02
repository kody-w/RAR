---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-manage-agents"
description: "Schedulable morning-brief email summarizing configure and manage agents for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_manage_agents", "rar_sha256": "4096463fcd816bdec477cee7a24e9db8f3b8a31ecfa82f631887d163147c8be8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_configure_and_manage_agents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-configure-and-manage-agents:20d401f3724de4fb42c224da64a55f295a47e5e48ce3468a56d4e956d53c93c8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_configure_and_manage_agents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_configure_and_manage_agents_agent.py` is
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

Configure and manage agents Scheduled Email Brief — Schedulable morning-brief email summarizing configure and manage agents for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-manage-agents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_manage_agents_agent.py` and embedded as the fenced Python below (sha256 4096463fcd816bde…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_manage_agents_agent.py` first:

```bash
python3 scheduled_brief_configure_and_manage_agents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_manage_agents_agent.py   # or on stdin
python3 scheduled_brief_configure_and_manage_agents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage agents Scheduled Email Brief — Schedulable morning-brief email summarizing configure and manage agents for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-manage-agents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_manage_agents',
    "version": '2.0.0',
    "display_name": 'Configure and manage agents Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing configure and manage agents for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-configure-and-manage-agents',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-manage-agents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c476e1f1cbadae6f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-agents'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-manage-agents', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConfigureAndManageAgents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndManageAgents'
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
    print(ScheduledBriefConfigureAndManageAgents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
