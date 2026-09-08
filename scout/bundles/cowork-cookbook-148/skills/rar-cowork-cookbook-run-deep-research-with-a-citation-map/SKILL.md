---
name: "rar-cowork-cookbook-run-deep-research-with-a-citation-map"
description: "Reads every document in a specified folder and returns a structured research brief on a topic: background, key findings, cross-source conflicts, three strongest insights, a citation map to source file and page, plus gaps"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/run_deep_research_with_a_citation_map", "rar_sha256": "e87afe12257adb884ba49caa0b9a8db751503a7537ac9f466128e62987ddb042", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
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
