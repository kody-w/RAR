---
name: "rar-cowork-cookbook-adaptive-card-convert-a-case-to-a-knowledge-article"
description: "Produces a reusable Adaptive Card JSON snapshot of convert a case to a knowledge article status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article", "rar_sha256": "358bfcfa08422a1a330db4dc927f80bafb8a7410962549f574496fe5f63c1479", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_convert_a_case_to_a_knowledge_article_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-convert-a-case-to-a-knowledge-article:6c642b14aa2a2519a539cdc248bfe47b4c6b4d6c19e51f3409a4758b0cdb0fd5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` is
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

Convert a case to a knowledge article Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of convert a case to a knowledge article status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-a-case-to-a-knowledge-article
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` and embedded as the fenced Python below (sha256 358bfcfa08422a1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` first:

```bash
python3 adaptive_card_convert_a_case_to_a_knowledge_article_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_convert_a_case_to_a_knowledge_article_agent.py   # or on stdin
python3 adaptive_card_convert_a_case_to_a_knowledge_article_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert a case to a knowledge article Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of convert a case to a knowledge article status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-a-case-to-a-knowledge-article
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article',
    "version": '2.0.0',
    "display_name": 'Convert a case to a knowledge article Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of convert a case to a knowledge article status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-convert-a-case-to-a-knowledge-article',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-convert-a-case-to-a-knowledge-article',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8080e10cee6d6244',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/convert-a-case-to-a-knowledge-article'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-convert-a-case-to-a-knowledge-article', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardConvertACaseToAKnowledgeArticle(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConvertACaseToAKnowledgeArticle'
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
    print(AdaptiveCardConvertACaseToAKnowledgeArticle().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
