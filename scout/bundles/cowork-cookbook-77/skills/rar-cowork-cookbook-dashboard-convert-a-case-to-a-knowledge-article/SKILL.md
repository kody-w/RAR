---
name: "rar-cowork-cookbook-dashboard-convert-a-case-to-a-knowledge-article"
description: "Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article", "rar_sha256": "f74c686192dd5bc73feda2c0e5cc1c16ae5a034db802cb5334251cdb9aafa629", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article`. The original RAPP
agent is preserved byte-for-byte in `dashboard_convert_a_case_to_a_knowledge_article_agent.py` and in the RCI capsule.

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
