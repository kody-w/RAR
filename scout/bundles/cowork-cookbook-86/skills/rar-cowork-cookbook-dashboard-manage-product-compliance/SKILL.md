---
name: "rar-cowork-cookbook-dashboard-manage-product-compliance"
description: "Produces a self-contained interactive HTML dashboard for manage product compliance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_product_compliance", "rar_sha256": "f639a07240f66c8af63e5f8af864e1caef8816f8d8b03a546d43ed7b263b4498", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_product_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-product-compliance:ab5eba16a5837f0bb81089609c674b195fd243457175505d2abc274cedbc6f9f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_product_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_product_compliance_agent.py` is
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
