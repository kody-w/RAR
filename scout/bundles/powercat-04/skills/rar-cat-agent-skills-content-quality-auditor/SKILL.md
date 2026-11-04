---
name: "rar-cat-agent-skills-content-quality-auditor"
description: "Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/content_quality_auditor", "rar_sha256": "cd8db2c4cd8e2a03a2e6ad4aa7879a1a9cf9f78cbaf3eb95e9ef25f0efdda293", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["content", "quality", "audit", "documents", "productivity", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/content_quality_auditor`. The original RAPP
agent is preserved byte-for-byte in `content_quality_auditor_agent.py` and in the RCI capsule.

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

Content Quality Auditor — Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#content-quality-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `content_quality_auditor_agent.py` and embedded as the fenced Python below (sha256 cd8db2c4cd8e2a03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `content_quality_auditor_agent.py` first:

```bash
python3 content_quality_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 content_quality_auditor_agent.py   # or on stdin
python3 content_quality_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/content_quality_auditor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/content_quality_auditor_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/content_quality_auditor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Content Quality Auditor — Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#content-quality-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/content_quality_auditor',
    "version": '2.1.2',
    "display_name": 'Content Quality Auditor',
    "description": 'Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.',
    "author": 'Simon Owen',
    "tags": ['content', 'quality', 'audit', 'documents', 'productivity', 'governance'],
    "category": 'productivity',
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
        "upstream_slug": 'content-quality-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#content-quality-auditor',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b2eca5049c1ef246',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.636, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'tag:governance', 'tag:quality', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class ContentQualityAuditor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ContentQualityAuditor'
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
    print(ContentQualityAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
