---
name: "rar-cat-agent-skills-linkedin-content-system"
description: "Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_system", "rar_sha256": "354dcb11218d125b0d047e466c38e3923af74d37dfc7bcd9a47de2e742b84fab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["linkedin", "social_media", "writing", "marketing", "content"]}
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
