---
name: "rar-cowork-cookbook-adaptive-card-define-organizational-structure"
description: "Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_organizational_structure", "rar_sha256": "94005c733c2b325ec32c47282fe11342a43e4ebc48466185a9d31c10021077bd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_organizational_structure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-organizational-structure:33d353531dfb6b7680ad90a1404316867e5109ffd17f04a1821a4c7ce6c3dba6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_organizational_structure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_organizational_structure_agent.py` is
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

Define organizational structure Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 94005c733c2b325e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_organizational_structure_agent.py` first:

```bash
python3 adaptive_card_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_organizational_structure_agent.py   # or on stdin
python3 adaptive_card_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_organizational_structure',
    "version": '2.0.0',
    "display_name": 'Define organizational structure Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8fc94787f9c893f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:define', 'word:structure'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class AdaptiveCardDefineOrganizationalStructure(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineOrganizationalStructure'
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
    print(AdaptiveCardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aXOj2JrmX2HcH6qq5TT7orxxIwahFSQQu1BlhZMdxL5JQHX99zlItjOzu6q7q2c+jBy2WN7zvPtywL8/2V0bFfXT5yfVt3NoY6dpHPk1ZOcexBW3ok7AV5E44Bdyi7ytY6dri7p5en7y/Mat47KNixwsP9aF17l+A9lQ7XeN7aQ+xHo2uH31Ic6uPYhXJRFqcrtsoqKFigDy/CDOfaioQzuPR3sCslOoaevObbvaB0d22zVQUNSQnzm+58V5CMU55NlN5BQAsnkGN+w4Bd+ARvPtrHkBgvm9nZWp3zx9/vW356cYHD99/v3JTe0GXHp6F2qSaXmXQPpBAPWdP0BK7TwES8oB2CgH56VfA2kycAnIDr2d/dz4afAM/eu/Jje7DptfPn/JobfPl6fpR+lyqI18qC3spvU9yLVL24nTuB1eIDa92UMDTAY45pPxgPpAzZfHym9IRQn9c7r384PJS+i3P395KoAId7G/PP0ymeDLU91Nxy8TSvnzLy9pcfPrn3/5htN0zsV32wkMSP3y+nb+BgsIv5HGwZ3rPwHqw9WO/+XpO+Wmz0PuSU+w8unlUsT5zw/gsi6ufm7nrv/zL38F60a+m6Rx0/63cH99AEe+7QGd3gT/5flu5N+g2ZtCH5h/zbYEbv07mgDyd3bP0Juh/gr7bv9/B52CGGs+LP6ncH+2YPZP6Ne/1O0/W/AMBV+eln4Kgrye8vAz9Purelxxv/7kfbv4029/AOj/EkYtutq9I7xmIEkCv2lfX3/9qblf/um3X3/qShBrIPNeuzr9M8w/s+udzw8WfKP6+ce1gL+eJ3lxy6GPSId+L8r/Vf/xAhl2Gnvfrjefoe/zZfrMoEmJd6YPE3yXMw2Q9Ts7/vL0BygW+aP8TLdBlv/Lv0CH2K2LpghaSHWLroWAg9s48yfhtShuIO0tqb+qwm6/f8m8rxC4OqU7KBF2l7bQpgYlCgL5MHl80gCUvq//270X10/uW3GF7bey9OqCuvT6KI2vP5bG14/S+PUF0iIgQ1HHYTwVTYU9HiE79PN24n6Pk6bLPl0nAYBw8aMAKdxuKj5Nl/r/gL7+LY6vd/CXcpjU+5IDf9mA3INaPyuL2q7jdIDsqX45Q+t/AhUY1Ji6SFPHdhNo+tOVL5PNzMjP3yzpgn7j977btT6UFi7QIohB1X4GwdAUKega7WTfJonTFPLiGhivqId7YwI++DyBff361QG94Ev+KNA49GhIDQwIPgSGPn0qaz9I4zBqv+S+GxXQT7//8RP0b9B/tuoOPvE4gq5xNx4I8vTRw0DGdhkga6ApXEA5unv09z8eXpmky0EHBXkWB7F/XwzQvoXHpMHDVe9+AjpPIvr1G6cf7QbdImAXKG6BtUDuN89f8gmiAKT1LW78dyM+Fj9M/+74B5/JJ82bDYGfgrrI7rT3yJyc6Ra19wLtAujDUkBd4Nd28mhUNC0I5tLPPT93B7DSbr+5MAe9vAHh0gTDM9Q1QNUJ+asDoCfjZKBo2e1X6MAdQf8rUvBnMtCdPVhd5PHk+LfIfVwGIPVPIMYW7xAvkOgDa0KlXdtlVNuNf6cL7EdEgL73vh6A21Du36Cp6fuTj+6BfI+85X8xbaiPaePHmeVLhyEoAf3/MtxMerCbjbLasNpqCa1ETbEeQTfNZpMNHuMcGC3uyPcM+jZuvFem95r9JU9j4Kh6+MeDMrjH2YPmQ1IPFBfljj9lfH3HjVsQLZP763qKcPtL/t4cnoGJgK+aqc6BpE6mElF8MJzuvksaAUWn82+DAvQIxClBQIhDZeeksQsFvu/ds6GN6inX3lwCQsef7AySw41+0AoC6CAsAD4EhIhBDIMGcjedCHJmMvM9AT7I42n8Kh8e9iCQVP4LZE4xDuK0gRwfzFATDbDCT3coKPOBjYGIHxZuIrt8CDPNy28C2iAEmjjMv7f/2y0QrVMPAtw+UhFggnrcAkvegAtApvUPv35I+eYpIGo2pcV90Y/OftMU+r6H/WNKRyDht9YABvx7+H4zDajhddbcyxJozEkDEj7z38IHxMG90788mvVjGviQ5fN/2CL8/Pd2Eff2q//ot89Q1LZl8xmGHy3yvUO+uEUGgwiJS7/56Jafpt716ZFrn37MtU8fEfwDk4fNPkN/T9AfIN7i+zOEviAvyHRrH7v+FMBvH2AX7tPC+kRMd7/kiv/N4YB9kQEJJz8MoDB/NJ93EtCBwtoPJ+JHM2qmHnYDbfNeA+/N5CMo3hIGlNg8nDpnU3yXyJNOk4sfHvyo1eBWPnUBb5oEQ3/aMKWT+I3/9Dnv0vT5Kbcz/29ulKbSDEIYGGbaaoFkAkNWG/v3M2BHIC4I2vZ++uO2USofYC/Qdiqj39G+J4vTeWCzAzpkarfTdusZ5JXtTSPkMyAHdT6easekRjuUk9yPHdQ0zX2Mev+R7z3BQWXyis9Tnt/hwd+PCXvi8tjz3HeUeQc2fb9O0/2kLCAFXx+0H3thx3/67U/EeBv2/0KIeKoxU1V6lAvf+xNVAEjtVx1o4N4kxje9vrErHjz+uIvXPnapvz+9l5Xp+DFNPIIKLPifjX+T3u9t+3XiYk9Y9yHtbob7yPtqA+dP7fm7W+E0a7w+AvbpM8D1n5/AYjAkgTl+vG/Wnx6iAZ2+DcsAAZSaT800bsAg3wASGALKSZ8ElMnvGEyXY+9OPx18/ssJ+79VMz7juIeT4Af1AodyaIpBbG+O2CiBEDhKMRTtkygyDwIPpQOEsFEGQ23CpV2fcnHQryggUQMiJLPfJILRyTdAlw8H/N9tAZ4eYKD1YCQF0OYEgpAujeMu5uAY6bs45hI0xmCBj6I4gdkE7hO+4xIMQVEoQ9pzD0ddFEEwFKFpx5vw3ubOh4Sv7zP+u7cedeQV5FwWT/Jjtu0yLo0S3py2KdfHEQd3fRRDPRr3EXKOBwwDWE7Ib0vfPDY59GGEKbDByAkGvuvE5/e3CJiClSIA5ZZoduzjw8Fzw6bIvaMsnBlNBcVaYxiWtlwnbIhswDaDwg0LPakSFBM26RDvnVN7zlS0KJ04E7KSiNeEXJLJFZcozzFGC/frtNVYX9S8koFRqXdJbrdXAuekZoqQmYf2AA/83tGEM5c2pmH0ZqQIp1K91QJDqNk5oCJlnzfJZUXT8IwvCZ2v0vhs6XpkV81JOFeN1AQpwQTc+crjG/IguL3Ab2bEQFe0UVkyyBNdtYWx9bizKmjenkV3WJiY5YruN3jnC06GEmaEzLvlAiGa7ZlhOrro9goz8+GIE859k1qlZAhxt64PlSicVPJM16mSNsqA3jpPr4/M2udHQ5f2yaJLpTLdWdf5yfH6Ut3o+Fy4ZVacn5HZ+bqTkcX5aJzV0E/jhbvmS/3QltytNAdS1irfXgkcul7bHV/nHCm6Pdaied/tOG2eK0EWuWWyjq+FqDlywQzq6kyeBlTbWpWhN6XWi6eQW5i+MPIL08AEHAk2GU8wLGnyx5bVLYQzZrQmFDS/WQTrZVddlo53OSR7Q+tovtpd1FIX9nQwrHe6YTprvTIyBW9CuAz52MY4pxSVAo3pxMkv/UI7jXy1Avnqn1HMQ2AJDbsyic3OWvi7c7+RY3XMbdn3zkVKUNLogNlPYhUnYsliVEWKOi0p32vsBeLjwSo/JCh1jtqccpqKQmYgPIRa1VGCoBusqERMra97h6Mrq7Rk0+NOx/02KjektHQbap/0KHJleIToUndcsegQFRqWSWLPkTGNNHEpWvp8wZDzucrg6zLuR4mERetCWDNcjJy9Nc52Ryk9o/wWO2uzdTN4xgql9cBot9sTHaHS6XTsnazHhFMU5EVzvI3XaGv3TIWJ62tXw7Ia5Ag1n2Vbiuu9tYaei7NBNm3GHec0Ywx7rHep/YA0eLnnxaCWK7R0Gc1sss0sQtrL5uyrgm6LAnxh46U7mEPHhprp+ZzRD/u95C4XRBquZ3veHlapm+vroY+S1bIQmSLuSuA7vtfmw0HdXdg+aghTY0+yuh2DQ92M3KI/bLd15t2qekfB3sq20fRc7ReSclZ5sLOIrmDk7Ucx0pixSMNophjdNY+dMylcPSXwmiD0q02a76n5NWCuxAIfz+SoSfsGN4bxmMJC657KatywxY0/zpjYbrmd3/eH/pRaZr1uHNZrwlYw8tn+IqpwrTd9MsekiFNsk+dSo2rKHWtYu11qRsQZxvGuZFHYlI+rWW4pEQzPPXG3BplOeJnQnOZtfEF49JJrzRFjkkLd6XZicAQT4qh1zlvZ4a4mw4YMprfJPslgJVuC7DiEjVLbEclsTqQQj6UjU1670mYCftXtPcapun6E02Y16HZoHGfRLlosFgbJ+jSVecsttsYk+aBqPG2t90p8S3tsLzZ9f8NVgdhlV/lcNqOmnlKd0Nh2SBChGebL7YaQ8+zk3kgRC0P2MAvWZ9NuN20XULJWUpGP75DjfG4sDjDn78au3lWmWDNbj67W9pFci9UI4mBwb8ekLkd5ZHY+C/upu7VHurFY9KqGuVB7or30+S1aZJtTl17EpJJv2Ro5dBWBh/jNMCU5OBSDKOkSLDnMaTuiIcOmW8nuVS92rvmV2EuyUDH0eGLbg3Z2OhJeLIldv5CFZSY41i5PZ7LZ1Vzo5jukWC0jTsYjHzbHLHMCEdZZgZxVeiOvQVRWZ3yjFqYwdgrNXvic9dfyrRfYvd00qmIssk2UROppu9W7TrYVuwn11trgrW6iGF4fbw6f2aTVJ/kJp5njGCO+vk50OTpXw6Y+NrBSGkV6FNLBHbHwsFOWgxSd4dOM2bh7a39tN3vruJnJUU7B8X6kSfp4PBopvMpxuGf8QqOHy0wXl+GBnzOmw+/ZvRkqt/LqHiVUE5CYEdU6tah6LbD4EdFsg9uN6I04hXZH+julWg9Xp4rVi9IoZIQOUiOqSK1vU8FYkGp1aXSeUeW1DMpO0fPyjZthaVlGdLMmUTFdqxLNJ6mwitQEmY/ngNd1l1VGaZ47RL1dnDsD5uJqxYgExy0vXjIjxzG9YcloKNtVN9wQB3ROS2J2S25dFMiarkXOWDiM1TsbG7MQArHCm7cH6XbKjDC3yEo0YO/CGSes6geM23O1nA+Gm/EXUyGuhtHxsx3KL+V+tuznKwJZV7vByxi5sX1NWHmkN6yNsw+LNL6WwporlWozto1plykXHvUTJtS4EQ1YcljjmngLRGF9unIXOZdLhNoNt8I7IQLoOH2CekOqXMeGW81V0jtUSFllPstGHSJGK5gd7PTY64I6DJ0gloTLHg6R2emk4qWYadiCmIk6iqx6t0+41JJ45+jNbPpiZaXaJLfIOvmr0l2krIg7dqUOxr66ZmYSFlhTd6fMrrDNcXRsG7F3kXcNBLKbH3QUzX27LUtDsJdwlAbbXanPWuqocCstD3i7BwPqCA5W1Abt4pRnFAuWqEO6u1q9cSrqq85nGRfiFXqzdj660u11bCUXceVjS/+2ODAnXVWUbqUrqmcCOS1OSmGkWZK2053gdmMmWzskKi+IiFbc1pdTW5mX5CT5SMhp1lHAih5BqoRK26YewXCxOAvb63VMaTJzhQtH8KLpXLdmlwUew5OzEEVIUerp0SVm8QkdnLOGu2Ob7ROfqxgnnNt2sTE3F4pjul6R8JscHdqQdeXNSZvj1NoqFeLY7pSdRvSRammxsC/nbr6WRpG31naN2CU6XDRyKyxsbjnm4vLqXBKmFFyn8LLtOVmRW+u86A2P0N2VKnVknOKss8yuebpayRqv0MXthu+RsNlFy2GdL0rjiDlVox1XV4Jbd0XCZqxD6+ohtoPiGiO4sAwTvOAbBoxzJjde50t5dxXscCcaJk1tlMFSt7atSoqytjGTD4WFA9rujUJKjdWpGL8lcKmrmZ4VLacudlvTb821shvJVKmJkt8h4/5ouHUncmGac8GSMS2RK52VZvEiIy+sDRtwQJXMGA1HPp8LIRwikhpaHRH20n4TOVeu1Od0kyz25JVnh6HimUuED+pBx9FFja3TVENTk5MXI1Itq4U07oDT9DJdO7KIu4HIrdu0ni0XB01XiMZWwKZF7iWD0jyTodh0X6n2IeGbYgm77nxjYlrVi5WipZhQDKdZQ86rlcKRGNzM8wNBuqSHesnWtIbQtkajb9ayTAasPAsWaJ8csoE5UK217+3rpmBxL3cWhrbU1/mKQaTSb0hQZhxFPtCRtVtTqCGs7QFBV8eT4Qe+sdLsVcFqJ2/WcfNMjEZrVe3keN9xiSTLoUgb+E3BKPxiiF3Zbw/MgbfDxleaSu8LDzQs8+hqZK3kBkOMecOXOLMQ53rMe8uzFl3PizF1VhYvk4vEZtTFwqVWRLhbNPYcpXpKmx3Ia2NtrlgULUtQfBlC8nAQ/81wJjlqVGIYzwQtCWRKh43M86jjbo0jOnJIBFKuk2HY8iGz14+robgZVyre3SI56ssLK+AtyZPxxVuxF+uCr6T6HJrZ6nKg23zXbqklqxtzVML2lHNBMVLuTsZsTy81t7L3zckglbNhYnTG0NHphgKJclrlEykgrF3oSoo7lAgyuFVqnUrXm8fLYHEaJKkvxA5NRrBuu2fQfHZUKnJfayoMapKEkuWZD/DktpKuEtjOUDFxjQaPJmycuzWjxfRkXKz2PiZSERjLcxw5X+TmgC0HfyX13PHWbZUxizcDXtzoFJ7jieNIQ0yWB6rAYn9rgVlim4LJOz8484ANZjgl77umSLnBOtJiNjPxgrylnLO0qNEdZHrLrREf0eogo0xmMzTJqS3whuax+XktYDdYklF653NM489m5SAG9hGeYRRMyL6pE5WGBjBRBpdiQWN4NMyCensuQuyWMlVSXdEzNWCrPJxTO1E+zwJ3ZNROoPgjtYrinbgYApQrI3OxKHqMKOIttiW4pHIRjc04hFw22Xnmzgu6TLWGPI5sb7ZUNYhjZR+5W4QprDNXTqeYPvqWS0ZZGo8CIh+oa+iQiSKiY3YCM1KwXTtr2OFx4hhd7S48Npp1reM1KPc9NpDLIN4PQoJeKn3Z+jIzny23bXdr3IOYhgdlVsVgk98Nrr3p0erS0SfTPs1a+NxbhVyoa9XMV+y4W50oQsLwm5/KHkbCCoKthC1Wb42VKStwHcfS2DgmznS8XJlk4Mj80ZnLSj/Dm2EmdjN5eVpIWkjOaOS4jndLRjOEaBkvIoEU+3myS7z4cKrXjOqh7C3kFNi6HU+IE0dNZS1Rb6mewj1lSaRkbJiDSrOtT4ZLp7d0L1QP/PV6vmWn+CTtTqyvmpuaYFODP9P6VZnVEu7OZnF4kGF/4TZn1aVy3THpslG0xcrc68R8Y5GlvliHJGGyvQd2StdFqnou4RhxO4fX576HGe2KrtEr0NhLjXiXzS+15FOrTGzO+8XZK7HRL5VeVxL9MJ+Vp/WVMPrZXj7p3jz3RmQsMLqUb9HYZPubbMG9G9iUvjjLN2kW2Mko7UOw2W/w+WUQsqVr2vN2dli4h0uJIfVpPRbioZ2jaWd4kkQeS/u8uFRLgbUuFUldWqLZ5ttxU3BcCcvGIi97XC8OS2pBLLcMJl3aMuYHH9DJws6v/CS+CtvBoE2KCDWYbb0W15UlQ6wvMB7MGMk7zw+wZrvwiQ6W29sSDhhGimWGWPoNvKTXJmXO0plIBEFRcbmRFmccPu5XF/vSuelVb/HrbYuT4q4fVf82jIyRU2phyyoje5ZcMawOK3v6vNxfmfXFFn3PCi3NybMyl0lnPROOCHaOQkHLRS3vgyA4IvGOAgaiTJLxNorkn+04dgx/r8lHZnmY21eyWsUWXLMHSnTUeoEusXYAszpfeKg7eJu2MHTcnNXWdS+1c6wg/a5DPdxeNaiwvlRxR2/Hg1/u5pcF4UkXkq9chjtT/dBsbyyfc2umE9k8m20MvapvKY6O+vJQnYtR4W9uoHoVrhak4puO7qa+joouUXXiXDqg15AmCIJVqT2K8jectO0lveUjvyVcORrjuVcnUop7ko7n7Lg4nI5j554vvYXzMCqExbE6aduTeqyDkfXPCEJsrqxXizd7b6zJ0LKVSl3tl9qcOIf7nlfP6Da5uE5QLSNyhuSSbcRbLz+mR8VLSkqE2fkpD41ZLsgs+/T8dH/3+/QZRSgKf36aXgy8Pd7/Hz//Dce4fH2Dxak59fz0/+4h5OOB4PsLwfsjd9/2Pt+5f/4fSvzb81PtxkC6x+PjJu3Ct4eQ/+4B7Ke/9YR4ghoeb7inN5p9+/76pAUTxSR5nHsdoB5eQdPq7s+ygTe6Zvrfl2b69ygXfD/d1c3K6R3CD+qB8ygGWrTF9Bw2vrOL8+lNne/Fdvt+Gr69B3h+8gbg19htXnGKfPXrclL77UXV9Kx2elP19Mf/ASJMcHrvJwAA -->
