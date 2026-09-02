---
name: "rar-cat-agent-skills-clt-hr-assistant"
description: "Assistente de legisla\u00e7\u00e3o trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde d\u00favidas sobre f\u00e9rias, 13\u00ba sal\u00e1rio, aviso pr\u00e9vio, jornada e tipos de rescis\u00e3o, e calcula verbas rescis\u00f3rias com mem\u00f3ria de c\u00e1lculo completa usando as tabelas oficiais vigentes de 2026 (sal\u00e1rio m\u00ednimo, INSS e IRRF, incluindo a Lei 15.270/2025)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clt_hr_assistant", "rar_sha256": "c3a3b868ca1ca03b82006c23c3c8829fb083d1e64b9dbaa6d054300752a39688", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "clt_hr_assistant_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/clt-hr-assistant:f178700f04c19a065da13afab46336c39f1c1943405f1e3101a89bc15eaa8082", "kind": "skill"}, "version": "1.1.0", "author": "Michael Ferro Pereira", "tags": ["rh", "folha", "clt", "brasil", "trabalhista", "rescisao", "inss", "irrf"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/clt_hr_assistant`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `clt_hr_assistant_agent.py` is
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
