---
name: "rar-cowork-cookbook-dashboard-replace-an-asset"
description: "Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_replace_an_asset", "rar_sha256": "7ff5bb0d3efe3bce4c4442fdd57ee76112c2976df098db6d791f567459fe3941", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 7ff5bb0d3efe3bce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_replace_an_asset_agent.py` first:

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
    "version": '2.0.0',
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
