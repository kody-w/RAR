---
name: "rar-cowork-cookbook-d365-plan-to-produce"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Plan to produce end-to-end process - covers 5 L2 areas and 30 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce", "rar_sha256": "db93fc493fb4f8a948b1bec17d2db14cc7875425ec6a4c5911119a49e1e7eb31", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_agent.py` and embedded as the fenced Python below (sha256 db93fc493fb4f8a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_agent.py` first:

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
    "version": '2.0.1',
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
