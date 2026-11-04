---
name: "rar-cat-agent-skills-work-iq-signalboard"
description: "Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_iq_signalboard", "rar_sha256": "5c8656fd0619330356b42a88ac5ec7cdf57ad539fe5f8f82863bfbf9618e1a43", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "4.0.2", "author": "Andreas Adner", "tags": ["work_iq", "microsoft_365", "dashboard", "visualization", "work_patterns", "analytics"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_iq_signalboard_agent.py` and embedded as the fenced Python below (sha256 5c8656fd06193303…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_iq_signalboard_agent.py` first:

```bash
python3 work_iq_signalboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_iq_signalboard_agent.py   # or on stdin
python3 work_iq_signalboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/work_iq_signalboard_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/work_iq_signalboard_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/work_iq_signalboard/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
