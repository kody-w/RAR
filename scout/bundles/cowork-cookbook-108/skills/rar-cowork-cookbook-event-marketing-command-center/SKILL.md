---
name: "rar-cowork-cookbook-event-marketing-command-center"
description: "Assembles event programming from a OneDrive folder, tagged calendar entries, a Teams channel, prior customer interactions, and Fabric performance data into an interactive HTML command center with linked artifacts and liv"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/event_marketing_command_center", "rar_sha256": "0bdcb1dae16eba1bf9c12f81a526691fef08818909215605c5028f9827fbbb29", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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
