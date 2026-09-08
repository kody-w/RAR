---
name: "rar-cat-agent-skills-work-iq-signalboard"
description: "Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_iq_signalboard", "rar_sha256": "aed7e0f4e887eb61a85f9bf095e590243f3d0b80feea9403a3c7ef8ec3227c8f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.0.2", "author": "Andreas Adner", "tags": ["work_iq", "microsoft_365", "dashboard", "visualization", "work_patterns", "analytics"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/work_iq_signalboard`. The original RAPP
agent is preserved byte-for-byte in `work_iq_signalboard_agent.py` and in the RCI capsule.

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

Work IQ Signalboard — Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-iq-signalboard
  Upstream author: Andreas Adner
  Upstream version: 2.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_iq_signalboard_agent.py` and embedded as the fenced Python below (sha256 aed7e0f4e887eb61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_iq_signalboard_agent.py` first:

```bash
python3 work_iq_signalboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_iq_signalboard_agent.py   # or on stdin
python3 work_iq_signalboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Work IQ Signalboard — Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-iq-signalboard
  Upstream author: Andreas Adner
  Upstream version: 2.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/work_iq_signalboard',
    "version": '4.0.2',
    "display_name": 'Work IQ Signalboard',
    "description": 'Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts.',
    "author": 'Andreas Adner',
    "tags": ['work_iq', 'microsoft_365', 'dashboard', 'visualization', 'work_patterns', 'analytics'],
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
        "upstream_slug": 'work-iq-signalboard',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#work-iq-signalboard',
        "upstream_version": '2.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '267a75f8911138e0',
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class WorkIqSignalboard(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkIqSignalboard'
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
    print(WorkIqSignalboard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
