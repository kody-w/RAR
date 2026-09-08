---
name: "rar-cat-agent-skills-action-items-todo"
description: "Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/action_items_todo", "rar_sha256": "1c5c79a035333e0169c363cc1f60b4849ce2a8297ef496801fa6e95e5988e3ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["productivity", "automation", "tasks", "teams", "email", "meetings", "microsoft_365", "action_items"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/action_items_todo`. The original RAPP
agent is preserved byte-for-byte in `action_items_todo_agent.py` and in the RCI capsule.

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

Action Items to To Do — Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#action-items-todo
  Upstream author: Matteo Pagani
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `action_items_todo_agent.py` and embedded as the fenced Python below (sha256 1c5c79a035333e01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `action_items_todo_agent.py` first:

```bash
python3 action_items_todo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 action_items_todo_agent.py   # or on stdin
python3 action_items_todo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Action Items to To Do — Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#action-items-todo
  Upstream author: Matteo Pagani
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/action_items_todo',
    "version": '3.0.2',
    "display_name": 'Action Items to To Do',
    "description": 'Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link.',
    "author": 'Matteo Pagani',
    "tags": ['productivity', 'automation', 'tasks', 'teams', 'email', 'meetings', 'microsoft_365', 'action_items'],
    "category": 'productivity',
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
        "upstream_slug": 'action-items-todo',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#action-items-todo',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ad7ddb14bd369108',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ActionItemsTodo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ActionItemsTodo'
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
    print(ActionItemsTodo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbOb2LLmX6H3eSjXlb3FPPjGiWgkQGIQIBAgqVzhYgYxikmC6vrvvdDWtl33VJ2+HdFPLTtCCHLlyvHLTNb+/cXtu6RqXj6/7NyuCytId2O3TF8+vgRh6zdp3aVVCZ46bucnYQuNVd9Ah9AtWshP3K79CBVh2KVlDHWNW76tADfdMoC0vsurKoMKN82hqGqgLgF0LVSHVZ2HkOt3vZvnI+S2WRjMjKGugoLqbXGU5mC30PUTqCoBcQu50C71m6qtog46VBBXQR1YCd3SLgHPgj6EArcLP0J1k1ZN2o1vfFogrx9CeVpmr0Cp8O4WYPP25fMvv358ScH1y+ffX/zcbcGtF9aftRW7sGgPVVAB+twtY/CgHoGRSvC7DhugSQFuBWEEPX99aMM8+gj9x39kN7eJ258/fymh5+fLy/zP6EugfAj0c9sO6Oq7teulORDyFWLzmzu2UBN2fVPOWrZdA8z0+rbyO6eqhv45P/vwtslrHHYfvrxUQAR3FvrLy88QMPGXl6afr19nLvWHn1/z6hY2H37+zqftvUvodzMzIPXr1+fvJ1tA+J00jaCvps6vn3s1oZ/WIWD+g37z5030J7unSb6+EX+o6o/QX3Oe9fknkPctzDzA96/ZAhuAlS+vlyotPzz3aKohLN3SDz/8/HdsQbD6WZ623X+L7y9vjJPQDYC1nib5+ePDfb9Ci6du33j+/bY1CJj/G00A+ft23wz1d7wfnv0vrEFcgzR59+VfsvurBYt/Qr/8rW7/bsFHKPrywoV5OoC48/LwM/T7I0R++Sn4fvOnX/8ArP+PbMxHas4cvhYAcqKw7b5+/eWnt4z96ddffuprEMUAar72Tf5XPP/Kro99/mTBJ9WHP68F+1tlVla3EvqWQ9DvVf0/mj9eIdvN0+D7/fYz9GMmzp8FNCvxvumbCX7IxhbI+oMdf375A4BNCbTpHwgzY80//vEDnpl+1XcQcHCXFuEs/CFJWwj8n1GjCYFd2xQY9kkH4n/28CxxFUG//U/f7T65cVh2n9oszfN26T4efk1nIPvaAST77RU6AE4AF+O0dHPIYHX9S/lYM+9SN2EbNgNAJm/swk8ggT/NF1BaQr/9C6+vj2Wv9fjbA2DTN2gz1uIMa22fh6+zAk4Slk9xfbeEwnvo94BjXvlg+we4fwSKtVU+hHNdaKGH6FCQAuDoqmZ88AYG+Twz++233zy3Tb6UbziMQc86swQE38SBPn0CekR5GifdlzL0kwr66fc/foL+F/TvVj2Yz3vooAQ8zQ0klExNhUD69AUgA54AvgPY8DD37388rQnYlGEDAeekURq+LZ7rTBi8m9bcsp9QgoS8EJgUmLOoq+ZRK9PuFRIj6Ju8YNP50Qz/SdV2UBDWYRmEpT8Cri5Q55sly6qDWhBjbQQKXN+Gj11/8xr3IWLxdS7Kv0G7tQ6KTZXPFbV5Fh+wuCpTYP5vjn+7D5g0P7XQ6p3FK6TOAQfVbuPWSeM+94jcN7+AIvO+HDB3oTK8fSnnQhrOpnpE/5t5ABGwjP906afZ55BfFSDVg/Z97weNO5fEw6M0Nl/K9hnZbjO7wgdIDzaN+zSY8f4/nyHVJlWfBw/7hc2D09MLwdMrjxh8K+fQo57PlnjrGr70KIzg0P8PDc1Dyc3G4DfsgecgXj0Ypzfj+1XZzU566+7A4nd52x+aj3eAecfZL2Wegkhqxv98o3y47Enzhl19AxQzWOPBH8QLMP7M9xHOc3g2zZwI7pfyHdCBzNADvYAfQO7PdgE2ed9wfvouaQISfP79vbg/3N8Es9YgZKG693IQTlEYBp7rZ0CqZk7JpzvL2aggPW9JCiz8o1YQ4A5CCPAHhgeigq9b+TCdWj0cCEVNVXwnT+dmDEgR9D6QNgmb8BVyQGTMkdWCVAYd1UwDrPDTgxWIF2BjIOI3C7eJW78JUzXZu4Du0xc/2v/56HsWPCSZhQc8XeB9YMnbDMNBeH/z6zcpn54CohZz3j4W/dnZT02hH+vOf34pHxJ+Q34AB/lcsn8wDQTSECTDHGtzkLUAkYrwGT7hM/xe3wqs+R6Lb7J8htbsAWLfoO9RiaAPxXuIP8qh9WeffIaSrqvbz8vlN7LXGIR/772m1fJfyto/3mrRp0ct+jTXoj/xfFP/M/SnQeZPFM9I/Awhr/ArPD9SUj+cQ+35+Qz15Tck+fDD9dNTD0+EwUeAejNEgjiZg7JNwuDRchjhd1cCaaoCwKH/gARv/FZ93klACYqbMJ6J36pROxexG6ibD97A2F/Kb+5+pgJAqDKeS2db/ZCijzIMnPeEhvcqAR6VHdg7mPuyOJzHn3xWtw1fPpd9nn98Kd0i/MuxZ8Z+EILAXPN4BJIBNDZdGj5+uX2Qzjabr/88I2qPCzef86Wa6+gM9N277R7yBg0QZk6wOJ3h/iMEZIxnvAMq3OYkm5sFb4bHFpTeYJa5G+tZyLexaG6kvnVZ/yrBI08foPt5TleAnaAj/gh9a24/Qu/jxmMYLHswyf0yN9azzoAUfH2j/TYCe+HLr38hxrPP/nshnhjyBtuuN9etWcW/0Alwa8JrDwplMMvzXcHv+1Zvm/3xkLN7m0F/f3mHiaeXnl0hIAf5+KmdS+UShDrYEPx+CzLw7L/RLz5XACAD7QtYgviETzEujBEYhoUwQjI+RmK+j0Qk7OE0zvgh6tIoQ4URzpA0jEQuGTJESDA0HWJAK2CuR3B+nTuAdJaCYKgIZhg0whEUDsA0jeJBQJM06RMUCruM5xIewbje96UZyL6nam+qzHb71ro+QvNNw99fPBIHlFu8Fdm3z3rJIK7nLD0jURZTvrjfMXKP7GoYzgkqoJvc4vzBOK0anjYJIQ6OlhBlYyGpWTj1cHOON1qqk+tlq1B5ea59y7Q3aEFKbAhv9qZ2aCll0ndUK98mFk8dxCU02baN9uKtt6EQSoR4pAjSie6Nd7g7SXFXzKrD0kJiloLrXHb2hrTboqaVK2r3pxp1GIEr0mMSoO6tUlpjU9f5SbCbkxqmO1mwjXPWiKhwGkfqvC7i3uY3urszSx/PHfd08HOcsio/YT3Rt4+ue1MscmxzuktrL5Epoxmy7CoZQoUIrq2tCQx0W+pF3CxaQ/IKAeH35XYiiKA9HgmSDpeCP+gXEguGpdErgVMV+ChjcnNe28dIN528qWS+Jw6cSiYF7dwFu25Eb7E/n/ouOHgSTu4JGZH2wmql7dEOq0n6HJ3G6WwX3bVQTwJ9Qy5XIbkop5G7B7KzSxoqsdCa5dpULAqaDZmjB3f1eVJ81B3qkOwFk5jkTWSXm4RnRPymq9fCde7OurCVjU2z55IVHR4jisPulDo9kmYtypy3saKHfEGftoKSDmTrS0NPnpRQyk0c1VCpuiZH9EBWJ/9K2na9xYWBjwPJ8lpgct+yYGu75C8rNm83sKmKJ8RFMtLc18zNlSRvuUCnsCT6k1LjasmnFjvGRMG3qH1bnYcy9Wo0KsaMJslVKqYMxhU5iYzDFjlRZ3pbEVnJZm0+tZctpbdDxhdUgFrqqTa2hCDElmW5bYpjI+xKdLMTin09OafQ54tTXkqLJb8+7haDlU6TeLnXFVWsw8sSXh7XB3nsFB9rF0oKMBg3SNUazWq4OGp1yQdF3MnLCzcajS8ZJpZQZxHMiIqEFbvlxu6Ek41XMG3QJrI+TtbkHy6ksIXXm+Wi9F25aptlccquKxglzX7D+2E79aeoawi5HldOaCHGnpEKxEzPK1rwuoH172kFEty/SwNzk4/jqLmELOjc8kjWoyiQY5j6VSfmFjE1qxu8vZzuUydbW7K3NswOtmrOj2li0oKFomt0u1Ni2yHvwVleY4eSFmQlXZ06oTytleQYX71YMTVuXwVJe54yszrbGenel5yuba3BX+ZGv+1Ifcccp+SoqLG9xhRhXC/v9vVslzSnbZlIzxjTKoJbDxo3TvXixG6Ja9ltl3vE6e2jmph5jbCNvfBCh7j5/ZS5Lak2MN8xgnXRrrhcKqTRtN4y45yKZSx2Ukicx9Yc0cNOOY2oG+3q0AEwOA3rMLzSsDSY7qXveoq5TKw9pER7zS43nrWuBL1cDPZpaV9z53zdjiYhMViZ3m0+9XT+tK20KCHuRn4H2QJ3qRD1iaTfV0ORiqCRYZgVEmeyq4RRzCxF/YZ4YpeR9nnKxxUwCbrnJOq8am77FYFq9dEn0gTVLslqT+/t0w29agQlyS1uyidRhjtC0Hn9FCdbX8Kn6USsF+HAaHbRU6EW1YJ5ZTZLd3+mDN1Bg/VQ3LQs90mRzgN74lwPLU5KhhzL+6YYipgwB3qBbqdxByqa5fN5z6O2Vdww75yH0uoWO8yh2w+1eXYP/WUDu60/yJgkZItl346L0Jyi6b5gtpFOK662L67DVRCdlaNeknLN5WZaX9VLenavqn6qJtceo6UimGHWdcIKTa+aenOc8rpFc22zc6vi1IlLBU45ia+3NCrW3X4fMOZNpkw2ExYX0GEdxVq1t1ea0WljKZ5x+3y+JrC0dOUsU/zTbcutSe3u5L7NuX7YHS5W0Ng9GF3XaLZHLwpWqkmAbAP0ukFrSxCMSTqbFR0eRArTbA6TyNCt1Bi9p4y/MIya8oM83bjpiLHnVaxak1RIIk50gbxEhD7NFM+3jox44XSEO7bmtVuwtS0LO/ZsLhQ5Y0JXxLSpHv370VfOFUrxlGWmsOPWi+R2IrVROIwrSqrQ3eY6VqS1NFaisQqqZOlFyzbHxTh25dVpo/B5J+4XyCJZyIWyT7fdsCSMs9BeSFJDz6JikGSA1jzOHwiap1YcZ7UrvkbvLs35DSbxsb2Kqlht7+oF2Tod0l9vFTyeRO64ckuFIOjw1gbaIVmyoJjsu4Wtgba0g5lFw9kMXPLbVnV2+oFVDbk0L7k4lsSqwm/JpldzRc4NtQ1QQWGthBM21lWX0QKtjYvanzYJjYgmzkiVkewHXTrnu41TeSN95vpu5ch0dbOsqpsYHkXq+xHbckc5A5A77NareLOwYkLyNgdpv1McRSoLEr1OhpQZW9XwzW1O89tNrnrF2uVjkexP+72NHmn+fi38s72zmut6xQMhOjq3xaWIwaFxXqaWK45xnvP76RpacpfaYtyLeYiu4iTc3V2lEgU2i1lb3jBdHWwGWMF9t+Wa0rgUcWa1ZlW1cc+0anWLmJVZ55O/WRlXRLy7UqyuzNZPsiFGu/ig7pVmaivG3zWOsYHh+wo9T3smvsPoCali0zRk+C4fkE1Dl7q50kQExK5kX3TbAFWi2DQEi9xX1Dbn43SgCe1gO5lUHxNU9bLNIDg3gVMmH05ktd0o4qmTprXmWatV6mr2neuztQlfkGVhU9QtzQ72mkoPOX24czAi7KrBWMfZHs+T9egLnbzFfSt1RakvMQ8DHu0E5GDD5wrRRqfrCX5TnWE0I6qbfHGVni1TzObjtSA0sd5WYuEsA1ku95cDyzd0OtqIoTmnVWrdxOvuUK8aOLcnLeWPNQ8aLQoPDDhonDRcB5YU4EfgAbKQr6BuD12Fs7uxqSd4mjK2isbrraPC2DB1gnXtVmFp62BMup4p8WnSzuOVyS6Dvcnthu2o2HHsZr2HR5RUtmqtMSnaKU6qbngy6JVLst96K3Q/Duerld8HdU3g52yT7eFsVAAmS7f+Ml1Gp6S2TWLFDqKwAROI25rJV2owldRt7Xh6cT1V4d5dqqtKu5qoH7VstxvG62WjTsJhpYEOdWMfj426ShDjiKnqyMM3fbemWRrgMnE1qWl/GpTbgdQ2MGkU/QaWw1V2QU+8x4tMF1toi7THE7dZOvxm72y1LldremnzCMW5TM1g58FFcz1zogi0EotxRyuI0HghEwT3uy0CqVyurwcM4YlqvS5PYSjA5U3u95QDe/2lQhTUs5yhxMhWQwZMU624DywM2dZyotRnaeeql9osBX0gOtD4WcjKAT1xT6PDSG4vbAzLhLO9H8qTBof4NqZw1loK6xO94KwNqfRUF0moQIn2uAsP15WOK5crhR9uki5NYD4JI1rw2c35YFEqdtTpY2TXNVVjlzYsN4LlazBco3ukOrrW0J4TAndOHLOjCcmIFknBL0meN3ktxC6YVZzsfF/hXjiejJGN4oXDa5l/OqTKeJ7AKCu5uUwFYwem5yZgYX/wUZLDWkSmkRzth5wIacmYjse7shtMIbF7fknDiq9xkyczh8kBg9jGdJsIPzKRHSTDKW2Y4ebwPqV4XbumnRUeBZwZykfDkEi5XRZ75oDJQcdey92SJFJ5rGFGwEmVGZntwrXJGmP85aFCxLzcyzv8nN/Epr2FJoa7xqDBUbRLNDu/UsdVdRf2ot3dz+V5odZU6BGDzQfHnuamNdJctd211wvyeKFWqsluF5OMhslRv2eHxEssxd+vVZRPUDu8exO+40aVatgty/Hs7cSpu9swnDCeswRtmvw8kgWZqHBzEvUQFf21iGiWOmzw+sDCeKSeznjOkf3tOFUbp4ubiNe4WyMRC3sCQ6m+3VqGSXCI2eVjfjkpZtt2rrrNWoO7sJPkc4NcwbqUX6wM3Ybc3XEGAtkHkV6f7oYe3d3wzh2O9OhomyXjDpf24GP8IZyGbWMYU64JNBZTMnFd3bjbst5oW9swmsVyQy62JLFCxhNWHp2L2phJetEW1ErAK7HDMoK8L2KC1vRDrdijMGHnowEa7ul+1Snz3KxXEZpXCBaDelJxDhVkx7BwzhitOohYhwly4fWc1KbDlcWUW7Qe1gSL2z25I3UqJ7BNynLyfZFuxRZUrLMuSUpcWtFZZfwmmKY1GlwGX1zhe7TpJjtNFx15p8SD3eSNo+sLxrcZmkxtgl6omja4NjNaGqmVztFEvQHk4BByp1xKcVIL9dUoYZaugaKmDRjNReEaPjPRdZmoOaEwd59nzQVRp6xLS+am7d0U7miRyzw7au0KF5oGZ7s4Opxh4mJ3XAOLq05DJAkdHNXsb9NFbo5jJOX0JVNqCTklbcVnaj7YizuJSrxw6C1qaPTEMJa6cIsP/k0eNoW+SaK5GoV3kjjiB8QJU9wS4WW8MkhquKuxLKwupbEeYb/Ztb3llY0BH2AczziKHmWUKw7RdYqCsyc2kxzoDm2bPdm0cHOtx+geBfdgiVFpuafo1dBbwXkhh0aWXnbOHWOx7GaylI3qCErIFzo9hEhJX5agCqMedeyCLZlfDwjuLntcputoc2zdRr97Z1jCuCyzkby8E80pcOCj5KjE1j1EGzIvy565UbWh3fQLSvsrIxJPwTkh42BX6xK881hcE/ZgGtF08xiPoUBemF4+qlPVgobyVGQ3tyszUb93p4DuadXa7rVF7BymhplUlh1h3TG39C1BTDhBF00fOz1Ld+7touMSolx65bA+q+45uNr3xbL14S5gx+jQTCaYJGVRD7Kh9uDrPIUlYXYNq/MwRe4txGn7Hl0G19PJhRayozFOQs2F5H0S147PWcU5SWE7R3SMbGhpIM/rY9QSQk7AGL4VUbfcnmyqZ3Lv6qy2lkOsrmTTIFOP2Pgpxel8t72kqEtt65DqFuaFX+7YO0WN0jKBTdi4JxXi7U9un51JNZIbdcEPlLVBwvN9s93iZstMMBiXBxnWieJmYsTp5EVZaqGMtDM95+QHAtxzOEpUx2TtJGi/3zPVRjKdxd0RuVUb7uJNoJoEiA2uKbxWjcVDz++WGOp5FyJGj+cD35PmFGLuBSOkZlduDky3altSDFhj2YvVobgstrbAnPEg6jo+OkSTHSV0QG2IYmq8jsCwxY4xXW+jOAJ+DR26jxB9CV/xDZuSrDaNoKzfT+qdMXc6lvrHBTqOzLipSHePdneLMJZwxAXqJCkZg0yEkB1JyiwdZ3nbHnkcW2C+TiUomPzyOe7qqbgx5WXHUryuMyN3cgRxNy0vlI5GJnxIJaUHymvMSU+dUsYPC11uzhkvXLkl0W3wA8YaPOFm5/gqt72sePHN14MQIRF8I3CrWxkTnB4wbC9ukBUccskhyth0c8cIWEATjDO2zTKJmbxPgj7AbsigVqs1R5fqmXYZeCGtyir0xgT1uZbAY6riA+q4AyGLL86wX6SbAr1tA40zXYqmEW7RLyN8IgWBJf1VWG5vE3ckjaxIaQcrStql7/flDcwjnW1XzpZGtGMp6XFEnc7HpKzuLMv+8+Xjy/w+/flW/O8PvudXkv/P3oy+vcR8P/N6vI4O3eDzY6/P/0aGXz++NH46S/B4wdvmffx8OfpfX+9++pdjk5l+fDsunk/f7t37gUDnxvOfRr28vbru0iHtZm3fzzIefwI1H1K28/d8Zjq/RZ+PQ8H389h0vvXtNOcrRhLz+h/UmAV/nsMAebFX+BV9+eN/A7CffxWHJgAA -->
