---
name: "rar-cowork-cookbook-scheduled-brief-update-access-to-systems"
description: "Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_access_to_systems", "rar_sha256": "6e2dfdd825e8920daf3d2bfbe65a605bbd30a9ec5951278551e6b2581a5b35e7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 6e2dfdd825e8920d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_access_to_systems_agent.py` first:

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
    "version": '2.0.0',
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
