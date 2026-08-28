---
name: "rar-cowork-cookbook-dashboard-release-production-to-the-shop-floor"
description: "Produces a self-contained interactive HTML dashboard for release production to the shop floor - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_release_production_to_the_shop_floor", "rar_sha256": "c9c40c22debcc7ff47363bf755032d7957d6c16842eb25ed4aeb1eab5cfe90cc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_release_production_to_the_shop_floor`. The original RAPP
agent is preserved byte-for-byte in `dashboard_release_production_to_the_shop_floor_agent.py` and in the RCI capsule.

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

Release production to the shop floor Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for release production to the shop floor - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-release-production-to-the-shop-floor
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_release_production_to_the_shop_floor_agent.py` and embedded as the fenced Python below (sha256 c9c40c22debcc7ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_release_production_to_the_shop_floor_agent.py` first:

```bash
python3 dashboard_release_production_to_the_shop_floor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_release_production_to_the_shop_floor_agent.py   # or on stdin
python3 dashboard_release_production_to_the_shop_floor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release production to the shop floor Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for release production to the shop floor - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-release-production-to-the-shop-floor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_release_production_to_the_shop_floor',
    "version": '2.0.1',
    "display_name": 'Release production to the shop floor Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for release production to the shop floor - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-release-production-to-the-shop-floor',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-release-production-to-the-shop-floor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77a76285666a1b3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/release-production-to-the-shop-floor'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-release-production-to-the-shop-floor', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardReleaseProductionToTheShopFloor(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReleaseProductionToTheShopFloor'
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
    print(DashboardReleaseProductionToTheShopFloor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
