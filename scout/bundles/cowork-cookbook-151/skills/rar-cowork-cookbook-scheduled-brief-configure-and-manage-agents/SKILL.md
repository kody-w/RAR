---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-manage-agents"
description: "Schedulable morning-brief email summarizing configure and manage agents for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_manage_agents", "rar_sha256": "4096463fcd816bdec477cee7a24e9db8f3b8a31ecfa82f631887d163147c8be8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_manage_agents`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_manage_agents_agent.py` and in the RCI capsule.

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
