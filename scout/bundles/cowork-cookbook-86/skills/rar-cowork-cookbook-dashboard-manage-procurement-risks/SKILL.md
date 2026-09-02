---
name: "rar-cowork-cookbook-dashboard-manage-procurement-risks"
description: "Produces a self-contained interactive HTML dashboard for manage procurement risks - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_procurement_risks", "rar_sha256": "5e9f4d875ea551765e9a24fb548fc277be7cd430236c242829c0c31e70d733d4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_procurement_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-procurement-risks:63c9ee3b0fe6fcdaecace47d63a430fdad3c0982c466aea78687055ab220085c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_procurement_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_procurement_risks_agent.py` is
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
