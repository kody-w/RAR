---
name: "rar-cat-agent-skills-campaign-deck-builder"
description: "Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/campaign_deck_builder", "rar_sha256": "c83e942f9e64a210e436258385a286a7ad7808a844d8e3b0bfcba90cdae4917a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["marketing", "presentations", "powerpoint", "automation", "scripts"]}
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
