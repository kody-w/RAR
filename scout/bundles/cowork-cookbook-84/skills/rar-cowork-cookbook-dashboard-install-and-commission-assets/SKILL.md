---
name: "rar-cowork-cookbook-dashboard-install-and-commission-assets"
description: "Produces a self-contained interactive HTML dashboard for install and commission assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_install_and_commission_assets", "rar_sha256": "76f639527c416774ccacd2f5575431e3fe65dc9a0f6dfb2335406718bb86901c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_install_and_commission_assets_agent.py` and embedded as the fenced Python below (sha256 76f639527c416774…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_install_and_commission_assets_agent.py` first:

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
    "version": '2.0.0',
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
