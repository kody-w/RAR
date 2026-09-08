---
name: "rar-cowork-cookbook-campaign-kick-off"
description: "Stands up a new campaign in Cowork: pulls prior campaign performance from Fabric, creates a OneDrive folder, drafts a Word working brief from the intake and email threads, and drafts a kick-off invite."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_kick_off", "rar_sha256": "fa1574b3a36e3aed2d7cd473459990dc162a230e6f53ca268f52bb3ccb577d6a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "fabric_iq"]}
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
