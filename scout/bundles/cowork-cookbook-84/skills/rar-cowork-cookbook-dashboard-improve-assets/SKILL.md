---
name: "rar-cowork-cookbook-dashboard-improve-assets"
description: "Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_improve_assets", "rar_sha256": "b24a712b65054e8dab1368bc92bca17b3d363ee82275c3869dce2ce1e255dad3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_improve_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_improve_assets_agent.py` and in the RCI capsule.

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
