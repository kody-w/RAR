---
name: "rar-cat-agent-skills-ai-demo-assistant"
description: "Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo \u2014 fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_demo_assistant", "rar_sha256": "91fdd28e1096d53816d4397debef31b39e5539d37b57a29783db543dc51482d1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Doak Moore", "tags": ["demo", "copilot", "microsoft_365", "sales_enablement", "content", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_demo_assistant`. The original RAPP
agent is preserved byte-for-byte in `ai_demo_assistant_agent.py` and in the RCI capsule.

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

AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_demo_assistant_agent.py` and embedded as the fenced Python below (sha256 91fdd28e1096d538…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_demo_assistant_agent.py` first:

```bash
python3 ai_demo_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_demo_assistant_agent.py   # or on stdin
python3 ai_demo_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_demo_assistant',
    "version": '2.0.0',
    "display_name": 'AI Demo Assistant',
    "description": 'Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.',
    "author": 'Doak Moore',
    "tags": ['demo', 'copilot', 'microsoft_365', 'sales_enablement', 'content', 'productivity'],
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
        "upstream_slug": 'ai-demo-assistant',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c768346e949547d4',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AiDemoAssistant(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiDemoAssistant'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(AiDemoAssistant().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+VaWZebSJb+K0z2g11NOgGxZ586Z9CKFhYBQkLlOjZLsIh9k0Ce+u8TSMq0q6uqp+eceRv5ISVx48Zdv+9GyN+e7LYJ8+rp9Wma2zEi5XkFnp6fPFC7VVQ0UZ7BR0ZbZTViI25bN3kKKiSzU/CMJFEGkNxHnLaG7+r6GbEzDylAVeeZXSNR1uRwUQVsr//U5J9qADxEitwqr3O/QUiGRiZ5ESV5g3ggzZHP7QgnKMSP3GFbO0H2eeVhan4BlZpDZdisc0GCgM5OiwRAuQTUSJG0g2V+myRQSxKdQdXfzajyc1RDRVEWQCk7e0YuURMiefHQnmfgk5tEbowMhg1S0FwlA9MKKrmpMICd1i8wGo8t66fXX359forg+6fXb09uYtfwqychmkLzhbqO6sbOGigPdwvgg6KHoc3gZxgSP69S+JUHfOTx6WMNEv8Z+fvf44tdBfVPr58z5PH6/DT809oMaUIAzbLrBobOtQvbiZKo6V8QIbnYfQ1j2zxSUzcVdOHlvvK7prxAfh6efbxv8hKA5uPnpxyaYA9h+Pz0E5JXcL+qHd6/DFqKjz+9JEPQP/70XU/dOifgNoMyaPXLl8fnh1oo+F008m+7/gy13qvIAZ+ffnBueN3tHvyEK59eTjC9H++Kh7SBzM5c8PGnv1LrhsCNExjtf0vvL3fFISxD6NPD8J+eb0H+FUEfDr3r/OtthyL633gCxd+2e0Yegfor3bf4/5Pqob3q94j/qbo/W4D+jPzyl779qwXPiP/5aXrvIdtJwCvy7Yuuzia/fPC+f/nh19+g6v9RjZ63lXvT8CW1s8gHdfPlyy8f6tvXH3795UNbwFqD/fWlrZI/0/lncb3t87sIPqQ+/n4t3H+XxVl+yZD3Ske+5cV/VL+9IKadRN737+tX5Md+GV4oMjjxtuk9BD/0TA1t/SGOPz39BiEhg960N9waEOFvf/sB53Q3bxsEJriJUjAYb4QRBMf61tsVgHGtIxjYhxys/yHDg8UQWb/+p2s3n+wAZM2nOo6SpMbs6MuAll/sN7z5+oIYUFNeRUE04JomqOrn7LZm2KWoQA2qM8QPp2/AJ4g8n4Y3EJ2Rr3/Q9eW27KXov94AMLoDkDZZDuBTtwl4GRzYhyB7mOvaGQRk4LZQY5K7cPsbLD9Dx+o8gTjaDM7eTEe8qIKe5Q98hgF5HZR9/frVsevwc3ZHSxK5E0+NQYF3c5BPn6AffhIFYfM5A26YIx++/fYB+S/kX626KR/2UKGDj3BDC1e6IiOwfdoUig00BdHV9m7h/vbbI5pQTQZ5DiYn8iNwXwzLLwbeW2h1Ufg0ohnEATCkMJxpkVfNwCJR84IsfeTdXrjp8GgA6TCvB64rQOaBzO2hVhu68x7JDDJhDWus9vtnpK3BbdevTmXfTExhH9vNV0SaqJAS8mSgq+pBEXAxJDoY/vfE37+HSqoPNTJ+U/GCyEPBIYVd2UVY2Y89fPueF0gFb8tv1J2By+dsoDswhOpW/ffwQCEYGfeR0k9DzhE3T2Gre/Xb3jcZeyAu40Zg1eesflS2XQ2pcPMbWQdt5A14/49HSdVh3ibeLX7Q0kHTIwveIyu3GhSWyMC6yDvtvo0P/69nlVtkFgttthCM2RSZyYZm3TPm5lkzZPY+7sEZAoFle+/O73PFGyq9gfPnLIlg+VX9P+6Stzw/ZO6A11YwTpqg3fTDIoPxHvTeemCo6aoausf+nL2xAIw7coM8WAYQMGBDDa68bTg8fbM0hKgwfP4+EdxqpvIGf2GdI0XrwJAgPoyIY8PQNOGQvrfUwIa4JfwSRm74O68QqB0GHuqHcYWmwj+X7BY6OYduwuD6VZ5+F4+GOQta4bUutDYEFXhB9rAVh3KsYf/DYWmQgVH4cFOFpADGGJr4HuE6tIu7MXkVvxloP3LxY/wfj763zs2SwXio0/bsBkbyMmC3B7p7Xt+tfGQKmpoOzX5b9PtkPzxFfiSrf3zObha+0wXEkGTg+R9Cg8DeTetblQ0QWEMYS8GjfGAd3Cj95c7Kd9p/t+UVmQgGItzx8kZfyMf0raluHLr7fU5ekbBpivoVw97FXgLYCa3zEuXYH7jwb3b0aWjHT+8E9judd/dfke8nm989fpThK0K84C/48GgTuWCos8frFWmzd+z5+MP7R5puaQDeM8TJAVRhkQwVWYfAuw0pGvieR2hKnkIAHcLbQyZ+56s3EUhaQQWCQfjOX/VAexfItDfdMNKfs/dcP/oA8kEWDGRb5z/05424YebuiXnnFfgoa+De3gA7ARiONcngbg2eXjOISM9PA1D+6XFmYAtYfzBcw7EHdgKEzSYCt09260VDzIb3vz80Kg/wGpolvyErhNl3mL7Z6w3wNXRXEA0EAVEaZAHEvcGFy9Bhw3jhQJfqGpK1N9jc9MVg5P24M4xe73PZHy24NSlEFy9/HXr1+QGt7+PwM/J2QLkd8rIWntB+GUbxwWcoCv+8y76fiR3w9OufmPGYzP/aiAeA3HnHdgamG1z8E5+gtgqULaRWb7Dnu4Pf983vm/12s7O5ny2/Pb1hxCNLjzkSisNm/FQP5IrBUocbws/3IoPP/o0J87ECohgceOASnvA9b8QBAucZjyY5gvEokmc9AGchknBIHtA0yXsk69CsPeJZjvQcmiI9lyYobuQRUN+9OL8MM0M0WOFCCGdIAvdtn3FHts2ShE+yHs25PuAAPyJsksFxDv++NIbd93Dt7soQt/dh91aadw+/PTkMBSVFql4K99cEQ82jY2FOF4roNUG7o0Ev9WzLKeRC11rKbL0qI2bj0wKzie1hpiXjPR2f7Ehf2Ifz9By6szGqiXTox6mfmiNUb9144y/DciEKUuaNvOwIsixdTCXpoohckZWNt6mZhnDs3V5PUOw8y1wzPV6FvKDqco/uqGPspl6aF7sjXsVrdlFvRPqodLtex/XwJOFX2zoofdg7p9VmhZWGZDCdHvmh3fU2idr5LiOvo/IQ7efXStZpcZseDF2HB8CupXf+SnFoVZP9UpVSuMCI+Naid2tPb0jNzoOkhzRRbaOaOJppvJqXJWqOjNoxRKbZaEbhCHiR7sj5SafIZYRy/KkzVuSipBg8KPFg3VSsQojSdGVfo12deidrE2Dr9kwmNOcdaJozO/e8KTgU5ZeHBbOLVKU21YlSSYXsZDo9Z85uJK5PlRUmy6PLFHufOlyysKyE5LwRNrsKx/G295V4wWx7fBJAollfJPVsEFiP5om/KKxKp06cs55ZqYQ70WiauVdcb2J9GgJKIohdIaZct6fd/MooZlqzMr9qGRWLF6vDajO3l/rlcsAJfKqu0T23PFoXLdlMbHS3uORO2Bubw1E7y6cK8Ap1ysexEo5YakY4UUbX0iZrTYqkL4xbxS1hWfJ1t6Z7z5xOa7Ivw6W/UbTCEMw4bQv83C+O4pSf6bWuXA7+KhZP+02rhY4Uy0Q9Mg4V5pGEcuXddVVIySmdGf3CymMqro8HYZqNwKrNzM5ZX6+5tVgp1xMY2zv/IHIYKzrjoFEbnBKaeHTuJddFDbDTrT3JL3dF4hVHY3Le981+PZ2cN8egOmWJFZv+xJkpGHtcTJfGlaPOnZFUfuWb9r6ag7l7uF6MHkM70dKt0dHMrBFIimW3b2JfNaVmQ9v6dTNjnb7brFv8gsZquSgVek4UB89si7PaqbLr1IcD2NM7j99n5OzCnUJ6fmKn/bTDKz3KsGNvl9Ppiim0xdgFLtlZtlfR66If62CHF1umSWU9Oo65uU3kliSjO2afZj0z51oeNoum7RPVphfzwxqV94V6CVo+zUdrVZ6bisRfHFkRiV6jz8fNcS9MSscblVsrVjW3nguzjSSlC71LVjtKiebuXpeXy63Q7yfXkknqulul1AQ9LXILJ/VVd1nFy1PErWk0NNqJ7bXZVjBKRjpPL8uQtzZRvThFkrpyziuvIDg/prGCziN86zhobmq04EVKnkmAi8+8P1tzHlWtbV8WU88h9n11mMMELZ3Two4SsXbiHZZSK5vaVPhlllvnYKLkjUauo9ZTJ1KDHbaBiRbVVvJyNuAFSt4xMlkzZGpe9gXGb/vdqg3txEw1byJP1+jG82W0FPWwRrljUWdTd7wJ9XJtnbU5CGl0sktINNH3sMCjIOIZwY+MrcrF/kkZscVSXpYhJjDj7XxvXaLxDLPYhEGtwuzMspucna3m6oXnz415yyiKGI+FneYwc5tpjOIwtxhjG1gzZjxe+ClDHddTzmaUwyqCbONcdUKBs/A5pcfwoB47Uzg5eJPmOJdqQ18ya1PfZb3MzHMTJ5uaMuXyahZKPLVyfoNdnZmPTStT3Go0OZtt53G+qiOSLYJDvrysNyAY6ZuRVracmBfdXKRVVcXO11XMYbs5jqKoaqxoLjYqbIJe41XZ2qd41hLnI8V3kbmc2FsxpvLdqIk1gqKObm/wu0DYl/JVV84SOz3u4RkQRFItrcvUbZbYBg8PxazMOHK5yqLVzt1NothY9tQY4uE6rusqOnm+aM396chpe8g/rXFeCBMXFGDsZ6aWKKqm9leFSGPGw0NBA1QwOUeuPGftMHHjOtEva6YwjBzttKU/8iMh1HBArNmwMeYLgotODmdlxaULJxW51cYBSvVJqvjUqokKn5mT2p5ec4bHdGrsr2fjy2674eKoMK1FfuaiYrPJu3E78uRre2jCJDZYiKjdYh1KFKnIrFUedgQ/YVKasHWzMLh4Vsxmo8jgXTa0HEoTLhw6uazNVbprNvJ6kniBuqCLLiuZ1TLSTGOzYWkUS5MV7y0n8liaLcpc4Zalup1PF2fNoh1tKh491lGJPmXUM3ns+vPYUVatzANOaMZOkNSBSPFMkVBgjDXcVs73neCzyQE2GC1qFzUG264JFko+mnZsTc6l0dJajmKhaCHtTuTJfE9HpDhbWmC0rPOVGCdaeWxiIZRX5lhPIHouVtuwpLXMt1w1uYg8nu9nBbOpTqd9bcp7tIstO1WTylwnWWKyx6Mw4xZ0T55W8UVdhtPFjtG1qRZH7EpTdxtrqTP0KikW0rSU8SVwW88t94XjzXkxhsRXiGe016betc9Ote7OJGJSFT2/HhOYdLU3YFkIsFQx9zjfjVN8dXAhYk568tgETUoHh/m8i9j2MjLGrFtxs2aRg0lELg0P7YrSC2O3QRU+EqytYJ5RNCKO/RLvFUOKQUidojqzdqtZJ1bcbnuM9ZFZtUEm2ddxrpvMldgxtC2HJWoQky0oaCVe5r7sUHZPdLZHeSdAhU6nceOtzZGytA96va9m9tk6Qt+rk1ytrcwbn61dFZlzrNovGU0S5os4wxinXEUrszeUtS5V1OmkdHiqoISwUHRbhsjfs+Y6Jcd96WTz6txIbARPWx49te2jUi3MGdUtCUnA5mCdbJPZeHea0zM6BaQnrrOtdxLGFReRMqU7zmyCri/Xq+mtHHu8u07tWbIqG45Taka9VrQ6VsoEE9attWdntCCsT6kgK0SYrluXdzl6fJjTRRmg4UrX5sLpYpzW+xVVpNEaLGeGOduYx3TltZVsgmYMW/JImMf9KNRG/d62DXXfcpeW8ZwlXmue3Cluma+ZcMVbqa4eNIuaU+ccx/sJufUzKhlvGzzZ6XBwzthTRAgnb+PWRjtvDycG73QGOyRrQiAXNFMyY7FtvCbUs92cNeVR4M0PxVGfOy6F97t6T83ozT61xROE73Z/vFZpKtjAPrhew/kzf0wp++lWQDNjz18OW2wkL7sOH1OR2KSKXPJKjeajshGFdC5edhJgGGx/BfWq8mYk21NKURnN/HDeHWhO8c4Q/OvN4io3VzFd7wSFPYoV3RB2FOAO2Lpnccysl+JW0PmNTJB4rPAtMc1oHt9M2lahwzoMCHRKSlpTtrNrv3AIIz2Xx3onEqUddJm3ryq54puIvnRrYV9pHE7jIq6Wmw6Lgx2m6gduaRyUhWCxNaug12OypiJ1RczOnEmM+EamZ9kJoGdZVdHlmZkla+cy5XyM2/rXJmFzNVJANRqflDl73LI7B21GicouLA/MywtKzLMxP6Xx7eWEXaLLNrzIAPSkEZXCZKvVLK2Js44Q6NyltLBQllSSSiuWaEBrjq4BPXHGuq21x33AiVMxo5vFmuXPzjURgWT5XHxp8M2iktbYcZNSVk/T8nZaogdSzgoFC2v5ao4WPOwg1s85iR6R5MFSLNO7oMwirheGrknkjFDRI+9RwnQdnpUjLpOxdzqm+zDylIBWEj5L/IKnUKWduenkUAGJ0tJ8maEXVMSphV8p/cF3NXmqn/hcO3ZzzTJ5eE6yOz5ZAPFamb23Czm1nFyzvXtUOZQtdNWddcuJz0rskZm72EJr5+V821xDLbzEIMZa0+2nY9bGStut19MgumAV7utGG4kr5nysqFAvLKWfWAUz6oyLmRa5MOKc8Gp5/YzkXMa4dni2UwNV3uhmO3OWYQcILyUJWxZFKKAdRXa7j3hC6sdtp8TUFASUNk+aYEofQEZdtuvN+ORIIZNN+MzdlCmFbik2om1swtGn1MOYCXVxBKPt225+dTuPVV3bn2WLLZWRwKiz+ASkiWgsrzhzkmSMWbV+EbVbj8s8luDzniGW7vZ4uHAzVRbno9QIqsVM8K8ksdh3buhiNotLHMuhdrTZX2Xrshnz5wVrn2xHCaWKHMH2A7jDnphDurWY6qpaRsQwkcnUZBBf97UwaTB9fFUZrNmAxTgReC3kM7SpyUl0NJYrf73SpiZL4OQIQASrDRbSha6QoxCemfwKrr6aJZFeq3PrcSzLMjEtWfTSw0hycfH2Ia3LvEy6bgIwIUwq7IJPXTGNK9dSDCBcyUSyA5/Hxhg2Caypv+e1JqQ2JC6shIK6HqOJI42NRV3aMp6hLjrVqmkxOy3ttjW9cHwgotmBs9LAnsBZrkTRtSh2FK5JXduLxqhnF4cA+MXJ6xy2czYO5VOdlsr+Zr8+T0+xoOEK6wcCKvLwbLbenZMjUc7mctEW6J5WN23Dj0oaKApTZ025s2cr28YPIwc1CmJyqil1mpZVG6/OjHFWREnYiBORg5OwbUzFaa+UXHRujsnymk9l0YOz6Yk9NKPSFGWDXO5zFtAG7h67HerwXNvUU98Hu6W7SjGTUlkZnj6tQqoIXuRmipOymBswKEb1QSuF6MRyDHmS9MdTZxIAk1JhpxKb4lQUGX8+CqLCsO74GswtKtv4aBAuxkXinsbKFde0c5fH59LZiJctUM9Bq4Y6XcDhxLvk2ElKvGWMCnwqpSKhR1tBEH7++en5abgLfNzo/fXPfMN1yv/Zrc79Aubtsv52lQZs7/W21+u/sOHX56fKjaAF98upOmmDx8XOP19NffrDfe8g399/HBt+Nuiat8vMxg6G/67xNIgP93j3H2/gu/eL5S8kQw/L7QTUX6DNzv1Xrpvw7ReIp5s73nBTfo6am52PK2No3mi4M3767b8BemkQt0AjAAA= -->
