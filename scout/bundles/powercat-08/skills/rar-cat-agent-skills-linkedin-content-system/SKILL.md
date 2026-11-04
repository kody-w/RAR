---
name: "rar-cat-agent-skills-linkedin-content-system"
description: "Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_system", "rar_sha256": "354dcb11218d125b0d047e466c38e3923af74d37dfc7bcd9a47de2e742b84fab", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["linkedin", "social_media", "writing", "marketing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/linkedin_content_system`. The original RAPP
agent is preserved byte-for-byte in `linkedin_content_system_agent.py` and in the RCI capsule.

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

LinkedIn Content System — Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-system
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_system_agent.py` and embedded as the fenced Python below (sha256 354dcb11218d125b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_system_agent.py` first:

```bash
python3 linkedin_content_system_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 linkedin_content_system_agent.py   # or on stdin
python3 linkedin_content_system_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/linkedin_content_system_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/linkedin_content_system_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/linkedin_content_system/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
LinkedIn Content System — Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-system
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/linkedin_content_system',
    "version": '2.1.2',
    "display_name": 'LinkedIn Content System',
    "description": 'Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.',
    "author": 'Simon Owen',
    "tags": ['linkedin', 'social_media', 'writing', 'marketing', 'content'],
    "category": 'general',
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
        "upstream_slug": 'linkedin-content-system',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#linkedin-content-system',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '207c56909d447f78',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class LinkedinContentSystem(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LinkedinContentSystem'
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
    print(LinkedinContentSystem().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
