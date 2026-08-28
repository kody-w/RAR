---
name: "rar-cowork-cookbook-adaptive-card-maintain-knowledge-base-articles"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain knowledge base articles status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles", "rar_sha256": "c8b35c4658d81366c0ae116921610ca705b647f1e597daf13b156befba5c15b0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Maintain knowledge base articles Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain knowledge base articles status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 c8b35c4658d81366…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_knowledge_base_articles_agent.py` first:

```bash
python3 adaptive_card_maintain_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_knowledge_base_articles_agent.py   # or on stdin
python3 adaptive_card_maintain_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain knowledge base articles Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain knowledge base articles status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles',
    "version": '2.0.0',
    "display_name": 'Maintain knowledge base articles Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of maintain knowledge base articles status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-maintain-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94b1c5f0ed4a3a8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/maintain-knowledge-base-articles'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-maintain-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMaintainKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainKnowledgeBaseArticles'
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
    print(AdaptiveCardMaintainKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
