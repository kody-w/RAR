---
name: "rar-cowork-cookbook-sales-target-attainment-tracker"
description: "Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_target_attainment_tracker", "rar_sha256": "61a05f8683189cac5bf4ff1e4f87e9c77c74383ffe40ff15c180f48dd3377b11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "sales_target_attainment_tracker_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/sales-target-attainment-tracker:b544c1e6858ef766fc26b2215fa27e594103dacb099336d8081072f0cbc181cc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/sales_target_attainment_tracker`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `sales_target_attainment_tracker_agent.py` is
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

Sales Target Attainment Tracker — Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-target-attainment-tracker
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_target_attainment_tracker_agent.py` and embedded as the fenced Python below (sha256 61a05f8683189cac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_target_attainment_tracker_agent.py` first:

```bash
python3 sales_target_attainment_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_target_attainment_tracker_agent.py   # or on stdin
python3 sales_target_attainment_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Target Attainment Tracker — Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-target-attainment-tracker
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/sales_target_attainment_tracker',
    "version": '2.0.0',
    "display_name": 'Sales Target Attainment Tracker',
    "description": 'Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'sales-target-attainment-tracker',
        "upstream_url": 'https://coworkcookbook.com/recipes/sales-target-attainment-tracker',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdb5fea7012d7cfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/sales-target-attainment-tracker', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:pipeline'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class SalesTargetAttainmentTracker(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SalesTargetAttainmentTracker'
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
    print(SalesTargetAttainmentTracker().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
