---
name: "rar-cowork-cookbook-adaptive-card-identify-opportunity"
description: "Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_opportunity", "rar_sha256": "10504ef24266b33e7185d853b3f51ced8d394cec126fb73a949530d191d78398", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_identify_opportunity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-identify-opportunity:5c05e7989647ee6656a0639cdab9687fa98583fefaf8d5a4f269f40cbd1d470d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_identify_opportunity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_identify_opportunity_agent.py` is
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

Identify opportunity Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 10504ef24266b33e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_opportunity_agent.py` first:

```bash
python3 adaptive_card_identify_opportunity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_opportunity_agent.py   # or on stdin
python3 adaptive_card_identify_opportunity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify opportunity Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_opportunity',
    "version": '2.0.0',
    "display_name": 'Identify opportunity Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify opportunity status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-opportunity',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17b202234e375ae7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/identify-opportunity'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-identify-opportunity', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardIdentifyOpportunity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyOpportunity'
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
    print(AdaptiveCardIdentifyOpportunity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
