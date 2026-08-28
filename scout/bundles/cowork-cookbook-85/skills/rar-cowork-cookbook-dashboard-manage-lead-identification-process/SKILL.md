---
name: "rar-cowork-cookbook-dashboard-manage-lead-identification-process"
description: "Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_lead_identification_process", "rar_sha256": "900ca17d19457d53af1a5d280e223e6afa5358ab37326b00a55b99163cd39620", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_lead_identification_process`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_lead_identification_process_agent.py` and in the RCI capsule.

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
