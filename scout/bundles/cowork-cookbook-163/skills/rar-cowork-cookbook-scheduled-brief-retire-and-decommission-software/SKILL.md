---
name: "rar-cowork-cookbook-scheduled-brief-retire-and-decommission-software"
description: "Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_and_decommission_software", "rar_sha256": "2ea83ffb837c1c8fde619e3951e9f035e50b3e3f24a9339d5cd49787a738f68f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_and_decommission_software`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_and_decommission_software_agent.py` and in the RCI capsule.

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

Retire and decommission software Scheduled Email Brief — Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_and_decommission_software_agent.py` and embedded as the fenced Python below (sha256 2ea83ffb837c1c8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_and_decommission_software_agent.py` first:

```bash
python3 scheduled_brief_retire_and_decommission_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_and_decommission_software_agent.py   # or on stdin
python3 scheduled_brief_retire_and_decommission_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire and decommission software Scheduled Email Brief — Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_and_decommission_software',
    "version": '2.0.0',
    "display_name": 'Retire and decommission software Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-retire-and-decommission-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e2057509cc0e181',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/retire-and-decommission-software'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-retire-and-decommission-software', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRetireAndDecommissionSoftware(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireAndDecommissionSoftware'
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
    print(ScheduledBriefRetireAndDecommissionSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
