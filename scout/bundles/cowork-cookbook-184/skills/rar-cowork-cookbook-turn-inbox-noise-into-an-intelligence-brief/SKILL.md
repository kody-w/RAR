---
name: "rar-cowork-cookbook-turn-inbox-noise-into-an-intelligence-brief"
description: "Searches the user's inbox for newsletters, digests, and industry publications from the past 7 days and returns an article-style weekly brief in four sections plus a deep-research companion on the top stories."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief", "rar_sha256": "1ec76a1a2ef4aaa6c4438c3ea22ba28bfe2f59b0eca76cd199a1ad31abb0fed4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "intermediate", "read_only", "automation"]}
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
