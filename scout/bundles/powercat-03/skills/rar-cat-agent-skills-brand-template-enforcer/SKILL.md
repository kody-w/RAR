---
name: "rar-cat-agent-skills-brand-template-enforcer"
description: "Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_template_enforcer", "rar_sha256": "c4732fde24a93d74c774a8b69f5ad43d891add5ea8d12223073f6488db1555e6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.2.2", "author": "Doug Bellingeri", "tags": ["branding", "powerpoint", "word", "templates", "documents", "presentations"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/brand_template_enforcer`. The original RAPP
agent is preserved byte-for-byte in `brand_template_enforcer_agent.py` and in the RCI capsule.

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

Brand Template Enforcer — Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-template-enforcer
  Upstream author: Doug Bellingeri
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `brand_template_enforcer_agent.py` and embedded as the fenced Python below (sha256 c4732fde24a93d74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `brand_template_enforcer_agent.py` first:

```bash
python3 brand_template_enforcer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 brand_template_enforcer_agent.py   # or on stdin
python3 brand_template_enforcer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Brand Template Enforcer — Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-template-enforcer
  Upstream author: Doug Bellingeri
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/brand_template_enforcer',
    "version": '3.2.2',
    "display_name": 'Brand Template Enforcer',
    "description": 'Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template.',
    "author": 'Doug Bellingeri',
    "tags": ['branding', 'powerpoint', 'word', 'templates', 'documents', 'presentations'],
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
        "upstream_slug": 'brand-template-enforcer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#brand-template-enforcer',
        "upstream_version": '1.2.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5bd07a11a05931f7',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:powerpoint', 'tag:presentations', 'tag:word', 'word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BrandTemplateEnforcer(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrandTemplateEnforcer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(BrandTemplateEnforcer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
