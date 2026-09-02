---
name: "rar-cowork-cookbook-report-evaluate-campaign-performance"
description: "Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_evaluate_campaign_performance", "rar_sha256": "ffca062dc109d47d683d17057c6ccc3d42de3786dbe2db15460ff9232335adb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_evaluate_campaign_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-evaluate-campaign-performance:1b2d03a78ae5767d8141393426f6e6604c993a348f9d8d544af6fff78fe91cd0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_evaluate_campaign_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_evaluate_campaign_performance_agent.py` is
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

Evaluate campaign performance Summary Report — Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-evaluate-campaign-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 ffca062dc109d47d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_evaluate_campaign_performance_agent.py` first:

```bash
python3 report_evaluate_campaign_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_evaluate_campaign_performance_agent.py   # or on stdin
python3 report_evaluate_campaign_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate campaign performance Summary Report — Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-evaluate-campaign-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_evaluate_campaign_performance',
    "version": '2.0.0',
    "display_name": 'Evaluate campaign performance Summary Report',
    "description": 'Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-evaluate-campaign-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-evaluate-campaign-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9da8e0f77b663fb6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-evaluate-campaign-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:evaluate'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportEvaluateCampaignPerformance(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEvaluateCampaignPerformance'
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
    print(ReportEvaluateCampaignPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjyLLlX+Hl+1Ddj6yUWAV5rc1GQhsgFrEJ1NWWxQ4CAWIV9PR/n0BSZlW9233f7bGxUVqmJIjwcD/uftwjyN+f7KaO8vLp9Un17Qza2GkaR34J2ZkHMXmXlwl4yxMH/EJuntVl7DR1XlZPz0+eX7llXNRxnoHpiyZOvQqyoaouG7duSt+DquZ8tsseKv0iL2soDyC/tdPGrn3Itc+FHYcZVPhlkJdnO3N9yHbruI3rHuriOoLqvLbT6hmqSz/zwPuoklP6duLlXVa9AA38K5CS+tXT66+/PT/F4PPT6+9PbmpX4NKTclt19ViReSwof1sPSEjtLARDix6AkIHvD23AJc8P3nX7qfLT4Bn6r/9KOrsMq59fv2TQ4/XlafxRmgyqIx9obFc1sNu1C9uJU2DJCzRPO7uvAAQAkuyBT5yFL/eZ3yTlBfTLeO+n+yIvoV//9OUpByrYI8Jfnn6G8hKsVzbj55dRSvHTzy9p3vnlTz9/k1M1zsl361EY0Prl7fH9IRYM/DY0Dm6r/gKk3n3p+F+evjNufN31Hu0EM59eTnmc/XQXXJR562cjjj/9/Fdi3ch3kzSu6n9L7q93wZFve8Cmh+I/P99A/g2CHwZ9yPzrZQvg1r9jCRj+vtwz9ADqr2Tf8P9votM486sPxP9U3J9NgH+Bfv1L2/7VhGco+PK09NO4BdHhpP4r9PubKq+YXz953y5++u0PIPp/FKPmTeneJLyBpIgDv6rf3n79VN0uf/rt109NAWLNt89vTZn+mcw/w/W2zg8IPkb99ONcsL6eJRnIZ+gj0qHf8+I/yj9eIMNOY+/b9eoV+j5fxhcMjUa8L3qH4LucqYCu3+H489MfgCSyOz+Nt0GW/+d/QkLslnmVBzWkunlTQ8DBdXz2R+W1KK4g7ZHUX1We3e1ezt5XCFwd0x1QhN2kNbQp7TiFQD6MHh8tAET39X+5N/b87D7Yc3Inwbd3Bnx7Z8C37xjw6wukRWDpvIzDOLNTSJnLMmSHflaPi97CA5Dq53ZcF+gU33lHYdiRc6om9f8Bff13Fnq7yXwp+tGYLxnwjg1c5kG1fwaT7TJOe8ge2crpa/8z4FnAKGWepo7tJtD4pyleRoQOkZ89cHNB+fCvvtsAdk9zFygfxICbn4HrqzxtATuOaFZJnKaQF5cAqhyUhpHUAeKvo7CvX786dhV9ye50jEH3+lJNwIAPhaHPn4vSD9I4jOovme9GOfTp9z8+Qf8b+lezbsLHNWRQG26YgZBOIU6VRAjkZ3MGwypoDA5APjf//f7H3RmjdhkoiCCr4iD2b5OBtG/BMFpw99C7e4DNo4p++VjpR9ygLgK4QHEN0AKZXj1/yUYRORhadnHlv4N4n3yH/t3f93VGn1QPDIGfgjI/38be4nB0ppuX3gvEBtAHUo8SPHo0yqsahG4BiqqfuT2YadffXJjlNVSB7KmC/hlqKmDqKPmrA0SP4JwBRdn1V0hgZFDt8hT8GQG6LQ9m51k8Ov4RsPfLQEj5CcTY4l3ECyT6AE2osEu7iEq78m/jAvseEaDKvc8Hwm0o8ztoLO3+6KNbXt8ib/UvOwn10XncewDoS4NOERz6/96jjIrONxtltZlrqyW0EjXFukfV2EuNRt7br1EeWOGeIt+6h3eieafgL1kaA0+U/T/uI4NbIN3HfGeSMldu8seULm9y4xqEw+jfshxD2P6SvXM9UHkM7WqkLZC1ycgB+ceC4913TSOQmuP3b3UfukfaaDSIYahonDR2ocD3vVu411E5JtMDexAb/oguiH43+sEqCEgHDgDyIaBEDIIUYHeDTgRJAXqle4R/DI/Hbgpo4TUu0BZkjf8CHcYgBoFYQY4PWqJxDEDh000UdPYBxkDFD4SryC7uyoz97UNBG9hhp/3gf++Axz0Qj2NNAct9JBsQant2DaDsgA9ALl3vjv1Q8+EqoOt5DPzbpB+9/TAV+r4m/WNMOKDiN84HHflYzr/DBrB0ea5usQYKbVKBlD77j/gBgXCr3C/34nuv7h+6vP5TT//T32v7b+VU/9Fxr1BU10X1OpncS957xXtx8zOoem5c+NWj+n1+z63P77n1+bvc+kH2HapX6O/p94OIR1y/QsjL9GU63trFrj8G7uMF4GA+L6zP+Hj3S6b43/wMls/PgG1G+HvAuB9V5X0IKC1h6Yfj4HuVqcbi1IF6eCO3W5X4iIVHogDuzMKxJFb5dwk82jR69u64DxIGt7KR3r2xoQv9cb+TjupX/tNr1qTp81Nmn/1/c58zci2IWADIuEMCyQNgr2P/9m2M4rf74revP2zrpNsHOx1TDGTavSa1sXeDETgYsMmYEqN2dV+M6tz3N2Ov9dGI/bPYW74CovHy1zFtQcEETfMz9NH/PkPvO5LbPi9rwJbs17H3Hm0BQ8Hbx9iPrajjP/32J2o8WvF/VmJM10sDSHAkv7HWZBXYTAHv1PcQGCvF+/0/MRCILv1LA8qwNyr3zdpvSuT3lf+4KV3fd5a/P71Tx/j53hPcIwhM+Fu92wjCe819u90dRdw6rBsmt+70zQaOHmvrd7fCsVF4uwfl0yvgHv/5CUwGHQ5ouYfbfvrprhEw5VtfO+pnl5+rsVeYgJwCkkAFL0YzEsCA3y0wXo692/jxw+tfNMP/mg5eEQf1ppg9o2yfmJEzj0JwBKMxHCUD0ifJKe7SNGZjOBXQHuUROG4HZBAEMyrwacT1Rv0qECVn+6HIBBk9AUz4gPv/qkl/ussARQQlSCAkCFx7SqKei0xpD595JIV5yGxKzFzSdV3Mw1HPx2YU6Tk+6jkIgZPTIKBRDMUwwvYcYpT3aBHvir29t+Pvvrkn5xtIt3M8qo3atku5MwT36JlNuj42dTDXR1DEm2H+lKCxgKJ8HMz/mPrwz+i+u+1j9ILuEPRm7bjO7w9/jxFJ4mDkFq/Y+f3FTGjDdkzZuUZbeEjpq6IRezU57V2Dz3K/QqtLj2d54hmYbRdhvp1bm5O/sNkQpua9dd0Ik0SBLZPgTASdTRb8oXQc+xDEusry9czHSmrSbKNw1fmnRKjIS8Pt41jz1qVADLoeD9OzpRF4ou/IUuROR8dV852jl1e0hydx7ht9ypbWeb3TeyM9HvaXknGHU9K30a43nGOvkylvHLBN2pd67ilp5sUcz04EvYUFaq1XJxyvdRPW0S2LStsTBctmStHyLkm0iKDb3TRCGMpkpWFImmPa8w2Qg17nGKU46WGduwfK4FJ6fp2kKtMweVji1DTXp9VS96lZV5j8cYWpUz+Ykpx2vPYXM6rPFyFSZPU0R5UkzWWcje3YqBlzuy405UAa10Qqs/ksZbErvb7sfJeszy3ZDEtSb47Vohc0x+BUn9UyROO02Ii4szo7EXO2D3WZFysa2VXni4E2RrltSWbLbHB37eznCwOvPWNZCPSUnrfyFex8B7cWNHUd41fp0il9eTkoeRDB22PAGLvEUIms4El+AZ/FM7e01DpBtqfDtpZi0uXEwq024bVg4WHmwr2NKbbE+d1WZUNP4/dTaX4osNXxRBIhvQS+ILrTZrKhnH55WhRHzGzSGdI3LOYSTrW70DK6U/BM6IVTNelhNp2Iua1wmuow3da4OD3Ttwc/FulGWF6bE89F4mblC6tgM92ecUBcReXZZj9csyHCWV90ZcFSmOZ4AlGlUqWn9GSpXyOSITCPNihs3cTdTiIm4qomLXiLRPnJHRbs/lJwKKFw5eGgqXWFnuzeZhsb9dMmCDvSyd1gPshXO4iyYC4ZJaHE9t6iAzqMG7norvA5Q8WrxxTODOby1kp3ysEJ4sY4oIKa56U6nGOVHyhYlJkgjjkk6Tr+2FJWv4x1+cTlLDU/K6UkU+ac5UtplvB2ulxmJhwWk8HkAsaKk9Y11Usn4S5QaW6TQn45CdO42i9dbRpze94pF2unM7oVF5M8b1VDSDmLK49llH6MvaA3KAqdejmBqev9jONzb5XprtAehZY5cwMy7Y/tlDIch8XPiL6dsNFUbLtEIKmsnUy21rWUjGGe7MNgne2QyYmFazqixdCSjMUC3iBnz7C1g8/sNj2VM76NiuFa54JaGAKx0zlz2mMxFy8FktsJlxyRGbQ5LildOugzjTOmuxMMX/sFuT1nBzoKOM0hZyIesOiZp1x+l7JL2OSqmvfM4xQ/UU2ecxjPqaphubBzKdxTXzDWlTIBSTmqNqg0V0+DuAoZVNH40KWXAx7nXFvnfa2m182Cm01ZEJf8noxgITVPcWSorNNz6H5RVay+qHfIhSjl86RxDTdUBrRbmo3GOxd9cEDRjKREZ45rN9weKqHyBlVdr1EusWu1WGaD77rR0ieOq12o2jUV9OnFVxPTlKeJfvFy80KIIpleBjFeLdMZzzTayl/VK7H0DLHKqjRFtLb1F0iACdkJaxSKAYkjk8JyU1wxy+J5oRNDckPrXbvxPZ+PQdr7CmBDcxdb5ulcXzredUNYL2Ian/J5rOKofKXm/mI/xNGKQPrZ8kpTp12CXcJmuh5WxVDKdSautvqCZSeDUurLnSZPhR2fl3IpcWrnLnWOZ1bF2o5IrmYyQ2vXWKYHrmSvV7YRKlqTsG2RV3WtnSRK2EXzWWhFW8Y/Fru5elLJLt+eTqEsd7ZiV41QzaXBxemgaqTAQrWd1l+zQmrbcx9suerqZmJAWAsDxSbX1MTT7cbB1EYcKpcO9wdeQ0vSFc31aYFOsXW17ff5viQEfJhwElm1bXrym0lwBI21vMDLYL1U2X5og3TRqR1zspIje5xmvcjEc46vjUtxZC9zShM9bIXEyBoURGbHioYrr6QgLgzROHIaS/BURxLzVZzH9rDAmbD3V6E1Cxg/P+HDoVAQzQ6WuRxjCMLLszwRt+vDfoK6V6yQCfkqRPqa5k+wP6DXdd8F/TnMy9w/SYGXNILZo9ji4omHQrXleBa5J9iLT8jQLjokPB5WlE9u+tNSpbZx0KU0KTS2ygp+PxwFQ8bife8OdrEza1S2SIJHrbKbdIqd2HyYKj2h8pGDBatB19wu4RWThwdvsrZCobUU3WGMnKrmF77XNlhsGMmWWgXuhBQKPknpBoV7/iBPvU14vHoBj255m5UKl53AZHI+7vTlaoGLe8NB0gjgZZ4XgntYpli9pyZGt4/OgYKsMGOn7y/zxEEY5LrrhKjgKV1J3KOe2RQlCzatnMKLkXsipRt2MT1zB3EIB0plF6u5rslEQEgBdyk1gWQT+4yHSxnsZSjRmdXm7qy7+plGBxbdrHYsZhDZJunUfgNn9eHMms4OvTrxdT14e+16UMhULyyZ3hixG9OaheX0itUkn0rhrS7CG2+SSPky8PklnCkrbXrsNVdvJbY4VoZgFSV1CEVdw4dFKmzcjJHtZSBsEoMnVukmmS7S9dTaGOg+l/YZGojzCEbFnSr3LBfvuVpqMds89OFkuprtc2KzyyJ+qcRMT7cFqES6VMj2JQ77cz1we3oymflx2naLUFxliojLXlZl5oCH7KmeJRKcCjUF8i0jkNyTa3pTbsy8dzXBcbxzQK2VaLJS5bwlSETsDky+CONQTENF8go0KQt/N58ofK45c6mPbDm/BpJmEaCcleuFgLjLhPLms4IvrqZoqcfjAk8jXq05bHGINmm2WxPKToQtZqkPas/Y1qW8bKZ8ZzaUqm9NvbZWKe1ej6e1enZXjC5yGVId1paMyYZ50PPDATRn6UFhsyT3tLkn1X5wXPYnfbldsc0F2U0LR8Mkeu6okYJFuHzedItVqh6T60o4lMpVI7d6NpGHJkXU9riyBnaTLrlTdIk4Mk6ncIqgpESkR6m0gX7Hc8caBicFKz8bNFVLNKNv5hvWsjkeQVLaOvGbSN4frwevI3isto6icyld/HBwRWrGhkuciifzaY0paYFHYrvdzIfZspRSQiXWjU/DvLA7N4mIiSd9tmeZTcULp5lnVLVJLa41OSSOJDl6Ru/huEtnZHvYJ4vJemnEslUSU2UPK9eLZCoWygukK/UN6VpUdTFBAS5kiczLlc/IKIBZ1Hrdv7bsNNxIqSFZMa2zfXCQ13K03nCtnJWbBeweGnF7qFlmH+0IdkuGMH4Q40FZDeUElkIHP0U0F3KbiO91pSBcajrjTyajNfCl4o76pTLzTZcU1/nkENd51YKG+zTXtPVJGGjuAnreOkOCKxfklV8n+1il576VMOWKJj3hmudL4hrrrDtcNyyyMTxdjQRtyesXUbjoR45YbFb7ebJYULKKqJ7J6FuMXzdRPLXJdgbaL9M6SQtlm9dLnBNCZTNhd8tJT6zr4dhZJu7yKetjrHidmbJwOJLEJk97eyPu2+02io47t8ov+sE3ZjC8WCF+w4XsVLWS1FpIhUb7xS49uvXK6s7NHm42G9auZJM5oMneTdJiZmzFuKjK8ELwxI6UGtPyEFNGSeeS82NZDld7f0k0Wxa39xcOZD1bHGxq66kqSEiTTm1SO5ulUZpXqdPdE00cKJ6YEQ4D55sLrk3KXdg351lsWgeTvgrecGyQ0HakvloG7tVOstUJxrzlSSsNdpK3CTrkuMztwgO/VZjB49zTHu5n28yVJsi8KjdNxBMHwZ1P8Rksiwa8mvepJpP6kdoX02JS03M60fRQwKqjQdRyOMR0d9Lx9iBJoG3DsNbC4P5al3Citkl8KbcgiVEv07zaBuVBHkJQYrZtXs6DOndP2ESD6aZq4dXKTNBNRpsTeJfhJOPjNLFuj3FfCdzO1khxH5lVWLP+YoFvUiXVFuf10DmLDcngOp0PhRhOZVzlFwu22yTbU5awVCh1Mg82NcwcXwrn4OquI4eo7eaIDVvFdQ6GdfbI5tS5gu9epuk53p3ogFc9XDlpjLPA5jlXdSV82nLXQcUydM9QgPORhMBgTon9pisvmjXE8bVZSSg8I/dlsus1/3hOqs1eo+eA02FyaJcZMz+y8jrYhA2btd1+uYfRUncze9KrLdFOfFlnJIlxcl22FoBXsqqDdaSTdqqXw7AVm8x5NtPpa1Xm8wKprsfsCIvFzHfWpbHyAEEuhw1m6u5RoQOvKzKYscL5jkIl1F907TXWImehc+6+F9FV6WWnyohpzqkHuI6W8wGdLucTT5F4G82vskGvfSbcESFOEZdt1bEu45H8XGzXhYKu8+4Cixlj+kWFN66EF6bdhoCGAlAYl1uymnnwzF+68j5Ql6wZF8IyQBYJsXYX28ZC97wIdhVC3R8tiVtEwr4z0hJ29K2ebjIry1q8klZFPki+j1oot/VAw2IdcK3svWRK8pJbhJUfbo6BHFsXUJbCjLnQtALLLhfTSLcNjNqtMUeESVRg9/iCcJfzDOZOpbkMnc0GNNKT9dnvXEV3axQmYaMIsSyutu4qMpdLy6vnKCKgmyEanPUsQTQTbIJLN+6QZSbkp4gExYgUsDg7Me1cDYHxwYSWbAxRQmUvJ1Zbga2FOO8krXNbVVS8BEMiEd/D/MzOTEb0V4u87mk4l09S3eIzCjsPZVDBRH2k6X19FUB60NgVI5FlH66JgZIqsT3Jl4D0V+ZUaePk2pAML2IIivd+B9ekSLddMCE81+nizcSBVyiW1MFRWV5XWbo9s1zerSURbDwJV+YCRwwdw2nYqaOUs8oRBusyOQ+OaJLbWdOertehWq8MwWELrK6aiUQx8Swug8OZOkx0O1Ay1qbPud54bTPXwkkNhysBILZbbRwyzsrzeO18OZNY7YhHA2kbOt1dBzTnZlK6Xe4rTw8wC54NyHJb4fIyMrOjqJmh2U5Qb44yCx5X2jWRM9WE6uzU9HWUaOwQxOma9I/Sgj46FUoahOTAiE03Ra/i8MBEJFLjXU1t/XYbrpoYqYhmQx0HK7AINvCv6kzYHUiMleUWFXJtOx8WgjNhGQO144VpNm283Osychoi0Gu37hD61rSfbtvQy2NLXNs9xQoGN+X13VxLYSp0aFY9GtvEdO0AA22EiJhi7kWZtxP1PQ32aag0CTGHrAy5UcP5fP7LL0/PT7fHrU+vyBRHieen8cj+cfD+dw9rAd0Wbw9pGEmgz0//784Q7+d570/mboflvu293lZ//XuK/vb8BBIHKHU/4q3SJnwcHf6309LP/84p7iihvz85Hh8kXuv3pxe1Hd4OmuPMa6q67N+qPG1ux8wA8qYa/4OkGv/JyAXvTzfjzsV41n9fdDz7zoH4on6r87ezXSb+eC3OxmdjvhcDdR5fw8ep/POT1wPHxW71BsB/88titPTxjGg8VB0fEj398X8Aq+stnhInAAA= -->
