---
name: "rar-cowork-cookbook-scheduled-brief-collect-interest"
description: "Schedulable morning-brief email summarizing collect interest for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_collect_interest", "rar_sha256": "8c1ed48c47ce69885a35cfee7cfc21a64cf71f290add4be7228537410e0b14f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_collect_interest_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-collect-interest:b113d9948891b13c9c3e9e78c2230a63b3c928f67b3a7a974c1151224086b10d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_collect_interest`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_collect_interest_agent.py` is
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

Collect interest Scheduled Email Brief — Schedulable morning-brief email summarizing collect interest for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-collect-interest
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_collect_interest_agent.py` and embedded as the fenced Python below (sha256 8c1ed48c47ce6988…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_collect_interest_agent.py` first:

```bash
python3 scheduled_brief_collect_interest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_collect_interest_agent.py   # or on stdin
python3 scheduled_brief_collect_interest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect interest Scheduled Email Brief — Schedulable morning-brief email summarizing collect interest for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-collect-interest
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_collect_interest',
    "version": '2.0.0',
    "display_name": 'Collect interest Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing collect interest for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-collect-interest',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-collect-interest',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '683a209afbec0233',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/collect-interest'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-collect-interest', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCollectInterest(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCollectInterest'
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
    print(ScheduledBriefCollectInterest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
