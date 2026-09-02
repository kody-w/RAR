---
name: "rar-cowork-cookbook-dashboard-maintain-knowledge-base-articles"
description: "Produces a self-contained interactive HTML dashboard for maintain knowledge base articles - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_knowledge_base_articles", "rar_sha256": "c4ff7ff7e7bea73800e5796703867e920e2b79a56d5ec50db063e2265c6dd9f5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_maintain_knowledge_base_articles_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-maintain-knowledge-base-articles:2b5bd2118bc3ecf7611713c6602de013b6298c46f6b938f928e572156fa76d5d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_maintain_knowledge_base_articles`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_maintain_knowledge_base_articles_agent.py` is
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
