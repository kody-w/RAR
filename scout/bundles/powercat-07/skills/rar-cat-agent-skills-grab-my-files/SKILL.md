---
name: "rar-cat-agent-skills-grab-my-files"
description: "One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/grab_my_files", "rar_sha256": "87306cef061485d897f062adf3691db5cd71059a53cae8f107662a09c353b298", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafael Alcaraz", "tags": ["files", "export", "zip", "download", "productivity"]}
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
