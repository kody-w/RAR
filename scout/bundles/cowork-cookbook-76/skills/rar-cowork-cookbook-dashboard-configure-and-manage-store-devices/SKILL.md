---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-store-devices"
description: "Produces a self-contained interactive HTML dashboard for configure and manage store devices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_store_devices", "rar_sha256": "69b9874d022131f35a9a24879fdbcf22b3ee73145d0365feae0830222fea2037", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_configure_and_manage_store_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-configure-and-manage-store-devices:bfc2c1f98c1db74d5e1d70b24d046d7ab276f7fdcce5ecad4200e872f592d681", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_configure_and_manage_store_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_configure_and_manage_store_devices_agent.py` is
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
