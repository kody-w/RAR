---
name: "rar-cowork-cookbook-scheduled-brief-retire-knowledge-base-articles"
description: "Builds a morning brief on retiring knowledge base articles from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, plus a saved email draft to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles", "rar_sha256": "94606535860425e77faa9a2574e0a3dfe98dc5c8ccd4705f94c3315d5d0c5211", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
