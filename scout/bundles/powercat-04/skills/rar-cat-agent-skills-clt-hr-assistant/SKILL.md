---
name: "rar-cat-agent-skills-clt-hr-assistant"
description: "Assistente de legisla\u00e7\u00e3o trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde d\u00favidas sobre f\u00e9rias, 13\u00ba sal\u00e1rio, aviso pr\u00e9vio, jornada e tipos de rescis\u00e3o, e calcula verbas rescis\u00f3rias com mem\u00f3ria de c\u00e1lculo completa usando as tabelas oficiais vigentes de 2026 (sal\u00e1rio m\u00ednimo, INSS e IRRF, incluindo a Lei 15.270/2025)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clt_hr_assistant", "rar_sha256": "f009d97229e7ac098108d20b4188d705620dfaebc5f359b00ec2bd747bbe2eea", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["rh", "folha", "clt", "brasil", "trabalhista", "rescisao", "inss", "irrf"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clt_hr_assistant_agent.py` and embedded as the fenced Python below (sha256 f009d97229e7ac09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clt_hr_assistant_agent.py` first:

```bash
python3 clt_hr_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clt_hr_assistant_agent.py   # or on stdin
python3 clt_hr_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/clt_hr_assistant_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/clt_hr_assistant_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/clt_hr_assistant/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
    "version": '2.1.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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
    print(CltHrAssistant().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
