---
name: "rar-cowork-cookbook-dashboard-manage-product-compliance"
description: "Produces a self-contained interactive HTML dashboard for manage product compliance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_product_compliance", "rar_sha256": "f082348e2e2e63e9a3b5ac19f5f6818eb5f1633eafec4a10c4b6c71db851f863", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 f082348e2e2e63e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_product_compliance_agent.py` first:

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
    "version": '2.0.1',
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
