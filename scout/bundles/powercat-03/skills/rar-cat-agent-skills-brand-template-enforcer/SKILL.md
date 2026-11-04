---
name: "rar-cat-agent-skills-brand-template-enforcer"
description: "Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_template_enforcer", "rar_sha256": "9b55307c395f49f3800d1bafe751f64efa1519e40b9e69b3a57e9bebbc02c541", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.2.2", "author": "Doug Bellingeri", "tags": ["branding", "powerpoint", "word", "templates", "documents", "presentations"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `brand_template_enforcer_agent.py` and embedded as the fenced Python below (sha256 9b55307c395f49f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `brand_template_enforcer_agent.py` first:

```bash
python3 brand_template_enforcer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 brand_template_enforcer_agent.py   # or on stdin
python3 brand_template_enforcer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/brand_template_enforcer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/brand_template_enforcer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/brand_template_enforcer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
