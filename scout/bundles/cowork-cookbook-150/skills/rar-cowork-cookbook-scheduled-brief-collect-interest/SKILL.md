---
name: "rar-cowork-cookbook-scheduled-brief-collect-interest"
description: "Schedulable morning-brief email summarizing collect interest for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_collect_interest", "rar_sha256": "8c1ed48c47ce69885a35cfee7cfc21a64cf71f290add4be7228537410e0b14f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
