---
name: "rar-cowork-cookbook-d365-source-to-pay-manage-supplier-relationships"
description: "A Dynamics 365 F&SCM expert scoped to the Manage supplier relationships area (a level-2 subdomain of Source to pay) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships", "rar_sha256": "b9d47fb93a6f9e30b073648c11ec1ba3d9a92245285c7c4709a25bb3a91c23a4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_manage_supplier_relationships_agent.py` and embedded as the fenced Python below (sha256 b9d47fb93a6f9e30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_manage_supplier_relationships_agent.py` first:

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
    "version": '2.0.1',
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
