---
name: "rar-cowork-cookbook-dashboard-install-and-commission-assets"
description: "Produces a self-contained interactive HTML dashboard for install and commission assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_install_and_commission_assets", "rar_sha256": "76f639527c416774ccacd2f5575431e3fe65dc9a0f6dfb2335406718bb86901c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_install_and_commission_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-install-and-commission-assets:e5444d724fc9e440b54fd6802c8e1fe37261e2f1da908fe6ccaa2fc35e5c2691", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_install_and_commission_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_install_and_commission_assets_agent.py` is
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
