---
name: "rar-cowork-cookbook-adaptive-card-generate-ideas"
description: "Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_generate_ideas", "rar_sha256": "26e4e642b49fd7115e63ea8fe6d698ff35d3f10d0e4ff585339cbaae441c2060", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_generate_ideas_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-generate-ideas:e979cedeefee511f3530309ced074d8a8f75958409cd6f3ad1843c28f4eb4b4a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_generate_ideas`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_generate_ideas_agent.py` is
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

Generate ideas Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-generate-ideas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 26e4e642b49fd711…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_generate_ideas_agent.py` first:

```bash
python3 adaptive_card_generate_ideas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_generate_ideas_agent.py   # or on stdin
python3 adaptive_card_generate_ideas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate ideas Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-generate-ideas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_generate_ideas',
    "version": '2.0.0',
    "display_name": 'Generate ideas Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-generate-ideas',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-generate-ideas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c419e909121e7833',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/generate-ideas'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-generate-ideas', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardGenerateIdeas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardGenerateIdeas'
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
    print(AdaptiveCardGenerateIdeas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
