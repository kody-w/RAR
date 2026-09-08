---
name: "rar-cat-agent-skills-brand-template-enforcer"
description: "Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_template_enforcer", "rar_sha256": "c4732fde24a93d74c774a8b69f5ad43d891add5ea8d12223073f6488db1555e6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.2.2", "author": "Doug Bellingeri", "tags": ["branding", "powerpoint", "word", "templates", "documents", "presentations"]}
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
