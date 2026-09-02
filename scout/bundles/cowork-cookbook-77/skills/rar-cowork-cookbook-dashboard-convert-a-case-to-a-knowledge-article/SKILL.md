---
name: "rar-cowork-cookbook-dashboard-convert-a-case-to-a-knowledge-article"
description: "Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article", "rar_sha256": "f74c686192dd5bc73feda2c0e5cc1c16ae5a034db802cb5334251cdb9aafa629", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_convert_a_case_to_a_knowledge_article_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-convert-a-case-to-a-knowledge-article:820497e855c6f62aac94c156a19cc1bce87c08044dd43bad061cebc0d85a89e8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_convert_a_case_to_a_knowledge_article_agent.py` is
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

Convert a case to a knowledge article Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_convert_a_case_to_a_knowledge_article_agent.py` and embedded as the fenced Python below (sha256 f74c686192dd5bc7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_convert_a_case_to_a_knowledge_article_agent.py` first:

```bash
python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py   # or on stdin
python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert a case to a knowledge article Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article',
    "version": '2.0.0',
    "display_name": 'Convert a case to a knowledge article Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-convert-a-case-to-a-knowledge-article',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9fe5146008fd725a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/convert-a-case-to-a-knowledge-article'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-convert-a-case-to-a-knowledge-article', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConvertACaseToAKnowledgeArticle(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConvertACaseToAKnowledgeArticle'
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
    print(DashboardConvertACaseToAKnowledgeArticle().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
