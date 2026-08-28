---
name: "rar-cowork-cookbook-d365-source-to-pay-manage-supplier-relationships"
description: "A Dynamics 365 F&SCM expert scoped to the Manage supplier relationships area (a level-2 subdomain of Source to pay) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships", "rar_sha256": "ded65032d7f063f83da2ccc9a96b34e9d68f047a06dd83e8593cf30b39f7537b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships`. The original RAPP
agent is preserved byte-for-byte in `d365_source_to_pay_manage_supplier_relationships_agent.py` and in the RCI capsule.

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

D365 Manage supplier relationships Expert — A Dynamics 365 F&SCM expert scoped to the Manage supplier relationships area (a level-2 subdomain of Source to pay) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay-manage-supplier-relationships
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_manage_supplier_relationships_agent.py` and embedded as the fenced Python below (sha256 ded65032d7f063f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_manage_supplier_relationships_agent.py` first:

```bash
python3 d365_source_to_pay_manage_supplier_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_source_to_pay_manage_supplier_relationships_agent.py   # or on stdin
python3 d365_source_to_pay_manage_supplier_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage supplier relationships Expert — A Dynamics 365 F&SCM expert scoped to the Manage supplier relationships area (a level-2 subdomain of Source to pay) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay-manage-supplier-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships',
    "version": '2.0.0',
    "display_name": 'D365 Manage supplier relationships Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage supplier relationships area (a level-2 subdomain of Source to pay) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-source-to-pay-manage-supplier-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-source-to-pay-manage-supplier-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '61c77d24ea23efc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/d365-source-to-pay-manage-supplier-relationships', 'uses_skills': {'custom': ['d365-source-to-pay-manage-supplier-relationships'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365SourceToPayManageSupplierRelationships(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365SourceToPayManageSupplierRelationships'
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
    print(D365SourceToPayManageSupplierRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
