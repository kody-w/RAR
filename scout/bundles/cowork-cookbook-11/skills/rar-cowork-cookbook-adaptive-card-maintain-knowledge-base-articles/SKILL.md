---
name: "rar-cowork-cookbook-adaptive-card-maintain-knowledge-base-articles"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain knowledge base articles status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles", "rar_sha256": "fc0ac82db82b1ec7a44e25f2b01f28635ceab7e278d1d7e74a372f5ec3ee3c19", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 fc0ac82db82b1ec7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_knowledge_base_articles_agent.py` first:

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
    "version": '2.0.1',
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
