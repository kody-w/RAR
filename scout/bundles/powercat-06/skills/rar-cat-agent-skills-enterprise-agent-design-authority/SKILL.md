---
name: "rar-cat-agent-skills-enterprise-agent-design-authority"
description: "An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/enterprise_agent_design_authority", "rar_sha256": "6332036335d5ea258d4f3f653326bece852ce05b4ac1cd5e7f10b442b0f8c49b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["assessment", "review", "architecture", "enterprise", "design_review", "copilot_studio"]}
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
