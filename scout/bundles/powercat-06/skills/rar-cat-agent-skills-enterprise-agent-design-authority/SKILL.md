---
name: "rar-cat-agent-skills-enterprise-agent-design-authority"
description: "An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/enterprise_agent_design_authority", "rar_sha256": "6332036335d5ea258d4f3f653326bece852ce05b4ac1cd5e7f10b442b0f8c49b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["assessment", "review", "architecture", "enterprise", "design_review", "copilot_studio"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/enterprise_agent_design_authority`. The original RAPP
agent is preserved byte-for-byte in `enterprise_agent_design_authority_agent.py` and in the RCI capsule.

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

Enterprise Agent Design Authority (EADA) — An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#enterprise-agent-design-authority
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `enterprise_agent_design_authority_agent.py` and embedded as the fenced Python below (sha256 6332036335d5ea25…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `enterprise_agent_design_authority_agent.py` first:

```bash
python3 enterprise_agent_design_authority_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 enterprise_agent_design_authority_agent.py   # or on stdin
python3 enterprise_agent_design_authority_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enterprise Agent Design Authority (EADA) — An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#enterprise-agent-design-authority
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/enterprise_agent_design_authority',
    "version": '3.0.2',
    "display_name": 'Enterprise Agent Design Authority (EADA)',
    "description": 'An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents.',
    "author": 'Faride Ilanda',
    "tags": ['assessment', 'review', 'architecture', 'enterprise', 'design_review', 'copilot_studio'],
    "category": 'analysis',
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
        "upstream_slug": 'enterprise-agent-design-authority',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#enterprise-agent-design-authority',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b69cc3ecf5e4507e',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.375, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:review', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class EnterpriseAgentDesignAuthority(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EnterpriseAgentDesignAuthority'
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
    print(EnterpriseAgentDesignAuthority().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
