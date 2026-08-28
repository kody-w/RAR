---
name: "rar-cowork-cookbook-dashboard-replace-an-asset"
description: "Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_replace_an_asset", "rar_sha256": "dbe2bf5a39383ca13481c7788b1f8c31c6ecd2d692f5912a52f486d7fb6c5418", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_replace_an_asset`. The original RAPP
agent is preserved byte-for-byte in `dashboard_replace_an_asset_agent.py` and in the RCI capsule.

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

Replace an asset Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-replace-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 dbe2bf5a39383ca1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_replace_an_asset_agent.py` first:

```bash
python3 dashboard_replace_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_replace_an_asset_agent.py   # or on stdin
python3 dashboard_replace_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Replace an asset Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-replace-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_replace_an_asset',
    "version": '2.0.1',
    "display_name": 'Replace an asset Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-replace-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-replace-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1729444ecdddc1be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/replace-an-asset'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-replace-an-asset', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardReplaceAnAsset(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReplaceAnAsset'
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
    print(DashboardReplaceAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
