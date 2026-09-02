---
name: "rar-cowork-cookbook-eco-impact-analysis"
description: "For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/eco_impact_analysis", "rar_sha256": "342629ab28db05ce912e4199dcf7edf9c1988f159a5c388250075d00a78b70b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "eco_impact_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/eco-impact-analysis:2107e11aeb6afe49e6ce601089b03c3671e11028d58398f175eb15721ec7b2c0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/eco_impact_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `eco_impact_analysis_agent.py` is
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

Engineering Change Order Impact Analysis — For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eco_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 342629ab28db05ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eco_impact_analysis_agent.py` first:

```bash
python3 eco_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eco_impact_analysis_agent.py   # or on stdin
python3 eco_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engineering Change Order Impact Analysis — For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/eco_impact_analysis',
    "version": '2.0.0',
    "display_name": 'Engineering Change Order Impact Analysis',
    "description": 'For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'eco-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/eco-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '517aedd76241ae96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/eco-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class EcoImpactAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EcoImpactAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(EcoImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eXOjWJbvV2E8f1TWyGmxiM0dHfEkBBISYhGboLIjk30Rm1gl6tV3fxfJdmZ1VfVMR0zEU0baAu49+/mdcy7+9cnp2risn16f1MApoI2TZUkc1JBT+BBTDmV9Br/Kswv+Q15ZtHXidm1ZN0/PT37QeHVStUlZgO1cCTZBVV1WZRP4UNIGOeTFThEFz1CYFH4DBX1Q36CVdHiGGicLGqis/aB+vrNKij4oAN0blJWeM5GEnDAMvBaQmp5fOqdokzABu/xyKJq2DpwcSvLK8doXIEtwdfIK0Hx6/eUfz0/gfvb0+uuTlzkNuPXEeiV/X7osnOzWJJP0GRANPKpuQP0CXFdBHZZ1Dm75QQi9XX1qgix8hv7rv86DU0fNz69fCujt8+Vp+nfsCqiNA6gtnWaS1XMqx02ypL29QMtscG4NVAdtVxcNMA6QOimil8fO75TKCvr79OzTg8lLFLSfvjyVQIS7Ib48/QwsBfjV3fT9ZaJSffr5JSuHoP7083c6TeemwGITMSD1y9e36zeyYOH3pUl45/p3QPXhRTf48vSDctPnIfekJ9j59JKWSfHpQRg4GXjLKbzg089/RdaLA++cJU37P6L7y4NwHDggIj69Cf7z893I/4Bmbwp90PxrthVw67+jCVj+zu4ZejPUX9G+2/+fSGdJAULy3eJ/Su7PNsz+Dv3yl7r9qw0gl748rYMsAbnkuFnwCv36VZVZ5pef/O83f/rHb4D0f0tGLbvau1P4mjtFEgZN+/XrLz8199s//eOXn7rqkWdfuzr7M5p/Ztc7n99Z8G3Vp9/vBfz14lyAXIY+Ih36taz+o/7tBTKcLPG/329eoR/zZfrMoEmJd6YPE/yQMw2Q9Qc7/vz0GwCFCTU67/4YZPl//id0SLy6bMqwhVSv7FoIOLhN8mASXouTBtLekvqbuucF4SX3v0Hg7pTuACKcLmuhTe0k2QR6k8cnDcoQ+vZ/vDtufvbecHMeeOXXB1R9dd4A6NsLpMWAU1knUQLuQcelLENOBEBw4nGPhqbLP/cTmwlOHzBzZPgJYpouC/4GffsTul/vJF6q2yTqlwLY3gEO8SGAxlVZO3WS3SBnwiL31gafAWoCvKjLLHMd7wxNP7rqZdLfjIPizSoeKAvBNfC6NriDcwbgHCDtM3BsU2Y9wL7JVs05yTLIT2pgiAnGJ9AG9nydiH379s11mvhL8QBbDHrUjWYOFnwIDH3+XNVBmCVR3H4pAi8uoZ9+/e0n6P9C/2rXnfjEQwZIfzcRCNgM2qmSCIHs63KwrIEm1wNouXvn198etp+kK0ChAznzqCvt5I8fXD1p8HDIuzeAzpOIQf3G6fd2g4YY2AUUPmAtkMfN85diIlGCpfWQNMG7ER+bH6Z/d++Dz+ST5s2GwE9hXeb3tfcom5zpgYr5AvEh9GEpoC7wazt5NC6bFgRmFRR+UHg3sNNpv7uwKFtQddukCW/PUNcAVSfK31xAejJODgDIab9BB0YGtazMwI/JQHf2YHdZJJPj3+LzcRsQqX8CMbZ6J/ECiVOJhyqndqq4dprgvi50HhEx9Qdv+wFxByqCYSrgWTD56J6198hjC5AQQTBVSoi59w+QNPUJ0KOCQ+8lHPrSoTCygP4/9h2TuMvN5shulhq7hlhRO1qP2Jo6pUnVR3MFugEIdBOPRPneIbyDyTvMfimyBPijvv3tsTK8h9NjzQO6uhqIdVwe7/SnxK7vdJMWBMXk5bqeBHW+FO94DpScAryZ9AIKnickKD8YTk/fJY1Bgj4/DPlW26FHvE1mAJEMVZ2bJR4UBoF/D/o2rqeUevMCiJBgSi+QA178O60gQB2YF9CHgBAJCFVgx7vpRJAak5fvcf6xPJk6JiCF33lAWpA7wQtkTqEMwrGB3AC0PdMaYIWf7qSgPAA2BiJ+WLiJneohzNS9vgnoTL4oc6cNfvTA20MQllPhAPw+cg5QdXynBbYcgBNASl0fnv2Q881XQNh8iv/7pt+7+01X6MfC87cp74CM35EeNNxTzf7BOACs67y5hx+opucGZHYevAUQiIR7eX55VNhHCf+Q5fUPLfunf6+rv9dM/feee4Xitq2a1/n8Udfey9qLV+ZzECNJFTRTifv8yIrP76Xod6QelnmF/j1xfkfiLY5fIeQFfoGnR0LiBVOgvn2A9sznlfV5MT39UhyD72598/0EYgBY3dtHLXlfAgpKVAfRtPhRW5qpJA2gCt4h7V4bPlz/lhgPlAFFoSl/SNg7qgBHPvz0Ab3gUTGBuj81aVEwzSzZJH4TPL0WXZY9PxVOHvzFrDIhKghIYIBpqpmwLqjbJLhfffQ808XvR7J72oB898vXKXtA9QL96TP00Wo+Q+/N/32EKjow/fwytbkTS7AU/PpY+zHvucETmLDaWzUJ+5hopu7qrev9oxBT0gCJvWCqz+VHFk4c/0AEfImioP4jEen+xcneoKBpnanmgVL7lsANkNMHTdHzBPYgsUCuAAjswIY/sgF86uDSgSrrT+p+t993tcqHLr/dzdA+xsJfn94hYfr+KPmPUAEb/lUnNlnxvYJ+nWg50457v3Q36r2T/AoUSqZK+cOjaCr7Xx/B9vQKICR4fppMVyegPR7vs+7TQwAg+fceFFAAYPC5mSr/HOQKoATqcTVJfQZA9gOD6Xbi39dPX17/rHH956x+RRGYDBDECVzCCYMFHRBeQMAITNEujHkYQSLgKYxSPk5hNBUiJB64CE6iSOCRLupN4kzeyp03vnNksjOQ+MOY/5P++emxBUA9ihNgD7ZACZR2XMDXhXEvoBE0WCA07XshGfgh7SE0BYTBaQf3MIpCcRgmcR+GHZJySdhFJ3pv7dxDjq/vrfO75R/5/BWAXp5MUqKO41EeiSx8mnSADTDYxbwAQRGfxAIYp7GQooIF2P+x9c36k3Meqk6hCDo50Ef1E59f37w5hRexACu3i4ZfPj7MnDYcAiXdY+zOaiKw8JBQML2Cz7VVGdm5J+pYEs+rMbJlvyyWHFktPdUQte3OGts9j6xlJZ6VR/rcY9KJTfZ6dUMTykwioxeK3Xm0KTKTaMrel5cE1k082+tKq95O5HbkboQR1bPWQ6SR67q9bZleJpC24/SuoI2z0SaqvOBM5FIppmSLm5rLcg7GLKVycLvbbRCuR2n5JDC+RLG7smJTO+4PGkydHf2Ybyh9dQaqmAfhaiWH64pbjBTar4833mUvBt6qOVIPoi2aKRbBUtHP5rKQzPycTIi5fXVaLKPnHCki+4a9GauMt13qukf8XYMqu30e6/BYpJyOFMphfs0OQl4V4urI+5KD0E3hdjuGS3aHwVLyAwyLhUrKwgVZrCPZMC4DfDi1MS8knao3M7MXVaFUUIlZr2+a6TNWQF7zS4p2SClKCb4oSsTTHVY8JTZjOMKasxJ2MQ49exZyd8Ox22LfoH25WuZ4eyIqtdnqUY6Yh6xvC95fHZphjyrDXuXFML/yeUAYg5zGqO60iHg9F7VyQke8OQQXnBVMASWt0jXSILMv5xLh3Xwhx+l+kbQr8+amSL0mYrMvGOfS187Fc/dzszikM4DrZ8dcUlqCo0y1Ms8HbySLuBzQ5tS5SR+K5wuI3nV19Ia5Jglu39FqyDqd1wGnzjdG4c92+8YVkJBb3zhr7AQwNFxa17kaTXoza8kwoyYU5gzldNVh2FwOvauHJmzkJDfaJb6ofRtLZMyFjZ5RZc8z2d4Z2dLXbtIG0TYb04zpNZ7SaKgZ6R49XGStwW/ByIz7mXAg9Zmia7zaRdrq4OrXcKbPxrFRsd0md7dhdb6GUTm3N6fGkhdRaEmKmyv5Xg0peTfOQrlHull63hzxIPEIG2tvSu0iOWFrl9o2T7BqJyolmTfuDDp/LgkJIXX4QrmmLLZb7GVzoS1W292u5PnwgjsGt+5TuVP8TtDbLD/YiuOuECHhOsb1uaUgHs+letBWO/SW41ufj3n71rF6ekx1DwU1vTYkb7MrF2dXmGeOtdWo7CRzopww5I5azG7hap5LIGo7KUvhBF2cis4/GoPr785yVlOu4Qv4AGbwcc7P+E1q3PSztp8LHskEjXTaXLr+mjHYcHTd475LePO0YUdb2gwY6eywKF1lM3gUqRMXbORoMz+ycGitHFxYSek5Ky1TaYndud/bOCesuGIRIMXIr4twiLwbTGVFStL8kUNFHFnEJss31lEh9JwWLyPTKD1jbJiiaUwuajI2uOb91RoOhs8I+81YW/3W8HfKqrAVm4R7udwPF+yMH+vcPXuJPOoyecCEcNyS3GwmJip+lBM3xLk0Q5bWwRRRAnfljPHQ9LoEKRo5TbVEJdJsyIo3JPhWqPy22Vz2uLAbD+2O47SOsRaYCiY9XHN3u1Vge/jY0y3fyXhHlsczSh5GnTqvLXiLanJQXAPVipfoCrVQX2c1ktry88suKmDlNNqCuVXWUjQ/zPsGpvXtVbEi6rTt7WHQFxeGuyENzCwRRU5VJVmEp77Y75CBX2fldmOt141u8cmsrRLsqCxvXkFKBTZyjVUcEJ3MxXTn9VhjmuhCI5y8H4zdifNLx1pGospsiCE9XURZjrCS4XWX6TYbPIwlRuW2Ej+sdlVHoFc3uCIjs9dDbn8wWpu1HI/JDEHP3O0RtRMSYTxFKTe6JPNNlVGivXDo64jQArPJVOLmiS5XEc66xLH5NlWNS0nzmhT0gpjMJcFAqV5llPIs7tVB3mKqqttxTZ8qo+5VLVKOmFaex+V8fmbX5Qwn0hbllvxFEa747KabQTgvFnDgyV2YCtaVKsMM4OAl82c+aZ1BrRssQr+063yjzmB+ddOTxemQN7vmSoo0zAwLJ9f5bnl0dJ0jKSm90gf2BMNBCFtXxKISnLHRaEfazOV8JmVl3XLsktw5K4RlcTBcHPcbDc7prcfLqXEhYo7CqnYjBkIkCAA7t0fpfPJKmpO3ZsJdAZDyvH1gJcY30KKOr9QNberiaNgKqqttZ2QuubAW28MVFkTzFtWocTzvHWwxjLkx667XE93U7PWyxtZXOZY4CWkGWDy1OddJTh2suaN0wfZRcM0sW++5WUDjIrqGk51UINacvW5OIk85p4NucexAUOLWcWpvG8RyzMarBXXlD34dOunpsLo1DKFKsi0hYns4eI5CV8MyLAM1XLI7JtZLV2RH9nhLV62d4GZphmuLY/jTzVdw9MiJilKtg2izY/1VZ6QCkq7ycecGp5y3ytNN987MSWZa57SvUDaL+FvYuIpdJqoz0+d7HzOdjGkvjEPsVpXtn4lxd4QJUlMHcytXt6xn7ZOyIjGbsCXekmdBXB2U2f6WqbOgduEGxc6VAwbzzdI6tUJJcFa+x3hkww+Jj7q6ya8RkexZrsz3F7EbKlm7pLubtJrty0OwOFP7pUZ0qLc/bLMjMovWNaMVyYZc1QfTOjFX69zEahQ3oWOwzYJZ6ws4F25e6J/kaquje2ep7sR+bm1NELfk6ULAXsSlCLvk6oRyBm97shfjxSQul2Q9U48kQXd0QWJXwS3Z+HhtJE/xCd0H8arFaNByu5pGDi2SEoh72re0LCahkSwK9dKbGDbLNpswVq7LmoQBRPsbi60NnhkUX2xQpGnjnRjPFdYsTNYmsjOltsSs05Jim2sHB2f6iFVjjbDh1h4PC5/g7HCr1BchvWXjkgrwYHkrjIQm8mq7FTliH63afGEIB4SKc2up3DYUh103w9k5anLsH47wmNSsqGdY6G0ZTTcVCyPivB32EnuQaqY583N9p/K+h57nCWjjVFxzwACgjt6y54uh3Ycz+5o7jpbEXScYOsepRIkYkTqOa0kXBrY3rWC2kYRslyzOrOrd9F2k2W7P0ZoFB1veyb1zW6s6X6gBypeLlczDxWqzOd2Iiva4uKIdfV7dGj1ZKuZYkjpxNmkLJJqQygzqHbGurEObhlOKYGlc50+KhK/pEp9LRkbQEWP3UsuMFwJZedSpl5D9DWTKiV7uYXfboGldiRKtW9Gxww9z0CiSrt8ypz6tN90Kc60Y7vSUrWJ1zc5KntVingXhrsn6euWzzl7P2sIZrrBhIfYgYsxKi013tuULbJduSJgtFoisob4HfFb2DdN0m/xYtJcNXISZcFmeUcNc7tcr0IrjSn3Yrohib59bYYmwF5u1cQW+0Ld9PgguADWNnudDsrXS4waQPm32xoUfxHajOWMlupZ6W9lDPWiHGJObHDQgh+NAiot+5hrRSipnG789tKKnYpLh3Vg2lAoAkUqkMAV8MZLc2Pjo0tY2lpebvTRfWiMVp3KRz1bnw4o35o1tIjxiF64D8xmzcVgZCajDmgPjDzVDS3PWlQXmrBeIV1oNKfL4OFCbXpgNe1pV3YZlT7pF7PIVeZxftGLFWVHZtFKRORe0Pa6i5LZuDqtoEDXluOiUbcAdzaBeNvoBdWMFNwQNzJtjohkDqMfri1yVIm/0+3iwUeS81EeBiX0lCQUOWUhbbc9u17xSy7Tl7MStq+9IQ2Er/Lg8uQaV7DQytfLTwfL88KRxlF4mzY4xCK9wLWNs7Ubh59ouuvEnlOiq6GYuDEwg8ZNDVTS3oPfbfUC2GqibvpG0bZM2VLcjLxju+6RCSvGtxYSLtWGwNh0w3aQUVdU62tuTWmqs0so547YIO9r8mMGzm3FZoLjhpn25dTuzolGnB4HH2qSMWAD8dP7M9XS/PBXMMh7d5crImjneLlfkpWP6kctKkhdpDUfwCMND3QrRoBJnwlzx0C5tIwubFZnfkhfaZRQ0RI0WR5Z+Fs1a7tqvZEvoQVzNjQW+LjBhnM/j1Uy5LPm6Defjer7VVFTufW92rsewjDGlL6w8OkWyBsu8dzwtOikWYNI2Wk0VToqYycQSvTkHZuZi6ZFdaUtH96WAH6vjdYVrEiGWnWTNubO/DajmPHSYV7uFFa0uOu53/ho4nhflPcWNkqj6N7QPdIpMBKbIj+fEPobHEye27g1L+lW5pPqh8eQ57YriFWMtg+MqrPCHmOpmt67GmfkiTJRK4/QInQVlzM7tLYpF1iHeemAYxORjK4oa0lclhu3h/ja4lDtH0rHdjExHHNcEY6vMntxsCgw+bRW6w2caPLIntw06dNk4aWIivT1urjTpwhQ2Bpf86nsLyRSDxr8esFBeYC4O5GU5aV24vd7ktSiDZjKxusHckTupTIPlqTlSNL/NXJjvmSW7xbMYBy1M3lKq03MDToWDCJfba5ay3sxghmLlKteYRNflTUNlfz/GfCg1i5m3WpQm35drl90LsxqezdxVBAfyAsyPWyKSKtCroScidKhmnQwLHr6aFt+l1up6aLZdNGwXzh5xZ6G+3xBrLQfwRRmFacA3dB1qdZO3QUDuR7to8RzzaFs4aN6YN3NS8fMZTqephJkbSqwzNiSRARvmJzYgxbrwTS3s2KvPFHvJHZTjfL+YXReLzTWOSIr2jnmzXR6Lk9/3Hdpe9yNibr31UjKTwd2ndY+03FwhFhlqSLQIt5hEGrUyIEInNMUKbo9ySQbM6rCklhyHqdmwLZHTCrPOyhI3ZSrChUxX+/Nsm8JnXbNFWheC7hR1ruwuju41EtcdBjqpxbYX/HYWj3SVzUMPp4mF4FKjza9Jj5qjmULBaZDTCcgva0/0YOYqrM11d9FaH05RP4zr1L0kAZr6BRLMj2HYwvG2qci1G9otGGJXja3hKyRmLvxKw3UTO6GnOSGsByd1jgswMtdnoRsuM3E2yAotLg9MxocGRuE7iY5AkAjitdkKl5vMNGi472jTPbZZgCHb2oAVS73QRbZM4QMpl8tNSRxYz2HR6y4jt+LleDFW/ZI8H2jXCXtX850g3YJyFgn89hgac0Le6kwwxlTIrTzzepjtOmrwhmWDLuuY0HeutcT7Y6ZlxqxqVQ9djvFNVxVrZgjOWlXo/SxZ1dIpMYMxlfj+QnTktokEep4q2ZD7VD2csNoBQbmrgm4xP8/GA9a3BGNgpGQU2BJeHcJblxxhR5VMzKkv2qjziEbjfCh3nb0QD3s/XKfDFmTjlqLwQN/wZyK4rKMdOssVcQ6rXJarWuCErrs+h6Q4breensZGr1Yq4abwiVrGOkNnh2W5XC7//vT8dH/N+vSKwAsMfX6aDu3fjt7/m1PcaEyqr2+bMRKBn5/+944fH0eB76/e7sfwgeO/3rm//ku5/vH8VHsJkOFx1NtkXfR2yPhPx6if/+Q0d9pwe7z+nd4DXtv3lxGtE93Pl5PC75q2vn1tyqy7ny4D+3XN9Ecezde3Y/2nu+h5Nb0juL/tfrwrSKLia1tO56hJHTxNf38xvdcK/MRp3y+jt5N3sP4GfJB4zVeMwL8GdTWp9fbCZzprnd74PP32/wDtGbAhrSYAAA== -->
