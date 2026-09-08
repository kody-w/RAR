---
name: "rar-cowork-cookbook-run-deep-research-with-a-citation-map"
description: "Reads every document in a specified folder and returns a structured research brief on a topic: background, key findings, cross-source conflicts, three strongest insights, a citation map to source file and page, plus gaps"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/run_deep_research_with_a_citation_map", "rar_sha256": "e87afe12257adb884ba49caa0b9a8db751503a7537ac9f466128e62987ddb042", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/run_deep_research_with_a_citation_map`. The original RAPP
agent is preserved byte-for-byte in `run_deep_research_with_a_citation_map_agent.py` and in the RCI capsule.

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

Run deep research with a citation map — Reads every document in a specified folder and returns a structured research brief on a topic: background, key findings, cross-source conflicts, three strongest insights, a citation map to source file and page, plus gaps

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
  Upstream entry : https://coworkcookbook.com/recipes/run-deep-research-with-a-citation-map
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
    "document_type": {
      "description": "Kind of sources, e.g. PDFs, research papers, contracts, reports.",
      "type": "string"
    },
    "folder_path": {
      "description": "Location of the folder of source documents to read in full.",
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
    "topic": {
      "description": "The topic the structured brief should cover.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `run_deep_research_with_a_citation_map_agent.py` and embedded as the fenced Python below (sha256 e87afe12257adb88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `run_deep_research_with_a_citation_map_agent.py` first:

```bash
python3 run_deep_research_with_a_citation_map_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 run_deep_research_with_a_citation_map_agent.py   # or on stdin
python3 run_deep_research_with_a_citation_map_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run deep research with a citation map — Reads every document in a specified folder and returns a structured research brief on a topic: background, key findings, cross-source conflicts, three strongest insights, a citation map to source file and page, plus gaps

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
  Upstream entry : https://coworkcookbook.com/recipes/run-deep-research-with-a-citation-map
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/run_deep_research_with_a_citation_map',
    "version": '3.0.3',
    "display_name": 'Run deep research with a citation map',
    "description": 'Reads every document in a specified folder and returns a structured research brief on a topic: background, key findings, cross-source conflicts, three strongest insights, a citation map to source file and page, plus gaps',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'run-deep-research-with-a-citation-map',
        "upstream_url": 'https://coworkcookbook.com/recipes/run-deep-research-with-a-citation-map',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ff25a03ce2c6fee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/conduct-deep-research'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/run-deep-research-with-a-citation-map', 'uses_skills': {'custom': [], 'ootb': ['Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A structured research artifact grounded in every source document, with a clickable citation map linking each insight back to the original file. Conflicts, gaps, and the three strongest findings surfaced explicitly.'], 'confidence': 1.0, 'deliverable': 'A structured research artifact grounded in every source document, with a clickable citation map linking each insight back to the original file. Conflicts, gaps, and the three strongest findings surfaced explicitly.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'document_type': 'Kind of sources, e.g. PDFs, research papers, contracts, reports.', 'folder_path': 'Location of the folder of source documents to read in full.', 'topic': 'The topic the structured brief should cover.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source. A structured research artifact grounded in every source document, with a clickable citation map linking each insight back to the original file. Conflicts, gaps, and the three strongest findings surfaced explicitly.', 'expected_output': 'A structured research artifact grounded in every source document, with a clickable citation map linking each insight back to the original file. Conflicts, gaps, and the three strongest findings surfaced explicitly.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "I'm giving you a folder of [PDFs / research papers / contracts / reports]. Read every document in full.\n\nProduce a structured brief on [topic] covering background and context, key findings, conflicts across sources, and the three strongest insights with rationale.\n\nCross-reference the findings against our live business data in Fabric - validate where the documents line up with our actual metrics and flag where they diverge.\n\nInclude a citation map that links each claim back to its source document and page reference.\n\nFlag any gaps or missing context I should chase.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A structured research artifact grounded in every source document, with a clickable citation map linking each insight back to the original file. Conflicts, gaps, and the three strongest findings surfaced explicitly.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads every document in a specified folder and returns a structured research brief on a topic: background, key findings, cross-source conflicts, three strongest insights, a citation map to source file and page, plus gaps', 'example_request': 'Read the contracts folder and give me a cited brief on vendor renewal risk, checked against our Fabric data.', 'inputs': [{'description': 'Location of the folder of source documents to read in full.', 'name': 'folder_path'}, {'description': 'Kind of sources, e.g. PDFs, research papers, contracts, reports.', 'name': 'document_type'}, {'description': 'The topic the structured brief should cover.', 'name': 'topic'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user has a folder of PDFs, papers, contracts or reports and wants a cited brief cross-referenced against live Fabric business data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class RunDeepResearchWithACitationMap(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RunDeepResearchWithACitationMap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'document_type': {'description': 'Kind of sources, e.g. PDFs, research papers, contracts, reports.', 'type': 'string'}, 'folder_path': {'description': 'Location of the folder of source documents to read in full.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The topic the structured brief should cover.', 'type': 'string'}},
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
    print(RunDeepResearchWithACitationMap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
