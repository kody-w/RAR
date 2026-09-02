---
name: "rar-cowork-cookbook-dashboard-send-knowledge-article-to-customer"
description: "Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_send_knowledge_article_to_customer", "rar_sha256": "17a3c3c6b5be20f80a55f189c14231503ccc14723d4692c7d9e3f21cb8afad79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_send_knowledge_article_to_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-send-knowledge-article-to-customer:11f02e8d0cff028c052c6fb5d9d901a5f532707f09c4fa56ec6dc80e4476ef18", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_send_knowledge_article_to_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_send_knowledge_article_to_customer_agent.py` is
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

Send knowledge article to customer Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 17a3c3c6b5be20f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_send_knowledge_article_to_customer_agent.py` first:

```bash
python3 dashboard_send_knowledge_article_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_send_knowledge_article_to_customer_agent.py   # or on stdin
python3 dashboard_send_knowledge_article_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send knowledge article to customer Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_send_knowledge_article_to_customer',
    "version": '2.0.0',
    "display_name": 'Send knowledge article to customer Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-send-knowledge-article-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '468f32be08458c18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-knowledge-article-to-customer'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-send-knowledge-article-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardSendKnowledgeArticleToCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSendKnowledgeArticleToCustomer'
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
    print(DashboardSendKnowledgeArticleToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
