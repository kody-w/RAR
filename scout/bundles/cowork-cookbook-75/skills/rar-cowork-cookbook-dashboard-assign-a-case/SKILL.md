---
name: "rar-cowork-cookbook-dashboard-assign-a-case"
description: "Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_a_case", "rar_sha256": "18cc806b3e7f12d9baf20810f4f47895aa89db9ea435aaa81bcb25819efc0779", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_assign_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-assign-a-case:fdeb04c797fd7d505aba7c7528ae48e91e2fc385a3241000639ed97841e0aa48", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_assign_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_assign_a_case_agent.py` is
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

Assign a case Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 18cc806b3e7f12d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_a_case_agent.py` first:

```bash
python3 dashboard_assign_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_a_case_agent.py   # or on stdin
python3 dashboard_assign_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign a case Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_a_case',
    "version": '2.0.0',
    "display_name": 'Assign a case Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-assign-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0eac7efdfc4f2899',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/assign-a-case'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-assign-a-case', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAssignACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignACase'
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
    print(DashboardAssignACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
