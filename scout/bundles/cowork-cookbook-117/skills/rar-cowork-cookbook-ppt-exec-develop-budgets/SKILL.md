---
name: "rar-cowork-cookbook-ppt-exec-develop-budgets"
description: "Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_budgets", "rar_sha256": "6908d1b13b7fa16f2a96d1a556f837eafe6d4a3eaa716f21495035f07bbcfe7c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-budgets:34e873ca7251162f3bd201414a56b6d32509598f25937c9ce321029ace756e72", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_budgets_agent.py` is
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

Develop budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 6908d1b13b7fa16f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_budgets_agent.py` first:

```bash
python3 ppt_exec_develop_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_budgets_agent.py   # or on stdin
python3 ppt_exec_develop_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_budgets',
    "version": '2.0.0',
    "display_name": 'Develop budgets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28284d3021c43063',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/develop-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-develop-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopBudgets'
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
    print(PptExecDevelopBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
