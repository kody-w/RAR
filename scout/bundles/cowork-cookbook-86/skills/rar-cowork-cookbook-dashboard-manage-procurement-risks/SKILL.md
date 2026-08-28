---
name: "rar-cowork-cookbook-dashboard-manage-procurement-risks"
description: "Produces a self-contained interactive HTML dashboard for manage procurement risks - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_procurement_risks", "rar_sha256": "2a16c9fbc426a91d27d5c4593b8ec0b8ce88a3bd814d5f3a9b6b06bdd128976f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 2a16c9fbc426a91d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_procurement_risks_agent.py` first:

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
    "version": '2.0.1',
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
