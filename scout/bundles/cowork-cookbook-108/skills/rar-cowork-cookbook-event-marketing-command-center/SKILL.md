---
name: "rar-cowork-cookbook-event-marketing-command-center"
description: "Assembles event programming from a OneDrive folder, tagged calendar entries, a Teams channel, prior customer interactions, and Fabric performance data into an interactive HTML command center with linked artifacts and liv"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/event_marketing_command_center", "rar_sha256": "0bdcb1dae16eba1bf9c12f81a526691fef08818909215605c5028f9827fbbb29", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/event_marketing_command_center`. The original RAPP
agent is preserved byte-for-byte in `event_marketing_command_center_agent.py` and in the RCI capsule.

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

Event marketing command center — Assembles event programming from a OneDrive folder, tagged calendar entries, a Teams channel, prior customer interactions, and Fabric performance data into an interactive HTML command center with linked artifacts and liv

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
  Upstream entry : https://coworkcookbook.com/recipes/event-marketing-command-center
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
    "event_date": {
      "description": "Date the event takes place.",
      "type": "string"
    },
    "event_name": {
      "description": "Name of the event, used to match calendar entries and channel discussion.",
      "type": "string"
    },
    "onedrive_folder": {
      "description": "OneDrive folder holding the event materials.",
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
    "speaker_name": {
      "description": "Speaker to build the prep brief for; also supply the number of days of social programming.",
      "type": "string"
    },
    "team_channel": {
      "description": "Teams channel where event programming is discussed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `event_marketing_command_center_agent.py` and embedded as the fenced Python below (sha256 0bdcb1dae16eba1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `event_marketing_command_center_agent.py` first:

```bash
python3 event_marketing_command_center_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 event_marketing_command_center_agent.py   # or on stdin
python3 event_marketing_command_center_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Event marketing command center — Assembles event programming from a OneDrive folder, tagged calendar entries, a Teams channel, prior customer interactions, and Fabric performance data into an interactive HTML command center with linked artifacts and liv

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
  Upstream entry : https://coworkcookbook.com/recipes/event-marketing-command-center
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/event_marketing_command_center',
    "version": '3.0.3',
    "display_name": 'Event marketing command center',
    "description": 'Assembles event programming from a OneDrive folder, tagged calendar entries, a Teams channel, prior customer interactions, and Fabric performance data into an interactive HTML command center with linked artifacts and liv',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'event-marketing-command-center',
        "upstream_url": 'https://coworkcookbook.com/recipes/event-marketing-command-center',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3acaf8ca2abf32c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/event-marketing-command-center', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: An interactive HTML command center with one row per event moment linked to its supporting artifact, plus live event KPIs from Fabric IQ - registrations, pipeline influenced, attendee engagement - surfaced alongside the programming.'], 'confidence': 1.0, 'deliverable': 'An interactive HTML command center with one row per event moment linked to its supporting artifact, plus live event KPIs from Fabric IQ - registrations, pipeline influenced, attendee engagement - surfaced alongside the programming.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'event_date': 'Date the event takes place.', 'event_name': 'Name of the event, used to match calendar entries and channel discussion.', 'onedrive_folder': 'OneDrive folder holding the event materials.', 'speaker_name': 'Speaker to build the prep brief for; also supply the number of days of social programming.', 'team_channel': 'Teams channel where event programming is discussed.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs. An interactive HTML command center with one row per event moment linked to its supporting artifact, plus live event KPIs from Fabric IQ - registrations, pipeline influenced, attendee engagement - surfaced alongside the programming.', 'expected_output': 'An interactive HTML command center with one row per event moment linked to its supporting artifact, plus live event KPIs from Fabric IQ - registrations, pipeline influenced, attendee engagement - surfaced alongside the programming.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "[Event name] is on [Event Date]. Before doors open, I need every speaker slot, customer meeting, content drop, and social moment organized in one place with the supporting material ready to go.\n\nRead across:\n\n[OneDrive folder] of event materials\n\nCalendar entries for customer meetings and speaker slots tagged to [Event name]\n\n[Team channel] event programming discussion\n\nPrior interactions with each customer attending - email and meeting history\n\nPull performance data from prior events and campaigns from Fabric.\n\nPrep:\n\nInteractive HTML command center with one row per event moment (status, owner, link to artifact, live KPI)\n\nEvent dossier - an executive overview of the full event program, key customer meetings, and strategic objectives (PowerPoint)\n\nSpeaker prep brief for [Speaker name] (Word)\n\nCustomer one-pager for each scheduled meeting (Word)\n\nSocial copy spanning [X] days of event programming (Word)\n\nFollow-up email drafts for the top three customer meetings (Word)\n\nThread every artifact back into the command center, so it's the one place to look during event week.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'An interactive HTML command center with one row per event moment linked to its supporting artifact, plus live event KPIs from Fabric IQ - registrations, pipeline influenced, attendee engagement - surfaced alongside the programming.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Assembles event programming from a OneDrive folder, tagged calendar entries, a Teams channel, prior customer interactions, and Fabric performance data into an interactive HTML command center with linked artifacts and liv', 'example_request': 'Build an event command center for Contoso Summit on May 6 from my Event Materials folder and the #summit channel.', 'inputs': [{'description': 'Name of the event, used to match calendar entries and channel discussion.', 'name': 'event_name'}, {'description': 'Date the event takes place.', 'name': 'event_date'}, {'description': 'OneDrive folder holding the event materials.', 'name': 'onedrive_folder'}, {'description': 'Teams channel where event programming is discussed.', 'name': 'team_channel'}, {'description': 'Speaker to build the prep brief for; also supply the number of days of social programming.', 'name': 'speaker_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use before an event to organize speaker slots, customer meetings, content drops, and social posts in one place with prep documents drafted for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class EventMarketingCommandCenter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EventMarketingCommandCenter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'event_date': {'description': 'Date the event takes place.', 'type': 'string'}, 'event_name': {'description': 'Name of the event, used to match calendar entries and channel discussion.', 'type': 'string'}, 'onedrive_folder': {'description': 'OneDrive folder holding the event materials.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'speaker_name': {'description': 'Speaker to build the prep brief for; also supply the number of days of social programming.', 'type': 'string'}, 'team_channel': {'description': 'Teams channel where event programming is discussed.', 'type': 'string'}},
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
    print(EventMarketingCommandCenter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
