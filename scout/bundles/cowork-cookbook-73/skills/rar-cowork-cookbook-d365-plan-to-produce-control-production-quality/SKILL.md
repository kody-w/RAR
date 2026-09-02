---
name: "rar-cowork-cookbook-d365-plan-to-produce-control-production-quality"
description: "A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce_control_production_quality", "rar_sha256": "0300a0b47e6e6e1540b3ec1913f2894d9f32b8c39432e1453da882750777a063", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_plan_to_produce_control_production_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-plan-to-produce-control-production-quality:734ca9a74e2844ead9cf2d753ac080bf9e3a00d2a903eefba5813c1c63ac2e28", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_plan_to_produce_control_production_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_plan_to_produce_control_production_quality_agent.py` is
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

D365 Control production quality Expert — A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_control_production_quality_agent.py` and embedded as the fenced Python below (sha256 0300a0b47e6e6e15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_control_production_quality_agent.py` first:

```bash
python3 d365_plan_to_produce_control_production_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_plan_to_produce_control_production_quality_agent.py   # or on stdin
python3 d365_plan_to_produce_control_production_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Control production quality Expert — A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_plan_to_produce_control_production_quality',
    "version": '2.0.0',
    "display_name": 'D365 Control production quality Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes.',
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
        "upstream_slug": 'd365-plan-to-produce-control-production-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a6e6b6671934857',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'plan-to-produce/d365-plan-to-produce-control-production-quality', 'uses_skills': {'custom': ['d365-plan-to-produce-control-production-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365PlanToProduceControlProductionQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365PlanToProduceControlProductionQuality'
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
    print(D365PlanToProduceControlProductionQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
