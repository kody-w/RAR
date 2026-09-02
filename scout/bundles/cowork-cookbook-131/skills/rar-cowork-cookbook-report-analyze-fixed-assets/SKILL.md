---
name: "rar-cowork-cookbook-report-analyze-fixed-assets"
description: "Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_fixed_assets", "rar_sha256": "bc75f05c1e3bee49bff1c69115ac7129d68bee13489772b670479ef6b23e5698", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_analyze_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-analyze-fixed-assets:66da9076f0e322eae8ce44a8229e610f9a991301f48a8c761747051e6a517afe", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_analyze_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_analyze_fixed_assets_agent.py` is
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

Analyze fixed assets Summary Report — Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 bc75f05c1e3bee49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_fixed_assets_agent.py` first:

```bash
python3 report_analyze_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_fixed_assets_agent.py   # or on stdin
python3 report_analyze_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze fixed assets Summary Report — Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Analyze fixed assets Summary Report',
    "description": 'Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-analyze-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0faf53284b08fa6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-analyze-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportAnalyzeFixedAssets(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ReportAnalyzeFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aaZOjSHr+K7j8oWes6gKJuzY2wroAgRDo4NL0RDVHcoj7kkDj+e9OJFV1t3dmvBvhsDq6SkC+9/VkUr892W0T5tXT69Me2BnC20kShaBC7MxD5vklr2L4K48d+B9x86ypIqdt8qp+en7yQO1WUdFEeQbJZ22UeDViI3VTtW7TVsBD6jZN7apHKlDkVYPkPmRrJ/0VIH7Uwed2XYMG0rhNdI6aHrlETYg0eWMn9TPSVCDz4O9BE6cCduzll6x+gYJBZ6dFAuqn119+fX6K4Pen19+e3ASyg4rsbsKmd0HcIGd6EwMJEzsL4IqihyZn8LoAlZ9XKbzlAR95XP1Ug8R/Rv7jP+KLXQX1z69fMuTx+fI0/Nu1GdKEACpq1w20wrUL24kSaMALMk0udl9Dg6EDsoc3oix4uVN+45QXyN+HZz/dhbwEoPnpy1MOVbAHf355+hnJKyivaofvLwOX4qefX5L8Aqqffv7Gp26dE3CbgRnU+uXtcf1gCxd+Wxr5N6l/h1zvkXPAl6fvjBs+d70HOyHl08spj7Kf7oyLKj+DzM5c8NPPf8bWDYEbJ1Hd/FN8f7kzDoHtQZseiv/8fHPyr8joYdAHzz8XW8Cw/iuWwOXv4p6Rh6P+jPfN//+DdRJloP7w+B+y+yOC0d+RX/7Utr8ieEb8L08LkERnmB1OAl6R39726nL+yyfv281Pv/4OWf+vbPZ5W7k3Dm+pnUU+qJu3t18+1bfbn3795VNbwFwDdvrWVskf8fwjv97k/ODBx6qffqSF8rUszmAZIx+ZjvyWF/9W/f6C6HYSed/u16/I9/UyfEbIYMS70LsLvquZGur6nR9/fvod9obs3o2Gx7DK//3fETlyq7zO/QbZu3nbIDDATZSCQflDGNXI4VHUX/fSar1+Sb2vCLw7lDtsEXabNAhf2VGCwHoYIj5YANva1/90b73ys/volei95b09+t3brd+93fvd1xfkEEKJeRUFEXyO7KaqitgByJpB1i0rYOf8fB7EQVWie7vZzVdDq6nbBPwN+foX/N9urF6KflD9SwZjYcMAeUgDUkhjV1HSw84Le5PTN+AzbKawf1R5kji2GyPDj7Z4GfxhhCB7eMmFowF0wG0bgCS5C3X2I9iAn2Gg6zw5w144+K6OoyRBvKiCjslh2x86N/Tv68Ds69evjl2HX7J788WR++yoUbjgQ2Hk8+eiAn4SBWHzJQNumCOffvv9E/JfyF9R3ZgPMlRo/81VMIETRNwrGwRWY5vCZTUypAJsNbdo/fb7PQaDdhkcdrCGIj8CN2LI7VvoBwvugXmPCrR5UBFUD0k/+g25hNAvSNRAb8G6rp+/ZAOLHC6tLlEN3p14J767/j3MdzlDTOqHD2Gc/CpPb2tvWTcE080r7wVZ+ciHpx7jdYhomNcNTNQCTk6QuT2ktJtvIczyBqlhrdR+/4y0NTR14PzVgawH56SwIdnNV0Seq3C25Qn8MTjoJh5S51k0BP6Rp/fbkEn1CebY7J3FC7IB0JtIYVd2EVZ2DW7rfPueEXCmvdND5jaSgQsyzG8wxOhWxbfMm/4RStg/wMR9viNf2gk2JpD/L9hxU4vnd0t+elgukOXmsLPuOTSgosGkO5Aa+EEUcS+Ib8jgvYm8t9cvWRJBv1f93+4r/Vva3Nd8Z8luurvxHwq4uvGNGhj8IZpVNSSs/SV77+NQ5SGR66ElwRqNh4rPPwQOT981DWEhDtffZjpyz6vBaJixSNE6SeQiPgDeLbmbsBpK5+FymAlgcCrMdTf8wSoEcod+h/wRqEQEfQx9d3PdBpYAxEH3fP5YHg1ICWrhtS7UFtYIeEGMIWVh2tWIAyDcGdZAL3y6sUJSAH0MVfzwcB3axV2ZAak+FLQ/4v1dAB7PYPYN8wKK+ygtyNT27Aa68gJjACunuwf2Q81HqKCu6ZDmN6Ifo/0wFfl+3vxtKC+o4rfGDrH1MKq/8w3syVVa33INDtG4hgWcgkf+wES4TeWX+2C9T+4PXV7/AZ3/9K8B+Nuo1H4M3CsSNk1Rv6LofZy9T7MXN0/hRHOjAtSPyfb54eLPt5L6fC+pH1jePfSK/Gtq/cDikc6vyPgFe8GGR+vIBUO+Pj7QC/PPM+szMTz9ku3At/BC8XkKW8rg9R621Y/R8b4Ezo+gAsGw+D5K6mECXeDQu3Ww2yj4SIFHfcAGmQXD3Kvz7+p2sGkI6D1eH50WPsqGHu4NGC0Aw84lGdSvwdNr1ibJ81Nmp+CvdyxDH4X5Cf0wbHFgqUC000TgdjXk7Ntd5u3yh+2YcvtiJ0NBwbq6z5tz5N28B8MJe8dQAINSTV8MWtx3KgNq+oBU/8j2Vp2wrXj561CkcBhC+PuMfCDZZ+R9b3HbqGUt3Fz9MqDowRa4FP76WPuxhXTA069/oMYDVP+jEkNxli1seUOrG+ZIVsNtEQxKc4/8MA7en/+BgZB1BcoWjlhvUO6btd+UyO+Sf78p3dz3iL89vTeK4ft93t8TBxL8M3BssP19jL4NPO2B8gaabq64wcs3G8Z3GJffPQqG2f92T8GnV9hgwPMTJIagBWLm620f/HRXBFrwDZgOatnV53oY/yisIMgJDuVi0D6Gbe47AcPtyLutH768/gma/cOaf6Uoz2YxmvIxgE8mwAaMCwjCZiYTFlBjzGdtlh3j2NgnGJtxaWpMEzRGjgFlk2Pa9gGUX8OcSO2HfHQ8+B1q/uHcfwVcP91J4VyYkBSkdVya9DHSHQPcAYBgHd8fuxQ7HpO2S48nrEcx8P4YJxiWpicORWMEzQKfciY4ICmWGfg9MN5dn7d3PP0eiXsFvsGaSqNB24ltu9DOMeGxtE25AMcc3AXjydijcYCRLO4zDCAg/QfpIxpDsO4mDykK4R0EV+dBzm+P6A5pRxFwpUDUq+n9M0dZ3XZM1elCYXRN2G53YLf7ONy6QJT3jdcc1TTJ8tjTcdtuA0JQtqLA7C/b2Uie9lbHy2i8G1kmKZrjCY3OpH0lOLbhR9p+JTU0wCsGbYUwWF5AQMSjbCL2ujGqxlK43hmJbjPVwnIM48qVbrHRrML3UZJTpRBLkyAM95O1FFHVtDkYcWcoV6lf4rK36UpjhCm6YSpFv9aKQ9/slB2X5muZO6d7PTL2IZkVp/V1ZZ8wnz+IFFCzsEfBebdVhWpEnXdjiaOaxAo3elnW3HpVjikrcKLmEAlSU1lhsi5cqjB8orzsukTbSOIBnPQ5s94LJ3Vpk1iZlvtTWGYd5ctmW8ic2xkJxRFGLnaaEXAzzXJSkOp1ZC65HSjrTRGvTmanmLZZnFJFT2tyzEotBUaMPHPLeJzWluRY3DQuVHl9tYusNKRe2xdWr+aeTIjzS3lQDtJhnZJ6JVAkMZoWXeigU2O5XCyaano8qI67XaP1QbpI9SQV833MaGQUR5EAd2NayW1G5+M+laRqE5W6eN0fdluf6eVu6cyaOs1lu/N6thOtvLhyMTYRWsLKdo7C8ZdsT14XcrHYEnPrYLjVTrR6IIKSdSfbU3Z2N8fNdcrUROUDlpo5ggO2jdGgHr8Wc2bVK1eG3WjrVjDH0TzSZZN303minFrcSrFJn7trgR+Vq8S6pOH0PDLkU8/1Lr9xsE48XUWfOMz6kX6VtwdB4kK1taA7OJTDi2Ni25dwtCBNj9Vdetn27FU50oq1YY4js4uc6/Yyy81NcuxJtGgoTMMoUGotWMdelq0zQpF4ShCu+bXWM0LniFDUz550yTcqhhrKLB61izEL5+kpJnVqvHWdg92P+UNT6WEbWtg6O3oTvdgsmbavNd5bCmvu7IjBifA8qyu5eMQJJyAyAqMX6fGSr6wllqla7DHl5rpke+doWxoXN8fIlg8L85i5HDOlZwWnHSeWtj+0EVXvpJ1ggdVkO2+tSOL34DBOXf6wVcSUYOOu5ca+YF4j8zCBQH5BCviW2Y0i8eJ3GXVu+llzxuRJJTLZpLULfGmN6ctoOjbsyq0dzFFZf8vVPk1J0uFMEa1U4Qm6lq0zcGRTYoL66vRiia1SnF9eOaCHdm6n2FJYVV1K0iHRW2dKV8PFXuDljDQpTeQKK1slslWCMr/uU0O35Z2O+u7xUmPXA21dGoJsWDU1vX6jk4rCJX3Mo8e4aMqdfsSYE0M30jKDfHS7Vpy+1Md5wpplaMxypwT93ONqrKoL2B62chms2AVNpXOxbgrP6OboeRqj5O7MR1O126KjMp/iu0VHWuyFxyS0n9arMcVa6imDu4Y8WB7668KMdhLd6BV/ui57Ty6IEzWa9XWhEd6117lly0XTFpewuSuQnbH0mCzalgvRPHSoru9KrCTIUXw6YPC2rGy89lSNZiR/DelVqUUSM9tRdDqp6N3Cbq7pyV8fI9Jj2bOAujN73Zvuxd2rbTOdhkoSSqhh2Dt+fMIrbTeZtuhR1ZZmqAlrq5UsflXmnSFSfbfE18ExIJTdUjWD2r20sZMS2xPpZQe953DFNArSXDEbPaWyvcoHiy1/sahRzgbBGifm+WY/TtlshUUam0jb7Y67GoEBnLhpNcvzFmMOm6b5hOcsfl96Mz01u/XVKq8NPsunc4Kbno5rLTa34qzwCMfrugmbWdyqmeiM4QpmihnFBDurmSOmNml1WGbiV1Y57BgSqHa17/iqaNGr0naSotHYON2capett7C/TSrKVXCuCMe4ydVCt8q3OWm4kAFzbXzfWTKjNE/ORMfmarjZWsr5rG7Yfr+c7VYrTzK18GqowXkvumOp1U9li+ErOmv7ub0vDmulnUb7pTGmlZOSsLADsTLtEUmkkWaMrwKMWi82sVnavXEOsq1IFJc9s2g0kZDUOT/fStx2r1Keuj/wjWzi21VpLtztAlQxM0pwozuvI9oqdruFZuE4gad4cT5xbtFcm2qXFFjmmeKxMpr8dLGxfDqzDLYSMiUeiyHVdIsNsK7HsAp3p8Vs2Ri0J9CGpCsUWxAQWvBx0hw30bY+LYjTfjwr9iW5EpVr01QUiLjGssV1ZfqFo86cgKgbcF1rXX2ekTu3hPhpTlWpqTWUwkoet3BG/Siy95otV1uGyIS2WiSbpS23W4cxbUNab4XFTJ3tdXqThM5ScnSS7w1UxzfaGOUue0s6SGPsoIlLbLbAnMkyHIsX+ZzPZf0AN35lxAIg9Gs33xxiJTaq0Vqqlym+rHgSHFsxWWwCUcwowJxVn/TK2Fvtlma7ml6JpFIEo6UPPaGLoi3RvDazLIGpTma6tSVeXUN8gdlWCM6+zTW0bG6ww2ZT8Ed9XkVB7BninsfXrBFg00Ym6Yl5YbkxVtDuFtRqg182lLfs1F1QdcnRj3jDZnR+Kfn8ZZpbI2maynMXlxR74cs82onjZbGMXQIzWndRsitdWB1s1cguo2qeFCa7XIYrbpReqcY5W1MVZ73z1jnp10sytYMpCXBttAl4YZs2ugGK666LCTBC2XMnXUeEPNnG9sqcOTW6pFKXni29s1VAXZt1wiUtqp580cty0upZ/lA68wl+zBwILIxueaKkCWg6ZbRS5tycn054aUzOq6Ok7Oh6QfIWv2m2FCPuWHXN5Z1sa67db6WNYZGSwDGF4TSMuxLFJF5EBlOsMXPLT+Mj55p0HLhXOiCm+4Az5JrIC7HtxKkAiwUTjLnoC1zhbi/6IT9Js1AaeX1fTkcMTaaTpC072MbEBSET8aF352LYXl3Z0UrqeJnNevtoBCS1Z3GCH+XLHQQbaF4S3CycYWHQUb2tGNa2HJ2YVU371LosuJVNxIEj11y3QreaY5bRWTheNxJZ2qGm791oubBSpScyfCTtd14klXpg4eRiJptiXlaGJ4/DqN8KUyrsNby1S2F6EknN0BQ5NQ1lLnOj89y6bFUbS9yz4UabC97xZuNv4mjtM0GQaXQRax4tnzR8t5zPa8mFo52rG5wRr42EZ44ytzSc3Y+wy55tDhUc8CgVVoFQ6jQFcm+Vj9dxo2fKZlIEbE6RbNSnDdgu6pRZnI77Kcn78iS5lOcg5iqwm/YKuQ5AyBFVp/XnUbQPyvhwRAWgLLBJxWDz0N4ut5Hg7qo2RK12OVsQ6rWqJpuARqNwGlq6N5Pjo7CesROhFjuwakdkuSqyvkxcv5qvfE3dHG3Ime3HksupykQu1GVfiuUE9zl/NV+Yhre/RDFLzF1jrmAijlGzcHvB6RNjrYjMnvNlHVD5YnvYJVUR9aeDtNoyQbhMV5suMpyoJ/fTiJqxsRRf/T3qYUlPW85FWhJclc1EjFcm4swHoqOelOmEjqV0tJoezWtmutyJ5ngl7ShSi8M+xeYndLKZzffaUYR4M2ZqjLGU9T7RdoEYpd2MzyNmFBtj2ZDmrLXaJarLLixZM65EUU43m3lECmsfFyZKaVPEqtVqFUUvXaOrAr7EvGZjigl5CeZKVS0ZB24f5JHJc9Cr2oKi5vNQuDTNGow8UBwb0t44pFipMDXbBB/bCctm3vaS+XtzdvUW+L6tNijOdeYsoydiXq/566a5CktJ264dmJcnv9Ih1vTq/mIQqrgOtJIfzTtv7bpbak7zmaug41NQXlq/JGr5eMH29AgON1afdu5BpryC2qZYjjZowMDeS8kQterHRg1olb2ctOCsKMqMEcbZ2TJHo66p2GZ/DvnSESD0mXiZ5zU2ZwXqNZABKbR5NfWb3D3hI2E0qs/qCKLXOJUy1kRHEBpTAGAsqZ4NBmtkgbYPOLtVsrJuCG88I/hkF1xnM/J6Wc140iU0NO+UTYAp9fy4P89np1NzWSzVrUlMk9zDDjvYKnuBlK8MQfP4QaK967lVo22h67GT6RiYhQt6YczD8ZbwzT7OwBIWZnrxLtLckSU0v0aubLLksZ7p81FLEQQ10uqLKrj6WKytuvPNueADr8H0fsOMcX5XrGfaanSuLYB6R7zDg6kc8xGabc3lboLSZO6vd5VyKPwjhK04WgnlTpAyicQXk+mxnou0rCZjdxFhma2e01VyKdrRWHWPErW3XUc2jhP/ZAM87ezxTtDp85TpmvFY4DXfxF3piEbpCu6v5UOTBe6asROivpTLdiXy9HzXdmG/7kDE03u07Le1zDbTi4pjXhQ1pbQY+wczyt3WUlTFgorMhSncygcLpzM0L7Tl1RkcL4mTiBl3PeGJROrMSrIXLlqiAapjHu8pk6XVBsxyorVwrC9R/SDto8lUlcn2tNB0FcDuF27lI1dDCOWn9FzXzTzlDkSb+TPZ7a7+wV057bFWFHozWYVVKp5JOjpYOdEb857aeikTeGERrHKL8MyzpPbrwNXbdkVTmyor6V0D4VA4z1bKemrxqMD4NuHOrO3FG4FVfZ2sAwnuokzMvAgyzzDjmnaWc8JyFk0+GXnpduLltHV209Jm56PGiQ0+d1F14ar7lBudNkRBXKrLMlckzWTVPWgazVpqcPKtac4TFlt5ETOCOubztrepKPHQc5NOivElNMOpvfbOrrQgrpUzikZjsqZwOmxNw/fNyr7yqwXqMd6o2TL5Aljq3JnTREBlaBeMGcdBRc0BJ+PEset2kdVCBU6+wwjoSMeX8io8T9Bw05Br/Opu3TxlVlg32yjz4nI8GPicJp0OrU924XX8yd6YLktGzgLHJk4Y2IegOZidxowm+3TFb6wtZfSmvwPLbpQmEBCfuTPLZ9Njl565koscn97KlOocqtl1Kjfz8SwVizVVxLTq7CC6LijjCkzPweHmkvE8egSu4rHE1gtN8DA1ddlDR88XF8KjJwdtTDg+QQPGnU4bd2X2NDbbW6jl7UpUmrnZ5iBPwow9r2I46qsJrYssLlG1cT6WTN2oLlGCTQgkx5ni9DibrYPaac3gHOSYMJEOAp6b7XWOt5vJ/LpmTxLGXuTpQaAXl5PHx5Ge9Ed0ynB8WaA9t81oU6aFyUxpuishlNNkEdrNeb9Y7jcbbz5d0r6G8Wi0SrzdkcPTjFGt/YLv2XxRy1RM1ge6al0lvLI8Rmd7rVlI0+n06fnp9m706XWM4Rj9/DQcvT8O0P/J09fgGhVvDyY4hbPPT/93x4T3I7v392m3Q29ge6836a//lH6/Pj9VbgR1uR/V1kkbPA4F/8fx5+e/OI0dCPv7u9zhZV/XvL9qaOzgdk4cZV5bN1X/VudJezslhn5t6+EvOOrhj3xc+PvpZkpaDCf0d1nwi+3ejszfmvzNi+oir4eD2ygbXmABL7Kb98vgcZj+/OT1MDyRW7/hFPkGqmKw8PFGZzgmHV7pPP3+3yYdPA2BJgAA -->
