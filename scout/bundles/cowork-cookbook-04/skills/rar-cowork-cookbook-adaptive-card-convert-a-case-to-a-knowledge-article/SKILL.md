---
name: "rar-cowork-cookbook-adaptive-card-convert-a-case-to-a-knowledge-article"
description: "Produces a reusable Adaptive Card JSON snapshot of convert a case to a knowledge article status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article", "rar_sha256": "7f402a43043fa166fe5c434ab4239dbbd2fda692e052e9c2f328f17566dbdfbb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` and embedded as the fenced Python below (sha256 7f402a43043fa166…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` first:

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
    "version": '2.0.1',
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
