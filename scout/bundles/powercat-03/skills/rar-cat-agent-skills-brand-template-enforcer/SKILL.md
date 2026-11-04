---
name: "rar-cat-agent-skills-brand-template-enforcer"
description: "Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_template_enforcer", "rar_sha256": "9b55307c395f49f3800d1bafe751f64efa1519e40b9e69b3a57e9bebbc02c541", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.2.2", "author": "Doug Bellingeri", "tags": ["branding", "powerpoint", "word", "templates", "documents", "presentations"]}
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
