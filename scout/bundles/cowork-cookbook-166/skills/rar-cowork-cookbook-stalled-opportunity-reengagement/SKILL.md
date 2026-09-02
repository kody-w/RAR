---
name: "rar-cowork-cookbook-stalled-opportunity-reengagement"
description: "Finds open opportunities with no recent activity and drafts a tailored re-engagement approach for each, so dormant deals get a deliberate next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stalled_opportunity_reengagement", "rar_sha256": "d72ba0991e8a63405ed186a11abd1b61f12ff1ee7071942182aea42a0de7f8e5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "stalled_opportunity_reengagement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/stalled-opportunity-reengagement:63d304d6252a8cacac5a4028770bd6cc3c8f6702a8da8a9f98f8dfe3380d4d13", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/stalled_opportunity_reengagement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `stalled_opportunity_reengagement_agent.py` is
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

Stalled Opportunity Re-Engagement List — Finds open opportunities with no recent activity and drafts a tailored re-engagement approach for each, so dormant deals get a deliberate next step.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stalled-opportunity-reengagement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stalled_opportunity_reengagement_agent.py` and embedded as the fenced Python below (sha256 d72ba0991e8a6340…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stalled_opportunity_reengagement_agent.py` first:

```bash
python3 stalled_opportunity_reengagement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stalled_opportunity_reengagement_agent.py   # or on stdin
python3 stalled_opportunity_reengagement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stalled Opportunity Re-Engagement List — Finds open opportunities with no recent activity and drafts a tailored re-engagement approach for each, so dormant deals get a deliberate next step.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stalled-opportunity-reengagement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stalled_opportunity_reengagement',
    "version": '2.0.0',
    "display_name": 'Stalled Opportunity Re-Engagement List',
    "description": 'Finds open opportunities with no recent activity and drafts a tailored re-engagement approach for each, so dormant deals get a deliberate next step.',
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
        "upstream_slug": 'stalled-opportunity-reengagement',
        "upstream_url": 'https://coworkcookbook.com/recipes/stalled-opportunity-reengagement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c6fcf710a3498b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/stalled-opportunity-reengagement', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Communications'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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


class StalledOpportunityReengagement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StalledOpportunityReengagement'
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
    print(StalledOpportunityReengagement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
