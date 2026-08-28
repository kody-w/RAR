---
name: "rar-cowork-cookbook-scheduled-brief-update-access-to-systems"
description: "Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_access_to_systems", "rar_sha256": "8e6d103651d8db7e54876a5cbe3b91af8d03025d380664bd9bdf6f8166489426", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_update_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_update_access_to_systems_agent.py` and in the RCI capsule.

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

Update access to systems Scheduled Email Brief — Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 8e6d103651d8db7e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_access_to_systems_agent.py` first:

```bash
python3 scheduled_brief_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_access_to_systems_agent.py   # or on stdin
python3 scheduled_brief_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Scheduled Email Brief — Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_access_to_systems',
    "version": '2.0.1',
    "display_name": 'Update access to systems Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '09ad37fd3a260daf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefUpdateAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateAccessToSystems'
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
    print(ScheduledBriefUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
