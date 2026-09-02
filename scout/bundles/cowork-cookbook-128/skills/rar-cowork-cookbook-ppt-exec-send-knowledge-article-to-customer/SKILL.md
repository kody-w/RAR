---
name: "rar-cowork-cookbook-ppt-exec-send-knowledge-article-to-customer"
description: "Generates an executive-ready PowerPoint deck on send knowledge article to customer status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer", "rar_sha256": "6f5a336ca89555b6396a48e7f45035297e0be37cf133e7758bf8dd2f25a5b511", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_send_knowledge_article_to_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-send-knowledge-article-to-customer:859fb017cad4b19df997266314eedf7ca80c5ae11e876e355ac217ed24bbd8c3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_send_knowledge_article_to_customer_agent.py` is
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
