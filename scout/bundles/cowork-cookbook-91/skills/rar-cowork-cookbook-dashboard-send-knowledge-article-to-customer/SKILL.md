---
name: "rar-cowork-cookbook-dashboard-send-knowledge-article-to-customer"
description: "Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_send_knowledge_article_to_customer", "rar_sha256": "d693a8872485e7600874c3e7fd950c23db34f0dfa62d59c120a389c48a448c27", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_send_knowledge_article_to_customer`. The original RAPP
agent is preserved byte-for-byte in `dashboard_send_knowledge_article_to_customer_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 d693a8872485e760…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_send_knowledge_article_to_customer_agent.py` first:

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
    "version": '2.0.1',
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
