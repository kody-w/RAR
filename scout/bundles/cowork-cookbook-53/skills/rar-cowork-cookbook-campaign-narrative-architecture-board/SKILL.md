---
name: "rar-cowork-cookbook-campaign-narrative-architecture-board"
description: "Builds a Miro narrative architecture board for a campaign from its brief, approved messaging, audience definitions, and positioning files \u2014 core narrative, message pillars, proof points, audience adaptations, plus a cove"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_narrative_architecture_board", "rar_sha256": "78b5a05a88b7f717feb12458bdd59622fcae455ff2dc2f62f36df54b4fcbd958", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "miro"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZejVrblX1HH+2D7kZkgBgnlW2+tRiAmMQkEEnLWSjODmCcxuP3f+6KISKfLruqqXv2plUNIcO+Zz97nBvr1xem7uGxePr8YgVOsOCfLkjhoVk7hr+hyKJsU/ChTF/xbeWXRNYnbd2XTvnx48YPWa5KqS8oCbN/3Sea3K2clJ025KpymcbrkEaycxouTLvC6vglWbuk0/iosgfyV5+SVk0TFKmzKfJV07cptkiD8sHKqqikfgb/Kg7Z1oqSIwLXeT4LCC1Z+ECZFsuhsPzyNrMr2+REsW4VJFrSrLz2KrHFgLVD4zY4Pb9KCVZVkmdOA3UBLGYL9SdG132lwfKfqnDcNVdYvPnnAHuBxMAKbgYqXzz//7cNLAt6/fP71xcucFlx6od8cUt51Ut+5vl88ByIyp4jA2moCUS/A5ypoQDhycAl4tnr79GMbZCAQ//mf6eA0UfvT5y/F6u315WX5o/fFqouDVVc6bQci5TmV4yZZ0k2fVlQ2OFO7agKgtliMb0HSiujT687fJZXV6r+Xez++KvkUBd2PX15KYMLT+S8vP61Anr68NP3y/tMipfrxp09ZOQTNjz/9Lqft3TvwcREGrP709e3zm1iw8PelSbj6amgH+k1XE3hJFQDh3/m3vF5NfxP3FpKvr4t/LKsPq7+WvPjz38De17J0gdy/FgtiAHa+fLqDxP/4pmOpt8IB2f/xp38k1osDL82StvuX5P78KjgOHB9E6y0kP314pu9vK+jNt28y/7HaChTMv+MJWP6u7lug/pHsZ2b/TnSWFKCF3nP5l+L+agP036uf/6Fv/2zDh1X45YUJMtAujeNmwefVr88S+fkH//eLP/ztNyD6/yjGKPvGe0r4mjtFEgZt9/Xrzz+0z8s//O3nH/oKVHHg5F/7JvsrmX8V16eeP0TwbdWPf9wL9JtFWpRDsfrWQ6tfy+p/NL99WllOlvi/X28/r77vxOUFrRYn3pW+huC7bmyBrd/F8aeX3wD+FMCb3nveBvjxH/8BoNdryrYMu5XhlX23AgnukjxYjD/HSbsCfxfUaAIQ1zYBgX1bB+p/yfBiMUDEX/6n9wT+j94b8MPvUP31G5x+/R7Wvz5h/ZdPqzMQXjYJgGwnW+mUpn0pAOIW3aK4aoI2aBZYd6cu+Ah6+uPyZpUUq1/+Jflfn6I+VdMvT9xPXhFQp4UF/do+Cz4tfl7ioHjzygN8FoyB1wMtWekBk5788AH435YZoKZuiUmbAj5Y+QnAF8Br01M2iNvnRdgvv/ziOm38pXiFa2z1SngtDBZ8M2f18SPwLcySKO6+FIEXl6sffv3th9X/Wv2zXU/hiw4NkMdbVoCFoqEqgDKjPgfLQMJAigGEPLPy629vEQZiCsDQIIdJmASvm0GVpoH/Hm6Dpz6ixGblBuFCgoCoyqZbCDLpPq2EcPXNXqB0ubWwRFy2HWDXKih8QIMTkOoAd75Fsii7VQtS04bTh1XfBk+tv7iN8zQxB+3udL+sZFoDnFRm4L/FzOcisBmwMwj/t2J4vQ6END+0q/27iE8rZanLVeU0ThU3zpuO0HnNyzIzvG0Hwp1VEQxfioWCgyVUzyZ5DQ9YBCLjvaX045JzwN85QAS/fdf9XOMszHl+MmjzpWjfGsBpllQshA+URn3iL7TwX28l1cZln/nP+AFLF0lvWfDfsvKsweco9P2E80+nobdx5f/7+WmJDMVx+oGjzgdmdVDOuv2asWWuXDL7OoqCIebp4bM7fx9s3sHrHcO/FFkCyq+Z/ut15TPPb2tecREEzAcopD/lgyIDGVvkPntgqemmWbrH+VK8kwVwYvVERlAGADBAQy11/K7ww9OPV0tjgArL598Hh2fNgNyAkII6X1W9m4EaDIPAdx0vBVY1Sx+/hRY0RLD09BAnXvwHr1ZAOqg7IH8FjFiSCgjl0zcAf737bvofNr7OR8uW5+zYgzZungKAHa95Ackekg6gmdO9jvHAz89PIcCNvOoW312QOODp68WgCeo+AeWxgOZrXIMKoPbH5eerp8vVYKxAeYJggQ6pehDdZ08t9ZSD6QfYAIoOtFgO6g5c9t6D8BTo5AtAAAB+G1dfJT4vvzkUPBtxobH3jYsjy55lMngtfqeYvseR81+VCZCXLyueev++0r5pW2QvWNoCPAQa3+++jhCfXqeA1zFj9S7385/OST/+e0epJ6+bfyyAz6u466r2Mwy/cvE7FX8CSAa/2tp+o+WP37r04/do8fGJFn8Q/ur359W/Z+AfRLw1yOfV+hPyCVluSW8F9vYC8aA/7u2P+HL3S6EHv4MtUF/mwNAlexOYA74x4/sSQI9RE0TL4lembBeCHQCnP6kBpOJL8X3FLx0HmKeIlgpty++Q4DkigOp/zdw3BgO3ig7o9pfRMgo+LSeyxfw2ePlc9Fn24aUAtfevHuYWqsqX2m6XcyDoIjCudUnw/PTdTLMI/PXvjstP3HtH8AGQb/CPMB945AZLN7mAIbrF4m6qFhNfz3XLJPiEpbH7sxb1+cbJPq2YAEBg1n5f629ktpD5dy35GlUQTQ9482Hlg1y0C/mCqC6OLu3stKA/QGv8pS3fSOerX3p/togpveds8w7Ki2PPjnwnrW9B+SboL9UABPWbZVAMywwg3Z8Vsc/roI0z/13HN9HvRPkPSREEYbHxe25c2uOvLXmf0f9swwUMRQuF+OXnZT748Aa0Cy064NO3IxII89uhddEQFH3+8vnn5Xi21Nhzy/IG7AE/vm369hsYN3j525/sAoY90Rtw4CLrdyN/X1o+j3WLC0B09/pbiF9B/jrA4J3zVtFv5wKwHIDdx3aZgmDQ+UA5+Pzao+De/92J4U1IGztgWAVStqRLOAjhkKS7DbfrbRi4axQnSNf3id0GRUPPCXCCCEPU99Bwg4bYxg8J3MVDz/V3BAnkvbb712XeSxbDiN02RHY7NMTXKOKDPKO475MbcuMRWxRxdq5DuMTOcX/fmiaF/+btq3dLKL8dXpaovDn964u7wcFKHm8F6vVFw9Da2+JbV68kuKnDEsc2J0IY8HMhjdRDJA7XR7untMO9hdFtcrTpQy25AmqXZsKdPcJWxjjSdgjDa7ZITmeshqq+TTNdRpXC28WtVOyjJJj6pt7Aj03Vq6eERlx5Y1zkWDcMLDZnVSZ4sa10y6vzg3RUFLPOyzptM6tJWxvmZwzG+0BwuUz0xdwnoVBEr1qfrfPLjjXzfDzG6lqLj9NRbkiztZJ6a1wIJEPvub8ujlFrJuJlM+lSnZw1RSTy1oin2SLH83E6W1yRi209XlrtkBqXTBe5tDaGkTUfqYOMaptWW4Iz2wSpHDK1HAS3E5mRHQ2kcjN7j0ex3WxbayYDyernMIwDydd71rfqvKVKtk4JX+wCTbFu3cHGIPZKm5XmqRhdas0pC7K06/S8Ho+XAA9ynD90ek9T54t0jG+PoiFi8i6Jlpyl6VSa1WgK2UiZ6r7rbjenzZzNQF25yohQVL9VPEvEPuGtJ3078APkc5tovbsNWZE2N+8IaErMcpWUxqAy03SdNuxxzPyI9k8y1ahkOoiTOtYpYrhzgR+OorctE4yiuHR6kA2NBJG/9TakN49YlfNZxVLIybmeAgJj6/5c2TJbUnC9M+pGMdiblTtjjbS959gM7Fq8XmXhiW1uJV9XBmydCplKsvtmIK0z624vLqKgkM7XDbYPBv3UNk1dR/GaD4j13rwhrMuNFNQ2rJSxpcONI/8AA6konU89MhreCQlu/N3StpZtckopykcdPzxYDYfMI5fbc7bLVI3uY/NOI4rhmt3QnNBOoK6N+LDI9VFnKqWN2k65ZxcP3a2vVaBH/cQGchvGjrxhp5CwLCLAjzBpl1d4DIwurQqcewwZNyTBUXP4VMkHXFOMM8LP8xpVZvKS11G50+aNGnBiSuCW/rgj6F2t7gQUzGO8LsJ0sj1zHpxbuwPr+Tbwz62EDywBcQyp8oGmKopx3/KoPsrFA8WCOSSvEqJXSBOIURqRjAHpNpl2Imo35llN6nPZSbzbxkZRQddNNXD4pKalrCR7IqScaTwe4ztBpKjKXtapn27Rmtc0DE23N7XibJc2JLltyvBQ19s9wjCcBRKQRhxFXpKNX03QFS9BlXaHnIrXnU0X+yt1yk69I6PngruX8p2cN4wdSB106O+FWJzPtarfHFWvHEgXL13qHjP7oh/jeeKVeYfNqsKyx8KXOrLkb/bEJYxAd9GDdCDv1KHZHdueQ2arDMoWMoixnmfyJrJdMHT+2iCmgh8fnM4dd/XdNuKdLnl6mLhFlZXGbTdduFjkEQo308u64SXbKvIYOqKyNKXZqJ1u+VoqqquedjtGCLgDkXAMTGA5Uc5rHB9LNdyUGeGus8y4ByIp7bvSPfgoTsVQZmyc61HK0yYh7YAuzTY9XAU2PJGQKMoQFmW+LtzC4dEiDCSsEeRIk6amNGSHD0ZvPRBK8qRiqoV0HQwZf71nNny7XYQh6yKzO8dZoCVbdxAo63ZX8Qt22iN3UWQ8xMrn0bhmQ76ZauTapioTOEo21oqCHJh5B1nduaoxohin6YRGfYVvihgueBUr6oN8P85SRrnBoeZ3homDgGIXgpyPoSehgnDZsjBADIbG4ziwVNndRmO0c2g5YyGbx2JVuYmIvDmdq4LQZQChW+R015xytCHSTa9DUNq0V4iQdPOHo5QIRTAp0sGPcJphN4f9epPvYymV9Yc97RSstFmCjZGKvuhZzGgXtpe93eWgnPRC8fkSr1KWCciHgx1Vio5Y5ChD+hHPpy6JGCHFur7cxWsrk4Xb/nLi9QuqIXmFjNZkYXc956hc3R8o/KJp9iW0YWsz2s2F5plCaXC/wE4yfk0sou7up3vDY8QUPPj7ehdd2NwSR+lwa6FzUutH1djCcotBhM4xzOHCuhMqIFq4MwT/HAT81bjTcWHyMIyDdq0TJGjmtaPxLUgpNtZbr1LpqhZmRgstdNzTXH2Srinca9mximvith+KDWYaayNL8GZwA1Yta4lXxHPiJOuAwmKDcTYna3/AEjRRWVaQDzp6wg2xw88bFk7C0dycuYyOH/1tbUItxEK4jd7vjEBu90nLbvcVNFq6HzieFcP8wIzV9a5rt4bKRDm9SZyfp5tr7ttjJVmYI7COq3Pn0HJ7GpM7ybLRB7uVnLvqJ5GUbccIPiEx7T5SJqmKdXCflPLoQ6oaqhS46/QepMgyeVHguN7t92OQPWhqUzu0MN/NGm9uUwXb+0iT2dM+4+a1yWWmYVOEfbiOliXVTnzbj6S7D+tKl9k94QnnzZRc7pa9Lik+sc3T/eTkW+PwIDz3csrMzCRAwLVJiSmDJffacCa5FGCfUJnrLEfa0DjteSWle+pykieMve6PUon7aya6uJN2YOBkPgZjK1zr9WTJKqNRosRRlecP0ai0lyppsyMi4Ee8IiXuuL0hYnkI71d58hwh9jtXJFpCtk5EbtEnWFmLZwLeHa5MjXK6LYeKw5xo5Fxoyu1innwyUPaM2LV3ybhPdx2Bq8lMdiLe6hKs4ufu0jy0stax/da82aVEJIZpnra2v8W1O51caFwUk831sFZDsy8zlo1Fr91XKuFC5XSI7ycKqrYwet3WIqdSkJ1pXMCOnlu0nL45dkZG8yGf6+P2cVufD1LA5VyGum55jWoA++rJIyxwQrlgJorm6ljUxompgqu7nnbqHAmzxkZkXAk+vpXJE8Eb15MquvJkaTjmEBLXGRfOmISapVK25lM6FIxyOxpjdzHIZE7UYewp11yPcGQiEM8crpZmyJN7sZJRRo3xaIhWnANQb6S1po7uXun9DY1e9QNpQkOwpavI2oQ0XeqH0RiusGSiqjtIjCayhIKd2IlULExIxGKzzvV0LYrRmYTisumkPEEjKcpjvCGM2m9qPVPoh9RSgh+BacoQcvMBm/v41G3uAp3sg7EmW784llUVxi15i5OTIESXXIUHlzArMzsK/t7KjCGO50K46evTg/YtSvf0IlMr63xM+73ghvDGq/ekmcTXg8haVH5bJzN9eNTTiO1PYyhPdJmJeGWOSVZfPTQ7W2zfuWzCYfxtfTgcnbWa6CpalYmV54x1uUtaK2S66rtS02Vc2RT7HsydhkU94nrNhGKOwMgU62p0E8473s7tUkiox0b0ouyEdB6aPjomHbajaWLpA/chBNdksm48s0KxyTuIrfOwcjALmQJJyKVHbyy5WxetTTEGs2avpDGx7GhPWd/2LcUfZ7TV+WRI4I1qTIo7lvhQCZjvNrrt+MZtNNd+6GRnrr/nUiPHcRsVAp1hu2l3ZvT6JmjidCrBQK0OHe3aVMteEGXYEOuaThNkkvoD71lmzup7sKZoD8bAJ7lgDzhyODc9ygVF6smGUh+mbJ1yiFUNmzAKoY1ap5WTn8O7P06HQ4s+6I4S+nu69tN7tGPa++NMkF46H0yXz9i4wDdYYySR3G1jykR0m4m2znnd16NDonWOp+VJqDfEVbkRPAZ4xWbDVN8fh/Q6SVaiP2jy2qgpwuNIWdj3C0BcZoN6j5ybpGCI8B0nuEI7QAchl6nbbpdv7imr5QcamyRSe7SQh2GXHkKvrR7IFz5EZf+m8AeBstM+6CbA09U4KFcuG6NzQ9iEnSK2lUM6eRoPdRWKD6e5iQRyOtjkAQwA3cwILb3BJcDeRwIhmsslmG8M7MEzfboLa4iWB+RR5ccWR9rzziJYHZKQvYLz0kmYhN1+9M0gvGjZuYU3tS7kO+oU+9z2GAxsMoS7G6JHslTGuCRYTiOiPR54OXdvdVwM7rDyqHsEno/JFp9RmIxF65Ld6a1thKngUJZwR0XUhZF8LSa7hIBhCNuRZMhgkRknRSZHxOBqrE7eSyU+VXRazRkYoyZ5d+oLMzI2nbQVa9+8rC+1bZpRWGijQF+G7dpv7tLI8xE6COI4OhK2VxKX4GzaOEQ4ppaqwacWinemyuRuPyUUezENAT1eNhaHnMggpCVIPBD2mczg+uRpWlSVJFk/av08zcP55mP4cCXFDpZlnTsI6V1J6HYE8xyk9lAdOEZnW7Udz0fERK7lvubkbZ1nPl5O+Pmm6+okYyKVPCiXsNDopK9VL9DifdfoSXkglbveXzhK8xn9mtbl8Xasplwq0XjQlCAPBLzNcIK+Yre7Qsb9mnD3V65xoyZuoeAiWbeZu4tRXbLnK1+jZiqh7JxREnc+QwyzgfGDIgB+6eyycxQP30IPXCMdmQrs+/HQBseLJRo0N1+lZN1ojzjCmiGf7ikSNnPecg9SZepWAOVxt2hMLG+XMQu7gse8BL5BYbmbtI2WYpio1KNJUXkskupN11KTcxmFkTf09YCI45nyxbFSmjNCQ3XGTsT6dLjeGGs7YWN7DZTLRqa5Qbeg4irx9uZQoNpB2d/23b0Xl98qlFthVJnsEIATx7Y0Wj0U8fzukMauA8xtaLtOEB91QqkC4x55cDKiFb114PUEDn7H8kxF1u5m67WD4qrtuB0YpRVXU40ZClFp2xgeenV2UKzSl9oab9CsK3cft7jbo68lGQ4zpbDRMs6xzcODsuucOGHQ8BFnXh6G3xpdgQUCFVMjb/h3ooIaFzsLu5LBsm2hQecth8vKzYH2WybQRsyflRH3nWQM/V2jbgFSn+BNCW0rLPZU+HaVLqFblDM0eygUKztluwZH6zCBiMvGw/dBqAZ90yGlYRXMyeehSRNU1rrlYbuHdugYooPqyescIdb5pFAoojkXqDFdJ9K8Hd+18JbxFIm5hGBWhCdCY1z+ntcjc9cmi46nw/qchCY5bJwWNg5BUB5Q220IeuO6vaNn7MWdIfTmdwV5camARWjcabv55G6uvaQ8uHT38NxhOp/beM/c1wpSynvs1m7rEIzGGLw/uJl+S8+B27jQUWNn0ACSV3h7/9re5+u1B7DPQzFHWzJ1b0GTP6hSpKBcUK5wdboa+hk59wjOGWJ/ytPzaZ4PJJUJ5zY9RyjlpPeNNLmnWbJyNw/lHXvrpTJwu1oLhnRIUaMVra2Et8RIzIXSC3KocgMiDfw67ZsWra40KUr5Bn/cjkn76M4Iu8N4NxYLCr8qGGUXhXuX0RODTqyIr81KOUebyzCKGDjU54Uq2Qz/SPCe065pwsVYZ+Dby3krOrDbbGS/FehrnJMnw6CM3NgPEEw7tx16K8aiisoDb6wXSMkOwD3WbXMb7ZubfYUQYY0T4CAloXo3InPbtGFLlsWFtiNqJscWCvenYkjmztkflNA+GD04NlBt4l3LQTtf/b2X6olwiOzDeKYhgvbMNXWJJWXmsPQWbU6JF1oI1B7PjKrn0bnASndMt3he9/p45LstBYZ6wxiYDD9ngOWKYgw1bMbRix9zYqmx2nil/UCjfSiVi/YcUviZ2e+bvOx5np5b0mXKfGjm7dybxmjtOi7ki8HShG3tDwcElPS92wSELMn6+qaaXmAQuR45UnyBzNm6CtpFv+l3MKqlNOib0xWC7M2mbdL+rjy2tEIn9+Q87XAqmFJtu7F3dmhaAQ8fULHH9Ya/wceJ7rfnWc+1Dj5RAwsb+dmv583Fof317N/c1Dpf+6aaOpZJtYDXbVVHPf+E7gKmSgga2ZvmjtbE3g3u+WFPCHB8x3LjrJcJAhUlk4Y3dmdWRidhXVqOx/XM8DnjbC3LcPnxcXkEBrydbkQGDw/+EvQk9Qget7jod9r2KgeIiAmgwq7BFspw+zGvRTu5HHvifnF7cMbPH0phBZgSW8q8w4dm24/W3rX42txTExM+kJ7zKQ/KMXAy7nHeM02UUgKxagjXzGeDHPf1utbAYdWT0e2j0k7jjdvnc8dj7S4I7jtTtZM7RqEkg8ATU3K4qJon1KQNLpob2J6bfcuVM+3Bmx1+NcN5xk9CY7PyyIviw7C4NNiA9hqS6w3n4tOdhyhWKutQvlK2zam+sJPX6lQ5aZ2vB6QfFJ4/xHCWXh+XLuMJx3V14TbxOezabO7U3Pxw3cSe+d3a2nLwoNxBN5P7vHkEHsbyQm3QfHPc7u+w+dBRoQ0f1SRM0w62S9g+o/v1Y1Y3SifCapN2RyZznXW/BSYrbXPyakgxxPY8b2T2uHuEyuNIk+60Tuut0t/qIiDnmjDUwWqwVp708GS1t2q9f7SZXCGyROEyf9q4iqqZHYaThbddM+41zZu2n3eVfaATRROjMG5wf9eTNKZR+82etBLjCnnUvioDMzoOZ+3s+1imhCacKo8Nooj7gHIfPH8koXEHEdKhuezg+upcq/VOZszAJuDLZDJRmEOK3TLbAnOhKzUWOyV3s3w+cTp3EYJU2Uo8OLMKg/bYqVoPOxDz2El7WkO8DCWmK64dL0FI3jjYhbPj7rC9u9m65c/whY3PIh4qh3Y9w3yPWaJHEChDXgKk3blIpW8ybiwuSjTLuaEQHODqC6Ze4SHAPJE43Now588N3xjktkC30JBBOiHZw10/5fJ82/A1tuuJykM0dC95G17Q+vTMCFLo3Q9Uiqr0iYYJBvIjnirPPcPCXRq6HeF6RCxGZqiGbDfqRIhsi7hRd2g08LuDeh8A5ip3SGKivvSP8DQljwrF+0cUXPtr7yAb+PRQfSh5eJN2lzIYSrZohTh72CYZ/zKiDD1u5Bz2xJx3p4qF3Zvu3VjTV5B15RHkBc58xr+ihjOq6xli0+sGvlvN3sLVObY7+oFxuxCU8xWlOv1RXdiOvEWsHZHBVj4MAU7YTLgthVHXkKknEGgbAp7D4j6T4xLX+VN6PGnYcZw7Rd6bp9gJcppqzrBQqQxE+GutGBswX3PnWN1PXDg7e/+kVnvE53cpLOwPalYQCDvFGKPzDRaP+YANzXXXQzy7z5hScDfEbTc3bAQbmjiabs0irWy7mPwou0onAFVgvWjRJqkj8oaqYtKRAD/l4aPAikmG7l7kq8Lj/CBlKvQPeYpORHdo7hjRaduC29n7enNSuHbnAXbjz8hjO3a4LML6QFEvH16WJ9hvz6H/va/GLY+x/p89TXt98PX+BZfnE8nA8T8/dX3+N+3624eXxkuAVa/PDtusj94esv3dk8OP/9KXGhYR0+v3zt4ffb8+ve+caPl29ktS+H3bNdPXtsyeX3QBO9y+Xb7L2S5f9/XAz+8frpZdHDQvzyfpXlB1X7vya+40abDcc/zHEoBFaQKURW8PUj+85ElTLp69fSUCOIR9Qj5hL7/9b+MztS1WLwAA -->
