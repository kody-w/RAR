---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-portals"
description: "Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_portals", "rar_sha256": "e9bd9a73424ee90cc4940877f63998890d75c892a12a2687cd1afa4fb1ce9ad7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_configure_and_manage_portals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-configure-and-manage-portals:1661770bd7d1286030ec5d46ceee6fad27e26bf50e198238df54f9368d9fb720", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_configure_and_manage_portals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_configure_and_manage_portals_agent.py` is
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
