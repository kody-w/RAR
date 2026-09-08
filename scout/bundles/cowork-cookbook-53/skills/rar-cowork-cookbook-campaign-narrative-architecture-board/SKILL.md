---
name: "rar-cowork-cookbook-campaign-narrative-architecture-board"
description: "Builds a Miro narrative architecture board for a campaign from its brief, approved messaging, audience definitions, and positioning files \u2014 core narrative, message pillars, proof points, audience adaptations, plus a cove"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_narrative_architecture_board", "rar_sha256": "78b5a05a88b7f717feb12458bdd59622fcae455ff2dc2f62f36df54b4fcbd958", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/campaign_narrative_architecture_board`. The original RAPP
agent is preserved byte-for-byte in `campaign_narrative_architecture_board_agent.py` and in the RCI capsule.

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

Build a campaign narrative architecture board — Builds a Miro narrative architecture board for a campaign from its brief, approved messaging, audience definitions, and positioning files — core narrative, message pillars, proof points, audience adaptations, plus a cove

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
  Upstream entry : https://coworkcookbook.com/recipes/campaign-narrative-architecture-board
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
      "description": "The campaign whose narrative architecture is being built.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "messaging_doc": {
      "description": "Document containing the approved campaign messaging.",
      "type": "string"
    },
    "onedrive_folder": {
      "description": "Folder holding the campaign brief, audience definitions, and recent positioning work.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_narrative_architecture_board_agent.py` and embedded as the fenced Python below (sha256 78b5a05a88b7f717…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_narrative_architecture_board_agent.py` first:

```bash
python3 campaign_narrative_architecture_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_narrative_architecture_board_agent.py   # or on stdin
python3 campaign_narrative_architecture_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a campaign narrative architecture board — Builds a Miro narrative architecture board for a campaign from its brief, approved messaging, audience definitions, and positioning files — core narrative, message pillars, proof points, audience adaptations, plus a cove

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
  Upstream entry : https://coworkcookbook.com/recipes/campaign-narrative-architecture-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/campaign_narrative_architecture_board',
    "version": '3.0.3',
    "display_name": 'Build a campaign narrative architecture board',
    "description": 'Builds a Miro narrative architecture board for a campaign from its brief, approved messaging, audience definitions, and positioning files — core narrative, message pillars, proof points, audience adaptations, plus a cove',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'miro'],
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
        "upstream_slug": 'campaign-narrative-architecture-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/campaign-narrative-architecture-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7700b56b2b66a651',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/campaign-narrative-architecture-board', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', 'Output matches: A Miro narrative architecture board mapping the core campaign story, message pillars, proof points, and audience adaptations - so the entire team is building from the same architecture, not interpreting the brief differently.'], 'confidence': 1.0, 'deliverable': 'A Miro narrative architecture board mapping the core campaign story, message pillars, proof points, and audience adaptations - so the entire team is building from the same architecture, not interpreting the brief differently.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'campaign_name': 'The campaign whose narrative architecture is being built.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'messaging_doc': 'Document containing the approved campaign messaging.', 'onedrive_folder': 'Folder holding the campaign brief, audience definitions, and recent positioning work.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset. A Miro narrative architecture board mapping the core campaign story, message pillars, proof points, and audience adaptations - so the entire team is building from the same architecture, not interpreting the brief differently.', 'expected_output': 'A Miro narrative architecture board mapping the core campaign story, message pillars, proof points, and audience adaptations - so the entire team is building from the same architecture, not interpreting the brief differently.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': "I'm building out the narrative architecture for [Campaign name] and I want it pressure-tested visually before we start writing copy. Pull the campaign brief, the approved messaging in [Messaging doc], the audience definitions, and any recent positioning work from [OneDrive folder].\n\nBuild a Miro narrative architecture board that maps the campaign's structural story: the core narrative (what we're saying at the highest level), the three to four message pillars that support it, the proof points under each pillar, and the audience-specific adaptations (exec, IC, partner, customer, press) that branch off the architecture.\n\nUse frames, shapes, and connectors to show how the story flows together - and add a tracking table beneath the architecture mapping pillar → proof point → audience adaptation → asset, so we can see at a glance what's covered and what still needs work.\n\nboard", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Miro narrative architecture board mapping the core campaign story, message pillars, proof points, and audience adaptations - so the entire team is building from the same architecture, not interpreting the brief differently.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Miro narrative architecture board for a campaign from its brief, approved messaging, audience definitions, and positioning files — core narrative, message pillars, proof points, audience adaptations, plus a cove', 'example_request': 'Build a Miro narrative architecture board for the Q3 Secure Launch campaign using our approved messaging doc and the campaign OneDrive folder.', 'inputs': [{'description': 'The campaign whose narrative architecture is being built.', 'name': 'Campaign name'}, {'description': 'Document containing the approved campaign messaging.', 'name': 'Messaging doc'}, {'description': 'Folder holding the campaign brief, audience definitions, and recent positioning work.', 'name': 'OneDrive folder'}], 'model': 'claude-opus-5', 'when_to_use': "Call when a team wants a campaign's narrative structure mapped and pressure-tested visually in Miro before any copy is written."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CampaignNarrativeArchitectureBoard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignNarrativeArchitectureBoard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'campaign_name': {'description': 'The campaign whose narrative architecture is being built.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'messaging_doc': {'description': 'Document containing the approved campaign messaging.', 'type': 'string'}, 'onedrive_folder': {'description': 'Folder holding the campaign brief, audience definitions, and recent positioning work.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(CampaignNarrativeArchitectureBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
