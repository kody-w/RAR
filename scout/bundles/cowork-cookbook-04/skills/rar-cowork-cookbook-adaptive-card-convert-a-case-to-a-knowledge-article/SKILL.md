---
name: "rar-cowork-cookbook-adaptive-card-convert-a-case-to-a-knowledge-article"
description: "Produces a reusable Adaptive Card JSON snapshot of convert a case to a knowledge article status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article", "rar_sha256": "358bfcfa08422a1a330db4dc927f80bafb8a7410962549f574496fe5f63c1479", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` and in the RCI capsule.

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
