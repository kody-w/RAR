---
name: "rar-cowork-cookbook-adaptive-card-manage-supplier-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_supplier_performance", "rar_sha256": "8a92d2aa71b4be771a504983497fb025d1707c2aeed0e2ecaf2af190569840bd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_supplier_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-supplier-performance:ea9415ecafb10cf9dc1e678a927971f6edfc1897c33db91bc51945dc2db88d4e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_supplier_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_supplier_performance_agent.py` is
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
