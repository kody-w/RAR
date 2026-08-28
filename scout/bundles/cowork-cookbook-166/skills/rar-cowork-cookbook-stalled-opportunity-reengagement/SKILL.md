---
name: "rar-cowork-cookbook-stalled-opportunity-reengagement"
description: "Finds open opportunities with no recent activity and drafts a tailored re-engagement approach for each, so dormant deals get a deliberate next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stalled_opportunity_reengagement", "rar_sha256": "1fc8b85de55701104f9a785b8d931084c36a68bcc85a2d00bb81f6af8a74900b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stalled_opportunity_reengagement_agent.py` and embedded as the fenced Python below (sha256 1fc8b85de5570110…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stalled_opportunity_reengagement_agent.py` first:

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
    "version": '2.0.1',
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
