---
name: "rar-cowork-cookbook-dashboard-define-product-policies"
description: "Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_product_policies", "rar_sha256": "b6fd7407953c28858dd38d070c8eda12a416d95e5c8a361e1dea865449909b33", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_product_policies_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 b6fd7407953c2885…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_product_policies_agent.py` first:

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
    "version": '2.0.1',
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
