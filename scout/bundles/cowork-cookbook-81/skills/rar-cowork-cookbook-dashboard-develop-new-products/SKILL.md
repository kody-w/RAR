---
name: "rar-cowork-cookbook-dashboard-develop-new-products"
description: "Produces a self-contained interactive HTML dashboard for develop new products - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_new_products", "rar_sha256": "b8fb51bc714ffbf8093a6fd500d048ea7fcaac5927e3943d1f99ac98e8da464d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 b8fb51bc714ffbf8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_new_products_agent.py` first:

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
    "version": '2.0.1',
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
