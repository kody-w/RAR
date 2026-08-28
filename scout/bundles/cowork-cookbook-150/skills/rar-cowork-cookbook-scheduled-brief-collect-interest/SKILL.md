---
name: "rar-cowork-cookbook-scheduled-brief-collect-interest"
description: "Schedulable morning-brief email summarizing collect interest for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_collect_interest", "rar_sha256": "c7beb0d5c0433585c73b7697d410c3fc098e34bd5dae73f82c97d4b254acb631", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_collect_interest`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_collect_interest_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_collect_interest_agent.py` and embedded as the fenced Python below (sha256 c7beb0d5c0433585…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_collect_interest_agent.py` first:

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
    "version": '2.0.1',
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
