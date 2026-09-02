---
name: "rar-cowork-cookbook-ppt-exec-manage-supplier-pricing"
description: "Generates an executive-ready PowerPoint deck on manage supplier pricing status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_supplier_pricing", "rar_sha256": "6402a017d03f78f78eed38e3ae82a288e019dfd4eaeecd9bb8b989f62affc55c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_supplier_pricing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-supplier-pricing:5447b09ef510cda943131d6b72021e59b8f720a1e57a2e5d62ac9e276cad20f2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_supplier_pricing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_supplier_pricing_agent.py` is
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

Manage supplier pricing Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage supplier pricing status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-supplier-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 6402a017d03f78f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_supplier_pricing_agent.py` first:

```bash
python3 ppt_exec_manage_supplier_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_supplier_pricing_agent.py   # or on stdin
python3 ppt_exec_manage_supplier_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier pricing Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage supplier pricing status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-supplier-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_supplier_pricing',
    "version": '2.0.0',
    "display_name": 'Manage supplier pricing Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage supplier pricing status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-supplier-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-supplier-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b27d875c676dfd6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-pricing'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-manage-supplier-pricing', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecManageSupplierPricing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageSupplierPricing'
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
    print(PptExecManageSupplierPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
