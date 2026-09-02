---
name: "rar-cowork-cookbook-dashboard-define-product-policies"
description: "Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_product_policies", "rar_sha256": "5eabbc8a4aca2688163d7786093e0d763cd49b02d2b844a11f347620308c9e28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_product_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-product-policies:5d69da0d9e2c5f40bc03972ebfd738cd4c6200d51798e2e6ecd8de31dc70ce02", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_product_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_product_policies_agent.py` is
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

Define product policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 5eabbc8a4aca2688…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_product_policies_agent.py` first:

```bash
python3 dashboard_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_product_policies_agent.py   # or on stdin
python3 dashboard_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_product_policies',
    "version": '2.0.0',
    "display_name": 'Define product policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '00e901a3587309bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineProductPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineProductPolicies'
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
    print(DashboardDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
