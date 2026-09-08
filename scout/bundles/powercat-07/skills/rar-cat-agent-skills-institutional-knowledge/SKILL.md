---
name: "rar-cat-agent-skills-institutional-knowledge"
description: "Preserve a departing senior leader's institutional knowledge \u2014 decisions, rationale, relationships, and tribal knowledge \u2014 by mining their M365 signals into a structured, multi-phase archive a successor can ground on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/institutional_knowledge", "rar_sha256": "dea44d1c2bf0f7803a9848d3d09ce9e461afd0b5dad71a53f21c4e8f374a544b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Srinivas Varukala", "tags": ["knowledge", "handoff", "leadership", "m365", "offboarding", "documentation", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `institutional_knowledge_agent.py` and embedded as the fenced Python below (sha256 dea44d1c2bf0f780…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `institutional_knowledge_agent.py` first:

```bash
python3 institutional_knowledge_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 institutional_knowledge_agent.py   # or on stdin
python3 institutional_knowledge_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
