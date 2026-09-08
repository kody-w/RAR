---
name: "rar-cat-agent-skills-lookup-dataverse-table"
description: "Search any Microsoft Dataverse table, browse matching records, and drill into full record details \u2014 sourced live via the Dataverse MCP Server."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lookup_dataverse_table", "rar_sha256": "7b24a8b526f90b9df0e2d3d9c0e0402b8757bba8c615da546a617fff0815b959", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Chris Garty", "tags": ["dataverse", "mcp", "data_lookup", "power_platform", "crm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/lookup_dataverse_table`. The original RAPP
agent is preserved byte-for-byte in `lookup_dataverse_table_agent.py` and in the RCI capsule.

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

Dataverse Table Lookup — Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table
  Upstream author: Chris Garty
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lookup_dataverse_table_agent.py` and embedded as the fenced Python below (sha256 7b24a8b526f90b9d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lookup_dataverse_table_agent.py` first:

```bash
python3 lookup_dataverse_table_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lookup_dataverse_table_agent.py   # or on stdin
python3 lookup_dataverse_table_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dataverse Table Lookup — Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table
  Upstream author: Chris Garty
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/lookup_dataverse_table',
    "version": '3.0.2',
    "display_name": 'Dataverse Table Lookup',
    "description": 'Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.',
    "author": 'Chris Garty',
    "tags": ['dataverse', 'mcp', 'data_lookup', 'power_platform', 'crm'],
    "category": 'integrations',
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
        "upstream_slug": 'lookup-dataverse-table',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '9a79dc859cb36791',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:mcp'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class LookupDataverseTable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LookupDataverseTable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(LookupDataverseTable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
