---
name: "rar-cat-agent-skills-grab-my-files"
description: "One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/grab_my_files", "rar_sha256": "4e061e2a8f91902cfcee4405227ad8e5b37c9e36652786af4f49858348569b10", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafael Alcaraz", "tags": ["files", "export", "zip", "download", "productivity"]}
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
