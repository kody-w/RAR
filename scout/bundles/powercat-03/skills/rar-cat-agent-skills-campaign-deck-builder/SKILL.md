---
name: "rar-cat-agent-skills-campaign-deck-builder"
description: "Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/campaign_deck_builder", "rar_sha256": "c83e942f9e64a210e436258385a286a7ad7808a844d8e3b0bfcba90cdae4917a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["marketing", "presentations", "powerpoint", "automation", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/campaign_deck_builder`. The original RAPP
agent is preserved byte-for-byte in `campaign_deck_builder_agent.py` and in the RCI capsule.

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

Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_deck_builder_agent.py` and embedded as the fenced Python below (sha256 c83e942f9e64a210…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_deck_builder_agent.py` first:

```bash
python3 campaign_deck_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_deck_builder_agent.py   # or on stdin
python3 campaign_deck_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/campaign_deck_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/campaign_deck_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/campaign_deck_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/campaign_deck_builder',
    "version": '3.0.2',
    "display_name": 'Campaign Deck Builder',
    "description": 'Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.',
    "author": 'Adi Leibowitz',
    "tags": ['marketing', 'presentations', 'powerpoint', 'automation', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'campaign-deck-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '23b22be138aae9b6',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CampaignDeckBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignDeckBuilder'
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
    print(CampaignDeckBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
