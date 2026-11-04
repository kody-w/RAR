---
name: "rar-cat-agent-skills-grab-my-files"
description: "One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/grab_my_files", "rar_sha256": "4e061e2a8f91902cfcee4405227ad8e5b37c9e36652786af4f49858348569b10", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Rafael Alcaraz", "tags": ["files", "export", "zip", "download", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `grab_my_files_agent.py` and embedded as the fenced Python below (sha256 4e061e2a8f91902c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `grab_my_files_agent.py` first:

```bash
python3 grab_my_files_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 grab_my_files_agent.py   # or on stdin
python3 grab_my_files_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/grab_my_files_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/grab_my_files_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/grab_my_files/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
