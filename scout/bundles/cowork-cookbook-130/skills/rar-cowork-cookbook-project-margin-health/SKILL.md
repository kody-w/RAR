---
name: "rar-cowork-cookbook-project-margin-health"
description: "Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/project_margin_health", "rar_sha256": "cec496cab5bf24f829348c6d5d3bbe968eda6cc0e20ae6da245c2d07efdc9051", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "project_margin_health_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/project-margin-health:b89c05e4bea20d13afd6ca6434d4eb0c71b3a4f77d93c09f58f370bbbe2557f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/project_margin_health`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `project_margin_health_agent.py` is
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

Project Margin Health Report — Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/project-margin-health
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_margin_health_agent.py` and embedded as the fenced Python below (sha256 cec496cab5bf24f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_margin_health_agent.py` first:

```bash
python3 project_margin_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 project_margin_health_agent.py   # or on stdin
python3 project_margin_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project Margin Health Report — Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/project-margin-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/project_margin_health',
    "version": '2.0.0',
    "display_name": 'Project Margin Health Report',
    "description": 'Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'project-margin-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/project-margin-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e8787a0e5d49d105',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/project-margin-health', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ProjectMarginHealth(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProjectMarginHealth'
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
    print(ProjectMarginHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZObyLrmX2Hqfujui10gdnyiIwYEEps2BAip3WGzJAixikUS9PR/n0RSle17u8+5J2I+jByuQpDvvjxvJvXHi9e1x7J++fSyBV6BzL0sS46gRrwiRKbltaxT+KtMffgfCcqirRO/a8u6efnwEoImqJOqTcoCkk/LvPJq0CBVXZ5A0CJ+F8agRdoS8YK287IG8XvIommRwGtBXNb9ByTKvPidokGuSXtEcq+OkwIBddlAzh/umoS1F8HnIPcSyAeybI/gXVDuFV4M6gYpI6QG4Tu7V6gjuHl5lYHm5dNvv394SeD1y6c/XoLMa+Ctl/Vj5eIuUQFe1h4hTeYVMXxY9dAxBfxegToq6xzeCkGEPL/93IAs+oD853+mV0jd/PLpc4E8P59fxn9mV9y1bEuvaaFWgVd5fpIlbf+KCNnV6xuobNvVRYN4SAP9WsSvD8pvnMoK+XV89vNDyCv058+fX0qogjd6/fPLL0hZQ3l1N16/jlyqn395zcorqH/+5RufpvPvnoLMoNavX57fn2zhwm9Lk+gu9VfI9RFfH3x++c648fPQe7QTUr68nsqk+PnBGLr+AgqvCMDPv/wd2+AIgjRLmvZ/xPe3B+Mj8EJo01PxXz7cnfw7gj4Neuf592IrGNZ/xxK4/E3cB+TpqL/jfff/f2GdJQUshjeP/yW7vyJAf0V++1vb/hkBLKbPLxLIkgvMDj8Dn5A/vmzX8vS3n8JvN3/6/U/I+l+y2ZZdHdw5fIHFlUSgab98+e2n5n77p99/+6mrYK4BL//S1dlf8fwrv97l/ODB56qff6SF8u0iLcprgbxnOvJHWf2v+s9XxPGyJPx2v/mEfF8v4wdFRiPehD5c8F3NNFDX7/z4y8ufsC0U0JouuD+GVf4f/4EskgC2nzJqkW1Qdi0CA9wmORiVt45Jg1jPov661VXDeM3Drwi8O5Y7bBFel7XIvIat6q0VjRbA5vT1fwf3jvoxeHZU7Pn8y6PnjVkOW9DXV8Q6QlllncCbXoaYwnqNwBZXtKOUez40Xf7xMgqCSiSPRmNO1bHJNF0G/oF8/UvOX+5MXqt+VPdzAf3vwaCESAvyqqy9Osl6xBv7kd+34CPsnbBn1GWW+V6QIuOPrnodfbA7guLpmQCCBriBoGsBkpUB1DZKYL/9AIPblNkF9r/RX02aZBkSJjVUCTb+e0+HPv00Mvv69avvNcfPxaPhksgDVRoMLnhXGPn4sapBlCXxsf1cgOBYIj/98edPyP9B/hnVnfkoYw37/d1JMGkzRNuulgj0S5fDZQ0yhh+2l3uE/vjz4f1RuwLCIKybJErAnRhy+xbu0YJHSN7iAW0eVRyB6C7pR78h1yP0C5K00FuwlpsPn4uRRQmX1tekAW9OfBA/XP8W4IecMSbN04cwTlFd5ve190wbgxmUdfiKqBHy7iloLoxrO0b0OAJvCCpQhKAIekjptd9CWJQt0sD6aCIIyl0DTR05f/Uh69E5OWxCXvsVWUzXEM/KbETg+olvkLoskjHwzwx93IZM6p9gjolvLF6RJYDeROCQ4FXH2mvAfV3kPTIC4tgb/TgxIAW4IiNcgzFG98q9Z94TsZEHZCMPzEbMu5nI547AJxTy/+EkMqouzOemPBcsWULkpWXuH3k2zlSj2Y8xDE4HCJwuHkXzbWJ4ay5vbfdzkSUwNnX/j8fK6J5ajzWPVtaN4k3BvPMfi7y+801amCCj2XU9JrX3uXjr79C6MdlHQ8c6TseuUL4LHJ++aXqExTp+/4b1yCP3Rv/ArEaqzs+SAIkACO8F0B7rsbye0YHZAkb/wHoIjj9YhUDuMBMgfwQqkUAvQwy4u24JywTOR4+cf1+ejBMU1CLsAqgtrCPwiuzGtIapCUMM4Bg0roFe+OnOCskB9DFU8d3DzdGrHsqMc+5TQe8Zi+/9/3wEE3SEESjtvfogTy/0WujJKwwBLK7bI67vWj4jBVXNx0q4E/0Y7KelyPcw9I+xAqGG37o+HMxHBP/ONbBt13lzz0qIrWkDazwHz/SBeXAH69cH3j4A/V2XT/9ttP/535v+7whq/xi3T8ixbavmE4Y9UO4N5F6DMsdghiQVaN4A7+OjtD4+YOkHZg/ffEL+PYV+YPHM40/I5BV/xcdHRhKAMVGfH2j/9KO4/0iNTz8XJvgWWCi+zGG/Gf3dj33iDVfelkBwiWsQj4sfONOM8HSFiHhvb3eceA/+szBg9yziERSb8ruCHW0aQ/mI1Hsbho+KscGH49AWg3EXk43qN+DlU9Fl2YeXwsvB3+5exv4KkxK6YNzpQH/DyadNwP2b14XJ6Ifx+sfd2+p+4WVjBZUjSobNiFXPvL/rHNZQobHkYohfoP6AQD1j2CVHM65j2Y2jgA/NaiAYgnDUu+2rUdHH7mactN7HsP+uwb1yYcsJy09jAUMwhSPzB+R9+v2AvO1H7vu6ooMbst/GyXu0GS6Fv97Xvm9OffDy+1+o8RzE/16JZ1d5tHzPH1FyNPEvbILcanDuICqHoz7fDPwmt3wI+/OuZ/vYSv7x8tY4xuvHiPBIp3Hn+U9nt9HQN8z9MnLzRpr7hHW3+z5/fvFg0Eds/e5RPA4KXx4p+fIJthrw4QUSwwkHDtXDfY/88lAB6v5tcoUcYNP42IyzAgYrCnKCCF6Neqew4X0nYLydhPf148Wnvxt3f6z+Tz7HBzgNKB94BB5OSC8KmcBjKJIKKeDjATvxSY+KWDbkyQDnI5qLSBb3fR8QNM1GNJTcwNDn3lMyNhl9DXV+d+j/bO5+eRBBUCBoBlIFIKB4qIlP+xFBRRzBkxQXMCEdklA2z3Ag9JggwAGBe4AJPYKiAyLEWRCFAY/Tk5Hfcwh8aPLlbeB+8/6j8r/ABpkno56E5wUctJcKeRayBiTukwGYEJOQJQFO82TEcYCC9O+kzwiMAXoYOyYknP/g9HUZ5fzxjOiYZAwFVypUowqPzxTjHY/dsb559PmaAXs6YjakfLbTwWydSXph6mo1P4tLoQesCWTdVctg6ywtRT1It2y/FEhCXefz6LBA+QW+3Garnuj65CqFxnyWRx254Ifhhp+nqiEyEwNTtaUeiYSr0zvDIHaBs2tv6qYNnU53C5LaHcjKuuk2XhZCPSN3TFrtylZNrHNJDert4Ke7o5Vstx0tn12Cne0Pl/mZ2ClyuzcWJ2siZnA2Lfb8rNCDxACLDOLpsp4KinruJr7Aejcl59KzbYIk03PLT66NEvOLnZFgC7cisPXlJhU1T4NIBHrLJ3vG6Ldg6yZdVtd25vhNuMnMaSlN9hVVWgYjGZipu87xnBnzHJ/ns9wJ/Ao7HO3O2fqcPCXO++08jIoZc0Vnp6zJt7dzXM+2rE4b4o6Tr2hcZ5Vuc3LPmfT5iicmAzZ6R8z3a4oB4ES6jVNY7CA1l2A4rbX5dcHPsm1NHaj1kkm9TDZ0ZzEjZ714wGMV7EpaOru0FtWtXe9W2F7dThlSm7WCsHEvTNcEBoSQvYOictNuYdRnjbG1VxLaymhCZ2d7cfOjuhO1rNiurot27baCn0uTfEPIJ2p5xPHTya07Y+oxa1139l2IsQ1acbwrn2npeDZ3Yqgerp2Kw0Xi0u1BhRnzW62YQ2nP9UQTg2Nnk0BgUFbyxbhdLTluXotZLw5sTszDw0UW9zsSVbfV3r/2+f4cDXpiuGCrwWZkdF2PW9MDrnOUyfnmbl+Kg49bq64WI8oqh6AfGttQdCVeH/y9ixtHo90ldWFWp0QaCrYz8zKbOKaTLys8v0izG8ppss/4qjhx1AW5o9fsbLacZUPuHrKdHy1uK96q+otIg9tiLZzXV2LBoXaZpYWxxfZKe6DX6wvdckcVSFM+n8t4VFvOteIuq911IaTVtjwvMMeA/Xqidzt9lgbBzFzsdsymU7rlJrjk8dRP63i+Cem+rW7lcVb1rAaTNpZMYZqjgJFjb83FlVJd68SJj4EwF3xTm1/6abzVUI3YyHtZy9JTvtcP08WZ0qdeMxw3O5FYs2uVI+UUVQo+iy3likfCJplTimrmUhmeiggPfIWWSAx41SINXL+XW346J/x1aDADV7BrzoxqpliuHKPniV1ITnhxC3pU0Q3C40xsfsvDyc6igmk/T/hS8FVCC+bMNELTATPiSr+cq1BiT8MQXzPPc7acHZ2r69nV97pxmWM1PTWswmNM27T3Z7VQBnR5mKULGqcyFlf7c70q7CgNFYFtkm2ZEa4guwnhWGtysGumnnmq00dXPrcOlzirVGHWg3IWbWhuVmQKa5m7m73PmySQL5ieUSS7FWyM9Hg1LZ3+rDBLtBRCR95pB8tnd6suqOib6830whCWB32+CIvKJ8z9xaqOC1s0tJlt+ZoqLUyP6LOV0B9dx2GmZyW5sjqBn/t5KNjLE43t+ENPSszA9MvZifJ471h3NbbI8LQLhP5SL86rmcSIeUivSYvY9iB1WSk1qqtJYFE7lTjltjnEQaUUu018DDPROM1BM5PYvVKkNspEB7Tw9FhVY6diZoGkdvZGTfj9hDpwqoCthsYqyGsaXI87n9G2A4V2ro+v8xXL1kEOACMN/lCJ7l7eedT05NIbb8JNV8LVD2+z49JtG+qw72vdPPBN1eWoZQPCX6iW0E5X5tEUszMjen69l3PiVhz3O2E6zUzNyL3tXjvZ5knvVYKVzUbcKpM4WWbxTKjFiWQ19ESF+6ODmw7apMtcg8NWLgux7SqeZvMhxIpwu7X3DokeAx/bp8oiThdFfZ5QATZfSba7BdduEIX5VsUwYFkWqp1Qy+KZOVaV6KowMiWozlPRWdK0Tc50QXVjs69cb70IanuxnZ3rzE6ciZMTSkOS8TA3cAtKl/1tMisiDl2tNS5ca1QP8H22dGfLXjVWiWo4YpdUIdtouOBPA7k9evg0XJ3s7qJLeqqgon7mF5aIGv1wyuoZtXOsUM8alFkF6BTMDA3YOSeuZ7k8aJgBfXCeDMGCr439bIKffJc+T42dZgdxQBDl+qK7dbN0p0rnaAfzVEfScSlvcnROCqwMW+SF0Kwhx828XTMBceYmk+HScsV+v6DbTOT0Qd4LmOmAqlt3my7GWHRONcpxetxCtCA8TMvlle6RssZziqou95Nd6BCX0yVqqYSJ0YlNK5PBm3oVNY01LJmCM6/Z6XVLH6yC6ibn3e6qy4udNAsZenYKZD2aokV5CvtD0eyxjLLsubXlLQxX8J0mpUo+7zYnagHiY6dn/UplLP6wUk6aXzK4rcfLIpqtnXOoJUxR6I5x0wQJTgryxPZjnXO7bnEqj+ZpOAlboKGWuSWKTewuyj3aOIlwjtPVxV8dDmUpo1WnhVdC2/Jed7Z8dH9k8dbTM5Cl2lGXzIlXqbOV0y3Eo8CoA7nIY2bVkkfZ1lqg+FghUUxlc3O5zHaxYiZ906R0IxXzVqTdyoPBSraSvWX3oR9byRmORJVdN9OjiR/y7XWjRm4dUGvT7GgfxTV945TiFR8wVrp1wprIiwunCFqKZoK1V4HVUHx3gLORZs1wZ74YwhmzbC4WjzL4gbipzY6SClk5ZHuSTGQ6zP1dsAuu7q6/8f6iLnZUMZmsVvvcnOjV5ML3BzcOUme1UQHvnUNuAztWthWaJX0d9qtrGho6pSSqM432xyPlSmeVrDls7cFR6pY4am4HWc+uqp2WV7utlE4prnFOg2RPCm+XKOK2Ly+xlx7FAm8n2Q2Wl+TKVdlTZ5Gh7JOGCtPEHay0wN0+z6LJIVWaYlh5uROega2FWWVhrerZyQJ3zlvxImsbGVNFTRC6PImpw2QilFvcxTP0SksVHHVtfWkSe7xZyufmotudjvceWszlUze5LSnCKft8VsrMLRQ6d3vL0ANzOJqTkjOOzm3W39L6vCkaCE5cybRs7NLUxFjggjpcbQ70k4bqBcVP+ukNF4wKI6/zG7ukymu3PW2cAK+VgNjQUjA/bLcrY8uqgcDU/cxJp7xZNbtKiix1Mu/7swfSeXtcWAO76aZUBGdB346NdMtucI1opyQ1vUyofdgc8PKkqMxyZy96L9nD3QJJrE6qfD665NVd4hSl3qwlM5h1nzKqpVi2dttuU3VCSx27WjoLvi/JbLpIo5xkdS0i8vQCrvOYYDbEbHCYQjXAAOcAc81Zq+1KHfKV7Mq5rZVT0sxkaaCKW10zabqTN6WbsFobBnLFXIXutKI0jhsYydG15rZnzNmhQXfSBVMq3C7K/CCw8y1q7uppmAqbFXU5mYcDnOWyS3tBhcVxrUCjATtVqtW0OMj9xchMZalshZmknddD7lfB7TypTl6GCiZ/dbIQbKh1Ipbzc561Us7Hzm6Pp9aePOGHvoqrs1Kifloxvs550sIInLmXLwl6tuhDmfa32o0p/NNpIlaSey7N7tbap74bcuncnyeo2GTFIG7goGI0RClV/o6Xu32/voJFEbQNcdAKoGQnfAMBaqU4qtTw5JzcW/vkJrLSoJ1XtFjruLzpZGlzRFf5JjztRBqOO/7aVXEdFax6f7XK8Mx37TEO7HnMdt6EIFcUuXRv5YRrPPZEduRmSRjn4BIesTU6VARbLtn5UK/RdbnvptHmtsKWDEdfmSlPiN6GThZLOorhzLdMWtb1ZSk2ImloMmw2lZhJHrAqsQQCulLC9bTMQXlwHWJ93vhX7OoHN06TVlTnAp+ko4CMY1ltvSVaDzUeR6mUkHu57FZdmunoYh5H+JUnDyAEua+SWcksrxqWtWHH5ByvCHhYRdGF0iJuZjWlwVwu5MTC5qSNlp2uMo2bEadCJgpaTSW3SdvWm5nU0pvy82VgVCdeJA9z6sALF3oVm6QU3SbZMlDn8ckbrvKiVWQlk5XtRj2lun4YZIZo8zwr/MKfYnJlW0O/Iq0NwCRlc/MXxJXt6CFXgL0/4ukNpbb2bnPABnZHHRyNJjbrBj0QBQ5SLL4wdM+Jl/1lC8hekUAI95b9jGzcaVRh89KUFvQ1FNl+fSEEobW16rRGOyY5bIMC7hzNSxeVkea6XIkuT4N9Ogkdc7mR4uImzrBOykJuZpJkSERBuBSnBGtbl9iYqg077bph6u+Mph4iL/JCi5KtlolhiYfdrluvgSMp4nITw70h6S9j40TZGdcKyazd3+R5MiFnq5tyuw6Y70YtnOqFZb3TGGbK2a1tc4VzU9ap4Bji1RoICY6tgbCYhUKuFPbimLhc0oQMdaIHvlSGjdz64hnVgHQ0NR5zbxxYK1R49BQubmdUSTdGaB+0qKFOcSyJVixsLo6rXeK9zSvA5525wndXN8txNKrY0yTjZtWmXHCXPiFSQijCKkyMnLJoFKQ2oREHaxqF9KoHwe56owpdXOWTfrCCIeK59QRXuoGhyTAl2Znqb6rBRHlqapKnG6ufilqhhGi4TJjdJBDzqPWIGGDzcHlblsc5V84uO+IU5od2WVhzYkY4Ox7gM2LKuvlmz2QQu8VbyMItM4eJQl40EH3Y8mL1fLXDWzM+bNb7PeZpu/U8mSkwQSP9YPIOS6SwfSo1ROeWi5VK8dkk9uYsQfqRJ/Mee5i4zIbrFih2ET0eUwRXIVsfpUuFN85Td7K+1qHU8QNJVdE8v67MmUPYnLpMjXIXcFJHztdRHF3IZsN3Dh9D5HcvZyA4isBT1woTDqQVLA8B46aXwrku9Ashe6ujhx1WtSw1OjYvyl3RnVp2cttwKDHv1HyJbhjQuxsWTCs+m1wkd2Xs95ckiuenYI8auOqiQx9fGblVrhLm95mYr7Kaaq6hlJNatkLJIhuYqO1a91R3N5lvpnx6MjTWhPsIdlXb09Vw5MKZGOC3JWqF9JGOxT0lsEdGNqy9QEVmZmWwnSwr/aAc4F5HE4LIay+g2gQZGbSe1Na9sAgPYobiGXVtOSW8KLHccdcgI3ROGKJ6f1i0k9USVbqokJTcohUHpUVvga5WB3flzYyUVRLnGGK6PS+xo1PoOY4t2QWgC8uPwUJggRaTl9LYxlfb3XObZrlyD6JwWWRGZoPt9JZx+FwkmFpK9ciU4faHb1YmvsTipZ2pN223jQVB+PXXlw8v95epL58mOEnwH17G4/jnofq/PHuNh6T68iQnGQpS/787MHwc3r29VrufbwMv/HSX/ulfaPb7h5c6SKAWjyPaJuvi58Hgfzn8/PiXp7AjSf941Tu+57u1by8bWi++nwwnRdg1MMhfmjLr7ufC0ItdM/5RRzP+3U8Af7/c1c+r8QD+8er55f0k+UtbjsuiZLyXFOO7KxAmXgueX+PnufmHl7CHsUiC5gvJ0F9AXY2mPV/pjGek4zudlz//L8UbsdW5JgAA -->
