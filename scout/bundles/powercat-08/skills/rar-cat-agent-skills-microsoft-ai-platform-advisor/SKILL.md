---
name: "rar-cat-agent-skills-microsoft-ai-platform-advisor"
description: "Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/microsoft_ai_platform_advisor", "rar_sha256": "7f2dc23f9d0ed9d385011b60976185e5cb7f1869b13f07b4f02e7dec0e229e38", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["advisor", "discovery", "architecture", "decision_making", "requirements", "risk_assessment", "microsoft_365_copilot", "foundry"]}
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
