---
name: "rar-cat-agent-skills-microsoft-ai-platform-advisor"
description: "Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/microsoft_ai_platform_advisor", "rar_sha256": "2a51178d9d3362113c7b11eecdb5b13b9ef1fc5e30fd699dea41b19f12f3f82f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["advisor", "discovery", "architecture", "decision_making", "requirements", "risk_assessment", "microsoft_365_copilot", "foundry"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/microsoft_ai_platform_advisor`. The original RAPP
agent is preserved byte-for-byte in `microsoft_ai_platform_advisor_agent.py` and in the RCI capsule.

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

Microsoft AI Platform Advisor — Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#microsoft-ai-platform-advisor
  Upstream author: Rafsan Huseynov
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `microsoft_ai_platform_advisor_agent.py` and embedded as the fenced Python below (sha256 2a51178d9d336211…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `microsoft_ai_platform_advisor_agent.py` first:

```bash
python3 microsoft_ai_platform_advisor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 microsoft_ai_platform_advisor_agent.py   # or on stdin
python3 microsoft_ai_platform_advisor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Microsoft AI Platform Advisor — Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#microsoft-ai-platform-advisor
  Upstream author: Rafsan Huseynov
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/microsoft_ai_platform_advisor',
    "version": '3.0.2',
    "display_name": 'Microsoft AI Platform Advisor',
    "description": 'Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance.',
    "author": 'Rafsan Huseynov',
    "tags": ['advisor', 'discovery', 'architecture', 'decision_making', 'requirements', 'risk_assessment', 'microsoft_365_copilot', 'foundry'],
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
        "upstream_slug": 'microsoft-ai-platform-advisor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#microsoft-ai-platform-advisor',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '80671ffc99dbbc48',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.5, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:decision_making'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class MicrosoftAiPlatformAdvisor(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MicrosoftAiPlatformAdvisor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(MicrosoftAiPlatformAdvisor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
