---
name: "rar-cat-agent-skills-business-os"
description: "A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/business_os", "rar_sha256": "50b4ed46678a131759dff285b8e288b0d0ecaf9cda86969b1d25453f21926a58", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Matthew James Davis", "tags": ["business", "decision_making", "problem_solving", "project_planning", "process_improvement", "governance", "skill_generation"]}
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
