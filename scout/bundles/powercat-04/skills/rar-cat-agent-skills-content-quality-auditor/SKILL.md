---
name: "rar-cat-agent-skills-content-quality-auditor"
description: "Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/content_quality_auditor", "rar_sha256": "cd8db2c4cd8e2a03a2e6ad4aa7879a1a9cf9f78cbaf3eb95e9ef25f0efdda293", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["content", "quality", "audit", "documents", "productivity", "governance"]}
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
