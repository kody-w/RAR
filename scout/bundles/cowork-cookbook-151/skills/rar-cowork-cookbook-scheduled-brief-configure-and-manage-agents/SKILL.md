---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-manage-agents"
description: "Schedulable morning-brief email summarizing configure and manage agents for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_manage_agents", "rar_sha256": "366eb15d7357943dd7d2ba31c2a1ac34a2aacfb7ff726cba068d478bdfc89bbe", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_manage_agents_agent.py` and embedded as the fenced Python below (sha256 366eb15d7357943d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_manage_agents_agent.py` first:

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
    "version": '2.0.1',
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
