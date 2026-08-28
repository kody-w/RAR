---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-process"
description: "Schedulable morning-brief email summarizing define sales process for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_process", "rar_sha256": "93c3ba416fafd86419f472ace7285763c96c3e5ac7bdfa7fd0a6f0c184caca66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_sales_process`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_sales_process_agent.py` and in the RCI capsule.

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
