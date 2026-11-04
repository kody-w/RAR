---
name: "rar-cat-agent-skills-work-iq-signalboard"
description: "Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_iq_signalboard", "rar_sha256": "5c8656fd0619330356b42a88ac5ec7cdf57ad539fe5f8f82863bfbf9618e1a43", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.0.2", "author": "Andreas Adner", "tags": ["work_iq", "microsoft_365", "dashboard", "visualization", "work_patterns", "analytics"]}
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
