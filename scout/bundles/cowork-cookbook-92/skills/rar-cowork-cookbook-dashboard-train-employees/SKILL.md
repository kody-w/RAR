---
name: "rar-cowork-cookbook-dashboard-train-employees"
description: "Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_train_employees", "rar_sha256": "d5da57c49c4e0a775574b606314363eed58888460b37702219520cf753dba550", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_train_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-train-employees:cf5220a503367e70ecceb9acc348f72f980d2677f15b0e9566fc31befe4ac69d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_train_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_train_employees_agent.py` is
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

Train employees Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-train-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_train_employees_agent.py` and embedded as the fenced Python below (sha256 d5da57c49c4e0a77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_train_employees_agent.py` first:

```bash
python3 dashboard_train_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_train_employees_agent.py   # or on stdin
python3 dashboard_train_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Train employees Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-train-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_train_employees',
    "version": '2.0.0',
    "display_name": 'Train employees Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-train-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-train-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a18802e620861b87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/train-employees'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-train-employees', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardTrainEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTrainEmployees'
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
    print(DashboardTrainEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
