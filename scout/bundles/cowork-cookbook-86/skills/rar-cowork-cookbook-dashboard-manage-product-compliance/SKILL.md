---
name: "rar-cowork-cookbook-dashboard-manage-product-compliance"
description: "Produces a self-contained interactive HTML dashboard for manage product compliance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_product_compliance", "rar_sha256": "f639a07240f66c8af63e5f8af864e1caef8816f8d8b03a546d43ed7b263b4498", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_product_compliance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_product_compliance_agent.py` and in the RCI capsule.

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

Manage product compliance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage product compliance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-product-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 f639a07240f66c8a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_product_compliance_agent.py` first:

```bash
python3 dashboard_manage_product_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_product_compliance_agent.py   # or on stdin
python3 dashboard_manage_product_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product compliance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage product compliance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-product-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_product_compliance',
    "version": '2.0.0',
    "display_name": 'Manage product compliance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage product compliance - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-product-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-product-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b6fa0286eaa2bd64',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-compliance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-manage-product-compliance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageProductCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageProductCompliance'
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
    print(DashboardManageProductCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
