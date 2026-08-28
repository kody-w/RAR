---
name: "rar-cowork-cookbook-stalled-opportunity-reengagement"
description: "Finds open opportunities with no recent activity and drafts a tailored re-engagement approach for each, so dormant deals get a deliberate next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stalled_opportunity_reengagement", "rar_sha256": "d72ba0991e8a63405ed186a11abd1b61f12ff1ee7071942182aea42a0de7f8e5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stalled_opportunity_reengagement`. The original RAPP
agent is preserved byte-for-byte in `stalled_opportunity_reengagement_agent.py` and in the RCI capsule.

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
