---
name: "rar-cat-agent-skills-enterprise-agent-design-authority"
description: "An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/enterprise_agent_design_authority", "rar_sha256": "4b5321c8bc9c9f1b4b5796650d54bc2e0d8503f8d957409875fc1ee01ce01a1b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["assessment", "review", "architecture", "enterprise", "design_review", "copilot_studio"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `enterprise_agent_design_authority_agent.py` and embedded as the fenced Python below (sha256 4b5321c8bc9c9f1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `enterprise_agent_design_authority_agent.py` first:

```bash
python3 enterprise_agent_design_authority_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 enterprise_agent_design_authority_agent.py   # or on stdin
python3 enterprise_agent_design_authority_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/enterprise_agent_design_authority_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/enterprise_agent_design_authority_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/enterprise_agent_design_authority/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
