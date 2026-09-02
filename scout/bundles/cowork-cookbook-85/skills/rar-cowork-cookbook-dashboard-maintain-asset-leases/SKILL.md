---
name: "rar-cowork-cookbook-dashboard-maintain-asset-leases"
description: "Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_asset_leases", "rar_sha256": "e8443302a96ef5a59abbbc4aef8159faf275ccef3669a579faf03dd0dee2e0e3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_maintain_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-maintain-asset-leases:4f7859494c102abf326c847d408297ec0fb27f5e1bd0cce7524770570e0e191d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_maintain_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_maintain_asset_leases_agent.py` is
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
