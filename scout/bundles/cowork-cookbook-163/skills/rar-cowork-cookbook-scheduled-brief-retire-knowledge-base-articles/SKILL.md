---
name: "rar-cowork-cookbook-scheduled-brief-retire-knowledge-base-articles"
description: "Builds a morning brief on retiring knowledge base articles from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, plus a saved email draft to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles", "rar_sha256": "94606535860425e77faa9a2574e0a3dfe98dc5c8ccd4705f94c3315d5d0c5211", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Retire knowledge base articles Scheduled Email Brief — Builds a morning brief on retiring knowledge base articles from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, plus a saved email draft to t

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am, daily, or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 94606535860425e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_knowledge_base_articles_agent.py` first:

```bash
python3 scheduled_brief_retire_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_knowledge_base_articles_agent.py   # or on stdin
python3 scheduled_brief_retire_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire knowledge base articles Scheduled Email Brief — Builds a morning brief on retiring knowledge base articles from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, plus a saved email draft to t

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles',
    "version": '3.0.3',
    "display_name": 'Retire knowledge base articles Scheduled Email Brief',
    "description": 'Builds a morning brief on retiring knowledge base articles from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, plus a saved email draft to t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-retire-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e72ff1217dac71b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/retire-knowledge-base-articles'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-retire-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily, or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where retire knowledge base articles stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on retire knowledge base articles for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads retire knowledge base articles, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on retiring knowledge base articles from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, plus a saved email draft to t', 'example_request': 'Give me the 7am brief on retiring knowledge base articles in USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily, or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a daily or weekly (weekday 7am) brief on retiring knowledge base articles is needed for the responsible owner, with a drafted email and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRetireKnowledgeBaseArticles(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireKnowledgeBaseArticles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily, or weekly.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ScheduledBriefRetireKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
