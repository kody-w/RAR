---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-store-devices"
description: "Produces a self-contained interactive HTML dashboard for configure and manage store devices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_store_devices", "rar_sha256": "69b9874d022131f35a9a24879fdbcf22b3ee73145d0365feae0830222fea2037", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_store_devices_agent.py` and embedded as the fenced Python below (sha256 69b9874d022131f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_store_devices_agent.py` first:

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
    "version": '2.0.0',
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
