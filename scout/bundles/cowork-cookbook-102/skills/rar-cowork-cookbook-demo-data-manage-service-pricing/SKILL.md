---
name: "rar-cowork-cookbook-demo-data-manage-service-pricing"
description: "Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_service_pricing", "rar_sha256": "aca92e6679888627bf996af9da39192d0ea92ba5d09204f681936cb69aa923f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_service_pricing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-service-pricing:970422df38e43a4249de788bb85498889189e03f15305c58bfc4ff8e7f8280eb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_service_pricing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_service_pricing_agent.py` is
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

Manage service pricing Demo Data Generator — Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-service-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 aca92e6679888627…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_service_pricing_agent.py` first:

```bash
python3 demo_data_manage_service_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_service_pricing_agent.py   # or on stdin
python3 demo_data_manage_service_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service pricing Demo Data Generator — Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-service-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_service_pricing',
    "version": '2.0.0',
    "display_name": 'Manage service pricing Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-service-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-service-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa378eb644197120',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-service-pricing'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-manage-service-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataManageServicePricing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageServicePricing'
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
    print(DemoDataManageServicePricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
