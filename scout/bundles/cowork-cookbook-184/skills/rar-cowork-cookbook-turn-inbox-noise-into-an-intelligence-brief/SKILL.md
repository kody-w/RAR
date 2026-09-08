---
name: "rar-cowork-cookbook-turn-inbox-noise-into-an-intelligence-brief"
description: "Searches the user's inbox for newsletters, digests, and industry publications from the past 7 days and returns an article-style weekly brief in four sections plus a deep-research companion on the top stories."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief", "rar_sha256": "1ec76a1a2ef4aaa6c4438c3ea22ba28bfe2f59b0eca76cd199a1ad31abb0fed4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "intermediate", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief`. The original RAPP
agent is preserved byte-for-byte in `turn_inbox_noise_into_an_intelligence_brief_agent.py` and in the RCI capsule.

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

Turn inbox noise into a curated intelligence brief — Searches the user's inbox for newsletters, digests, and industry publications from the past 7 days and returns an article-style weekly brief in four sections plus a deep-research companion on the top stories.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-inbox-noise-into-an-intelligence-brief
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
    "company_name": {
      "description": "The company whose internal newsletters get their own section of the brief.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "delivery_schedule": {
      "description": "When to send the brief; the recipe defaults to every Friday afternoon.",
      "type": "string"
    },
    "exclusions": {
      "description": "Personal or consumer newsletters to leave out, e.g. hardware deals or fundraising mail.",
      "type": "string"
    },
    "industry": {
      "description": "The user's industry, used as the fourth section of the brief.",
      "type": "string"
    },
    "lookback_days": {
      "description": "How far back to search the inbox for newsletters; the recipe defaults to the past 7 days.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_inbox_noise_into_an_intelligence_brief_agent.py` and embedded as the fenced Python below (sha256 1ec76a1a2ef4aaa6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_inbox_noise_into_an_intelligence_brief_agent.py` first:

```bash
python3 turn_inbox_noise_into_an_intelligence_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_inbox_noise_into_an_intelligence_brief_agent.py   # or on stdin
python3 turn_inbox_noise_into_an_intelligence_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn inbox noise into a curated intelligence brief — Searches the user's inbox for newsletters, digests, and industry publications from the past 7 days and returns an article-style weekly brief in four sections plus a deep-research companion on the top stories.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-inbox-noise-into-an-intelligence-brief
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief',
    "version": '3.0.3',
    "display_name": 'Turn inbox noise into a curated intelligence brief',
    "description": "Searches the user's inbox for newsletters, digests, and industry publications from the past 7 days and returns an article-style weekly brief in four sections plus a deep-research companion on the top stories.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'work_management', 'intermediate', 'read_only', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'turn-inbox-noise-into-an-intelligence-brief',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-inbox-noise-into-an-intelligence-brief',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31b2eba58bba78fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/curate-information-briefs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-inbox-noise-into-an-intelligence-brief', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A curated weekly brief that surfaces meaningful trends across the publications you follow - without the time spent reading them.'], 'confidence': 1.0, 'deliverable': 'A curated weekly brief that surfaces meaningful trends across the publications you follow - without the time spent reading them.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'company_name': 'The company whose internal newsletters get their own section of the brief.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'delivery_schedule': 'When to send the brief; the recipe defaults to every Friday afternoon.', 'exclusions': 'Personal or consumer newsletters to leave out, e.g. hardware deals or fundraising mail.', 'industry': "The user's industry, used as the fourth section of the brief.", 'lookback_days': 'How far back to search the inbox for newsletters; the recipe defaults to the past 7 days.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cut through a week of newsletters to the stories that actually matter to your work. A curated weekly brief that surfaces meaningful trends across the publications you follow - without the time spent reading them.', 'expected_output': 'A curated weekly brief that surfaces meaningful trends across the publications you follow - without the time spent reading them.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Search my inbox for all newsletters, digests, and industry publications received in the past 7 days.\n\nThen write a polished, article-style weekly brief covering four sections: (1) [Company] internal newsletters, (2) AI & tech news, (3) World affairs/news publications, and (4) [Your industry] - weaving the key stories and themes from each into flowing narrative paragraphs, not bullet lists.\n\nExclude personal or consumer newsletters (hardware, food bank fundraisers, etc.).\n\nEnd with a 2-3 sentence throughline tying the week\'s themes together. Write the output inline as a readable article. Include links inline to the actual emails in case I want to read more.\n\nThen, as a Part 2, pick the top headline stories across the brief and run a deep research report on them - pull the primary sources behind each, summarize the substance, and surface the context, key data points, and "so what" for my work. Deliver this as a separate research companion to the brief.\n\nSend me this weekly brief every Friday afternoon.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A curated weekly brief that surfaces meaningful trends across the publications you follow - without the time spent reading them.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Searches the user's inbox for newsletters, digests, and industry publications from the past 7 days and returns an article-style weekly brief in four sections plus a deep-research companion on the top stories.", 'example_request': "Turn last week's newsletters into a weekly brief on Contoso, AI, world news, and finance, with a deep dive on the top stories.", 'inputs': [{'description': 'The company whose internal newsletters get their own section of the brief.', 'name': 'company_name'}, {'description': "The user's industry, used as the fourth section of the brief.", 'name': 'industry'}, {'description': 'How far back to search the inbox for newsletters; the recipe defaults to the past 7 days.', 'name': 'lookback_days'}, {'description': 'When to send the brief; the recipe defaults to every Friday afternoon.', 'name': 'delivery_schedule'}, {'description': 'Personal or consumer newsletters to leave out, e.g. hardware deals or fundraising mail.', 'name': 'exclusions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants their past week of newsletters and industry publications condensed into a written intelligence brief, optionally scheduled for Friday afternoons.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TurnInboxNoiseIntoAnIntelligenceBrief(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnInboxNoiseIntoAnIntelligenceBrief'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'company_name': {'description': 'The company whose internal newsletters get their own section of the brief.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'delivery_schedule': {'description': 'When to send the brief; the recipe defaults to every Friday afternoon.', 'type': 'string'}, 'exclusions': {'description': 'Personal or consumer newsletters to leave out, e.g. hardware deals or fundraising mail.', 'type': 'string'}, 'industry': {'description': "The user's industry, used as the fourth section of the brief.", 'type': 'string'}, 'lookback_days': {'description': 'How far back to search the inbox for newsletters; the recipe defaults to the past 7 days.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TurnInboxNoiseIntoAnIntelligenceBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
