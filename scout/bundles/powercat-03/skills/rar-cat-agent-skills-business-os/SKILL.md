---
name: "rar-cat-agent-skills-business-os"
description: "A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/business_os", "rar_sha256": "50b4ed46678a131759dff285b8e288b0d0ecaf9cda86969b1d25453f21926a58", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Matthew James Davis", "tags": ["business", "decision_making", "problem_solving", "project_planning", "process_improvement", "governance", "skill_generation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/business_os`. The original RAPP
agent is preserved byte-for-byte in `business_os_agent.py` and in the RCI capsule.

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

Business OS — A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#business-os
  Upstream author: Matthew James Davis
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `business_os_agent.py` and embedded as the fenced Python below (sha256 50b4ed46678a1317…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `business_os_agent.py` first:

```bash
python3 business_os_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 business_os_agent.py   # or on stdin
python3 business_os_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/business_os_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/business_os_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/business_os/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Business OS — A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#business-os
  Upstream author: Matthew James Davis
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/business_os',
    "version": '3.0.2',
    "display_name": 'Business OS',
    "description": 'A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…',
    "author": 'Matthew James Davis',
    "tags": ['business', 'decision_making', 'problem_solving', 'project_planning', 'process_improvement', 'governance', 'skill_generation'],
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
        "upstream_slug": 'business-os',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#business-os',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '0f102cac2f8ea262',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BusinessOs(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BusinessOs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(BusinessOs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
