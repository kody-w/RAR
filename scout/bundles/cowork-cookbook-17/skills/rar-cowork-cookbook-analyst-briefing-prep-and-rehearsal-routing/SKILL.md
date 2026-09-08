---
name: "rar-cowork-cookbook-analyst-briefing-prep-and-rehearsal-routing"
description: "Builds an interactive HTML analyst briefing dashboard (positioning, top three messages, anticipated Q&A, speaker notes, source links) from prior firm interactions, their research, and your launch materials, then schedule"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing", "rar_sha256": "8299484571ff05ed47499550f9b6c9f60fe21d67e20758b381c0738c0bc562c1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "advanced", "read_only", "automation"]}
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
