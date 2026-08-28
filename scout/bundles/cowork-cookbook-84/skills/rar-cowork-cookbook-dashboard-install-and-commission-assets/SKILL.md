---
name: "rar-cowork-cookbook-dashboard-install-and-commission-assets"
description: "Produces a self-contained interactive HTML dashboard for install and commission assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_install_and_commission_assets", "rar_sha256": "44a708178601b0c4eb5a17a0fc05cd69cc816d1be5c9d1b02f91f0adf087d1f0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_install_and_commission_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_install_and_commission_assets_agent.py` and in the RCI capsule.

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

Install and commission assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for install and commission assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-install-and-commission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_install_and_commission_assets_agent.py` and embedded as the fenced Python below (sha256 44a708178601b0c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_install_and_commission_assets_agent.py` first:

```bash
python3 dashboard_install_and_commission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_install_and_commission_assets_agent.py   # or on stdin
python3 dashboard_install_and_commission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Install and commission assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for install and commission assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-install-and-commission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_install_and_commission_assets',
    "version": '2.0.1',
    "display_name": 'Install and commission assets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for install and commission assets - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-install-and-commission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-install-and-commission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cabf7554c892d1ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/install-and-commission-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-install-and-commission-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardInstallAndCommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardInstallAndCommissionAssets'
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
    print(DashboardInstallAndCommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
