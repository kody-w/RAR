---
name: "rar-cowork-cookbook-adaptive-card-subcontract-production"
description: "Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_subcontract_production", "rar_sha256": "68fb1529ce4397d4668abe8320ced359ece56aa6970d2fb0ec09f78e3dcd1cd3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_subcontract_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-subcontract-production:367b2e8bc630441a8092d576dcdadaa6ec37bc62d01a6cafad68e8285b136dba", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_subcontract_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_subcontract_production_agent.py` is
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

Subcontract production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-subcontract-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 68fb1529ce4397d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_subcontract_production_agent.py` first:

```bash
python3 adaptive_card_subcontract_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_subcontract_production_agent.py   # or on stdin
python3 adaptive_card_subcontract_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-subcontract-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_subcontract_production',
    "version": '2.0.0',
    "display_name": 'Subcontract production Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-subcontract-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-subcontract-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f75505b2fd3a03ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/subcontract-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-subcontract-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardSubcontractProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSubcontractProduction'
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
    print(AdaptiveCardSubcontractProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
