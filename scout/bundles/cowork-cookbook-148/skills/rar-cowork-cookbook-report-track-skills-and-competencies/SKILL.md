---
name: "rar-cowork-cookbook-report-track-skills-and-competencies"
description: "Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_skills_and_competencies", "rar_sha256": "1f43b1d9a3c679d631cc4e1a3c94a32a68f89f04b96600ea41c040e5b5485b18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_skills_and_competencies`. The original RAPP
agent is preserved byte-for-byte in `report_track_skills_and_competencies_agent.py` and in the RCI capsule.

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

Track skills and competencies Summary Report — Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-skills-and-competencies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 1f43b1d9a3c679d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_skills_and_competencies_agent.py` first:

```bash
python3 report_track_skills_and_competencies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_skills_and_competencies_agent.py   # or on stdin
python3 report_track_skills_and_competencies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track skills and competencies Summary Report — Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-skills-and-competencies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_skills_and_competencies',
    "version": '2.0.0',
    "display_name": 'Track skills and competencies Summary Report',
    "description": 'Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-track-skills-and-competencies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-skills-and-competencies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7fd32993af6a78b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/track-skills-and-competencies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-track-skills-and-competencies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTrackSkillsAndCompetencies(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackSkillsAndCompetencies'
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
    print(ReportTrackSkillsAndCompetencies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+bOi2Lbmv0Kf90NmPTOPzGLeuBGNIAKCyqRIZUUWMyjjZlKr63/vjXpOZr1XdftWR0ebgyKbNXxrrW+tDf724nZtUoKXLy9G6BbIys2yNAkB4hYBwpVDCc7wrTx78B/il0ULUq9rS9C8fHoJwsYHadWmZQEvX3RpFjSIizQt6Py2A2GANF2eu+CKgLAqQYuUEdIC1z8jzTnNsuauwy/zKmzDwk9D+IXfpn3aXpEhbROkLVs3az7Ba8IigO/jcg+E7jkoh6J5hRaEFzevsrB5+fLzL59eUvj55ctvL37mNvCrF/2u1Rw1GneFbBFwP6iDAjK3iOHK6goxKOBxFYKoBDn8Kggj5Hn0sQmz6BPyn/95HlwQNz99+Vogz9fXl/GP3hVIm4TQYLdpodu+W7lemkFHXhE2G9xrAxGAiBRPeNIifn1c+V1SWSH/HM99fCh5jcP249eXEprgjgB/ffkJKQHUB7rx8+sopfr402tWDiH4+NN3OU3nnUK/HYVBq1+/PY+fYuHC70vT6K71n1DqI5Re+PXlB+fG18Pu0U945cvrqUyLjw/BFSj7sHALP/z401+J9ZPQP2dp0/5bcn9+CE5CN4A+PQ3/6dMd5F+QydOhd5l/rbaCYf07nsDlb+o+IU+g/kr2Hf//IjpLC5i8b4j/qbg/u2DyT+Tnv/TtX13wCYm+vvBhlvYwO7ws/IL89s3YLbmfPwTfv/zwy+9Q9P9RjFF2wL9L+Ja7RRqFTfvt288fmvvXH375+UNXwVwL3fxbB7I/k/lnuN71/AHB56qPf7wW6reKcwHLGXnPdOS3svof4PdXZO9mafD9++YL8mO9jK8JMjrxpvQBwQ8100Bbf8Dxp5ffIUcUD3oaT8Mq/4//QNTUB2VTRi1i+GXXIjDAbZqHo/FmkjYI/DvWNgghrk0KgX2ug/k/Rni0GPLar//Tv5PlZ/9JltMH5327E963B+F9gwz27UfC+/UVMaHsEqRxWrgZorO73dfCjcOiHfVWIGxC0ENG8a5t+Bly0efxA5IWyK//jvhvd0mv1fXXO3emD5bSOWlkqKbLwtfRy0MSFk+ffNgBwkvod1BJVvrQoiiF9PoJet+UWQ8ZbkTkrg0JUgDdLyG7j7Ihal9GYb/++qvnNsnX4kGpBPJoEc0ULng3B/n8GboWZWmctF+L0E9K5MNvv39A/hfyr666Cx917CC9P2MCLZSN7QaBNdblcBkMFwwwJJB7TH77/QkwFFPAngYjmEZjnxkvhjl6DoM3tA2R/YxTNOKFEGWIcD6iC3kaSdtXRIqQd3ufvWxk8qRsWiQIK9idIN5XKNWF7rwjWZQt0sBEbKLrJ6RrwrvWXz3g3k3MYbG77a+Iyu1g3ygz+N9o5n0RvLgsUgj/ey48vodCwIcGWbyJeEU2Y1YilQvcKgHuU0fkPuIC+8Xb5VC4ixTh8LUYm2Q4QnUvkQc8cBFExn+G9PMY87EvQz4Imjfd9zXu2N3Me5cDX4vmmf4uGEPhw3YAlcZdGoxN4R/PlGqSssuCO37Q0lHSMwrBMyr3HDT/5VhgPMeIR0NHvnY4ipHI//eBYzSUXa305Yo1lzyy3Jj68QHgOBiNQD9mqVEezKJHsXyfBd6Y5I1QvxZZCrMBXP/xWHmH/bnmB5d0Vr/LhzGHAI5y7yk5phgAdx++Fm/MDU1G7jQFowLrF+b3mFZvCsezb5YmsEjH4+9d/B5CEIxOw7RDqs7LYEpEYRh4I4JtAsayemIP8zMc0R2S1E/+4BUCpcMAQPkINCKFhQKxu0O3KaGbsKIiUObfl6fjbAStCDofWgsnz/AVOcDKGLOjgeUIB5xxDUThw10UkocQY2jiO8JN4lYPY8Zh9Wmg+4zFj/g/T33P5Lslo/FQphu4LURyGNk1CC+PuL5b+YwUNDUfa+9+0R+D/fQU+bHB/ONrcbfwndBhSWdjb/4BGgSWUv7IzJGRGsgqefhMH5gH9zb8+uikj1b9bsuX/zaff/x7I/y9N1p/jNsXJGnbqvkynT762Vs7e4VlA1uan1Zh82xtn++l9flRWp+hss8/ltYfZD+g+oL8Pfv+IOKZ1l8Q7BV9RcdTSuqHY94+XxAO7vPi+Jkcz34t9PB7nKH6Mod8N8J/hb30vb28LYE9JgZhPC5+tJtm7FIDbIx3foWR+Fq858KzTiB9F/HYG5vyh/q991kY2Ufg3tsAPFW0UHcwTmdxOO5dstH8Jnz5UnRZ9umlcPPw39uzjGwPExbiMW52YOnAeacdT8EjtwvSEZTx8x+3Z9v7Bzcbq6scO+dI7e9cencgANC6sRzjdCT4Twg0Ooa0OPo0jCU5jgce9LGBNBsGoxPttRqtfuxpxvnqffj67xbcqxrSUVB+GYv7EzIOyp+Q95n3E/K2C7lv7YoObsN+Huft0We4FL69r33ffXrhyy9/YsZz/P5rI56M8+B41xs71ejin/gEpYGw7mBrDEZ7vjv4XW/5UPb73c72sYH87eWNVJ5Reg6LcDms3s/N2BynMJehQnj8yDp47v9qjHzKgEQIRxgoBItIwsOCuUv49Gwe0ATm+2SIwcM56RK4SzMRM49Q0pvTNIqGLon5KImGlEeRDOVhDJT3yN9RS56OduGu6zP+DCOD+cyl/ZBAPcIPMRwLZkSIUnMiYpiQhBC9X3qGPPp09uHciOT7RHtP1ofPv714NAlXimQjsY8XN53v3SmheJtEmdjoZHGcTjRiX1l5e8X2k/3VYgLMr7IKJa9Bh85EzGM1zsrLtSMttE1Dn/CIXooEt2uyeTewVVqtAyqnaJXBydYa2JSxJ5Od41nC0uID0s335DqkixvBVo7DSe2e2l/rc4o13Zqxa/x8ODa3vWOv0v18Oj1bDCAO4dGth1trVDVJrBOWME/y/HAr9zNrfVELb2Z4Kd61+2a9v9UOft02lnVYETd97lQGc1MBGBqXHyJRyfCwUMhpVBRkZmaT6S5qJkI+sblEUq7ihsNyyllVEq6Q2GDgmLBOGwq9necDxmzPk2ZNpzW16nTaqfnaus0voNjtzW3uU5MbeVL3im2c+CM4KBejEQffG1gNHoUp1cSzOk3bDHCkcnaiSt67s6bFt3rSzLO51NHhdJ0JYX1eHurjeoJuFucglPhibtzs2olB5hNSuCJlTi+8nosVfe/O7a5CO9sKWf887Faasl6zQZShtropwLLzgZDL3bXd5+qZXAvU+Vpju7Lb66tLuJ5VtslhkrVXqYON3TTxcplcJUUwmhWKuywGsplyzSszP2cHc4ioIJ/vbslRqSpVxQGrVPxqeT2j5Bbk4k3KVIIoJ23QLDFLXAoD0RUe3xAFOwG9t4mDXYsOMpAXQX6MnGnhxy7hdUNS8BIQSZdSUro9yEcguJIQpXNwvoKjKSW3aRvXarIsZH2KVtzQO9NkJ8oDOBxTG18qfJheLzvS9r3IaIL6cEkonrrh2M70TaPzq+2l21oC7ST2cViuDDUM1naDbyM9lTclBf8lCrYiDLNOe+eQl/EOpUkgHc1BFwd3R5bRMdRBYZRrNGJ31Sl2dtF8Ml/5Kt/MrAvoj112kSumaNyb4HFU49rmeebVx7MPloN7XplLwjVORnOeJgqPyxqjruKTtNX5rjIFLV7K3iaTrVu53QbmjCPILm0lOaVF7hi2qjYfuKi8sm6pnl1dQg1fu/lmF2uohtvGGi/LXDqtr/XSbW6XMj9Jt3l4lW2O3i2UGdXqJHWLz5IWnItUlDdsQZvVeSVpS4ta+xfcVKkizz3HVoJAbphUlHCm0ghwWUx7JkgvzTxSOZ1LmIPfYLR88Q/1dbIapKV7rRnzMDli4qElZcm94bFMAgtl90Y2QW8bxhYO212VxUtT8N1aNfZXZ7W1r6k8q+O9EDo6iLHoymiJJQxt6V2CQ23K1HQu71f56kzzu7TIFbS+VckGw4BJ93WTSXu4a9jK5kCuQddwplPK+gwH5XGx2dsbcVHVBL9OTkZO1aGOzQ1Kwgq0A1aFqlZVkGcCGIKkH6dJXevOonZIkVpyKZuZq0NM2I7AocUtE9Q1p6+XwOCU6SZt/dw123mSbJYSXsm+pth25/hkWcQxqdK7QokpeZieV5SNGmE0IbZHovBQvD2dnFNU0KmKT0pgabDIKYDWS3tTtDmWwp2DNo0dItCP1HRJ9QcO69GDtUEBuSNmUZx0szmexpc8Ck4cL08Oy8vG82pVjHehetaYKazg+XmtXAbVywZcHVZBXSa6TF/oFJM1x/AL6VQQQ9ssAZuS8xNFtbaXi5luUTgVl9O1lM13S3HPlgsl4Wkn3Z/TfTRspbxQdsfavK2kBW9lbGpVrdau8L2XdoRzQTe+xs5dy9L1ysJCIXHAsQhDVVX4gdaOCc/pzhFoKdCLxNqK4tHvJE4LG3fboFyva1zP+PnhyIS3Xr5uaPd2AtgkgEQ82eEEe8FrP4iIyDAsx2xpS/cK9+yxRbM9aSTuTKayKpxgOohKs1kmWlIwk5tMTqaT7VouRCbfTadgJjXaeiXomCq1YHa5iAuFXW9S/ZwUbs/yzJqU1ztnClqVXPjOJrBVNOPyxvTZHM3Lk02u4+MhOGwLudaoBLsIjqyhM+0Qw+InF0LSsAEx9MUyWx9uGl0qiy162pMk1y6Z2ZlO8Jl85vcXi8WEVXaTr9yS59ed5w+Ut/dOyXR7NfJZlkuVa4GFv5HazUHUgNFv8zOKudmWPOczmWhvBxoEC7bTjysV3/HMuVpHFwuUjm80mhZUxSW35r1V7Wf+TTv0XhwYtcd5An7cWav2KnCSKPgN2ifJYj4EqRYs3Y0C7IicrPYbaRXVkgE7oJy4C0voQi80/c1RnC2dzUTlBNEDyqxLzoUWmuySsRTPHbzqGOMmdgsxv244Y71leX1TOf3eVTOW1zqOdZu877yEoupYwsLEruXQ1ao5pyh2yZU6T26ENPPTjDjoSqkyF7GW1cysxJ15JTYHR2kO5NHcn3yH5OL1+oRKnUD0An0IXTSxjNWxVGM4dM2aANsot8xEEyGBETvtOEtxaKeTJXsStMYxaYzsinHLA9Fc3Gm1Quf6dRabDTEB9d7Qt/7NP/LcAh3yxtHj3W3Ws9tyH6hLeWqW+IaG7kigqWVvzkawUAJKaoyjWNW8UCpZpwXN/jy4zrK0iK0uL2p1vTxvgQoKf8HXk2ylwO7sdZGxqxoNZedXP+rQbVvxU2+jEnx8nITCIE8kUdlcsQJQO1QGe2wf7pe+n/HElDhNVlg5STJJrRZZuunN2dFbLdXVBQvRMNgDF9crpZ8NTTO1y7C5hKZy2cptglcTf0+LZ12aLAJwCwmWlOIVV7GHNdNSF89dd/us4efLfe0ck7q0eUq5bWi/wDZHtdJWsovxckMo6/3KwcXUpurUsHPQTq/nPFpfddLsztk6P58nKxqj1ma6BK2Fyua54Nano3USSG5xaICMdpOlezZvReDhbuyR0ilPcrfKCh5YF2HHoAllaPNKtuAAOBgxWA2KwS72m9VluNSGbFAyqFSKOFs7orgmy1q/1jlRYhl6zXcpbBQdhJVP8bnviCq+LwdXIJeM7nV9nE723WHdkTYc8FaM1Thh4wh5lfSuSVqXINxwpn7oDXHBcyfNJI7eRstXPJtZQct5moTHkyllOhuqMAUrk67OTJvD2ZxfLq7eZrcmK3XQy3V1RJd5bJftRp1J3uEEsulBBLg1HxZlUYSXhpQYfbPduCq+WLWnuDhYnhOvMbPMjXnBcWq3yY59KcdTuQGVvNGobXyx6ujGcgRqxsImL6HU3W1jad26bsw0P0t6nYo+7u+PV9Y2kogMlBzkXmkpFHeTsRjd3c7+TPYiMl2AVdAyy/WUEYh9IvKa10wtNIEEiC10TbmcGdu14bDNSO2xl2vTdRnZzM4LQQgHK6Sm1qpDjarg0YQLnAb1onm31K9hLKNyq3sXzt2KTcJpw3LX7UC9bOK2BdPLXpRYEhKvQDArnrealW3AQfqCx7NAlI5Sku9vcydXToHoklPX3LIbMwe2u0p1Yr04AID1c0ls6Y0moc2wchpcX9cJuVDkbZDXN5Hd5sxa88ojFp6JSLZMOCUXYhlE1619aNBkf5aJORqH6No1XCBJNiOguScHtwKtlXzBwPlZOh0XDRapwcm/oIzXoYIqHk+nsFyq9VGZuZNds+vhfO8QDmqvtEIMKbThMrH0naWlG4wWw/aUg4S+spYn9rbdrKRJ6JTerQDZet7Rej0xZ31CKnQagHbPVLVXYR6JRs4wm9BlOGuxxkTJmTv1u5NYK+FVnQf+pd4uj5ecwqYdSmL6lTa43ukDUZ/FAymQfD1VbVE4mSF/amZTjNJwXRfsm+rw+44l6ICP6cDZuiJguN2a76/TJEJP6JGdpFgg9FE9qEAQSw33Cbrf9hE30SdKIKaTZUrnqkLNXXZqBsQ+o9qhcFatuuO7bWvueL3TiW1CbthQnM6pQ8TEqngWzCU3nfgRWYfmnFlWse+Edq06jUMwMuGQdeBYJQvnnUXUsgIAad9xV9Hvp2yx3EkYje2CNXXaJwvqgpOSLeYiyZ6PgXWgYTfgnOk+DsUD06PEeuLPlPh4Ojgtd2Jomid8FmgZS5Tkfs4x5WU4bbgi19HUCSODKBODMHm/DzN20h8aKeg9olam/W5VHlSX2s0ufNJvr12NcWSinHZoEl/X/G6HskrfzGbRwG73J9c1e5CVONgUZW/roNuXEUZYdB9hp9t8pXAdzZk06xjceqaK5oxW+L4jmKlEO5xQ473niYelnuGCC8dFvI+psOhQuKW/lPZCzPkbHE5uW+I2EdDJYB71RZTK9g2Xq06CW5TVDtolpEEiz6WyT+V4O8uKSZUXS2nFw32OW8xw+WLQGnrd2EtNMAU0FheEzAaJsIhncVUuqTnOl1eTEZvUI4vZCahKIbZr/HShNUo7p5CitClRouFO9PXbjCfNg8qgTRe0ZzRXq/JEcB67p3ebqOq182FOGMf5eSvMQybfCxtmUmvZTZlIp2xTM1GRNRNG387o2VLYXPLhOKso1IIOnmhP87ItoaQJzjnCeondPJPbMloF+mTbpvg1JA5dvrLxhE9F4YbJsVafFJEvgEjz/a3F1iHhL+jAE6iWoWy22tnHqsdXfib0uL/Kcxy1gwXwPcciqjbzTwfMOx9WpX8Rl75oXITwBDcj5AB32+W23hDTyKgDAg5/LJ8dpxezPnb8vjklZMjOU08GdRah+5TTPG/KK6G0KD2Mwo9bfna9eRFsda4TYASzZLo1RbFXimZ0uOMX3cP8dNjRG2vVz5V4QivtjOKHfBLsE4dWlXZFBpFs69aEsgKAh1NtGlVMMmv6mZDPTm1kBgt3ze7JoUrZI1N5btsfhjWBm8cVdpilG9HY2HNv34iE2V8SV6hJKp5jTLjdBUOZ5qdsuW3bjCCIxLfJFru5RxlyczWDG7R46S0PB+w6qLS4ATc24qe8cZCY6RpS91bUiOaKBaaXwC3D3HO93jODhnZOOX0Oj4fzkdDmwlVQ+0ba8QkcvlrTTqJIgduLiGWzUNIWkcuCzVSlpbrHhF4+WfMt2NhykpH2POtMpbJRgMPWO3fEjiWZSQpukX1a9OkMDlJsNsn5ZX+z09SZezul2la3bmhv6FHrrrCW2qE0+N0pPmTDITEu3YUEbjPNdbbekZlPYW3RtjJPbGnKWAyxSpxdpb4IlHZ0lRJIB67w5oC1CV2yDV32F9XUCcW4D3wyIVYmGmLbG3HpRG02YfG6zalDuWZZ9uXTy3gL+Xkj+G893x3vuv0/u/n3uE/39ljofg82dIMvd11f/p5Zv3x6AX46GnW/0dlkXfy8JfhfbnN+/nceKYwSro9Hp+NTrEv7du+8dePxJ0AvaRF0TQuu35oy6+43Wz+9eF0z/hihGX+v4sP3l7tzeTXeQn4ohR+SFITf2vIbCFv46WX8mcD4WCYMUrd9O4yft30/vQRXGKPUb74RNPUtBNXo5vPxxHindHw+8fL7/wbRKq9oWSUAAA== -->
