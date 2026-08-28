---
name: "rar-cowork-cookbook-dashboard-release-production-to-the-shop-floor"
description: "Produces a self-contained interactive HTML dashboard for release production to the shop floor - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_release_production_to_the_shop_floor", "rar_sha256": "04a47ddc9a3a1dd2e24a89d7ff94ebbcbebaabef788bdb670fd76bfb074243b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_release_production_to_the_shop_floor_agent.py` and embedded as the fenced Python below (sha256 04a47ddc9a3a1dd2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_release_production_to_the_shop_floor_agent.py` first:

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
    "version": '2.0.0',
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
