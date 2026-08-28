---
name: "rar-cowork-cookbook-report-process-change-orders"
description: "Builds a structured summary report of process change orders activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_change_orders", "rar_sha256": "1b52508998d27aa84f0a02802fc218cec432a51d088f2bf199b28a515ce7fb87", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_change_orders`. The original RAPP
agent is preserved byte-for-byte in `report_process_change_orders_agent.py` and in the RCI capsule.

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

Process change orders Summary Report — Builds a structured summary report of process change orders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-change-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_change_orders_agent.py` and embedded as the fenced Python below (sha256 1b52508998d27aa8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_change_orders_agent.py` first:

```bash
python3 report_process_change_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_change_orders_agent.py   # or on stdin
python3 report_process_change_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change orders Summary Report — Builds a structured summary report of process change orders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-change-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_change_orders',
    "version": '2.0.1',
    "display_name": 'Process change orders Summary Report',
    "description": 'Builds a structured summary report of process change orders activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-process-change-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-change-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa0273976fb2b6ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-orders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-process-change-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportProcessChangeOrders(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessChangeOrders'
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
    print(ReportProcessChangeOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZObyJb2X9HUfLB7ZBdiB9+4EYMQICEJIcSqdoebfV/EIkD99n9/E0lVds9037k3YmJkl0tA5snnbM85mfi3F7tro7J++fJy8u1iJthZFkd+PbMLb8aWfVmn4FeZOuBn5pZFW8dO15Z18/LpxfMbt46rNi4LMH3ZxZnXzOxZ09ad23a1782aLs/tepzVflXW7awMZlVdun7TzNzILkJ/VtaeX4NJbhtf43ac9XEbzdqytbPm06yt/cIDvycoTu3bqVf2RfMKVvYHO68yv3n58vMvn15i8P3ly28vbmY34NaLcl9NfqzE3hc63NcBMzNwBYZUI1C6ANeVXwdlnYNbng/QPa4+Nn4WfJr9x3+kvV2HzU9fvhaz5+fry/RH6YpZG/kAqd20QE/XrmwnzoAGrzMm6+2xASoDExRPe8RF+PqY+V1SWc3+Pj37+FjkNfTbj19fSgDBniz69eUnYB2wXt1N318nKdXHn16zsvfrjz99l9N0TuK77SQMoH799rx+igUDvw+Ng/uqfwdSH75z/K8vPyg3fR64Jz3BzJfXpIyLjw/BwHVXv7AL1//401+JdSPfTbO4af8puT8/BEe+Dbzz8Qn8p093I/8ymz8Vepf518tWwK3/iiZg+Ntyn2ZPQ/2V7Lv9/4voLC785t3ifyruzybM/z77+S91+0cTPs2Cry8rP4uvIDqczP8y++3bSebYnz94329++OV3IPp/FHMqu9q9S/iW20Uc+E377dvPH5r77Q+//Pyhq0Cs+Xb+rauzP5P5Z3a9r/MHCz5HffzjXLC+VqQFyOPZe6TPfiurf6t/f53pdhZ73+83X2Y/5sv0mc8mJd4WfZjgh5xpANYf7PjTy++AHIoHH02PQZb/+7/P9rFbl00ZtLOTW3btDDi4jXN/Aq9GcTMDf6fcrn1g1yYGhn2OA/E/eXhCDIjs1/907+z42X2yI/QguW9Phvv2YLhvD4b79XWmRhPdxWFc2NlMYWT5a2GHftFO61W13/j1FTCJM7b+Z8BBn6cvs7iY/fqPxH67S3itxl/vJBk/WElhNxMjNV3mv05aGZFfPHVwAcX7g+92QHhWugBJEAMe/QS0bcrsChhtskCTxlk28+IaqFsC+p5kAyt9mYT9+uuvjt1EX4sHhaKzRw1oIDDgHc7s82egUpDFYdR+LXw3Kmcffvv9w+z/zf7RrLvwaQ0Z8PjTBwCheDpIM5BTXQ6GAfcAhwLCuPvgt9+fhgViClC0gMfiIPYfk0FMpr73ZuXTmvmM4MTM8YF1gWXzyaqAl2dx+zrbTIXpifdZrCbmjsqmnXl+BcqQX7gjkGoDdd4tWZTtrAGB1wTjp1nX+PdVf3Vq+w4xn1zV/jrbszKoE2UG/plg3geByWURA/O/x8DjPhBSf2hmyzcRrzNpisJZZdd2FdX2c43AfvgF1Ie36UC4PSv8/msxVUN/MtU9JR7mAYOAZdynSz9PPgfFHNRmUF/f1r6Psadqpt6rWv21aJ7hbteTK1xA/2DRsIu9qQj87RlSTVR2mXe3H0A6SXp6wXt65R6D8p/W/dOzP3hU7NnXDlnA2Oz/rJOYgDGCoHACo3KrGSepivUw2NTpTIZ9NEeTPBA1j+T4XuvfmOKNML8WWQy8X49/e4y8m/k55gdVFEa5ywc+Bgab5N5DcAqpup6C1/5avDEzgDy70xDwAshXEM9TGL0tOD19QxqBpJyuv1fpu8tqb1IahNms6pwMhEDg+55juylAVU9p9LQ5iEd/smofxW70B61mQDowPJA/AyBikBjAdnfTSSVQE2RQUJf59+Hx1PsAFF7nArSglfRfZwbIhCkaGpB+oIGZxgArfLiLmuU+sDGA+G7hJrKrB5ip+3wCtJ+++NH+z0ffI/eOZAIPZNqe3QJL9hOLev7w8Os7yqenANR8yrX7pD86+6np7McC8revxR3hO3GDFM6m2vuDaWYgdfLmHmoTAzWARXL/GT4gDu5l9vVRKR+l+B3Ll//WcH/813rye+3T/ui3L7OobavmCwQ96tVbuXoF+Q9KlhtXfvMsXZ+fKfX5kVKfHyn1B5kPE32Z/Wu4/iDiGc5fZvDr4nUxPdrFrj/F6/MDzMB+Xlqfsenp10Lxv/sXLF/mgNcms4+gVr6XkbchoJaEtR9Ogx9lpZmqUQ8K4J1HgQe+Fu8x8MyPh7aAHZryh7y911Pg0YfD3ukePCpasLY3dV2hP21Gsgl+4798Kbos+/RS2Ln/P2xCJjoHETpdgG0LsDpoYNrYv1/ZnRdP1pi+/3GDdbh/sbMpncqpNE7c/U6ad+ReDWBN+RfGE4N/mgG0IeDBSZl+ysGp/jtAuQbwqe9N6NuxmuA+NilTw/TeTf13BPc0BvzjlV+mbP40mzrfT7P3JvbT7G1bcd+kFR3YV/08NdCTzmAo+PU+9n3/6Pgvv/wJjGc//dcgnhTzIHXbmUrRpOKf6ASk1f6lA7XPm/B8V/D7uuVjsd/vONvHjvC3lzcWeXrp2f2B4SBdPzdT9YNAEIMFwfUj3MCzf6kvfM4FjAd6EzAZdnAEX1A0TXkIadsUFizsBUItkMBFYMr1XQxFbBz2FhQVIE4A07SDUOAG7vpk4FAkkPcI2G9TeY8nPP4i8FEaRlwPJRAcx2iYRGzaszEgf5JDLsjAA0Xh+9QUEOZTyYdSkwXfW9R7kD50/e3FITAwco01G+bxYSFat0mDdJTIoWvCt84mtHFijVDNs1PvRB9eC56zYRDWvzV8ql0aThpFDpZSt9/belsLh2hFMwUprq9d4QvrrZSJHs3xwuUkqS7pdmeoKJL2xDGnRCLOm2ynxYabURdNibTcaLptYtpIimDZqANLc/UNgjYVqR/Srk33olGlxAW5RJqxg/adYPLHSiEHN08XmU8gZVSbNszp+nFsBkkRzkYx54P8YsVSWnmVe0Ydd3Uk/GAdQ4cbP3rdrabM84UMChQLYlK7iNU+rDPdY+HWuOxZpQWwlFpVDilh7D3NkSm+4wdTE6Wz7ia3jScQCQazsEtwPXxCK6QQ526DxpWL6Fa9xVnK2bKWcFiEoZC07g0+tumWKMsa2Z52pqDwgGc93eN8BaEcWQ9OdReh3UHZ4qoo8/Ko9ayUUkwiE7dEjfWwzFxr7CyAR2THGtrH+lyVCFw/6NkVYblY6EfeOTK8h52hes3ipO6y84BNjSqL0BjhqmN+2LYcEeKL8sxb9VWvN6eqIdqY1w1T2tv5is6PxrbFpHYBr2qjztVKYou9aDf5NYBI+RIUp940x2O9bphLusdUUefPo8cgAU7khGvyTRscotCq6oOE8We1w9CEbLxGYBdzVOWMJs/mSpIUiDEqUUQGfbTNTSO77i8LKM94kNq1OSKbA847yoYv+mzo1TkSNzfOdgWhiBz+bN2gYS/waZ1h4Wm/uO7dU7RoSpRz1p6uWX4fnyF6PMDc2Fwul0VDHJJo5eZBNrf4Q5Pgm32XqfBIqzI8qNLjx9ubhNPfOJKWLiTGFWR5o8wC265HTqKhUuH5yzyh+94vQDYHqjyXM4IfYM01lUGvjLwdaS7gBWSvlk0trm9ncbOrPGFnZAPAOlhWzppzDl7FppzQ9WZ+q3ov3CwdiavV23bNdEUcyUnu65wYwx4e2ZK6MvndwFKMXyLxBfhgu9ytseLMKeERMU5CEVbpJmFvu63d3pabDojugpE0WQTizV3sqGIczjmRk5XDUUv4PhwK4uaN6zbo+yJoMUoltXZP5qLQcUFI3FqzM13CN+coySIHj8r4CKUReFsjOiRWrtl5iKz5RySTcK5tqnovaBB32GJtuDTn9LJW99CI7eIrMZqRHK8EqhQ9XF8ainbWkLgiq2JTnSvlIsLBOFd2OL7wU4FsbTE54xR19ja5uaHoocyMHdXcNueG6OBKMvHgRG27i7TdkpqF113jqnjJKzVyLa2DpK9xvmpQRxP1XjRKIbAEfwnTShKh/KKrOdEkwwzFYrRWj2usDAJ9vtFKxK1RnGti6VIl6tGp22IeiNjYGCvtumLhasmn/g3de5K+5QiLSTLNDQtFy73DOR3PigRSukbKY0b5Jp8d0crYjRiL+Nc1VduFXq2vBZy6hGeR9rYqBrK+5Axjiw3iZcAr9pxZsnTiwlCZNXpMV+ji0HdmkEQURAqc6m/Jy5oNxxbStLNlD7CcF0fPpcn0wpl+RnFarZwiUWGlHDeYwdQFdicbvmF4MVOrKcQ3c4pfdWtCtS6aOzedDKFX56SSrnPDl1l0dFbSKgv5mr0cyW7jncubOl+5USUk8S49G7UfReLJSvYOv5PbAkFJ1zgoN0VjNqeE14xSl5RQTw184+7iNYu5a47dHt06t21rky+UettvUDLUO/bEwzdGuPXbLouILlkQCLNudBDAc6XWguC66mkf1Qe4YSXYWcKgboqikutXthitepFYGs2mHr++BXUv9ler6xreixptyx3SQFaxcfQgKNjulKDHoFhU5GxNVReGNyQc11B+y4hyqIAGwZb3brilNsJVj8vznmAIVfIKbpEi8Vl1RX4hlLlZ8jDWIEQdxyVnFD4H+zGxOrb2jUfZZvS4ziIOB/9gW5e4yeXLkiH3FawNtMHMyRFJgppHeXerM4tTge5NDV7zZrO50ZGaFD6/YZUj6idIQCedGOhVdzoRen3IUS+rAbPq/EpRcIHh4p4SBRrmMyFrxwOHnTJjM8c1LBzQJXsLDReN3YtLWosVyMyDaEpnOfL8pGW22vV0jqPmRASX/jqncizklPyqEAUKb4ZoOA0xtuRyQko107Wprk70QVPP+Ly/9B68tdgQJp3Alzaiu94c5YQD/UojacjR3ODzKzHXEYWJ1Q2Ir9NhZ1ODhq1DXHdgfU+D9JTBlpwV1WuExGuj2HpMPMJzJmYcSlgrx6tycmqZz3BfA0gzJIeXGYalul6R5VHp4fagbEw2YPJcjqIxpCGYADuMcZ+y0Wbtc4V7LXPEa6SwBvVSZUdjedmvIu/qqAeJY65o2645KdZa49r4CJSLNr1F8so1Yu66hC5Eq6anZIca4SJsmTOJmBq9PBHK2HFmIt/8hS2rXSKeWAEf04qKx53Icw6D90ZPUb11Y8JmPBoxclvW4cnT2YHnhfJYxCHRjJG14aQaqRjz0iNYC9lctrEXzGifIS+bI+waclcmkaRa51/Clb05qN5tFVrLM7xzdMQQLNTht+srVKxHOIVac7OvjNWKI5XMhIzTGpdCWx99OldV3zq0ZrYwiFzHAlc5JhUuD9d2cTZCQ9C748aWjNqpezPaRUfG3QjuzZR73qpETE423ibuVWvRmYxmOj1+IEz8zPbSgb+sFAxHNEIbXfNwHNeul3tH6ppJUpeVUX9sLjuY324WfDEOmsmbgZZZ21w8uHv+CK+3obVuznZW+Z14idaiDZM6gYfF0tvveyJN2FobMnm+iKrTka5ETVu5m1O4ZXt2ZJa6xEf9cNmKJx4UgD2d9NviNuB90s/LUZD0StDFhQK3OhoJjAVSutgMydlIWEsN1Zq/bnFqJxq4lddRFNkUGZ2GjBhSzb4I8FlOVHFBLkQJJ+jNnjuIa7YfrManWfewskvHAimetANB41C1OaNnTtP3fbV25wquHrnoZEuA16p9z2u41o3LwwVGlicVvbH1VnFlg3KhjRKmRUz7HDMGEk00+T48kkdMhFuhx9hmAXwH7y9HRRquF1UVb+eLiN6Kcb1BDuGpy3xZctF1EmVE7qLzBBDAqFyEslRPaV5GxVDwhMtTJHLJT8usI89kdmrRntA7a3VyPI6P3JtbjQekUXWHW5HCLQ5DCb+erfLUL1vG8lh1kPGoRY+EzoiL3eCmQnc9Wdj5aB6zBTf3nWFZ09zFcqttTcX2SoGoLs1lM93JkVRv/Y2phR3CiWvmOGBQl6pMCi9Isr6lKysY46FN52G4qJbqIj4HGVtGCL01Vpvz+jg38I4nuaFWjYVBMULheXpp82vX4kXdR9YlVzfxBRfSS6BzeSLpmiz3qHijYN7CzSpxXWNMpfQsyrG+wtETP2wLM761h1pd36qjHnuYfKEMLb+cZHIeaWU+6MHYsgme10vdUWWEiUBuCzhpbvObhwxlT3KuOKwGWmXMnTfwA2DI7qBx8wZOCXtVhxCORxsuPFJr+TwuHHcDH4XEuF1OKzVaj6gL+XLr1AaE+JKDm3WwLq/JGeloM83TLtG7Kp1DZji/eNA+0Lv5XKe6tVxTud83gdd1G1AGGEEkJatESaLYpRJqMdpaEpOmThmMsUEKU4XFNLLj+lCK9o2b38CWOFYTs79Wc1QpOVCLzsVpJds80cu0U4rzzbI7n6/7uqYNul6tG40IV6BlNbtlcKS5DkKU/TqQtjqV00fCWiYd2hDkLtfr3YrCVjtv2wtm4SVlkCQ3HgoMs4A4s2C1Oj4eMBOijgHa8CQmx7EPGMG1ZGRsKaw8mHa6b4nTqrdvHGOtrc5XNht0d2NlTNiKlMCQPCnWrHM8SsyhkJnj2FMhVbHESWHcKFJlqlv2Nt4C1kBuhbJMqu0gkS1xWIZzNBVuPHcgW6qq0UyQ9mJjugIs5lzQtzvq2HLUgDIQ66M3QztcYXK/GlBOPTnCvig8KurRwjF1Kgn27a2wnX602dtaWNeo71Eetlltl1f5vOCRBSlHVrta27QyejUk2ZADtpGGzTWXU40eJWx52W3W5I3aJaE7B/sjEvTJpaCRdtG5in/iA9fQEdexFTSfE2DnV4f5MrsFl9yXDKe9Juo13Q/9ScO2XkePoxVTENcttHBgFw0Wr5QKFf1hPSxukIXe/JBnzKvRgAjlscopL7xfx86h1C7GKkxyzr8xVb+96RrrzHdDsWdvUQI6AXGO3c6Di9HkaaEErHDahKYXDCvITxSM8iJhVwbsFk5uzojJsHOyxpyVXbFhtS212Of0UrEOnhjKGmbC5OBpC3QUnL1xDQbfFVeqRs0D3onrZvAJL99cnUFucOJsWAaAgENI6qxoGhF4QUx5wlH3EkSsmWDleQrdzDsPtaU5rgqLrRsS1yWT0nPKx3tsO0TMau7Pwx7ZlTuVbKXyGp6sVlnXyxwr+X5E1qZ6s8kukmixu9AjXtXNHoGsuIdXV6IMIkKCjbJ2rzSh4MxitTyYC0rFoZMXWQlDhH6PU9tCmS+OISYrA1VmPGxebaUOqPmIHnN0ZPzUuwbV6ngLEMehu8BuUM+B3IO5DFxkDSPb4xrCTmchqDX5wMj1NbyNNyzKE9IeIKoMBGJYKgKMWNRuV+xK26WEHF3LQRhcsc1x1Rm00kbYDkW9kE1C3thvm5CXbX1Z13hAZT2EnFuts2plAfhJzqyIFgOsl5gFl+I7jaZ0WabhKhaTOD0UTYYu0IgNzq03WOTgQLaaeFW77mEsLMds4S8O8jEJ5wyE+tpmP27t+W4vH8l25FXVGdoRCVQnuJon1w2kYWnXjMFXgrSQO5tWRZJd95gHxGo0pskjnezXPSOiLEeZSGjfoBsbb6N5JeEHmwGVcovv3euWbqWR9LbzzIfrnZmFLnaLd1hXtz25YaGgb0RXTKHtnqc5JEQG9mzWnYzvmpu0hqxwnEP4GFOYsBGToErVrj6etwixo1JKiA4VyF2pounbYQk2Z07v+wx62oVoUezGcFgUinhsgMtxcXndR5tC85XVUEHL+TqEys7pSabCA3tjwZ4WETLE8IVsFzS3ZRjm5dPLdDb8POH9p17MTqdq/2uHe49zuLf3O/ezVd/2vtzX+vLPwfnl00vtxhOY+8Flk3Xh86jvvxxbfv5H7wSmmePjHef0+mlo3w6/Wzuc/lPOS1x4XdPW47emzLr7oemnF6drpv8l0LxBfLkrk1fTUfBjsceZcBwW39ryW+23ce2/TG/wpzcqvhfb7dtl+DzABeNH4I3Ybb6hBP7Nr6tJwecbBqAX8rp4hV9+//+X+zel5SQAAA== -->
