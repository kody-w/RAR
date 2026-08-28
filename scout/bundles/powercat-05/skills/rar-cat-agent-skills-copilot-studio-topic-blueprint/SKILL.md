---
name: "rar-cat-agent-skills-copilot-studio-topic-blueprint"
description: "Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_topic_blueprint", "rar_sha256": "c11337248088a38d1cbbbba408808e2a111734b20ccebd659534832ff67882f2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Elliot Margot", "tags": ["agent", "blueprint", "topics", "design", "power_platform", "orchestration", "adaptive_card"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_topic_blueprint`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_topic_blueprint_agent.py` and in the RCI capsule.

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

Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_topic_blueprint_agent.py` and embedded as the fenced Python below (sha256 c11337248088a38d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_topic_blueprint_agent.py` first:

```bash
python3 copilot_studio_topic_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_topic_blueprint_agent.py   # or on stdin
python3 copilot_studio_topic_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_topic_blueprint',
    "version": '2.0.0',
    "display_name": 'Copilot Studio Topic Blueprint',
    "description": 'Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.',
    "author": 'Elliot Margot',
    "tags": ['agent', 'blueprint', 'topics', 'design', 'power_platform', 'orchestration', 'adaptive_card'],
    "category": 'creative',
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
        "upstream_slug": 'copilot-studio-topic-blueprint',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '05163d5246a491ef',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.667, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'tag:design', 'word:blueprint', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotStudioTopicBlueprint(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioTopicBlueprint'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(CopilotStudioTopicBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V667OiWJbvv8Kc/lBZQ+aRN5odHXERRRQVRQSxsiKLx+b9fgp163+/G/WczOyp6umJmG/XzFCBtdd7/dba2/P7i9nUfla+fH5ZxnGQ1cjOLL2sfvn44oDKLoO8DrIUPlWbMkVMJEvBpzhIAdJUALFN+BakdQYfWE0QO59KYDo9sgvsMqsyt0b4LA9iyPRUN04AyTyQ1ogVNyAv4brPSAnsLElA6gDn+bDuc4CYqYNkpe2Dqi7NUYGPSA052dX4mcXwI0qzLgaOBz4irVkGphUDeNdEOhBDjgDhHBNq3gKEN0vnI1IBuymDur9zflOKL4ET1BWSZvV9MXxkIm5QVlALKBnJYzN9hY4ANzPJIf+Xz7/8+vElgN9fPv/+YsdmBW+9PLk9LFRHLedv9sG1kIUHifIeOjmF1zko3axM4C0HuMjz6kMFYvcj8p//GXXQ+dXPn7+kyPP15WX8pzQpUvsAGm9WNXSVbeamFcTQoFeEizuzr6AnaxihCloAfRak3utj5TdOWY78Y3z24SHk1QP1hy8vGVTh7uEvLz9Dl0N5ZTN+fx255B9+fo2zDpQffv7Gp2qsENj1yAxq/fr1ef1kCwm/kQbuXeo/INdHMlngy8t3xo2vh96jnXDly2uYBemHB+O8zFqQmqkNPvz8V2xhithRHFT1v8X3lwdjHyYptOmp+M8f707+FUGfBr3z/GuxY2b8TyyB5G/iYOo+HPVXvO/+/yfWY8VV7x7/U3Z/tgD9B/LLX9r2rxZ8RNwvLwsQwwIqx9L6jPz+9XRY8r/85Hy7+dOvf0DW/y2bU9aU9p3D18RMAxdW1tevv/xU3W//9OsvPzU5zDVgJl+bMv4znn/m17ucHzz4pPrw41oo/5yOWJEi75mO/J7l/1H+8YpoZhw43+5Xn5Hv62V8ochoxJvQhwu+q5kK6vqdH39++QPCQwqtaez7Y1jlf/vbd2h4srOmRmCA6yABo/KqH1QI/D/WdgmgX6sAOvZJB/N/jPCoceYiv/0f26w/3THyUxUFcVxN7AfyfK3u0PP1jpBf38H1t1dEhWyzMvCC1IwRhTscvqQPkIUi8xJUoGwhmFh9DT5BGPo0foFwjvz2rxl/vfN4zfvf7pAZPKBJ4dcjLFVNDF5H03QfpE9DbDNFwA0iMGQfZzbUxQ3ucA1VyGKI0fXohrtRiBPAllBn5QOpoas+j8x+++03y6z8L+kDR0nk0ZmqCSR4Vwf59Aka5caB59dfUmD7GfLT73/8hPxf5F+tujMfZRwgnD8DATXcnOQ9Agurgc0JtogxqhA17oH4/Y+nayGbFJQIDFvgBuCxGCZmBJw3P59E7hNBM4gFoH+hb5M8K2sIzkhQvyJrF3nXFwodH43w7Wew9TggH5tiaveQqwnNefckbFZIBbOvcvuP9yY8Sv3NKs27igmscLP+Ddnxh3unhG+jmnciuDhLA+j+9yx43IdMyp8qZP7G4hXZj6mI5GZp5n5pPmW45iMusEm8Lb83/hR0X9KxKYLRVfe6eLgHEkHP2M+QfhpjjozdHga2epN9pzHHlqbeW1v5Ja2eOW+W4D4eQFV6xGsCZ+wEf3+mVOVnTezc/Qc1HTk9o+A8o3LPwX+aPu7NGXnvzsiXhsBwCvn/dbIZPcStVspyxanLBbLcq4rxiJydpfWo8WM0HJnD9H1U6bfJ4w233uD7SxoHMA3L/u8Pynu8nzQPSGygVhCGlDt/mGwwciPfey2MuV2WYxWZX9K3PjGafQdFmA4QOGBhjfn8JnB8+qapD9FhvP42M9wDUDqj7TDfkbyxYhh8FwDHMu0IajUG9C0FYGGAsbY7P7D9H6xCIHeYf5A/TBBk9CnsJXfX7TNoJixlt8ySb+TBOIlBLZzGhtr6oASviA5LckzLCuIAHKdGGuiFn+6skARAH0MV3z1c+Wb+UCYrozcFTYgIVeCl3/v/+ehbCd01GZWHPE3HrKEnuzGLHXB7xPVdy2ekoKrJWPT3RT8G+2kp8n07+/uX9K7hew+BWBKP+fmda2B+lUl1z7gRCisIZzBnH8bBPLg3/ddH334MBu+6fEZ4TkW4B27eGxzyIXkrt3uXPf8Yk8+IX9d59XkyeSd79YLab6zXIJv8l275t2dX+/Toap/uZffpvWJ/EPDwxWfkhy3RDxTPtPyM4K/YKzY+2gY2GPPu+fqMNOk7Jn347vszbPewAFjA6R1sYdKMGVr5wLmPNQr4FleoTZZAsBjd3cN2/d7H3khgM/NK4I3Ej75Wje2wgx34zht6/kv6HvtnXcA+kXojOFTZd/V6b+gwko9Avfcb+CitoWxnnP08MG6K4tHcCrx8Tps4/viSmgn4bzdDY0eBuQldN26gYJXAQaoOwP0KVvIIiZDwfvnj5lO+fzHjV0Q0R92/0b6502ogYkLAgMhWj1uqj7BgTGfE849j08njYASFUfERhiHLxy5pnNjex7n/KvdeuRBynOzzWMB39vD9fYoepTz2Nfd9YtrAjd0v4wQ/GgtJ4cc77fuO2gIvv/6JGs+B/i+UCEbwGOHmgQPA+RNTIJMSFA1st86oxje7vonLHjL+uKtXP3aiv7+84cUzKs+pE5LDwvxUjQ13AtMcCoTXjwSDz/6n8+hzOYQ3OBHB9TaOkyRLUFNsOjXJqYPbFnyZFLzEpoAwcRxnScoiMNsGlsPQM5qkpiThugw7nRIuAfk9svTr2GiDUSUbYjtD4phruoxNmCZL4i7JOvTUdsEUzAjcJBkMm2LflkawDJ92Puwanfg+Go/+eJr7+4vFUJBSpKo193jxE1QzGYq1bv4FHRhg7MJptNGKhj0ZjVQ7Qu1X6c7hIr/E6/OqW17PJznfxafNYr8og64SKn9Bc+mwOZByAgRtJlunWeQcDXSlyStXTg8tPaSLxY7rmikmpeCUgljQA5tcCSUrUjpe5F0TVMJiMptKMlVEXZLvvMG5WoW6TiXJF7YTDvAi15anwt0k2rKXjax1Vrc+IWbSTuequisrPLyEvsoVQ+uw8elcTI02rrQ5f83StWrd1Do89bgYEUJ/2VzlmEyb7UW9Gu451ypcG+xTcYjlWKMkuCgHfHZbnoMA37pSusxVdX3RKl3DgK7IjsNflEJj9pK05Wf0jjYjYuWH66MmC9G5qHpvvQ1Zlj3o26FnmkvaBZf0Rs/c3I2s0Dy69lTCYqBfdTYV4tYODlJqGd2pFy9yoaWoYPINX3jBZsuu91q5npK35HSwGUHVNjyfUaXEn+QtftPrZEsIaUfc8JWRXDaKZ2X0WdvV4VZdTb01E08LqheC88m8Da6x0Cfn20wotsCRCR+fbbEbWgzS9WYUe+u2PcnTxWDmJM8oTRyV+s7qORW9bpx0KubrGl13GCs2NIVy+bCPLl6449TrLkSPvcXuMg0lBKVRWbwOzFXpoYs+N6qAPmNXgWoaZ7vW813Q6lKFHeAODt9Mb2t2rlVJd9obAId+Y07kvu9MYR31TV7j5Zk+nO1MOh/lMFkqp5XRRVRUXS+8lyzJs466ohKW7SoLKB9dOedJKUP/+jW508MV485P/TXAYZld89NOtCpP53owbX3f7ulK34gcKM5ePRn66ijt/UOwuMyquZCse6oqbXtlk7Mh22+1oCmmg9lZjDs5QQKerYKhotp+mhkF0dQ3jcHClGaX1YCH0m7aTIca3cLcsHWb3e8wpqt6g2wmvbNSrEC55gW9wy5YMgxitjx0hkaJC0ISEzFmh1wXVluUxDbnlR5iSrULsSmdTv0ze+yFzY66pAK/PsMtcBrF0bEVzFrqhVUb2fR6Xrk3N8us1Q07O+WQJMe4xpuwjk5TI8Zrbd4pdZXf/DJZ3GoMRWXZGbbmeaJaLc2rdFAOacrJ6bXwlC5Z5xIpYF61Cep0bgb77FoKV3xf0DpVJhSPhSEmbRhW16mltFIUIOzcjh18USbTKpl1TRlRt4MItmiVCjOd3TgaRYMNic72atCDaC+WNJUQhdCKmk1OKGcLWGErxzkbTojmVk5Jn8upCju2NJzAzjrVCkwXl7trsj3Z9gwiUpRjaCPvV+k6nGbVdO1vlM1ExWaMVO8WjKUZmd2lEXOe8OjKr8uIjkLutl1S51oZXI1eF2RRnoPsuD+Dqp80wyV0CxSLrGts583JoWMKJfh2s4BVaGGHQ28YrTLdnrAgvJylA4hZKr6o2357K/VpUmDH8DrNW0OdRiEhCihFyvnMHtSQiaIEEPN+1pusSyeqtbDt7XVldieS4nFcSsPeFlYzVZljJy9MccZOlAXIr+2g54cZEOlYCrUWvw2zU+BUN0yU1DO1SSbHayxzClYVkXJIyiBBL6pODPGZKLdGSxqrJSDd3LqKYbunB7VQi4OM62KgSQV6NWs8tqilsdHaoyWpBAR5gi3mt+AGWlWhGGeiLmhm2ggqClauyDT7K+m7t97Fp4uiZuceJV1XDJ/jnLssNy4cvbAyTyYiEQ8boeivveQlgFQajQPO+sqd9FIIaH162XnZZl2IKFjvCGLTTLtqGTfLdt2ha42RNOF6bQ+HabPiZL7Z0WLI87LitFTZFR2biJpPSWJ6pU+Rsw4Y/pIAd9kWexSPtou9Xczzy7paGNwSOJdSlXl+XfEANw3faUV5g83CbU/DbViSTfedeDxyBM9cE07WWdN0eH6LtXYsS+1sGQ75nGsNXPO0bONt7OK4mx+mfb69+N6C2fF2KqfWwmhXLJXCutAgcGa1s8q1JhO20XoxzEt1r8clo/RH5WwuXKyYqLdLFvLz0hO6Y3PZ5bZerdWtbtjHpZAqQqUp57xLyKGfAfui3Rh8PfDchRLPHSyvMs0jn1xknaPRc1puwlnITM8EEHdTmUZ7Mr4eNmDfAE8wMblarIT5pe9vFsjI1WzjcJurt7cHK5SkRqOqxWwZVa7hZ2tnblZkidP2Mj5dT6ucx9fnNCAYkvLzatNTDC/jUtly56vnYFpxzIg51qvBjumyfVdvcv52ooWZv7w1BW9HjhIu2HS90qZefPZ5Roj8QJDlK1Oph2VN8WS77pewqq7NPlqIgrA6R5gQbvB431LXq8FRHj5bWougVoWlvtDSbOJnRzUcMHbTpRqlX69rTs3j06lMiPNVXfSqJmLaIZ0wG5TUJGzNSJyfRlms75o64RX3skoWblEftgdCCW/bCPg2PTsI14hU2oPndXYscOkxUorqjFOZ3zX2YuDcnWFwyiqZcpRig8yb09srTN6jHzqDmpb1RsGVE32CA0BhKqjQnVgZp2J9E1+OgmNci0qa7myqCpbVfmrXYmWk8yUn6kE5uzjdLhRj6kyqzNJgZKFRXDCbX+Ggwl0WFBoF57kvroO1vz4f9tetzWeKMqWo89LyObsHOuqkLKedhDQ6oUvDNQjD2YoAN6owXmM23EypKpQvuMcpeT76asoNaxbP9NiwwNbSJ0dcyOatJbWhWrW7udTDmXtBZvp5fkpyXzsVHl12czCrgnmQr0VS8YTLbRiC2LeKJlzOaF09VX7TlMdr1Hj7E0SPbcFxiiXM5k1UDUsmzL2aEkJfqYBlcZuIAVta5ERpYRLX+NAuT2quyS5TNvvDSj8SMnWWz32PEnvZC/fzlbTdbJfZkRYoT+9ovLziIRbPhNkRgs2ekNUiN1AzLatDw+yrzFekKXaq9oMmS6rERG7cOn4ibvWB2YKVcp6vSWlQrmoi6xWl7911GW9bdymGymkteyit7BfmUaHypRUbzFaSl5v8ej5Imb0tOnuymnR50J6zvM6JbjLHPC5ZXfcMjVKBZCZMWHgWGzTkZMPh1S3EWINFc1NcOrubvcApMj22OO3mtoEz8w6rqCbG6i1OEElCxmcKRKvu1ErNhGx1xhpIY58O6QRc5u4+c9JiwgZwPhlqZifXoaErbUMxUhZtGmLfUxgzU1FTLCXCnPiTzZGXDcBftnluar7J9qbTTVAWon4zSHRr43EtVwej1/pDcb1EPJur1HDo3NmuZfjwsr16M6ZqUXyiX5aGaDoh1wyRz65WAnYgNviBxZKDtCSAN3GIWQz3K9ds7m7zrZwJLcQ/tw1lLkMbd1Le5pOOO0gXw3TJCznVDpupPoNDL9+GsTctV47Gw/1sIUNESZLMdAV2LhalzPkb8RQuUzQgualYHGo98z2PAius0HfAu3RSHO7meLKkgmng3sYOxxik1bjBbaetYPtVblI7p1ar1ikEniPmdGsNkQhWlLDZwyFYXxKGMoFj/u2GhSSI+SGe2HgdTdCVxx5IQ8U3Bev2ZLXcJyjLduXSRkvLwTPz1FndlE2oS0ZfyRvp8fluH1ON3xhhhV4OCiqHZzs9oUNQ4u1EP5z7HcS8+RUOwHG3LqsOqCSl3zIZc92dstfiLXtRspuQG7P6dk2v6D5nwSUutKVzaeC8zQ9lIe8KFGb3eUHOdydOQJmL0XbFhToKt/YYiE02X7KBTtEHo46na7Yu0ey65G4rcxO4bTZZioZwHnB3wR/CFSkINFBMG43n3nbdnjY+TQprI3Flstoelo1zprY05m0J6tTyEJa0Cp0UCjUD7ToKgi3pXUo4fu5spmJIr5kx3U1I9rKVhwbrJvpCOa6teCcoxiSheVzF02A5nU4uGtUdd+eW9XuKSEVn5gQSoAMLBVRESPIu7poGE6/kKgAGv1TX7MD0u4275+lDN1wyAj01NTE5+ermbJsmyXWbSWyYOGHPjWPnonbhDcTW22xn7cVIO6vSvSkeseiSp2wL1gdGroZM3XUzTGtU5wC6iV73Kz2z0XZJg4AR0HBPRYGBd+fMXZItDyL8zFS3dbbod27W4LMEM1TJmquoKkkgAU0MjsMKbv5de61QR6IhhN38OCGc64S3nKxO9fbqT2yNndlL6kDZu9mh7qh4gcZ4dWnEazQBh4m83a7mUm26rEwyKa0zedqKGTZxWHSOojxFrCZbhidIr21dG+50iGlGF7y5m6vDWq0PV2fCD5mpmbaWUXCbXEhNf0gOgki1Ow7jImp7nk0vJDnM8mATWks5bSZJGBXtOriZ86LV4oxu3QsI1QY/DT3lH0VnwWNdJ3OTExYFwoY5zvT5PNSNoq3rxYkt3brdX8KyASrhl86Zq/anNZu3O5qJQ0JKFxUuEOp5QskXNuw5IfbUZul39d67RZNQWkhb+mQdbYwbsqHfcPKhBqSZS7JNZrGppBrNyfuqiyYmM+2Jqei2siDYsTfrbRE9VVCRTQ6aCNXyBCaltRQTkl1pG9qTA+KQsA1vBnONhKOfyGELXKXTIhfxRqBkEyMwUfRk7Cav+loBS36hOAE+9/ObS07ndl5YB62H4zBpe1NHqIYAzSPLo2m23sBtSGfluVL7sRdzHPePl48v4wHi8xjw3/wBcTyH+V87Dnqc3Lwd/9/P4YDpfL7L+vzvKvTrx5fSDqA6j/OuKm685/HQP592ffrXx8nj4v7xg9z4E8WtfjsorU1v/EOS57nSx5fvVzx+CXocFAbe/RBx/OuLr+9ndR9ffvjtCF6bz1+Dvtpm6YzqPw+modbEeDL98sf/A/UVJbDiIwAA -->
