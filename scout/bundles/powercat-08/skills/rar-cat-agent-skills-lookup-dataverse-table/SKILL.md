---
name: "rar-cat-agent-skills-lookup-dataverse-table"
description: "Search any Microsoft Dataverse table, browse matching records, and drill into full record details \u2014 sourced live via the Dataverse MCP Server."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lookup_dataverse_table", "rar_sha256": "7b24a8b526f90b9df0e2d3d9c0e0402b8757bba8c615da546a617fff0815b959", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Chris Garty", "tags": ["dataverse", "mcp", "data_lookup", "power_platform", "crm"]}
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
