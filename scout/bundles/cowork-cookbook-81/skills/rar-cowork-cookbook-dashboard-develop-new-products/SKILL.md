---
name: "rar-cowork-cookbook-dashboard-develop-new-products"
description: "Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_new_products", "rar_sha256": "d9df357452aa25d635f94ab5e736393939ea102eeaea0972095941683cab5646", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_new_products`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_new_products_agent.py` and in the RCI capsule.

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

Develop new products Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 d9df357452aa25d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_new_products_agent.py` first:

```bash
python3 dashboard_develop_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_new_products_agent.py   # or on stdin
python3 dashboard_develop_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new products Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_new_products',
    "version": '2.0.0',
    "display_name": 'Develop new products Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-develop-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9be9227ee6aa189',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/develop-new-products'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-develop-new-products', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopNewProducts'
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
    print(DashboardDevelopNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
