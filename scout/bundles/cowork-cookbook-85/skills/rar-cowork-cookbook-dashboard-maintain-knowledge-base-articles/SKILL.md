---
name: "rar-cowork-cookbook-dashboard-maintain-knowledge-base-articles"
description: "Produces a self-contained interactive HTML dashboard for maintain knowledge base articles - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_knowledge_base_articles", "rar_sha256": "c4ff7ff7e7bea73800e5796703867e920e2b79a56d5ec50db063e2265c6dd9f5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Maintain knowledge base articles Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain knowledge base articles - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 c4ff7ff7e7bea738…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_knowledge_base_articles_agent.py` first:

```bash
python3 dashboard_maintain_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_knowledge_base_articles_agent.py   # or on stdin
python3 dashboard_maintain_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain knowledge base articles Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain knowledge base articles - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_knowledge_base_articles',
    "version": '2.0.0',
    "display_name": 'Maintain knowledge base articles Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for maintain knowledge base articles - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-maintain-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '880dbc6fa917b7b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/maintain-knowledge-base-articles'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-maintain-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMaintainKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainKnowledgeBaseArticles'
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
    print(DashboardMaintainKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
