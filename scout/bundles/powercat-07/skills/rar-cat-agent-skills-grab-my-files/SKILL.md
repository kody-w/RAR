---
name: "rar-cat-agent-skills-grab-my-files"
description: "One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/grab_my_files", "rar_sha256": "87306cef061485d897f062adf3691db5cd71059a53cae8f107662a09c353b298", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Rafael Alcaraz", "tags": ["files", "export", "zip", "download", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/grab_my_files`. The original RAPP
agent is preserved byte-for-byte in `grab_my_files_agent.py` and in the RCI capsule.

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

Grab My Files — One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#grab-my-files
  Upstream author: Rafael Alcaraz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `grab_my_files_agent.py` and embedded as the fenced Python below (sha256 87306cef061485d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `grab_my_files_agent.py` first:

```bash
python3 grab_my_files_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 grab_my_files_agent.py   # or on stdin
python3 grab_my_files_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Grab My Files — One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#grab-my-files
  Upstream author: Rafael Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/grab_my_files',
    "version": '3.0.2',
    "display_name": 'Grab My Files',
    "description": 'One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download.',
    "author": 'Rafael Alcaraz',
    "tags": ['files', 'export', 'zip', 'download', 'productivity'],
    "category": 'pipeline',
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
        "upstream_slug": 'grab-my-files',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#grab-my-files',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '846bd7a050af6ac5',
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['tag:export', 'word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class GrabMyFiles(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GrabMyFiles'
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
    print(GrabMyFiles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
