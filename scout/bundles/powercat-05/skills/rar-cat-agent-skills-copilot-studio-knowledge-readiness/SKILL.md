---
name: "rar-cat-agent-skills-copilot-studio-knowledge-readiness"
description: "Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_knowledge_readiness", "rar_sha256": "9e86d57d4ff70581b2367925a2653531ce3b14d3dde20848b17b720b60511a93", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Jay Padimiti", "tags": ["copilot_studio", "knowledge", "rag", "sharepoint", "dataverse", "governance", "readiness", "assessment"]}
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
