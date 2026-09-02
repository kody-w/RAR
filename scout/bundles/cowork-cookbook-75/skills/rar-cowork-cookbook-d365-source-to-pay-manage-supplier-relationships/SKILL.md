---
name: "rar-cowork-cookbook-d365-source-to-pay-manage-supplier-relationships"
description: "A Dynamics 365 F&SCM expert scoped to the Manage supplier relationships area (a level-2 subdomain of Source to pay) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships", "rar_sha256": "ded65032d7f063f83da2ccc9a96b34e9d68f047a06dd83e8593cf30b39f7537b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_source_to_pay_manage_supplier_relationships_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-source-to-pay-manage-supplier-relationships:0ca65bc12f459eb42d2c43eb93f73f7b2ce30a0f5de5dba858aae0259073b273", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_source_to_pay_manage_supplier_relationships_agent.py` is
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
