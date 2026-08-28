---
name: "rar-cowork-cookbook-dashboard-manage-procurement-risks"
description: "Produces a self-contained interactive HTML dashboard for manage procurement risks - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_procurement_risks", "rar_sha256": "5e9f4d875ea551765e9a24fb548fc277be7cd430236c242829c0c31e70d733d4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_procurement_risks`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_procurement_risks_agent.py` and in the RCI capsule.

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

Manage procurement risks Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage procurement risks - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 5e9f4d875ea55176…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_procurement_risks_agent.py` first:

```bash
python3 dashboard_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_procurement_risks_agent.py   # or on stdin
python3 dashboard_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage procurement risks - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_procurement_risks',
    "version": '2.0.0',
    "display_name": 'Manage procurement risks Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage procurement risks - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '347101b42a7b5dc9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageProcurementRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageProcurementRisks'
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
    print(DashboardManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
