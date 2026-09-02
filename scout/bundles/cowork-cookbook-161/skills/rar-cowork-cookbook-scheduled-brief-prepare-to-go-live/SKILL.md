---
name: "rar-cowork-cookbook-scheduled-brief-prepare-to-go-live"
description: "Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_prepare_to_go_live", "rar_sha256": "43555b388702ee2000daf0c00bc277e4a60164ad697ac3c8217e4fb569b08f10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_prepare_to_go_live_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-prepare-to-go-live:e4fc22ac08684717bfe080106c396918a73fde11b63e62d7680f0a3647f7bbb5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_prepare_to_go_live`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_prepare_to_go_live_agent.py` is
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

Prepare to go live Scheduled Email Brief — Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 43555b388702ee20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_prepare_to_go_live_agent.py` first:

```bash
python3 scheduled_brief_prepare_to_go_live_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_prepare_to_go_live_agent.py   # or on stdin
python3 scheduled_brief_prepare_to_go_live_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare to go live Scheduled Email Brief — Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_prepare_to_go_live',
    "version": '2.0.0',
    "display_name": 'Prepare to go live Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-prepare-to-go-live',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dfbcccce34b780bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/prepare-to-go-live'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-prepare-to-go-live', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPrepareToGoLive(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPrepareToGoLive'
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
    print(ScheduledBriefPrepareToGoLive().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
