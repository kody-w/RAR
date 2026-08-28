---
name: "rar-cowork-cookbook-adaptive-card-manage-supplier-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_supplier_performance", "rar_sha256": "8a92d2aa71b4be771a504983497fb025d1707c2aeed0e2ecaf2af190569840bd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_supplier_performance_agent.py` and in the RCI capsule.

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

Manage supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 8a92d2aa71b4be77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_supplier_performance_agent.py` first:

```bash
python3 adaptive_card_manage_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_supplier_performance_agent.py   # or on stdin
python3 adaptive_card_manage_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_supplier_performance',
    "version": '2.0.0',
    "display_name": 'Manage supplier performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4eaf49ac79a364f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-supplier-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-manage-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageSupplierPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageSupplierPerformance'
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
    print(AdaptiveCardManageSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
