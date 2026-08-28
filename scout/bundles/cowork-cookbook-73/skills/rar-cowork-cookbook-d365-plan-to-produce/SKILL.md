---
name: "rar-cowork-cookbook-d365-plan-to-produce"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Plan to produce end-to-end process - covers 5 L2 areas and 30 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce", "rar_sha256": "6a87f9b46894475b65dceaee8ac8287a1cd09607d0b4bda05bb903a142d88362", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_plan_to_produce`. The original RAPP
agent is preserved byte-for-byte in `d365_plan_to_produce_agent.py` and in the RCI capsule.

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

D365 Plan to produce Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Plan to produce end-to-end process - covers 5 L2 areas and 30 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_agent.py` and embedded as the fenced Python below (sha256 6a87f9b46894475b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_agent.py` first:

```bash
python3 d365_plan_to_produce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_plan_to_produce_agent.py   # or on stdin
python3 d365_plan_to_produce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Plan to produce Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Plan to produce end-to-end process - covers 5 L2 areas and 30 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_plan_to_produce',
    "version": '2.0.0',
    "display_name": 'D365 Plan to produce Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Plan to produce end-to-end process - covers 5 L2 areas and 30 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-plan-to-produce',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-plan-to-produce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c35ff720ac0f9bbc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'plan-to-produce/d365-plan-to-produce', 'uses_skills': {'custom': ['d365-plan-to-produce'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365PlanToProduce(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365PlanToProduce'
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
    print(D365PlanToProduce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
