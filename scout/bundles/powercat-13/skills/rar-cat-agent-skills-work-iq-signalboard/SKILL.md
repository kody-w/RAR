---
name: "rar-cat-agent-skills-work-iq-signalboard"
description: "Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_iq_signalboard", "rar_sha256": "aed7e0f4e887eb61a85f9bf095e590243f3d0b80feea9403a3c7ef8ec3227c8f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "4.0.2", "author": "Andreas Adner", "tags": ["work_iq", "microsoft_365", "dashboard", "visualization", "work_patterns", "analytics"]}
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
