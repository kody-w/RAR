---
name: "rar-cat-agent-skills-content-quality-auditor"
description: "Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/content_quality_auditor", "rar_sha256": "d8b1870486fa4ca8f04150a70925851ae31980f7535850af3297aa10318d464f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["content", "quality", "audit", "documents", "productivity", "governance"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `content_quality_auditor_agent.py` and embedded as the fenced Python below (sha256 d8b1870486fa4ca8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `content_quality_auditor_agent.py` first:

```bash
python3 content_quality_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 content_quality_auditor_agent.py   # or on stdin
python3 content_quality_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
