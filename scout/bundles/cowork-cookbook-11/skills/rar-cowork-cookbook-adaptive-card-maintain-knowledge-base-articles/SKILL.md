---
name: "rar-cowork-cookbook-adaptive-card-maintain-knowledge-base-articles"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain knowledge base articles status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles", "rar_sha256": "c8b35c4658d81366c0ae116921610ca705b647f1e597daf13b156befba5c15b0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_maintain_knowledge_base_articles_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-maintain-knowledge-base-articles:646ed86f04e5ba2a132c3c317cbbfd6f453cde72beca00cb159545e20d89707e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_maintain_knowledge_base_articles_agent.py` is
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
