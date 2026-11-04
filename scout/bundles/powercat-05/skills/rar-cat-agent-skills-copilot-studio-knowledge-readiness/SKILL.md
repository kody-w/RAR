---
name: "rar-cat-agent-skills-copilot-studio-knowledge-readiness"
description: "Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_knowledge_readiness", "rar_sha256": "9e86d57d4ff70581b2367925a2653531ce3b14d3dde20848b17b720b60511a93", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Jay Padimiti", "tags": ["copilot_studio", "knowledge", "rag", "sharepoint", "dataverse", "governance", "readiness", "assessment"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_knowledge_readiness_agent.py` and embedded as the fenced Python below (sha256 9e86d57d4ff70581…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_knowledge_readiness_agent.py` first:

```bash
python3 copilot_studio_knowledge_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_knowledge_readiness_agent.py   # or on stdin
python3 copilot_studio_knowledge_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_knowledge_readiness_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_knowledge_readiness_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_knowledge_readiness/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
