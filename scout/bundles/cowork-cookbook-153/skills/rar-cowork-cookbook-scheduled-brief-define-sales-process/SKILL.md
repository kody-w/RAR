---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-process"
description: "Schedulable morning-brief email summarizing define sales process for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_process", "rar_sha256": "946dd80a045e1b66b992dcec4aff7736fcc9cbae224a63be35c756a539a3566b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_process_agent.py` and embedded as the fenced Python below (sha256 946dd80a045e1b66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_process_agent.py` first:

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
    "version": '2.0.1',
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
