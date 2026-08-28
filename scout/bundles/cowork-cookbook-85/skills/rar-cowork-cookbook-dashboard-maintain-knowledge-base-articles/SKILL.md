---
name: "rar-cowork-cookbook-dashboard-maintain-knowledge-base-articles"
description: "Produces a self-contained interactive HTML dashboard for maintain knowledge base articles - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_knowledge_base_articles", "rar_sha256": "53a68110c05bc044f953956363e1ca8a75dcd1dc3c3e3121cc19902d715fb4c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 53a68110c05bc044…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_knowledge_base_articles_agent.py` first:

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
    "version": '2.0.1',
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
