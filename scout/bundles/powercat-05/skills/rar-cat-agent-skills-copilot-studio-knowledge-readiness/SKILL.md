---
name: "rar-cat-agent-skills-copilot-studio-knowledge-readiness"
description: "Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_knowledge_readiness", "rar_sha256": "ff5febf605e0ed1a3f38a7e99ef1f90a3eef5861fcdd7ffe650fa70cda95c97d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Jay Padimiti", "tags": ["copilot_studio", "knowledge", "rag", "sharepoint", "dataverse", "governance", "readiness", "assessment"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_knowledge_readiness`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_knowledge_readiness_agent.py` and in the RCI capsule.

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

Copilot Studio Knowledge Readiness — Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-knowledge-readiness
  Upstream author: Jay Padimiti
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_knowledge_readiness_agent.py` and embedded as the fenced Python below (sha256 ff5febf605e0ed1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_knowledge_readiness_agent.py` first:

```bash
python3 copilot_studio_knowledge_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_knowledge_readiness_agent.py   # or on stdin
python3 copilot_studio_knowledge_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Knowledge Readiness — Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-knowledge-readiness
  Upstream author: Jay Padimiti
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_knowledge_readiness',
    "version": '3.0.2',
    "display_name": 'Copilot Studio Knowledge Readiness',
    "description": 'Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.',
    "author": 'Jay Padimiti',
    "tags": ['copilot_studio', 'knowledge', 'rag', 'sharepoint', 'dataverse', 'governance', 'readiness', 'assessment'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'copilot-studio-knowledge-readiness',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-knowledge-readiness',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd4fe7450b56dfe2a',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'word:assess', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CopilotStudioKnowledgeReadiness(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioKnowledgeReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(CopilotStudioKnowledgeReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
