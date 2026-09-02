---
name: "rar-cowork-cookbook-demo-data-appropriate-budgets"
description: "Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_appropriate_budgets", "rar_sha256": "aa6886f42ad8c69e48194cb22222999ce4b5f9d2c9fb98d529e43391dbc47a1b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_appropriate_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-appropriate-budgets:f40510edd839cbe1f6396ee3f735691135e2b3c1d533cff8084e041a133e361a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_appropriate_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_appropriate_budgets_agent.py` is
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

Appropriate budgets Demo Data Generator — Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-appropriate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 aa6886f42ad8c69e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_appropriate_budgets_agent.py` first:

```bash
python3 demo_data_appropriate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_appropriate_budgets_agent.py   # or on stdin
python3 demo_data_appropriate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Appropriate budgets Demo Data Generator — Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-appropriate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_appropriate_budgets',
    "version": '2.0.0',
    "display_name": 'Appropriate budgets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-appropriate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-appropriate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '993295cf5c3b2419',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/appropriate-budgets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-appropriate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAppropriateBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAppropriateBudgets'
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
    print(DemoDataAppropriateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
