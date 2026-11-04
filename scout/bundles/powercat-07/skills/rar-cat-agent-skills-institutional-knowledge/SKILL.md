---
name: "rar-cat-agent-skills-institutional-knowledge"
description: "Preserve a departing senior leader's institutional knowledge \u2014 decisions, rationale, relationships, and tribal knowledge \u2014 by mining their M365 signals into a structured, multi-phase archive a successor can ground on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/institutional_knowledge", "rar_sha256": "489ff33a6d36e72d27f064145f456dd7ae0a8cc8194bfbc704bd650b013ea9c7", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.3", "author": "Srinivas Varukala", "tags": ["knowledge", "handoff", "leadership", "m365", "offboarding", "documentation", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/institutional_knowledge`. The original RAPP
agent is preserved byte-for-byte in `institutional_knowledge_agent.py` and in the RCI capsule.

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

Institutional Knowledge Archivist — Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#institutional-knowledge
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `institutional_knowledge_agent.py` and embedded as the fenced Python below (sha256 489ff33a6d36e72d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `institutional_knowledge_agent.py` first:

```bash
python3 institutional_knowledge_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 institutional_knowledge_agent.py   # or on stdin
python3 institutional_knowledge_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/institutional_knowledge_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/institutional_knowledge_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/institutional_knowledge/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Institutional Knowledge Archivist — Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#institutional-knowledge
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/institutional_knowledge',
    "version": '3.0.3',
    "display_name": 'Institutional Knowledge Archivist',
    "description": "Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.",
    "author": 'Srinivas Varukala',
    "tags": ['knowledge', 'handoff', 'leadership', 'm365', 'offboarding', 'documentation', 'productivity'],
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
        "upstream_slug": 'institutional-knowledge',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#institutional-knowledge',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3ac7896e76455716',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class InstitutionalKnowledge(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'InstitutionalKnowledge'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
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
    print(InstitutionalKnowledge().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
