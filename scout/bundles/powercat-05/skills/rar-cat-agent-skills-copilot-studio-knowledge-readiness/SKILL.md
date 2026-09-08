---
name: "rar-cat-agent-skills-copilot-studio-knowledge-readiness"
description: "Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_knowledge_readiness", "rar_sha256": "ff5febf605e0ed1a3f38a7e99ef1f90a3eef5861fcdd7ffe650fa70cda95c97d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Jay Padimiti", "tags": ["copilot_studio", "knowledge", "rag", "sharepoint", "dataverse", "governance", "readiness", "assessment"]}
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
