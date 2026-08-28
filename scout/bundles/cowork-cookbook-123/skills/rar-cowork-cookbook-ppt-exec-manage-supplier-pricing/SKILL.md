---
name: "rar-cowork-cookbook-ppt-exec-manage-supplier-pricing"
description: "Generates an executive-ready PowerPoint deck on manage supplier pricing status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_supplier_pricing", "rar_sha256": "1b9c1d23f63330beb8b5c094b57596a9b1a78f8ffb2fcba8b55b460b0ba6bf7b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 1b9c1d23f63330be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_supplier_pricing_agent.py` first:

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
    "version": '2.0.1',
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
