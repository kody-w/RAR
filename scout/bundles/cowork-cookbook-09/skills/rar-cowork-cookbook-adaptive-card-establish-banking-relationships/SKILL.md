---
name: "rar-cowork-cookbook-adaptive-card-establish-banking-relationships"
description: "Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_banking_relationships", "rar_sha256": "c72ec9ba0105be9a5d4d8fa1ca6f29381bd13c91e1880ff68a6735697cdc6030", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_establish_banking_relationships_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-establish-banking-relationships:ebeb8049ea2f32df1a0a3f98652e8f6b6c40c49da55a6c13f6feae927a594403", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_establish_banking_relationships`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_establish_banking_relationships_agent.py` is
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

Establish banking relationships Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 c72ec9ba0105be9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_banking_relationships_agent.py` first:

```bash
python3 adaptive_card_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_banking_relationships_agent.py   # or on stdin
python3 adaptive_card_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_banking_relationships',
    "version": '2.0.0',
    "display_name": 'Establish banking relationships Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of establish banking relationships status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a32fcec0833829c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardEstablishBankingRelationships(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishBankingRelationships'
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
    print(AdaptiveCardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
