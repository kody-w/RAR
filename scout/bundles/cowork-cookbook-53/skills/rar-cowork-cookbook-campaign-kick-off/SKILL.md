---
name: "rar-cowork-cookbook-campaign-kick-off"
description: "Stands up a new campaign in Cowork: pulls prior campaign performance from Fabric, creates a OneDrive folder, drafts a Word working brief from the intake and email threads, and drafts a kick-off invite."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_kick_off", "rar_sha256": "fa1574b3a36e3aed2d7cd473459990dc162a230e6f53ca268f52bb3ccb577d6a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/campaign_kick_off`. The original RAPP
agent is preserved byte-for-byte in `campaign_kick_off_agent.py` and in the RCI capsule.

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

Campaign kick-off — Stands up a new campaign in Cowork: pulls prior campaign performance from Fabric, creates a OneDrive folder, drafts a Word working brief from the intake and email threads, and drafts a kick-off invite.

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
  Upstream entry : https://coworkcookbook.com/recipes/campaign-kick-off
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
    "campaign_name": {
      "description": "Name of the new campaign; used for the brief and the OneDrive folder.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "intake_brief": {
      "description": "The attached intake brief document for the campaign.",
      "type": "string"
    },
    "kickoff_date": {
      "description": "Date for the kick-off invite.",
      "type": "string"
    },
    "launch_date": {
      "description": "Date the campaign launches.",
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
    "stakeholders": {
      "description": "People to invite to the kick-off meeting.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_kick_off_agent.py` and embedded as the fenced Python below (sha256 fa1574b3a36e3aed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_kick_off_agent.py` first:

```bash
python3 campaign_kick_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_kick_off_agent.py   # or on stdin
python3 campaign_kick_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Campaign kick-off — Stands up a new campaign in Cowork: pulls prior campaign performance from Fabric, creates a OneDrive folder, drafts a Word working brief from the intake and email threads, and drafts a kick-off invite.

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
  Upstream entry : https://coworkcookbook.com/recipes/campaign-kick-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/campaign_kick_off',
    "version": '3.0.3',
    "display_name": 'Campaign kick-off',
    "description": 'Stands up a new campaign in Cowork: pulls prior campaign performance from Fabric, creates a OneDrive folder, drafts a Word working brief from the intake and email threads, and drafts a kick-off invite.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'campaign-kick-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/campaign-kick-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4077548e3506203e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/campaign-kick-off', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A Word campaign brief - grounded in prior campaign performance and best practices - saved into a dedicated OneDrive workspace, plus a draft kickoff invite with relevant stakeholders.'], 'confidence': 1.0, 'deliverable': 'A Word campaign brief - grounded in prior campaign performance and best practices - saved into a dedicated OneDrive workspace, plus a draft kickoff invite with relevant stakeholders.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'campaign_name': 'Name of the new campaign; used for the brief and the OneDrive folder.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'intake_brief': 'The attached intake brief document for the campaign.', 'kickoff_date': 'Date for the kick-off invite.', 'launch_date': 'Date the campaign launches.', 'stakeholders': 'People to invite to the kick-off meeting.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar. A Word campaign brief - grounded in prior campaign performance and best practices - saved into a dedicated OneDrive workspace, plus a draft kickoff invite with relevant stakeholders.', 'expected_output': 'A Word campaign brief - grounded in prior campaign performance and best practices - saved into a dedicated OneDrive workspace, plus a draft kickoff invite with relevant stakeholders.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': 'I\'m kicking off a new campaign called [Campaign name] launching on [Launch date]. The intake brief is attached, and there are email threads discussing details of the campaign.\n\nPull prior campaign performance from Fabric - channel ROI, message resonance, conversion patterns - and surface the learnings that should shape this campaign. Create a [Campaign name] folder in OneDrive for the workspace.\n\nUse the intake, related threads, and prior-campaign learnings to build a working brief in Word - objectives, audience, key messages, deliverables, named owners, and a "what worked / what to avoid" section. Then schedule a kick-off invite on the calendar with [Stakeholders] for [date].', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Word campaign brief - grounded in prior campaign performance and best practices - saved into a dedicated OneDrive workspace, plus a draft kickoff invite with relevant stakeholders.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Stands up a new campaign in Cowork: pulls prior campaign performance from Fabric, creates a OneDrive folder, drafts a Word working brief from the intake and email threads, and drafts a kick-off invite.', 'example_request': 'Kick off our Spring Renewal campaign launching May 5 — brief is attached, kickoff with Dana and Raj on Apr 22.', 'inputs': [{'description': 'Name of the new campaign; used for the brief and the OneDrive folder.', 'name': 'campaign_name'}, {'description': 'Date the campaign launches.', 'name': 'launch_date'}, {'description': 'The attached intake brief document for the campaign.', 'name': 'intake_brief'}, {'description': 'People to invite to the kick-off meeting.', 'name': 'stakeholders'}, {'description': 'Date for the kick-off invite.', 'name': 'kickoff_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when starting a new marketing campaign that needs a brief, prior-campaign learnings, a workspace folder, and a kickoff meeting drafted for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CampaignKickOff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignKickOff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'campaign_name': {'description': 'Name of the new campaign; used for the brief and the OneDrive folder.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'intake_brief': {'description': 'The attached intake brief document for the campaign.', 'type': 'string'}, 'kickoff_date': {'description': 'Date for the kick-off invite.', 'type': 'string'}, 'launch_date': {'description': 'Date the campaign launches.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'stakeholders': {'description': 'People to invite to the kick-off meeting.', 'type': 'string'}},
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
    print(CampaignKickOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
