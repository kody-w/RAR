---
name: "rar-cowork-cookbook-dashboard-manage-lead-identification-process"
description: "Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_lead_identification_process", "rar_sha256": "900ca17d19457d53af1a5d280e223e6afa5358ab37326b00a55b99163cd39620", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_lead_identification_process_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-lead-identification-process:978d9f46d8618758fda7a84dc169fb2fc32508572f4c42f8502b067f6ffaf29b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_lead_identification_process`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_lead_identification_process_agent.py` is
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

Manage lead identification process Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 900ca17d19457d53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_lead_identification_process_agent.py` first:

```bash
python3 dashboard_manage_lead_identification_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_lead_identification_process_agent.py   # or on stdin
python3 dashboard_manage_lead_identification_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage lead identification process Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_lead_identification_process',
    "version": '2.0.0',
    "display_name": 'Manage lead identification process Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-lead-identification-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aef2cf17888ccb26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-manage-lead-identification-process', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageLeadIdentificationProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageLeadIdentificationProcess'
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
    print(DashboardManageLeadIdentificationProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
