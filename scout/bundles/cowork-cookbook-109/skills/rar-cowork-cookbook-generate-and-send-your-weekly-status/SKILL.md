---
name: "rar-cowork-cookbook-generate-and-send-your-weekly-status"
description: "Drafts a Monday-morning weekly status email for your team, combining your top-of-mind priorities, key executive meetings for the week, and progress metrics pulled from Fabric, held for your review before sending."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/generate_and_send_your_weekly_status", "rar_sha256": "c92fdc84076bdbe2468d7aead9bde7d9cd546ec7b0f9302dd3c48dcc4ecb15a9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "intermediate", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/generate_and_send_your_weekly_status`. The original RAPP
agent is preserved byte-for-byte in `generate_and_send_your_weekly_status_agent.py` and in the RCI capsule.

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

Generate and send your weekly status automatically — Drafts a Monday-morning weekly status email for your team, combining your top-of-mind priorities, key executive meetings for the week, and progress metrics pulled from Fabric, held for your review before sending.

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
  Upstream entry : https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status
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
    "fabric_metrics": {
      "description": "Which Fabric metrics tied to your priorities to include, with progress since last week.",
      "type": "string"
    },
    "key_meetings": {
      "description": "The week's meetings to feature, typically executive ones, from your calendar.",
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
    "schedule": {
      "description": "When it should run recurring, e.g. every Monday morning.",
      "type": "string"
    },
    "team_recipients": {
      "description": "The team distribution list or people the weekly email goes to.",
      "type": "string"
    },
    "top_of_mind": {
      "description": "Your key priorities and projects for the week to highlight in the update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generate_and_send_your_weekly_status_agent.py` and embedded as the fenced Python below (sha256 c92fdc84076bdbe2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generate_and_send_your_weekly_status_agent.py` first:

```bash
python3 generate_and_send_your_weekly_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 generate_and_send_your_weekly_status_agent.py   # or on stdin
python3 generate_and_send_your_weekly_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate and send your weekly status automatically — Drafts a Monday-morning weekly status email for your team, combining your top-of-mind priorities, key executive meetings for the week, and progress metrics pulled from Fabric, held for your review before sending.

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
  Upstream entry : https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/generate_and_send_your_weekly_status',
    "version": '3.0.3',
    "display_name": 'Generate and send your weekly status automatically',
    "description": 'Drafts a Monday-morning weekly status email for your team, combining your top-of-mind priorities, key executive meetings for the week, and progress metrics pulled from Fabric, held for your review before sending.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'work_management', 'intermediate', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'generate-and-send-your-weekly-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b680518adad3eba7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/manage-communications/produce-recurring-status-updates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'work-management/generate-and-send-your-weekly-status', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', "Output matches: A ready-to-send weekly status, drafted from your real meetings and conversations, that lands in your team's inbox to start the week."], 'confidence': 1.0, 'deliverable': "A ready-to-send weekly status, drafted from your real meetings and conversations, that lands in your team's inbox to start the week.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fabric_metrics': 'Which Fabric metrics tied to your priorities to include, with progress since last week.', 'key_meetings': "The week's meetings to feature, typically executive ones, from your calendar.", 'schedule': 'When it should run recurring, e.g. every Monday morning.', 'team_recipients': 'The team distribution list or people the weekly email goes to.', 'top_of_mind': 'Your key priorities and projects for the week to highlight in the update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replace the Monday-morning scramble with a status update that writes itself. A ready-to-send weekly status, drafted from your real meetings and conversations, that lands in your team's inbox to start the week.", 'expected_output': "A ready-to-send weekly status, drafted from your real meetings and conversations, that lands in your team's inbox to start the week.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': 'I create a weekly email to my team focused on my top of mind for the week - I send this Monday morning, and it includes my top of mind as well as some of the key meetings for the week.\n\nThose key meetings tend to be executives, and my top of mind are related to the key priorities and projects the team and I are working on.\n\nPull a few key metrics from Fabric tied to our priorities - progress since last week - and weave them into the update so the status is grounded in real numbers.\n\nCreate a skill where this occurs every Monday morning.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A ready-to-send weekly status, drafted from your real meetings and conversations, that lands in your team's inbox to start the week."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Monday-morning weekly status email for your team, combining your top-of-mind priorities, key executive meetings for the week, and progress metrics pulled from Fabric, held for your review before sending.', 'example_request': 'Draft my weekly status email for Monday with my top priorities, exec meetings, and Fabric metrics.', 'inputs': [{'description': 'Your key priorities and projects for the week to highlight in the update.', 'name': 'top_of_mind'}, {'description': 'The team distribution list or people the weekly email goes to.', 'name': 'team_recipients'}, {'description': "The week's meetings to feature, typically executive ones, from your calendar.", 'name': 'key_meetings'}, {'description': 'Which Fabric metrics tied to your priorities to include, with progress since last week.', 'name': 'fabric_metrics'}, {'description': 'When it should run recurring, e.g. every Monday morning.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need your recurring Monday weekly team status update drafted, or want it set up to run every Monday morning.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class GenerateAndSendYourWeeklyStatus(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GenerateAndSendYourWeeklyStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fabric_metrics': {'description': 'Which Fabric metrics tied to your priorities to include, with progress since last week.', 'type': 'string'}, 'key_meetings': {'description': "The week's meetings to feature, typically executive ones, from your calendar.", 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'schedule': {'description': 'When it should run recurring, e.g. every Monday morning.', 'type': 'string'}, 'team_recipients': {'description': 'The team distribution list or people the weekly email goes to.', 'type': 'string'}, 'top_of_mind': {'description': 'Your key priorities and projects for the week to highlight in the update.', 'type': 'string'}},
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
    print(GenerateAndSendYourWeeklyStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
