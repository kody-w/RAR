---
name: "rar-cat-agent-skills-clt-hr-assistant"
description: "Assistente de legisla\u00e7\u00e3o trabalhista brasileira (CLT) para equipes de RH e Departamento Pessoal. Responde d\u00favidas sobre f\u00e9rias, 13\u00ba sal\u00e1rio, aviso pr\u00e9vio, jornada e tipos de rescis\u00e3o, e calcula verbas rescis\u00f3rias com mem\u00f3ria de c\u00e1lculo completa usando as tabelas oficiais vigentes de 2026 (sal\u00e1rio m\u00ednimo, INSS e IRRF, incluindo a Lei 15.270/2025)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clt_hr_assistant", "rar_sha256": "f009d97229e7ac098108d20b4188d705620dfaebc5f359b00ec2bd747bbe2eea", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["rh", "folha", "clt", "brasil", "trabalhista", "rescisao", "inss", "irrf"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/+16WZOj2JLmX6HjPlRWKzOQQCzKa9dsECCQhBBiEYLKsiz2fV8EVNd/74NCGVlVXdU9YzYP8zCKMEmAH3c/vn4O+vXF6tqwqF8+v5wiJ7S8FNp5dV1Akld7UW29fHxxvcapo7KNihxQUU0TNa2Xtx7kelDqBVGTWl+65dIjHu9oAbW1ZVtpCMgsyK6tJkpnTtAHWlB/hEoLfPWqLiq9ZuYg85AHMR443VoZYDtLbprCSl8h2WvKIgc07szZt/rItRqoKezag/yHsE0dWc1HaIXOR7YFNVb6OL+qo+IjBBY0BVTWb6T9fCou6txygQJQG5XFQ4EabC9qnrp/BFccK3W61IJ6r7aBvO/XfXQWBzlFBmVe9n5mZuK8iZ0XFjNBmXpg811j5W4BgTWtZXsp+Cz8yImsqIH6KJht+NAAWSI49OH3ukMP7p6bRxlQaS8qCtBrL8u7j1CUO2kXPdhCghdBK+wVIZYw4IH9+Aq85Q3WLL15+fzTzx9fIvD95fOvLw4QDk690GnL128utPIWkKdWHoDz5QiCIAfHpVf7RZ2BU67nQ8+jD42X+h+hf//35G7VQfPj5y859Hx9eZn/5C6H2hAYtbBAbLjAhKVlR2nUjq8Qld6tcTZj29V5A7Ru2jrKg9e3ld85FSX0r/nahzchr4HXfvjyUgAVrDn0vrz8CBU1kFd38/fXmUv54cfXtLh79Ycfv/NpOjv2nHZmBrR+/fo8frIFhN9JIx/6qkgs/ZRVew6ISsD8d/ubX2+qP9k9TfL1jfhDUX6E/przvJ9/AX3f0scGfP+aLbABWPnyGhdR/uEpoy56L7dyx/vw49+xdULPSVLgx/8tvj+9MQ49ywXWeprkx48P9/0MLZ57e+f592JLEDD/JzsB5N/EvRvq73g/PPsn1mmUgyT55su/ZPdXCxb/gn762739dws+gsrywnhpBLLfslPvM/TrI0R++sH9fvKHn38DrP9HNkrR1c6Dw9fMyiPfa9qvX3/6oXmc/uHnn37oShDFnpV97er0r3j+lV0fcv5gwSfVhz+uBfK1PMmLew695xD0a1H+W/3bK3S10sj9fr75DP0+E+fXApo38U3omwl+l40N0PV3dvzx5TdQa3Kwm855XAb14x//gEBHqYum8FtIcYquhYCD2yjzZuVV0B4g8D9XjdoDdm0iYNgnHYj/2cOzxoUP/fK/HKv9ZM318lOTRGnawE7afg3rr9a3QvbLK6QCRkUdBVFupZBMSdKX/LFkFlKCGu7VPShM9th6n0D+fpq/gFoK/fJnVl8fq17L8RcIFO+ZZFZRpvdzUWu61Hud1ddDL38q61g55A2e0wGGaQGaB+SDhge6EhBapD0oivNWH4pDbgTKRlvU44M3MMfnmdkvv/wCGk34JX+rwij01m8bGBC8qwN9+gS24adRELZfcs8JC+iHX3/7AfoP6L9b9WA+y5DABp/GBhoelLMIgeTp5o4L/AA8ByrDw9i//vY0JmCTe/XcBSM/8t4Wg+BLPPebZRWe+oRgOGR7wKLAmllZ1C0o7VDUvkJ7H3rXFwidL83FPyyaFvS80gN9PXdGwNUC23m3ZF60oIm3UeOPH0H79B5SfwEg4qFiBrLYan+BTrQEWk2RgrdZzQcRWFzkETD/u9/fzgMm9Q8NtP3G4hUS53B74JAyBOjkTYZvvfkFtJhvy9u5xebe/Us+d1FvNtUj9t/MA4iAZZynSz/NPp8bP0h0t/km+0FjzQ1RfTTG+kvePOPaqmdXOKDOA6FBB5ANqPb/fIZUExZd6j7sBzSdOT294D698ojB3yExgKzegBVAU186ZLlaQ/8fp/0/jNMe7uM4meUolWUgVlRl4y2snCKfnQa9oXIAoCCQW28l5Duo+lY4v/WPL3kaAQfW4z/fKB/B+KR5q8ldDWJHpuQHf5AJIKxmvo9EnROvrucUt77k3xoV8Ar0qMogVkFVA1k/J9s3gfPVb5qGoHTNx99ByyOwa3eucSAZobKzU5Aovue5tuUkQKt6LjbPOAVZ682F5x6C8eMPu4IAd5Ac4eyOHKgKPu75w3RiAbYJ6oxfAxe/k0dzDAAt3M4B2oZgfnmFdFAv5pxpQJECSHGmAVb44cEKBAewMVDx3cJNaJVvyhR18k1B65nG6e8d8Lz2PcEfqszaA6YgcFtgyvvcYFxveHPsu5pPVwFds7kkPRb90dvPrUK/b6j//JI/VHzvaSD60xmL/M42EKgwWfNoLXOhbkCxzbxn/IBAeMCO1zfk8AZN3nX5DNGUClFvVf3RYqEP2bfm/ejz2h+d8hkK27ZsPsPwO9lrELVhZ79GBfxf+vU/QJf9FNaf3rvsH1i+7f4z9JcD6B8onxH5GVq+rl6X8yUhcrw55J6vz1CXv9fKD7/7/nTYwyGe+xHU9bkJgHiZg7MJPfcBqWTvu0eBVkUGCv5s6BEAh/f++o0ENNmg9oKZ+K3fNnObvgNk8OANbP4lf/f6MyXABvNgBgeg4H1P1QfQaJuni977ILiUt0C2O+POwJunu3TebuO9fM67NP34koNS/FdT3Vy8QSACa83DH8gJgNvayHscvWO4+eCPs/0jW0Cau8XnOWk+QjPe/gi9Q+eP0Ldh5jFp5h2YE3+aYfssEpCCj3fa9xsHtvcCBtF2LGdN32a/GS0+UfzfK2GVZTr+l8rXFrPoP3ED7Oq5VYEiNyv0fYffBRdv0n57KNq+jbi/vnxL1qeVnqATkIOs+NTMvRgGcQYEguM3H4Nr/zMcfS4A5QTAI7DCXy437oZAkI1HWM5yQ66WpIss7fWKJF1iieHI0vUtz3YwH8U2NugoDmK7xJqwbQ/xvPkmzFtofJ0RRjQrMVcosPdPILq875fBKfep/Zu2s2ne0e+8y+cmfn2x8TWg5NfNnnp70fBiZaE6EY8HfbFaSVoTkclBFVKi4RLKvyFEHuMmaVImad3PQ9LwLFsmil4PoXqolGO7qwcPo/mRanaewB/lajOlTt+KZKQS+VXcRdUlQSaEEbZCw4RlHFl3HEyjpH92iOutiOC+JtAF558ZEjsP511cYVdNXVZpWx1DDdfuO7iUm6BOZUNNrOuxPjjmrUQcOu/aZKkW6WHh2UaZpv1xuaRanNzBfaSGbsSudK5ka2PauUjWXJeDKJu0cDDpYXmS9yPqbvEAv1vioMgq6y1dgV0qQWpX4nDen7HyKKyXWuWum+2R2bq4uKctZdSixpTUdvAjV20aSSBl9FwgU2sie2IkPEaTFCNNtIV+IbGGF6atpWKkL+Vr/KZE9k5rFLOJBJHOwmhF1helH/zroWR5Gm0GtfPskQ/ORYPKi/6uhL7ghERlc0OShwtZjg+HdJsTKr5zo5y8OUh2S4C7drtNPsh8667lNNyxhoFsuyOy0ZbDsqx3+2Z1syTQ2sngvjPZfBGZnZNjyAn14GF32DcxnE/srb7FRzrNlOmsrrKiSAZj8sM+41BOi3zSCGHxGNrsitU3Y5ujSSnj2tqWyRhDEjw5hUWlNQNbmhHsJ/p1Z9mCsT9546RJ47EfGcQpb527Efd7Rjj39WotkEaDxxZFMZJqXdf6Xbuwhhxw7ggbTmKno2FHXM2q9xOGpWlxXbJVb4pFH9Kpyup6nWpDfLybSi3enOrmjud+uJGmzklYPdAlr4crspgqZoFRu0kiBcUY42mkVLyHs353l7fEWhW36qkivdr1sJ1A4Squ99PKJchbfPUGtsjwZWzJPAzXa5SMPGN09iizX1ICwAq7KxeeeJbZLU/tRSodXCbM4OBoFXnNQwfkUYQyLRNzxkg7GibfCW7YwrBTibFl3EQssQ6D48BchLYKM20IAYaDXhalntji1H3vVmJ7yIWJNEh0I92I6XgZh+xAofEUDzItJLZ9cZRLscWOhXpU1trFuGg2SpzWWYazSldLga0a9wVcsJwJXyJ1uCDXtGTtu9HsDN2p7jLcrPVzy6oaikRHSfA2JohRP2K51MCijb+TqisWLlyxFyI8uC9ybHHtaIQOStFoVAK76OpESvm0hPlM6jDyfF9NPYZX/SSuFm7Pw5NeTxjWo1i/1p3VjtOTPtsJO1aN6TVyof3YoUelM6c6PBAhh1yTzO3po5BXB7nwTmZzI/ySuUx0EO9rpWAuQXQNyIQ1zF3QOezRp1guOw2NmTBEVu+W24t+WJ4s5jbu+HAbXrSuPlhxi+meQlJ339mIwKZKptlJHAXTyacWRLfDztpmediax+F2Mm83Sb7oWaSzXbnJNKCq5grXnmDNbSNGF3sj76x1Q+Khky1Gm4Y3bNEw28FkNnZiWnc/Hfjlja6YY1+468uaGi/l+nTtVY4b4Wm9v1D1tkWPjWhhzuhiZYKV5TW5HxfXxMhUS1Jp2FvfmaqhxkS0jJi/9LZ+5a7RxmGxJrWlxd3A6yCOPY2wOxRngqigvEurt+MGr7dVnOtMflhnzh3f2ME6pDNTS8/IWdyI1dG0TUVKp8Bjt23JUcu9QqwNHN3Lwh33lM1Zl/a7NR4YNS8nJ4BboojnYLwGHXjZrfCTtRRGZtRIoJorOCuFcdJzhMAhC2/3XToWso1pQ0ghXHO8YEvW9+XtyKukGPd8lu+XNxnzF3bECDtOQC/kSQ9IMyMHDrvIVKDlqbjUtqpVGhXfuziGxIWMZ5eavhQ8jhCsT4uNyStnMm3Ei5ttTl113NbN0T5mpxrzj4phhR6hx747xMYiu1IFYdYH7ozRtzFDT8JVryOZUiLLAKG9knnnfkVZlUDN+lSxujORV8HZZDEfGIhO02w1NqMAYmmIt+cTKjWasu9Q2PAFU4QlkrUyxdkEWOZfyVVsSwfO1pXr4JNcIYOqKCpwCS/7PbzaHypv6p2iPPWTV1cZt+uFveGKCTrC2H7D7vAU2y/2TFzE8In39XId2ThOON1JCs6hIJErs+VAyWb3Iqpfs8uqXHPcpPdnXgsPyymoWuXEUsUhH00Y9hJhMdzZMRVx1W6pdcmKhrEw8FE+LRhhjJMBprk4vXugdRQsutOvGHaBResGIvCkgLG7JYMNdhQOsWJ56FgMQtr6Dr2OTwRy3+mX0E/LdMXdt9TYOLzCigXS7dO4HE6dl6rZnsbCwNie67YpNZV3KoLgda9qWHbaLGytQBBiM60zy7zB+prboA5/rXNz8Peby4aXlqdQuvRclp3K7IR12hUfvO2CR5l+PVSghKTnC2fzu5VFYceKHYy2GZHj+W6ejr1neLKduVF23JRb+Shk+bS5TQtp7cmq5OOcJ0zERHWLijsqNENeGo0fbm64uF60DV5eKXLYta3NsxolmwCA4eGVM5nQRPDVWBwxXA+1wljQhMoVMR95JwUWXdYq9tOKkbN7ainEKi1Y+FBZ991ZHpmjmKZrTyQWfZPe84pJbrKcMM7JXN/5IRdoPGJAyx23p0EdJle76Midc4TKdDWXONj7OL01FT3FdcJSdTsxtpsbkZA4aKtlhs3KWufvBX3DHVQLCXnuLN0KdtHyDi/dcFgLPGdPZ3sGy9o7ta12N083jqSibdaNWlSXhTwG/aBMDCvvd0zfoEeRXzMRI5+TXuLc5pgwxdUQnMtpsrfcXsaMVJmCg6e6FW1u7ouVsSgWXMhc6KvZLwgBbw6gH6nyQEiyu5UV4BZz32LDfUXTvjHKXneS8SnV3a6T2JxaHNiFSJ/3F6II47rir/ywGInF8hJ1jnH1Ioe1LAWAJjnYCHimMwOLJIxCnPl+wuPD/b6WShqNcK2/F8pyxnLtUrftvFiHgtkmF5xPkSONa06gWLAiRAJIP/VMDqVeHM9nguGzdns9Bj3j0yhyVip0vKN3WqZNt8t1Gtg+20dFI5K3HXdlkYMldGS5Xh6tbQ3wRRkR+70h37nu7kQXuGV5/nKRPAcXzFOUs1lXwIImnUijkGw+YAzpcDsn+uSwt2a7Z4+2fVgWVkYlZs2vAcgclCJMEqdOFkW+089Uc5iieLGS1kl8rLiiNU5HWUVtxXCU4K6s2Au6c0khubla1ziYqU4iiI7Ax/c8wMZsWytr9uxsUhTjkE7nusigO8vZdCjmD8RO1pOj7yrUdqsZYtQj60LX3Qg2sIrSg06XRPjCU2fplJ7vi6DSDXVVbFWiMyytoxN51V8XkULS7Zg1OoxLnUZxhmE5CmbeNm0GcLWsuAdpp6MI6zOhXWK8eAhRLNnf1rR8BePz5RKKV2d/7CrurthDbnkLN/BoN9HzCNsqon2vMH1987GYSRfpKsooahgn8ZJYbMxeTif+xrAXcRrL+66PBEYspytdHqoUs5FJ964I7DWCWS6R/eZ0OfbSQgmogTVVp5SWzsb1SDFYZWsZxUkrsleqndwF1KaQ0fVu9PLWTmlIxQef1Jbxcan1tbpBzyx95OqAPNwUn1udrbQiOVqIt0S3PMpBEEi+dlnZTMmUjnMdz6l2x85mJuBrxBGUQ+EjyKFHvb0ybmxl164u9bVI7HaFoYuyTbubbfpq3Uw6sTqbiBDfbo5nDiaYQwJ9j08+i1PyxSEMldwV7l0xKOGIO3t17ZZ9lB8RsTQbk0Mc9RxcTFb1t/CiZ/l1UhFqNl53VScFy+LYD6vgBHDXXT8Fi8LZltRm38EIcqJReuLQraDtusbsJgFkejIe1oYYIvsC3w19a2xrRBJvgziVQurS240KK81tHw/EcJN4D7sVZw5JrI7VDw5F+pRIeVv+3kScEMfwwK5iR7YX8mmvh/JyccJFla2P2hS2673CcwxOjTTvHu/q9kTLMFaIoYWVXnfIVF52bFllCrQ3cGbVB5RLi+srjQr4BrtMCXdOhVOv7NJdw8Illq1d0NqDdaye79VFovgaLr2gW6yjijYGPSF69rwnCQsvWcYR+TtmcRV8MdhzPC6SBY52OnYp76fDajlpN+ZWr7XW2CCC5tc4IWv+qoc7DmFHTtFAU22o1S5hBmyxu49Em0sxhxiRzaWEbSwGNqYObXjNzW5VE4tbWae8252K3S3F+0Zeok299FuyBihioCifOE7mmtXg3eTYyT4U4l3chgdXYGpZGwDwt/xMGRRHT7Qt6G93WFjelLCLLgesu9XsZkU2vByfwEASXNacyVZbUeJWDcf0obEU80iTbORyO0uXa8qag1z5XnTr8UxisMUmup8usLc9GnJWBdlyqrrNyajAhEbeM1zc6ue4MPbHHS8jGXrdhrDZHK5X3RcS/r4eF0yyjvFzjU3OeYTXdiucZB1NbHdasQGIlaOhlu1Wl8mQMCkZGI5E8puXL4aTS55XK8I+2Hrr9cukoXmWE7HlNi+YCLW3cX1cM/ySJM/h6Xa32hbz9LO9OxC22JoXOwtOCHIH0A64dZmVODquYtW+gEK3kzOOSxyKYb1brdH9bbE+kPeKivamsprEktgG8kVKDL+ES3dHCdwFI5hRPdZVekZVjWZXHXqP0IiyuI1k8MyQe1lrbaRDry+xJjd6/1wpgyCDco/6vFtd4TNl97XDG7FbXFuS1cA21iW8WG5RtiJEFxQR2yZ5CWb142I6LjBzEbHbCXfM48jn2TkMWQrDMkuyK2u6wj6hoVVuyAVu1rFxkrTz7dDHZ0m7ocVFHQ2h3VG0vtwSTH0qNtOJX0nJPOvurOyYeMtSy9uwv7ZDtWT3AAaV+k3zxzFewHm0FSf64h00vz2S4Y7LfHmB0I2QnPKtSi8o8VR40jlfXgyrM/cHFIyNIQ/rVdbJmiOR+4DBnEWNMNFlseJWYCRWa9Mx0YzYLuNQc7PUNSYBtiw4srEB2bRUG5w9cp1cSI2KyzG0kG6tLXBaRQ1v6M63YwzvkzwFQ+gNFSU+Ue1rd72FTcW0hCV14wQPYjCx55t/Ds/4fdrSOufvEKLNbE7DHDTxS29pVGjlorjqHS2E2nh5mFrSmo7jk16crb16coi0AV6cjN2mPmnjYu/xx7UExlVhq6NYffDTa1jF2wI5ayHMbUZUvYEu6h6J1Th4mz05Xdhly6yScCEe3d3maO57pFFl17XSVPZou2eY7KiOoNeUcrsvNj7iefoioD2VIbPxVNF6N4XgGqKdrdVigxRK5K+vESl1qMtqxgQL+krPfdI5HRJ1FTHKGdOYs7drLofO3LlZ057rEFYA1FxEdJpjG3nrhi22HRF9s0fEFeKM+eoiC9fM3NU4Xfdop+l3I9ts0gsX43CNqaVCpAslXhLNfhgIvQhWN9M8CGw5hIVmA29XhQITEoCS8PGKVbHVNkXMMMtSxwf81PNpad2WxBoTyPNJ7Mftvg4pw0ruCX+79kcDEbvbdA/rCxYv6dNxW91SITjKhiEyh4qOSSzpzF5RMakRg73cMSbRRRnKTXLONGGcuFums9OG8IJlrtZih3TL3YY9JwWas9phI/vbqpBqhlYXXUEM3oLeYb1N0shN9ye9u2/hQWMFR2uS2D1KZSz0OLZgd4ZMyT4lyDmxm8Z9tia3KrPBlme0RWldqahFO+iIDmPnLYGuW3ZY9fkoSUg65oizwgOE5LcbqR1bhLFQp88Q0dv7WMhU9w0PiyzBOTCC70K4q0qEb12+qFSTXqKrvNv65S2oQ2mNVYlyuTAaMVeve9ZRoJ1WZRecTrnu8v0dP1pddHNavYlZx45uZJ8ckcgC0LYGg9YgSwkVZZsrVhMh03Mhj/Y4g6g2bTtwv4kWSLjWQLb3Usx0+XBrUz5aV5tlgCNnqUW1vu9LAeP2io1GXWhngrVz6RUoWaWdwlMn1cRmvZMkreDrTgCDvL2OJqtcbvLTeb2Cy8kvUGYt3e+FZtVJfwPN3YNJhhWvm6RoVhRF/evl48v8lOL5rOFvfy8x34X+v3bD++2+9bcHio+nDJ7lfn7I+vz3Kvz88aV2IqDA2137Ju2C5+3wP9+z//TnJ1Iz+fj2G4P5webQfnvG0lpB81AgnA1RpOF8Ox6sBu9vD83n5xHfn6TP9/4fT6Kt4uXxm5hm/qhrf1bu+fwK6IS8rl6Rl9/+EyK+8n5/KQAA -->
