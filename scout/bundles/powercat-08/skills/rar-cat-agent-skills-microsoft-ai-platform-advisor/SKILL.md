---
name: "rar-cat-agent-skills-microsoft-ai-platform-advisor"
description: "Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/microsoft_ai_platform_advisor", "rar_sha256": "8bbf35ee4a97ee4ed92876adbbfd13d2b7624c98a137dc949f1f46080a0637d4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Rafsan Huseynov", "tags": ["advisor", "discovery", "architecture", "decision_making", "requirements", "risk_assessment", "microsoft_365_copilot", "foundry"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `microsoft_ai_platform_advisor_agent.py` and embedded as the fenced Python below (sha256 8bbf35ee4a97ee4e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `microsoft_ai_platform_advisor_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
