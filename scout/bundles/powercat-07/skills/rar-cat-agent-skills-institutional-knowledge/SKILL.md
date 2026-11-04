---
name: "rar-cat-agent-skills-institutional-knowledge"
description: "Preserve a departing senior leader's institutional knowledge \u2014 decisions, rationale, relationships, and tribal knowledge \u2014 by mining their M365 signals into a structured, multi-phase archive a successor can ground on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/institutional_knowledge", "rar_sha256": "489ff33a6d36e72d27f064145f456dd7ae0a8cc8194bfbc704bd650b013ea9c7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Srinivas Varukala", "tags": ["knowledge", "handoff", "leadership", "m365", "offboarding", "documentation", "productivity"]}
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
