---
name: "rar-cat-agent-skills-microsoft-ai-platform-advisor"
description: "Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/microsoft_ai_platform_advisor", "rar_sha256": "7f2dc23f9d0ed9d385011b60976185e5cb7f1869b13f07b4f02e7dec0e229e38", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["advisor", "discovery", "architecture", "decision_making", "requirements", "risk_assessment", "microsoft_365_copilot", "foundry"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `microsoft_ai_platform_advisor_agent.py` and embedded as the fenced Python below (sha256 7f2dc23f9d0ed9d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `microsoft_ai_platform_advisor_agent.py` first:

```bash
python3 microsoft_ai_platform_advisor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 microsoft_ai_platform_advisor_agent.py   # or on stdin
python3 microsoft_ai_platform_advisor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/microsoft_ai_platform_advisor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/microsoft_ai_platform_advisor_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/microsoft_ai_platform_advisor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
