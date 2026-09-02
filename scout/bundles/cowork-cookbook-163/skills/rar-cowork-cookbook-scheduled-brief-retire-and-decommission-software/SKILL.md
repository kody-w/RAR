---
name: "rar-cowork-cookbook-scheduled-brief-retire-and-decommission-software"
description: "Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_and_decommission_software", "rar_sha256": "2ea83ffb837c1c8fde619e3951e9f035e50b3e3f24a9339d5cd49787a738f68f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_retire_and_decommission_software_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-retire-and-decommission-software:3b603d11d2c315b6755940ec06974d9f9d8069051339ab713fb62f8d2fea78fe", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_retire_and_decommission_software`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_retire_and_decommission_software_agent.py` is
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
