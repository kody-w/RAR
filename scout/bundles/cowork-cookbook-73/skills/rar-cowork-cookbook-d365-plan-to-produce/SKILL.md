---
name: "rar-cowork-cookbook-d365-plan-to-produce"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Plan to produce end-to-end process - covers 5 L2 areas and 30 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce", "rar_sha256": "6a87f9b46894475b65dceaee8ac8287a1cd09607d0b4bda05bb903a142d88362", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_plan_to_produce_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-plan-to-produce:123bdea62ec239f6f55240fc93ab1552d68cdf4b2c8aec667997032ed6c04902", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_plan_to_produce`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_plan_to_produce_agent.py` is
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
