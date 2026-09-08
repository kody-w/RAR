---
name: "rar-cat-agent-skills-clt-hr-assistant"
description: "Assistente de legisla\u00e7\u00e3o trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde d\u00favidas sobre f\u00e9rias, 13\u00ba sal\u00e1rio, aviso pr\u00e9vio, jornada e tipos de rescis\u00e3o, e calcula verbas rescis\u00f3rias com mem\u00f3ria de c\u00e1lculo completa usando as tabelas oficiais vigentes de 2026 (sal\u00e1rio m\u00ednimo, INSS e IRRF, incluindo a Lei 15.270/2025)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clt_hr_assistant", "rar_sha256": "f5b73a62818607a07ab31b5e8dc4218a277a3e7c1d97f5847706efa80d1bd0aa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["rh", "folha", "clt", "brasil", "trabalhista", "rescisao", "inss", "irrf"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clt_hr_assistant_agent.py` and embedded as the fenced Python below (sha256 f5b73a62818607a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clt_hr_assistant_agent.py` first:

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
