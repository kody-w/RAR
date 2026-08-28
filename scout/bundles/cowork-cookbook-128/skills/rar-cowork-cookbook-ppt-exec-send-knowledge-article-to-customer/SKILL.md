---
name: "rar-cowork-cookbook-ppt-exec-send-knowledge-article-to-customer"
description: "Generates an executive-ready PowerPoint deck on send knowledge article to customer status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer", "rar_sha256": "6f5a336ca89555b6396a48e7f45035297e0be37cf133e7758bf8dd2f25a5b511", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_send_knowledge_article_to_customer_agent.py` and in the RCI capsule.

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

Send knowledge article to customer Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on send knowledge article to customer status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-knowledge-article-to-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 6f5a336ca89555b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_send_knowledge_article_to_customer_agent.py` first:

```bash
python3 ppt_exec_send_knowledge_article_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_send_knowledge_article_to_customer_agent.py   # or on stdin
python3 ppt_exec_send_knowledge_article_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send knowledge article to customer Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on send knowledge article to customer status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-knowledge-article-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer',
    "version": '2.0.0',
    "display_name": 'Send knowledge article to customer Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on send knowledge article to customer status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-send-knowledge-article-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-send-knowledge-article-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '243ce8eed0bfe83a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-knowledge-article-to-customer'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-send-knowledge-article-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecSendKnowledgeArticleToCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecSendKnowledgeArticleToCustomer'
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
    print(PptExecSendKnowledgeArticleToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
