---
name: "rar-cowork-cookbook-ppt-exec-send-knowledge-article-to-customer"
description: "Generates an executive-ready PowerPoint deck on send knowledge article to customer status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer", "rar_sha256": "2c84adb102500dfc8a23e3cd7767bc62ff9ab986b9b4b0a34ddfa890560b88c4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 2c84adb102500dfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_send_knowledge_article_to_customer_agent.py` first:

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
    "version": '2.0.1',
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
