---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-portals"
description: "Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_portals", "rar_sha256": "e9bd9a73424ee90cc4940877f63998890d75c892a12a2687cd1afa4fb1ce9ad7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_portals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_portals_agent.py` and in the RCI capsule.

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

Configure and manage portals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 e9bd9a73424ee90c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_portals_agent.py` first:

```bash
python3 dashboard_configure_and_manage_portals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_portals_agent.py   # or on stdin
python3 dashboard_configure_and_manage_portals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage portals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_portals',
    "version": '2.0.0',
    "display_name": 'Configure and manage portals Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-configure-and-manage-portals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9bc5455755650843',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-portals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-portals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardConfigureAndManagePortals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManagePortals'
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
    print(DashboardConfigureAndManagePortals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
