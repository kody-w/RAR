---
name: "rar-cat-agent-skills-clt-hr-assistant"
description: "Assistente de legisla\u00e7\u00e3o trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde d\u00favidas sobre f\u00e9rias, 13\u00ba sal\u00e1rio, aviso pr\u00e9vio, jornada e tipos de rescis\u00e3o, e calcula verbas rescis\u00f3rias com mem\u00f3ria de c\u00e1lculo completa usando as tabelas oficiais vigentes de 2026 (sal\u00e1rio m\u00ednimo, INSS e IRRF, incluindo a Lei 15.270/2025)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clt_hr_assistant", "rar_sha256": "f5b73a62818607a07ab31b5e8dc4218a277a3e7c1d97f5847706efa80d1bd0aa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["rh", "folha", "clt", "brasil", "trabalhista", "rescisao", "inss", "irrf"]}
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
