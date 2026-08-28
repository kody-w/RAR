---
name: "rar-cat-agent-skills-clt-hr-assistant"
description: "Assistente de legisla\u00e7\u00e3o trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde d\u00favidas sobre f\u00e9rias, 13\u00ba sal\u00e1rio, aviso pr\u00e9vio, jornada e tipos de rescis\u00e3o, e calcula verbas rescis\u00f3rias com mem\u00f3ria de c\u00e1lculo completa usando as tabelas oficiais vigentes de 2026 (sal\u00e1rio m\u00ednimo, INSS e IRRF, incluindo a Lei 15.270/2025)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clt_hr_assistant", "rar_sha256": "c3a3b868ca1ca03b82006c23c3c8829fb083d1e64b9dbaa6d054300752a39688", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Michael Ferro Pereira", "tags": ["rh", "folha", "clt", "brasil", "trabalhista", "rescisao", "inss", "irrf"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/clt_hr_assistant`. The original RAPP
agent is preserved byte-for-byte in `clt_hr_assistant_agent.py` and in the RCI capsule.

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

Assistente CLT para RH — Assistente de legislação trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde dúvidas sobre férias, 13º salário, aviso prévio, jornada e tipos de rescisão, e calcula verbas rescisórias com memória de cálculo completa usando as tabelas oficiais vigentes de 2026 (salário mínimo, INSS e IRRF, incluindo a Lei 15.270/2025).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clt-hr-assistant
  Upstream author: Michael Ferro Pereira
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clt_hr_assistant_agent.py` and embedded as the fenced Python below (sha256 c3a3b868ca1ca03b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clt_hr_assistant_agent.py` first:

```bash
python3 clt_hr_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clt_hr_assistant_agent.py   # or on stdin
python3 clt_hr_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assistente CLT para RH — Assistente de legislação trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde dúvidas sobre férias, 13º salário, aviso prévio, jornada e tipos de rescisão, e calcula verbas rescisórias com memória de cálculo completa usando as tabelas oficiais vigentes de 2026 (salário mínimo, INSS e IRRF, incluindo a Lei 15.270/2025).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clt-hr-assistant
  Upstream author: Michael Ferro Pereira
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/clt_hr_assistant',
    "version": '1.1.0',
    "display_name": 'Assistente CLT para RH',
    "description": 'Assistente de legislação trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde dúvidas sobre férias, 13º salário, aviso prévio, jornada e tipos de rescisão, e calcula verbas rescisórias com memória de cálculo completa usando as tabelas oficiais vigentes de 2026 (salário mínimo, INSS e IRRF, incluindo a Lei 15.270/2025).',
    "author": 'Michael Ferro Pereira',
    "tags": ['rh', 'folha', 'clt', 'brasil', 'trabalhista', 'rescisao', 'inss', 'irrf'],
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
        "upstream_slug": 'clt-hr-assistant',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#clt-hr-assistant',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b57e7dd7cdb6e7f3',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork', 'Scout'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class CltHrAssistant(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CltHrAssistant'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(CltHrAssistant().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
