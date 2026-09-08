---
name: "rar-cowork-cookbook-generate-and-send-your-weekly-status"
description: "Drafts a Monday-morning weekly status email for your team, combining your top-of-mind priorities, key executive meetings for the week, and progress metrics pulled from Fabric, held for your review before sending."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/generate_and_send_your_weekly_status", "rar_sha256": "c92fdc84076bdbe2468d7aead9bde7d9cd546ec7b0f9302dd3c48dcc4ecb15a9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "intermediate", "integration", "fabric_iq"]}
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
