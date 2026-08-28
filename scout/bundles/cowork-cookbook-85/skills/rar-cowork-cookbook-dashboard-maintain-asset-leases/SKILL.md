---
name: "rar-cowork-cookbook-dashboard-maintain-asset-leases"
description: "Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_asset_leases", "rar_sha256": "e8443302a96ef5a59abbbc4aef8159faf275ccef3669a579faf03dd0dee2e0e3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_asset_leases_agent.py` and in the RCI capsule.

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

Maintain asset leases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 e8443302a96ef5a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_asset_leases_agent.py` first:

```bash
python3 dashboard_maintain_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_asset_leases_agent.py   # or on stdin
python3 dashboard_maintain_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain asset leases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_asset_leases',
    "version": '2.0.0',
    "display_name": 'Maintain asset leases Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-maintain-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5f172e71398d16c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-asset-leases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-maintain-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardMaintainAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAssetLeases'
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
    print(DashboardMaintainAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
