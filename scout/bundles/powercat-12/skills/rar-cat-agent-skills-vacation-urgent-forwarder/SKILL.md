---
name: "rar-cat-agent-skills-vacation-urgent-forwarder"
description: "A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vacation_urgent_forwarder", "rar_sha256": "c4a04ec663c7617f56de6dfe01f5dff6d5ee25a69d631c6e6d25f66d513f1024", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "email", "teams", "out_of_office"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/vacation_urgent_forwarder`. The original RAPP
agent is preserved byte-for-byte in `vacation_urgent_forwarder_agent.py` and in the RCI capsule.

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

Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vacation_urgent_forwarder_agent.py` and embedded as the fenced Python below (sha256 c4a04ec663c7617f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vacation_urgent_forwarder_agent.py` first:

```bash
python3 vacation_urgent_forwarder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vacation_urgent_forwarder_agent.py   # or on stdin
python3 vacation_urgent_forwarder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/vacation_urgent_forwarder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vacation_urgent_forwarder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/vacation_urgent_forwarder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/vacation_urgent_forwarder',
    "version": '3.0.2',
    "display_name": 'Vacation Urgent Forwarder',
    "description": 'A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.',
    "author": 'Giorgio Ughini',
    "tags": ['automation', 'email', 'teams', 'out_of_office'],
    "category": 'productivity',
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
        "upstream_slug": 'vacation-urgent-forwarder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e2fd9f42fce2d9e9',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.636, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VacationUrgentForwarder(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VacationUrgentForwarder'
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
    print(VacationUrgentForwarder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
