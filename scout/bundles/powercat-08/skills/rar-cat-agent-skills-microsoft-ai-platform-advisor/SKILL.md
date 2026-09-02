---
name: "rar-cat-agent-skills-microsoft-ai-platform-advisor"
description: "Guides a customer through a discovery interview, recommends the right Microsoft AI platform (M365 Copilot, Agent Builder, Copilot Studio, Foundry, Foundry Agent Service, Windows AI Foundry, or Agent 365 as the governance layer), scores technical complexity and risk, and plots them on a 2x2 quadrant chart with planning guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/microsoft_ai_platform_advisor", "rar_sha256": "8bbf35ee4a97ee4ed92876adbbfd13d2b7624c98a137dc949f1f46080a0637d4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "microsoft_ai_platform_advisor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/microsoft-ai-platform-advisor:fa30c647a442b6334fb843c4226a3b59f1a7332132de5563b5ffba79faf64c04", "kind": "skill"}, "version": "2.0.0", "author": "Rafsan Huseynov", "tags": ["advisor", "discovery", "architecture", "decision_making", "requirements", "risk_assessment", "microsoft_365_copilot", "foundry"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/microsoft_ai_platform_advisor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `microsoft_ai_platform_advisor_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
