---
name: "rar-cowork-cookbook-analyst-briefing-prep-and-rehearsal-routing"
description: "Builds an interactive HTML analyst briefing dashboard (positioning, top three messages, anticipated Q&A, speaker notes, source links) from prior firm interactions, their research, and your launch materials, then schedule"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing", "rar_sha256": "8299484571ff05ed47499550f9b6c9f60fe21d67e20758b381c0738c0bc562c1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "advanced", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing`. The original RAPP
agent is preserved byte-for-byte in `analyst_briefing_prep_and_rehearsal_routing_agent.py` and in the RCI capsule.

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

Analyst briefing prep and rehearsal routing — Builds an interactive HTML analyst briefing dashboard (positioning, top three messages, anticipated Q&A, speaker notes, source links) from prior firm interactions, their research, and your launch materials, then schedule

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
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
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
    "analyst_firm": {
      "description": "Name of the analyst firm being briefed.",
      "type": "string"
    },
    "briefing_date": {
      "description": "Date of the analyst briefing; rehearsal is set 48 hours prior.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
    "people": {
      "description": "Speaker name for speaker notes, plus spokesperson and briefing owner for the rehearsal invite.",
      "type": "string"
    },
    "product_area_and_launch": {
      "description": "Product area for their published research and the product/launch materials to cross-reference.",
      "type": "string"
    },
    "source_locations": {
      "description": "OneDrive folder with launch materials and the approved messaging doc.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyst_briefing_prep_and_rehearsal_routing_agent.py` and embedded as the fenced Python below (sha256 8299484571ff05ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyst_briefing_prep_and_rehearsal_routing_agent.py` first:

```bash
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 analyst_briefing_prep_and_rehearsal_routing_agent.py   # or on stdin
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyst briefing prep and rehearsal routing — Builds an interactive HTML analyst briefing dashboard (positioning, top three messages, anticipated Q&A, speaker notes, source links) from prior firm interactions, their research, and your launch materials, then schedule

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
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing',
    "version": '3.0.2',
    "display_name": 'Analyst briefing prep and rehearsal routing',
    "description": 'Builds an interactive HTML analyst briefing dashboard (positioning, top three messages, anticipated Q&A, speaker notes, source links) from prior firm interactions, their research, and your launch materials, then schedule',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'advanced', 'read_only', 'automation'],
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
        "upstream_slug": 'analyst-briefing-prep-and-rehearsal-routing',
        "upstream_url": 'https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f90aaeef5b8abf33',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/analyst-briefing-prep-and-rehearsal-routing', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: An interactive HTML briefing dashboard - positioning, top three messages, anticipated Q&A, speaker notes - and a rehearsal locked on the calendar 48 hours out with the dashboard attached on approval.'], 'confidence': 1.0, 'deliverable': 'An interactive HTML briefing dashboard - positioning, top three messages, anticipated Q&A, speaker notes - and a rehearsal locked on the calendar 48 hours out with the dashboard attached on approval.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'analyst_firm': 'Name of the analyst firm being briefed.', 'briefing_date': 'Date of the analyst briefing; rehearsal is set 48 hours prior.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'people': 'Speaker name for speaker notes, plus spokesperson and briefing owner for the rehearsal invite.', 'product_area_and_launch': 'Product area for their published research and the product/launch materials to cross-reference.', 'source_locations': 'OneDrive folder with launch materials and the approved messaging doc.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Prep the [Analyst Firm] briefing package and get the team rehearsed before the room. An interactive HTML briefing dashboard - positioning, top three messages, anticipated Q&A, speaker notes - and a rehearsal locked on the calendar 48 hours out with the dashboard attached on approval.', 'expected_output': 'An interactive HTML briefing dashboard - positioning, top three messages, anticipated Q&A, speaker notes - and a rehearsal locked on the calendar 48 hours out with the dashboard attached on approval.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "I have an analyst briefing with [Analyst Firm] on [Date], and I want the team walking into the room aligned.\n\nRead across our prior interactions with the firm - email threads and meeting history - and the [Product Area] research they've published recently.\n\nCross-reference that with our latest [Product/Launch] materials in [OneDrive folder] and the approved positioning in [Messaging doc].\n\nBuild me an interactive HTML briefing dashboard with positioning, the top three messages, the questions we should expect with our answers, speaker notes for [Speaker name], and links back to source materials.\n\nThen put a 60-minute rehearsal on the calendar with [Spokesperson] and [Briefing owner] for 48 hours before the briefing, with the dashboard attached once I approve it.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'An interactive HTML briefing dashboard - positioning, top three messages, anticipated Q&A, speaker notes - and a rehearsal locked on the calendar 48 hours out with the dashboard attached on approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds an interactive HTML analyst briefing dashboard (positioning, top three messages, anticipated Q&A, speaker notes, source links) from prior firm interactions, their research, and your launch materials, then schedule', 'example_request': 'Prep my Forrester briefing on March 12 and set up the rehearsal — dashboard, top messages, Q&A, and speaker notes.', 'inputs': [{'description': 'Name of the analyst firm being briefed.', 'name': 'analyst_firm'}, {'description': 'Date of the analyst briefing; rehearsal is set 48 hours prior.', 'name': 'briefing_date'}, {'description': 'Product area for their published research and the product/launch materials to cross-reference.', 'name': 'product_area_and_launch'}, {'description': 'OneDrive folder with launch materials and the approved messaging doc.', 'name': 'source_locations'}, {'description': 'Speaker name for speaker notes, plus spokesperson and briefing owner for the rehearsal invite.', 'name': 'people'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when preparing for an upcoming analyst firm briefing and you want an aligned briefing package plus a rehearsal booked before the room.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AnalystBriefingPrepAndRehearsalRouting(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnalystBriefingPrepAndRehearsalRouting'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'analyst_firm': {'description': 'Name of the analyst firm being briefed.', 'type': 'string'}, 'briefing_date': {'description': 'Date of the analyst briefing; rehearsal is set 48 hours prior.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'people': {'description': 'Speaker name for speaker notes, plus spokesperson and briefing owner for the rehearsal invite.', 'type': 'string'}, 'product_area_and_launch': {'description': 'Product area for their published research and the product/launch materials to cross-reference.', 'type': 'string'}, 'source_locations': {'description': 'OneDrive folder with launch materials and the approved messaging doc.', 'type': 'string'}},
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
    print(AnalystBriefingPrepAndRehearsalRouting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
