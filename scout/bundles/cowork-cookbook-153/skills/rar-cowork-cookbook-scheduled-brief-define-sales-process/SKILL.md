---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-process"
description: "Schedulable morning-brief email summarizing define sales process for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_process", "rar_sha256": "93c3ba416fafd86419f472ace7285763c96c3e5ac7bdfa7fd0a6f0c184caca66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_sales_process_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-sales-process:5c2a98427d963e733842afc223428b941d937f218535ddd8e3acdb29873053de", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_sales_process`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_sales_process_agent.py` is
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

Define sales process Scheduled Email Brief — Schedulable morning-brief email summarizing define sales process for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_process_agent.py` and embedded as the fenced Python below (sha256 93c3ba416fafd864…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_process_agent.py` first:

```bash
python3 scheduled_brief_define_sales_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_sales_process_agent.py   # or on stdin
python3 scheduled_brief_define_sales_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales process Scheduled Email Brief — Schedulable morning-brief email summarizing define sales process for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_sales_process',
    "version": '2.0.0',
    "display_name": 'Define sales process Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define sales process for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-sales-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-sales-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a4cdf5cb02e3723',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-process'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-define-sales-process', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineSalesProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineSalesProcess'
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
    print(ScheduledBriefDefineSalesProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
