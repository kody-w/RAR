---
name: "rar-cat-agent-skills-microsoft-ai-platform-advisor"
description: "Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/microsoft_ai_platform_advisor", "rar_sha256": "2a51178d9d3362113c7b11eecdb5b13b9ef1fc5e30fd699dea41b19f12f3f82f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["advisor", "discovery", "architecture", "decision_making", "requirements", "risk_assessment", "microsoft_365_copilot", "foundry"]}
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
