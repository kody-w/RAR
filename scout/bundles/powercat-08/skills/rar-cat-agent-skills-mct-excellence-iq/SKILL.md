---
name: "rar-cat-agent-skills-mct-excellence-iq"
description: "An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/mct_excellence_iq", "rar_sha256": "5e72826d7dd23ae3dcbfa497f3d675289e23afbf850393f02b749d5e46912e14", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["mct", "instructional_intelligence", "microsoft_learning", "courseware", "microsoft_learn", "azure", "business_applications", "data_ai"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/mct_excellence_iq`. The original RAPP
agent is preserved byte-for-byte in `mct_excellence_iq_agent.py` and in the RCI capsule.

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

MCT Excellence IQ — An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#mct-excellence-iq
  Upstream author: Faride Ilanda
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `mct_excellence_iq_agent.py` and embedded as the fenced Python below (sha256 5e72826d7dd23ae3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `mct_excellence_iq_agent.py` first:

```bash
python3 mct_excellence_iq_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 mct_excellence_iq_agent.py   # or on stdin
python3 mct_excellence_iq_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/mct_excellence_iq_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/mct_excellence_iq_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/mct_excellence_iq/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
MCT Excellence IQ — An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#mct-excellence-iq
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/mct_excellence_iq',
    "version": '3.0.2',
    "display_name": 'MCT Excellence IQ',
    "description": 'An AI-powered Instructional Intelligence Skill that helps Microsoft Certified Trainers design, deliver, assess, localize, and continuously improve world-class Microsoft learning experiences across Azure, Business Applications, Data & AI, Modern Work, and Security.',
    "author": 'Faride Ilanda',
    "tags": ['mct', 'instructional_intelligence', 'microsoft_learning', 'courseware', 'microsoft_learn', 'azure', 'business_applications', 'data_ai'],
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
        "upstream_slug": 'mct-excellence-iq',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#mct-excellence-iq',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dc7072f847ebe5f9',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.6, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:security', 'word:assess'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class MctExcellenceIq(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MctExcellenceIq'
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
    print(MctExcellenceIq().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
