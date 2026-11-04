---
name: "rar-cat-agent-skills-lookup-dataverse-table"
description: "Search any Microsoft Dataverse table, browse matching records, and drill into full record details \u2014 sourced live via the Dataverse MCP Server."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lookup_dataverse_table", "rar_sha256": "8b0277b43675440ff607ba85c746d410d864d62ddc5682363f111737c00be4c4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Chris Garty", "tags": ["dataverse", "mcp", "data_lookup", "power_platform", "crm"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lookup_dataverse_table_agent.py` and embedded as the fenced Python below (sha256 8b0277b43675440f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lookup_dataverse_table_agent.py` first:

```bash
python3 lookup_dataverse_table_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lookup_dataverse_table_agent.py   # or on stdin
python3 lookup_dataverse_table_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/lookup_dataverse_table_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/lookup_dataverse_table_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/lookup_dataverse_table/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
