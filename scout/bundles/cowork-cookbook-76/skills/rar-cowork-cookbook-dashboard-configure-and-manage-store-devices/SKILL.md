---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-store-devices"
description: "Produces a self-contained interactive HTML dashboard for configure and manage store devices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_store_devices", "rar_sha256": "40c7d4ca1a269ef870a867d4647a7d49c9a4c5a9e7bb84b57fbc42bb63dc1df3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_store_devices`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_store_devices_agent.py` and in the RCI capsule.

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

Configure and manage store devices Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage store devices - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-store-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_store_devices_agent.py` and embedded as the fenced Python below (sha256 40c7d4ca1a269ef8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_store_devices_agent.py` first:

```bash
python3 dashboard_configure_and_manage_store_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_store_devices_agent.py   # or on stdin
python3 dashboard_configure_and_manage_store_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage store devices Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage store devices - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-store-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_store_devices',
    "version": '2.0.1',
    "display_name": 'Configure and manage store devices Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure and manage store devices - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-configure-and-manage-store-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-store-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14ac8681f9aeed5f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-store-devices'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-store-devices', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConfigureAndManageStoreDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManageStoreDevices'
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
    print(DashboardConfigureAndManageStoreDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
