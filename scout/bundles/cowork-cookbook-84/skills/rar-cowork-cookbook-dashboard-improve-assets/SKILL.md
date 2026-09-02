---
name: "rar-cowork-cookbook-dashboard-improve-assets"
description: "Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_improve_assets", "rar_sha256": "b24a712b65054e8dab1368bc92bca17b3d363ee82275c3869dce2ce1e255dad3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_improve_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-improve-assets:1dd7f21f792d177a367822b9e2910548d3994dfe3d3d1233a63d7c9378c200b8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_improve_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_improve_assets_agent.py` is
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

Improve assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-improve-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_improve_assets_agent.py` and embedded as the fenced Python below (sha256 b24a712b65054e8d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_improve_assets_agent.py` first:

```bash
python3 dashboard_improve_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_improve_assets_agent.py   # or on stdin
python3 dashboard_improve_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Improve assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-improve-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_improve_assets',
    "version": '2.0.0',
    "display_name": 'Improve assets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-improve-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-improve-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cac617b8558a1329',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/improve-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-improve-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardImproveAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImproveAssets'
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
    print(DashboardImproveAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
