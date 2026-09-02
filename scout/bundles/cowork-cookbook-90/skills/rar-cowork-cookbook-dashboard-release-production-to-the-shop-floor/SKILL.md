---
name: "rar-cowork-cookbook-dashboard-release-production-to-the-shop-floor"
description: "Produces a self-contained interactive HTML dashboard for release production to the shop floor - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_release_production_to_the_shop_floor", "rar_sha256": "04a47ddc9a3a1dd2e24a89d7ff94ebbcbebaabef788bdb670fd76bfb074243b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_release_production_to_the_shop_floor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-release-production-to-the-shop-floor:c6053086ca08a85bc6f88245aab00bb5dab68580ad09fc235ee46f1d6744894b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_release_production_to_the_shop_floor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_release_production_to_the_shop_floor_agent.py` is
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
