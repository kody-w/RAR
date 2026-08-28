---
name: "rar-cowork-cookbook-ppt-exec-manage-supplier-pricing"
description: "Generates an executive-ready PowerPoint deck on manage supplier pricing status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_supplier_pricing", "rar_sha256": "6402a017d03f78f78eed38e3ae82a288e019dfd4eaeecd9bb8b989f62affc55c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_supplier_pricing`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_supplier_pricing_agent.py` and in the RCI capsule.

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
