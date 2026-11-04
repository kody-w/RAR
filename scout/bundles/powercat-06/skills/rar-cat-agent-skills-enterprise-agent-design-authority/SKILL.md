---
name: "rar-cat-agent-skills-enterprise-agent-design-authority"
description: "An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/enterprise_agent_design_authority", "rar_sha256": "4b5321c8bc9c9f1b4b5796650d54bc2e0d8503f8d957409875fc1ee01ce01a1b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["assessment", "review", "architecture", "enterprise", "design_review", "copilot_studio"]}
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
