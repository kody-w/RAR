---
name: "rar-cowork-cookbook-turn-a-document-into-a-visual-framework"
description: "Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_a_document_into_a_visual_framework", "rar_sha256": "135628175770127efee50e33fdc10b5f48f03fd5c348b6c761fb4c5c14c713a0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_a_document_into_a_visual_framework`. The original RAPP
agent is preserved byte-for-byte in `turn_a_document_into_a_visual_framework_agent.py` and in the RCI capsule.

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

Turn a document or deck into a visual framework — Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_a_document_into_a_visual_framework_agent.py` and embedded as the fenced Python below (sha256 135628175770127e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_a_document_into_a_visual_framework_agent.py` first:

```bash
python3 turn_a_document_into_a_visual_framework_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_a_document_into_a_visual_framework_agent.py   # or on stdin
python3 turn_a_document_into_a_visual_framework_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn a document or deck into a visual framework — Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_a_document_into_a_visual_framework',
    "version": '2.0.1',
    "display_name": 'Turn a document or deck into a visual framework',
    "description": 'Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'integration', 'miro'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'turn-a-document-into-a-visual-framework',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74a9754863ab3617',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/visualize-concepts-and-frameworks'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-a-document-into-a-visual-framework', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.4, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class TurnADocumentIntoAVisualFramework(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnADocumentIntoAVisualFramework'
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
    print(TurnADocumentIntoAVisualFramework().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOj1pL2X9HUfLA9qi6BAIH6hiNegZCQEKsWEG5Hm+Ww74tYPP7vc5BU1faMPXM9MR9e2R0ScMh8cnsyD9SvL2ZT+1n58vnlCMx0sjXjOPBBOTFTZ8JkbVZG8CuLLPhvYmdpXQZWU2dl9fL64oDKLoO8DrIU3n4yIzBxQFqB10lbBnUN0vsNIK3vwuqmTCdBPQnSOpuYEzsGZjm5BVVjxpPaB5MamMnEhhBMu4bn4n4CUs/0wKQNan/y6f6VNfWkykHqBKl3v8l0a1CmWZZOSuCUZjuehzqsfuJDnW8QJOjMJI9B9fL5p59fXwL4++Xzry92bFbVCBqCWq0zu0kgzB1EtrrcEW1KMwGj8VBCbKYeXJr3UH8Kj3NQulmZwFMOcCfPo+8rELuvk3/7t6g1S6/64fOXdPL8fHkZ/1Ob9GFmZlY1cKCluWkFcVD3b5NV3Jp9BU0YfVRB51TQzan39rjzm6Qsn/w4Xvv+oeTNA/X3X14yCMEcg/Dl5YdJVkJ9ZTP+fhul5N//8BZnLSi//+GbnKqxQmDXozCI+u3r8/gpFi78tjRw71p/hFIf4bbAl5ffGTd+HrhHO+GdL29hFqTfPwTnZXYDqZna4Psf/kqs7QM7ioOq/qfk/vQQ7APTgTY9gf/wenfyz5Pp06APmX+tNodh/TuWwOXv6l4nT0f9ley7//+T6DhIQfXh8T8V92c3TH+c/PSXtv13N7xO3C8vaxAHN5gdVgw+T379epRZ5qfvnG8nv/v5Nyj6fxRzzJrSvkv4mphp4IKq/vr1p++q++nvfv7puyaHuQbr92tTxn8m88/8etfzBw8+V33/x3uh/nMapVmbTj4yffJrlv9L+dvb5GLGgfPtfPV58vt6GT/TyWjEu9KHC35XMxXE+js//vDyGySJFFrT2PfLsMr/9V8nQmCXWZW59eRojxwEA1wHCRjBn/ygmsD/x9ouAfRrFUDHPtfB/B8jPCLO3Mkv/8++E+on+0mos9Her+ZX50lAX0duhMcPVvzqvpPQL2+TExSflYEXpJAu1ZUsf0khN0JqharzElSgvEFSsfoafIJ09Gn8AZl28ss/qeHrXdhb3v9y5+rgwVUqsxt5qmpi8DbaqvmQ0x+WjUQNOmA3UE+c2RCUG0CWfYU+qLL4Bnlu9EsVBXE8cYISOiEr+7ts6LvPo7BffvnFMiv/S/ogVmzyaCbVDC74gDP59Ala58aB59dfUmD72eS7X3/7bvLvk//urrvwUYcMWf4ZGYhwf5TECay0uydg0GCYIY3cI/Prb08fQzEp7H4wjoEbgMfNMFMj4Lw7/MitPs2JxcQC0NHQyUmelfWj77xNdu7kAy9UOl4a+dzPqhr2xrFzgdTuoVQTmvPhyTSDbQ2mY+X2r5OmAnetv1ileYeYwJI3618mAiPD7pHBbpmNMO+L4M1ZGkD3f6TD4zwUUn5XTeh3EW8TcczNSW6WZu6X5lOHaz7iArvG++335pyC9ks69kowuupeKA/3wEXQM/YzpJ/GmMMmn0BWcKp33fc15tjjTvdeV36BM8GjCMxyDIUNmwJU6jWBM7aGfzxTqoLtPXbu/oNIR0nPKDjPqNxzcOzYEOF7Qo/QHUiI78ifA8VHYk++NHMExSf/P04nozmr7VZlt6sTu56w4km9Ptz8gew+m8EZYQJz7VFS3+aGd9Z5J98vaRzAnCn7fzxW3oPzXPMgtAbCgOSh3uXDzIBuHuXeE3dMxLIcU978kr6z/Ovo0ZHSoAmwymEVjMn3rnC8+o7Uh6U8Hn/r+PdAl87oXZick7yxYpg4LgCOZcJ41X45Ft8zPDCLwViIrR/Y/h+sgn6uy9Fh1SQbIwS/2vTuOjGDZkKPumWWfFsejHMUROE0NkQLJ1nwNtFg/Yw5VMGihcPQuAZ64bu7qEkCoI8hxA8PV76ZP8D8Ln/MZyx+7//npW/5fkcygocyTcesoSfbkYYd0D3i+oHyGSkINRkr9JEtfwj209LJ75vRP76kd4QfzA8LPx77+O9cAzO1TKp7To+8VUHuScAzfWAe3Fv226PrPtr6B5bP/2Xe//7vbQnuffT8x7h9nvh1nVefZ7NH73tvfW+QNWYwQ4IcVPc2+Mn89F7Tn8YihMeP8vv0Uct/EP/w1ufJ34P4BxHPzP48Qd+QN2S8dAhsMKbu8wM9wnyir5/w8eqXVAXfQg3VZwkkRvvOBbCi3/vQ+xLYjLwSeOPiR1+qxnbWwg56J2IYjC/pRzo8SwXyfOqNTbTKflfC94YMg/uI3Ue/gJfSGup2xmHOA+NeJx7hV+Dlc9rE8etLCv32T+5xxr4AkxY6ZNwdwfKB81EdgPuR2TjB6JXx9x+3fNL9hxmPFZaNPXZsAvV7XdwtcEoIbyxJLxhbwesEovYgY45GtWNZjpxqQSOrCuK779jqPh9hP/ZA4zz2Maz9VwT3yoaU5GSfxwJ/nYyD9evkY0Z+nbzvWu57wbSB27afxvl8tBkuhV8faz92tBZ4+flPYDzH9b8G8WSd17txpjW2g9HEP7EJSitB0cAm6ox4vhn4TW/2UPbbHWf92HD++vJOLM8oPYdLuBxW8KdqbKMzmMxQITx+pB289r8dO59iIB/CeQfKQTFiMadQkiBJBJ2TsE0DAgEY5jo2iliEi1MuAg8IG8Mpa2GTC9S1cJuwUdwmUcwcYT1y+Os4MgQjNIC4AFuic9vBFnOCwJcoOTeXjomTpukgFEUipOvAlvHt1gjS6dPeh32jMz8m4Hu+Psz+9cVa4HAlh1e71ePDzJYXc4YdLNE/THVkSl9nUwU752eksOpU56cFqPDG7hHzaHW1I3biMWcVf18EiUILpSXhRDRV99P2hB3cg8dAAj1GjXGT9LXYWCq3upbs7HZDtAutbjz8ZhIsz9dsWISwvM9qoBaNyi8ObUHJvViXutCJh10IE2XY6zhpOG531ahzHly04XxEEUOP7XxzbpRLaTgEHxTHwqy8HZWcRXZzrC9mcE53IZvFy6gt5apAlem5aOJDqKGXQpheHPVC8RofLdFbs9/YcZRHnbM5ZB0fWn1CLP2wUi8lSUcyXbhyWiILFzMWtkuw6WGKA/myPDCLthS3pR8NWeNfDtxhY5ptJR7LVNmesPV+WYSHBI0zsfWQtgoH1+wSMjwnSn4S+O0WrWn6ts6XHeDjIb/4lVXwnSvwXoapvZcRc8G3D4RWq4nKG2a/ncaJqm9Z9ERL82y59Qi0NEUdaU7uZkuc9vJGWFgb5hr3LdneNkQk+ZtD7vAbfz8txOMxIvcm1e/PWdzsF6Uho0MaexhVKJnZZv1axh0DWxsMxaer5Vzf5wGCkNvjFWNmSeIowhQVgkzDFmi8P/eORm4UTd+INramdkp13La6lWfytuKu9XHh7AM6zElnikon1OUNX7rUwfZyZJzduU+qnF+bS486LTWRmkthqtviRRxWlIDnDUWiBCUWRN9esRMOqu11J9TB1TWWse1tsfpmrLR9IRLKWnI4Iu6s8srTVE1x0E3IiTYiniJCylLhGFJKzDr19Q2qHGaBKetMxS3XmzrTdlS8LIDS4ChANxefXG+iWXLTz6jUlUV5PAXg5NN24sZze7Ov9ni01fsIzwbb6LnNHjtJyXboSbWLMN4pzqSCYJtpn15jwISAyUDnzQK6C4ljAPisPs28QZe6eDmVsQXb2myJnrKr1tmWBhKW7Yjc7KSwp3KpzY+Ezs8FreYiyb3tu+astdfOt9hc2q5VGt8IgQKKW0xjtESgQg4k5URgB2Yb9quEYTJrYNAi2Tb0xd4q3JS+iUQvcoS+73fzlnV25WG/bdjL6XyJjE0iaQayP/m9iHGeNJ/vkenuMgxDiPsY0scz2YuGlKD3U+c0NcUTboCwtJPAza7LtL2mhWvGeWoPlTAl8fQYqmEcSj025WYsaTJFgAxH6oYGwqK/EUIeLMFZSTZseCyNQZsraKq3OFuJG0vhjmiF02YbT5FBpiBllFOvyorVsFScWpElWjC2Bigu18WwRFqS32vM5nxzeFEUjIGYqTLUl7XakNMGuggximq3K7rQk3STI0pgTTP7RO3YDFs09WUzL287zNnTBo5I/T7eCZurBlR0qRxZXEOakiXOaZRjuKeHxmbXXWdw/pLOOHIudIK1Alo/bRMP0xYotUyRhBPE241jxJzZoGKRe7whmlLbcoEoRkGzi8N8EHyADvGOQZ1TZqg6aUl71pd3TUP0s2R+4qi2PhUoSxKNJTsgE2pD9NsZSuzO8eKq7z0jQfrk5mmWhDTMzTTmiw4gVukylscZVkcuZoBdXiXSkRmWsiKSP0peXRHHlbmTw70g3JwjN9vzgSjIKiH4frJCs8tZ2rmCbooYw2jriGTR5fRArvYERh9zuqP1YToL9hHhu6Uo6oRNiPH8WPpe5By9Uxr70LiruxBbmj2srskpFvwpl4s0e9uZq5pFHGtekHiv0Vq2Xon8jjkHl01zvKzs8qqv/V3VgiYYalGYG95RNtqL7Hdz9xAwEVfSt1JelXuNK4XUCBMqDRbd9SQFVbSYgpSYzwCHSrto2zJF3aENOtsTl+gi80m/u4lppqyrs8al2YmgzpS24izdBm1z2TCsKxO7WYMNp262XFqiTEj8aeiIKenJmwOemZGkXcRO4+j9Ctb08eyHhmycjdjIw4K47FJHMb1kugjMo6HaiNQOJqdeDu3K6y9eeaz7xb5HyMwroqtp5mEaOSotmWscUy+csTPZ2RU5c60GHO2iBOtobu6FwDlmiKrPZTw/GW2o5mSCdDYWsMfFOQlYGqcqO173WIOv9gXHRzQvxvomRHUrCqW4PNXiPDd7rRYVneTctaIphsa2YKENoUDgEjJ46Xw3EOyO0a950Z6dmXZpS4o8KO3pROd7MEhYh2BRgNsVUqcb5lQxHL8sd/zKFWgE27awb57BVpCXanKhDxTjqqJcW9xF2m1TzpxNm4uRHBcRoWQ8J5VShhx7ugLa2Y0NUbd1ehi02OINqj7zKEKrPbtVO9rnOuGwVYmePznGorqduuQwdzbFSWpvtXNJQc6cVjyX7EKdUXez7S1qet1B0SncjPRIJHiCBdjY1q8JW8cYWOVbpsKDjSh5+14cpoOopHtx7YaZmB83fb8MtLZSnSHmKfR0nGuxG0YVQlm6Mec7JmzoTKB9liAOtqTvqaNTBDMkDzphby0ideEiBk83/JrcoNPQFjIdkElEs+sKo7Pe3Z9irl41yVrhI7hPTXZ8ZR7kcFck7Z7ut7jqoQFXOsNCXYqBFm35tbyc+8sqk82IBN521dnU5cqdfepmGeVax4fkNC8zyKhF2J9ld+bKSFu6YSpQuZYyO2nJcNP8KrYWd/JxfDEAIwgWF1en9dxJ2+X1OJPSM7mdY+Zt2+mZ6rPhdY3c5iXhsLJK00pYivZgY5siTlfDnCY22IGV0EBxB7SfycMitLZstmZ8TWn1jdcnVnJRFtWU3oURUZJ2le/jvooAm+b7c57vRT9pgBnhNT+/xCkfw7l/q6BrPlkw3dnU4gaH/mSOBNnDEeim0BWrDqc2d1SNFDMrSKemwtZ7ECllQUfEvpaq6x76M9zhxolYZUcEjWKbHHYcwdJnOka5tcqty5B3N4rluFd/y22WCt6nu+GyjbZzZW8G64sLIqqgcCWb2fUt4U56tTHra8zkihXyVmFA8dNZ3xUrY7U97fh4Y9WblbRKtjDCosCYQ9t40xluEnsjPaHny6rISWU5JbQ1K/eayPFZLrQ7Za/dFoyqlMg2oS+puCobR5z3y+kqaXbyhkrbvT7lw65DM2W/4C6Uy0hM61S+U+A4lwcse7KbTbD0kr3In5sUXZWLpXd23QPntcgWRSKUKhKKCoXyXKM6wp4rVLCNa3qwnL1RUQcDzlMWuc8b8jTM55zdnJuqVsRQoDmXRRsHzi+BfKyYC4az5AIJkqwAN36j5LvCivi9W8XUol8EGyZfHvb4rXdOOs0vqpWUxRLDYbvCo7RAF/bbZHcq5Ti0qD3u7PbkIlYkWJXi/hJ1/tnbz5oTTNlKqdF8hitw3nZctA4tMKitamh9lQ4GIrZM5AnqHIanDo3DXF3UklZcW7qx0YuuIMzhouh8QcSkAlMZ9m1LyWtr0HDCVkydPc/N/kzIw3bNEBmJ7xxXXd7YZis12TFApA7H3EorRPrY3nDSswxCFKVzis3nx15Rk2Zq8xtOEp1kR2EaYQEZX6d4rR2kuW0ILFWv1f64s4ZgvS4Su3Hy9bIL0tOsN4k+POdLqo+xyCyETtUIlOqvSdAfmg2XLUy84fhdqFbbKgaza0i4jeM5oD5XczzeksTpBjjvFuyxBhWYtr2oO2yOSMuexKYxUGKsWVfkgsdA43AZBCMvHaUbmMiPnVnZGnlXsCKKbcDgmQdltprim25jNTAc3GE75VIDm/HySlCdw+UsWBx928kLdaWIwTxxOHaZ3YbVjKgZgeb99YHGYwdYy76y6U4tVi4BHIBvZivhSLYE3l6oU663F5QOPHJKSn1ZzY1tLchDITnogVaB00g0Jcsrbko6jkutxG1E6CwrDpxMXeT9bLs8D319s/KtPd+RK5au4EatLs6Ko+p4M/fG4UXHGIMrjZt3Y+VztIg5Xxz4kjkNHkSZyoKF7HCPymFMVdvuppZASTVh5LnTEPpJ7s5WJx97eZ1mstPR9WCsm2F6Rsk+5LbsnG/UzdHw06V8nLEHR5b7bnEdpjiDn8kZ6+qYfjZ89iiT5ApXh+rWNF5J9PiaPOwQ30P2g5dYQyTrDu0tMmt9tJYVukEQQlIlKXTtmzoLixuqzkoOA4K2N5ADVrE9sjrPr1KKITrnQphTFRlY61SBZr6qrqFQ8QgudLULILcuM6wgvLMOuGQ9pJw9iNjQbJBpG15V2g0MbZiLRrMLbSsR/EO4CRx/v1wfpIDwRDJOp0KoJixHe2vYMR1yi+8vZUFoZbDj82hxpT2rZiSX8VrQakhwBc5qKkSzdclpgJ/i03ZN4NtjnXWADdIui4hpQVPUVA5DaUc6HH7SGAqhGqdGmBTHWB9RjKhSCP4ikdG8bXh3XdJUUXIUlp0P3cISNHlG9VI0zwjg6h1PpKQcNucKmg8Odcqpx0GYC0YpNue1eVvfrtcoihS9rIV2OcuGmbV2LLqMlo3j2EJTHzlW0stTMl3DidWUAGUV0myNnYkZaJMLgpYLlggaxgRSV/uQ6+LNbX7hLOx0PUgediurojadoqxipBS8Dj1k12sYENiqRAyZXierKxNcZqqW1uSuDpwtvVlNu5C6SOGy8OnWXS8XKi83CYgWGEUQdQMnS1ahdqRrXZh2Ma3nA+a4JqI5xpJzD5oDNpsahBufpIL55WaiQx9c2oEyM+4WYuaMtNlbsHbiLgdVmcb9BQFyc9HNpX5DZAz2M4k8TFujwUkdOShS4G2p67lbiYAtRA2T4TCyHOw1Uyz9bZhpt2ZZ9NERJbt8scl3e++cH/DGvYW+Hm1YEZKyM53662Xrpgmcd5NmqR07l5c3znbQaOWsquRNWq0zZ+6u1tRtcWbts4URKlqwgn8uDoDWd8b45ArMGzxytu0BPQqV53DLSK4oR9mREtdR5013Ypd4TA70sGK61ndpJDtGrT/YsDJ25FIzjshCGOi5dvSU6YXU1kePODTwLDfMdlpYSkJaKnoUYK0zp/LVcTHUSN7qLWMuS26fg7qtveVQkY4VSRfMggzOyTotWDOeucDOQWuY6kb6Cjmgpd0h83CBIR2ZOEJDE+26JrahNvdqfr1WndhnWqRzApyhFrlApvaUQmbegUas6mZnZBiJB/ES2E1zxblZu0WBaBPg6K1Wqx9/fHl9GR8rPx8O/933w+ODuP+z54GPR3fvL4zuT2aB6Xy+6/r8t5H9/PpS2sGI6/4EtIob7/mg8D89//z0T75vGIX0jxew41uurn5/sF6b3vj3RC9B6sCRpOy/Vlnc3B/Evr5YTTX+YUM1/u2LDb9f7iYm+fh4Oat9UMLvO+7EHF/ZjvrHu4AXjK84X8a/PqiB93wc/PqSBGU2WvZ8VwENmr8hb+jLb/8BjWYfVbklAAA= -->
