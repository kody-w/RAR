---
name: "rar-cowork-cookbook-dashboard-retire-software-licenses"
description: "Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_software_licenses", "rar_sha256": "b3992c1b6102e6c9867de725a7841c80599ae0669c93c61a124962e737c89293", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_retire_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `dashboard_retire_software_licenses_agent.py` and in the RCI capsule.

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

Retire software licenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 b3992c1b6102e6c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_software_licenses_agent.py` first:

```bash
python3 dashboard_retire_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_software_licenses_agent.py   # or on stdin
python3 dashboard_retire_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire software licenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_software_licenses',
    "version": '2.0.1',
    "display_name": 'Retire software licenses Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-retire-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93cd5747bf498122',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/retire-software-licenses'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-retire-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRetireSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireSoftwareLicenses'
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
    print(DashboardRetireSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
