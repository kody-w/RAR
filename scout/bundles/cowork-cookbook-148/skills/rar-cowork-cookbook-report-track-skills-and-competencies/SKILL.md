---
name: "rar-cowork-cookbook-report-track-skills-and-competencies"
description: "Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_skills_and_competencies", "rar_sha256": "3809f5df10852d5a5c19fb69a3539257c8d817e2b1252ae87088b9c29178df70", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 3809f5df10852d5a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_skills_and_competencies_agent.py` first:

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
    "version": '2.0.1',
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOi2LbnV6HP+yOzHplHBgHJGzeiURCQSVFUrKzIYgaZJxmq67v3Rj0ns96run2ro6M5gwx7r3n91tobf3ux2ibMq5cvL3vPyiDeSpIo9CrIylxolXd5FYOPPLbBH+TkWVNFdtvkVf3y6cX1aqeKiibKMzB92UaJW0MWVDdV6zRt5blQ3aapVQ1Q5RV51UC5DzWV5cRQHUdJUt95OHlaeI2XOZEHbjhNdIuaAeqiJoSavLGS+hOY42Uu+JyG25VnxW7eZfUrkMDrrbRIvPrly8+/fHqJwPnLl99enMSqwa0X/c71MHHc3xkymbv6gR0gkFhZAEYWA7BBBq4Lr/LzKgW3XM+Hnlcfay/xP0H/+Z9xZ1VB/dOXrxn0PL6+TD96m0FN6AGBrboBajtWYdlRAhR5hZiks4YaWABYJHuaJ8qC18fM75TyAvrn9Ozjg8lr4DUfv77kQARrMvDXl5+gvAL8qnY6f52oFB9/ek3yzqs+/vSdTt3aV89pJmJA6tdvz+snWTDw+9DIv3P9J6D6cKXtfX35QbnpeMg96Qlmvrxe8yj7+CBcVPnNy6zM8T7+9FdkndBz4iSqm3+L7s8PwqFnuUCnp+A/fbob+RcIfir0TvOv2RbArX9HEzD8jd0n6Gmov6J9t/9/IZ1EGQjeN4v/Kbk/mwD/E/r5L3X7VxM+Qf7XF9ZLohuIDjvxvkC/fdtvudXPH9zvNz/88jsg/X8ks8/byrlT+JZaWeR7dfPt288f6vvtD7/8/KEtQKx5VvqtrZI/o/lndr3z+YMFn6M+/nEu4G9kcQbSGXqPdOi3vPgf1e+v0NFKIvf7/foL9GO+TAcMTUq8MX2Y4IecqYGsP9jxp5ffAUZkD3iaHoMs/4//gJTIqfI69xto7+RtAwEHN1HqTcIfwqiGwO+U25UH7FpHwLDPcSD+Jw9PEgNc+/V/Onew/Ow8wXL2wLxvd8D79gC8bwDBvv0IeL++QgdAO6+iIMqsBNKZ7fZrZgVe1kx8i8qrveoGEMUeGu8zwKLP0wkUZdCv/w75b3dKr8Xw6x07owdK6StxQqi6TbzXSctT6GVPnRxQAbzec1rAJMkdIJEfAXj9BLSv8+QGEG6yyJ0b5EYVUD8H6D7RBlb7MhH79ddfbasOv2YPSMWhR4moZ2DAuzjQ589ANT+JgrD5mnlOmEMffvv9A/S/oH8160584rEF8P70CZBws9dUCORYm4JhwF3AwQBA7j757fengQGZDNQ04MHIn+rMNBnEaOy5b9beC8xnjCAh2wNWBhZOJ+sCnIai5hUSfehd3mctm5A8zOsGcr0CVCdg7wFQtYA675bM8gaqQSDW/vAJamvvzvVXu7LuIqYg2a3mV0hZbUHdyBPwbxLzPghMzrMImP89Fh73AZHqQw0t30i8QuoUlVBhVVYRVtaTh289/ALqxdt0QNyCMq/7mk1F0ptMdU+Rh3nAIGAZ5+nSz5PPp7oM8MCt33jfx1hTdTvcq1z1Nauf4W9VkyscUA4A06CN3Kko/OMZUnWYt4l7tx+QdKL09IL79Mo9Bg//si3YP9uIR0GHvrYYgs6h/+8NxyQow/M6xzMHjoU49aCbDwNOjdFk6EcvNdEDUfRIlu+9wBuSvAHq1yyJQDRUwz8eI+9mf475QSWd0e/0gc+BASe695CcQqyq7jp8zd6QG4gM3WEKeAXkL4jvKazeGE5P3yQNQZJO19+r+N2FlTspDcIOKlo7ASHhe55rTxZswmpKq6ftQXx6k3W7MHLCP2gFAerAAYA+BISIQKIA291Np+ZATZBRfpWn34dHU28EpHBbB0gLOk/vFTqBzJiiowbpCBqcaQywwoc7KSj1gI2BiO8WrkOreAgzNatPAa2nL360//PR90i+SzIJD2hartUAS3YTurpe//Dru5RPTwFR0yn37pP+6OynptCPBeYfX7O7hO+ADlI6mWrzD6aBQCqlj8icEKkGqJJ6z/ABcXAvw6+PSvoo1e+yfPlv/fnHv9fC32uj8Ue/fYHCpinqL7PZo569lbNXkDagpDlR4dXP0vb5nlqfH6n1GTD7/GNq/YH2w1RfoL8n3x9IPMP6C4S+Iq/I9EiOHG+K2+cBzLH6vDQ/z6enXzPd++5nwD5PAd5N5h9ALX0vL29DQI0JKi+YBj/KTT1VqQ4Uxju+Ak98zd5j4ZknAL6zYKqNdf5D/t7rLPDsw3HvZQA8yhrA2526s8Cb1i7JJH7tvXzJ2iT59JJZqffvrVkmtAcBC+wxLXZA6oB+p5kegSurdaPJKNP5H5dn2v3ESqbsyqfKOUH7O5beFXArIN2UjkE0AfwnCAgdAFicdOqmlJzaAxvoWAOY9dxJiWYoJqkfa5qpv3pvvv67BPesBnDk5l+m5P4ETY3yJ+i95/0Eva1C7ku7rAXLsJ+nfnvSGQwFH+9j31eftvfyy5+I8Wy//1qIJ+I8MN6yp0o1qfgnOgFqlVe2oDS6kzzfFfzON38w+/0uZ/NYQP728gYqTy89m0UwHGTv53oqjjMQy4AhuH5EHXj2f9VGPmkAIAQtDCCCLxDaJ1wfRRYE5hIW4aC0b5O0hRM4jRGUs3AXKOVhNooRmOUtKGSxsGkHo1Fq4frUJNMjficuaTTJ5SG+h9Mo5rg4iRHEHAzFLNq15pRluWA6hVC+C2rF96kxwNGnsg/lJku+d7T3YH3o/NuLTc7BSGFei8zjWM3oozXDZVsNZfiMwEtzBu/wY2GkzYAe4eNgLFzUKZICmQ9ui1ACajO7lZHm0kVc7tSavGI+yQn4alsndNsxRVRILpESpLLA5o3RMdHiDMPbi22sOYN151Z6nEsemY04U1wuK7E5EsehjCO0bqXFucTik1mPx8uZj470bBYbiwo/eaZVdmOzL8o5LoUMfrhu6NOYHylD6pXMpvZ2hLXNsZaOY3nBBq02jBOPjzp9KfaLUamqrrbYzhfkBPMyeT7zs2yeHBJ4tvVreJ3C51UoyoOgrtCUuPCFiMlztNtj6FqKagIZY7pDF1oM1xIZlQTf6uSlZEtjpPsq2x4PWuoQ8Di/Kkf5vL+yZnWS+30tdI7dMTtw5UVEHVBlFDVJtZrL8cUvNkeLqhtM08OaTmixJb2ZlKy9MuZOpSnBiLqMXU9kM3o/nstLUCUOLnr8fLPSM/u2CmT9aNHntkDas+ExTtxt+Z0sSYzrJ8hZUbOKa51qnW7aoTmmSjyX1kQ8lOg2b48633sSVZwPK1Q0jgpxOqPjTuh7eBDl9b7mEcxi0Cqh5CEtDmmcnA4dCO+U3o6hKReFomAVIxcszw0xMteqVBjFRMHxHG7cmkMNgVt3eJvZbI1nDFzdbDVwtw3SbarN0k1N/zLLnMDC7bYLM1ashLlFyBHZnDZmtbbEtR/RVTxU5kEMx1kTlErIZRt9hhSr7naZhVth01UnMzpjnMx60dBv52fH9ve1W576kGCJEUO3B+ewb51C61vNWJOX8Gx2HL9XPFc615jm69FGzQnwF8ooj+8PZXS7nNI82CLkvBLNQ6cLnbWd577p6VW2zyXEZ7bFNbhsfRqmeUdha8roq5vZJv2mWGS1Na7tFVFb50NM2aUZOxXXWTF/4HBrf93X8SyUWWyzWyh8cBU1nW2Lw3oXcBtbTTbGmGuae6BW+LyNGnETkcLK9BplR3crPx8YK1diSxeRvbMbnUMb7JAddt5LWJ6n4lUaSs6qxz5Pr+JIe8PmvCK3S5kiGn1OjEEs7tw4i4SNymTkoYh5cccZhOT0I5sWC3w8qHWZwG2MeToby94xt3simI0zrTdx7xYxYm/Asra3aGPeyuuLz4ocq150f0PZijVWpwUXKBfKWC/Wpc1IxX4mXTJYjkpBQIZuv4laVec3FqFcBXmuczSys9JWydHOmhGeyJTsnO/UOXwzNvEChpE2OrAnZ5mh+3ENG5cYyciyL+gzet4jEtbz2bqYm+sjflpuFgiX09QRUbi0rKIoQFA7RI2uYB10a8JwoQT2SB6OpQELEjfSe7kvVohS+0F/FBcxOBPoaKkz++Iq7eRbE4XWnojSbL0U49W6Wa5vaX+Cz8omhfsOizibC27isSpxpXUMEB4Of+FHFHHi3B5Zp6I2Wxm2cWASGrZOIdr0t3Gh875nrNuNqg4uSuqsjI3YKPXqIVT8Tpm1eW3CkYNXSwunZGtFHhcsRc+QHa6SlL5zRl5cUTG+WZlt06A822UZv889l8wQZ1ivyXm67uY2b7IabezEmjbpixWLXKEd6sNIdQa2Oka64/WLBVw0ozzkpUM4neEmsbXIIjYPDDHrlqjSS+RBunVr7mAnmeJuCFZhQmkf6KWB5Fh1kRribNdzktfElddIopgvcmsrDTUa67ebxq+XnSsqu2so1vVRvBzzscsF9lprZ24pbk9b4WSxZzFnzzB/kGtPvZxrindVu0dJWgP462ejHZjjWWtv1K3YiMoGm0l5ApBeDQ4n4ZA7B2U2q+NV387Ja4PwK7PcjbB/iUHt9LdrbrzCh2xGo3RsiInM5FbLn470fM4GSbDWenHY9c05YOG1wSdZTaOn1mNaJW6r1tyHtrFpGd06OHrlrPdKxRfCIUbFxZycr+I0t46l3AFBFmLQYaJCzc99NDTyRXSNdXCzdAlxlljpufvjjqLrYVl2OUOW4f4SE8vV8prg69ZcgGVu380yYqO7e4o3VOkYaFp6Sq9sjobHbLRMq9knzt52YxsjKtqtA+Ys1lfNFkJ4b6yFeQkCvd2cRLFdjPNRcvDSKWlNL+Vz02mboxo2EaVk5fJ0WYXcNapPlj90DExqPaNEqpahcgb711UaswLKFeuO4uYNU67wrZrJbVqzdMTFs3TDXFVQiXBzOIiCHESetFYbSzXivb0ZqJuVnk/L5VpgNmWK1GjZ8PsgDM7LYG0czrNt5yD4LraaHYDUmyoa8FJNKgMIHS64qN+3+kAVYoJwnlmhHG8VCJsVBNUWSoLJTr0pe41bgF5irZPKcUXhES0LW2sXbdja4Hf99uRiGpkmRFeQZtSNlq5nhbRWUAWP481MwwplB8v7y/66qmzMVM/Y1TrlhNvJmI2fUSmUslavlWXIkHPbUPL5mnDxSEBWdRopswI5cDRQhzvCZ06Fg60zN7RFbGwUFkGXJbIGwKZhq8FsuMgo7UTkApRPVjvh2B5HjQnRmRWuqXqrnreFYGCSxZwI7YabwmkRzpo2tped4m+lOTdT2CQlLAAdCRnTJVlmUtRq+5CaEf2MNZHZrot5Jxh6DS/cWL1GGmuSmbXVIryxRSw5o+QJOxfI9mTeNsk847CBQmaKRMuDyPmrFiVuNmNwO3ZpBJXqnZyuaRJfHLDlIpJQpd7RJ3m5yIiUVg4AinkkZznVusanQ5JIV4W6EpvF8bKRRxeZEdZhu9bFRTHb7ZPDbu/LruUkmz46IqXFFcOhEHRF0iNnyVSnY0ri55W631Bjm1Dqbr3g9HE3Nk43hnRuRhls7ZBC9JC4LJf1fLM7Xs11xQRRejU7E90ohcOhWLoYBykbe2JXHkXCPdjIviOJw7o3gdaYaC37g9PW19iWEEuNkJWXN+i5u/jSmRXOCxZRw6snYVxzqsve2M1uG0cy26123eTXY8EG11DPZapex/mBZYOh1LDlOuco0/edok4dqoikfXpR6NLbOk24EgmVzxLHaE3RWBs1udJ31eKU8sAx8gUfZhWLUitnHiwO422HOZwnpgLf8JQYnvruUEnrtlvvK2TcOGO45M48WZ8NpfM5+Ihwbe4IO6s8ClQQ2vNNt0pHRK30rI9L8SwcT0DTPSeiPdva2qq9MHK1uy2UZHRH1ZCExfKSkp0lEHvNj9VsoQf0VcOw1XoGM1Q5v4a5ivmStUsC1QrEXJgPJ7mRqcCAOaM+1/imUR2uIEFfHt1MaevMSvZoFU4fWmao1bCl3jB8lffbHUfymJjMw0ZYYrtQNKMtKqAoc+o8DJ3N8ysnej5KB5QnL8PSW8rFavRNaudq11iJzVG6YPWYEO21Mdxmc2P4DXWsVFkX7YSpUHqOw/USc/mcs04mW8MXcX3cLZgkzjTqeLkG64OnSirCWbfBvsXlpoPjwxXRMkqorierKweOwsjddi+om/U5juXFyrK3cdv3JKr2DCx2GndpGWzfpC3RmtZJxUkpZhW9vyEr7qis6Wa2RQScODnKWJNyJR3YzCGxzf5q8FokMYWXm65g2+fO1RmpqdCqwljOFzSkIXp0SDzcZXC/oNHOWdN6SyOl5+CqMdwWltDOXdw3bi5GYkvSoRO3xfUrus5sHm5rExUYxaQccoZbjhUQbrEBXmnD3O0sZ4Us0Vm7ua764haC9aQ/wLktllFFpEoY4QxFa2HnanWmLlF4uU6WM8rvbqRucSu/t9ronKFm6kZXhLE1Cj1n5+zqi7N1e+39VX888AkCN4xftVQ5gNWZXl+9WAhn69Pmds0B9axDQLMjz+DFVYU7nh2iMFrOZsp24W43MLwydrxyq2hewTgK5sZ2ceTr0mBcPRUbjJFQtD+jS0Kuz7NAj7LYpMmsThZE2THInFoom+uBhZmB00r5uEb4jTIr51sWAAhJJa7mJoOiVwoW6guXXhIt45Z75oA5Enb1DHOup+FhFMmDst0WtmEWdlHU5+0+8vGrwWmzhkJVGheuJ5lXvcydh905s8/Hfejsmj6zdt0l2SSZJQr4yaVvc1GQ9Ebd4GiHUG48In6Ro7iE3AaipP0b2feLaxKe3eVyxijhck23bOHS6xDHL7Bfu8pyhdvnprnKkjjYq5s2qiBQnNvhbG1Jz0TkoOqXxBjCxO1CzFakb25akbmNXEUQnDHjN+0mFHbNGOlaF3u1cda5TqCHfoaMesTJy4ytbweXAgu+o2gRfBGJUhGR5jKw60DbRUHndickMhbUcnHZwCymNwud7ul4PV6RxNZJWjTyvc7iVH6mEHIrXDWRopeIXKUn64TzyEDanIHoRNgEIp21NwQP9rI3FgoM1h9w5oBFUQz7rrgnEprrhxSFt+OA+Z4ouLQbSen8YGougpASfMl0V83V4XZJ+h2xVKJsZRFNEQqOiIDcEE6jTQiXCreXsr0Le7YkSK4Tj30ThiMa0ssZgZGNamsirakljMFGESBZUSM4wbZWhFM8exhtU9YCvG3q3Eawoe0rqxlY1mh3YaTJlbm66QCAYVPtGCNzecrPqmM7xj3oOwfFJwtUOS4l+NA525WnqzGK7htS6lmxaWbh+sYziEouKEVYusSluQ17v1FaksIY76x6C0b3aJgJz+K1kWGiEGi+ZM9Y1vmugLnIdT76WrmLaT7Bro52S6u89B2Jx6mtn/u3xWJHw0d6Rfn96Va1TCIw0sI0dEbzjOZ2Ol+ttT3K9dUq3J6/Fmm1aEp4SW1m805doc5i7pHwVhC0ztBHvYsyDxR8iuo0GT5Z/U3hEjJEaMSizZUaybJF7DiXbXGC2V5nYShz3jkBLV7G5gfsYrVFswNe95qbem6q9uRq/Xjcb2t2r1C5ExFSfMYUIexA84UVVbfNMirdqUGwb7icaZrATWf8kT/iZIDHRA4SLK7iblhUWAcKClKRR+pU35yaxVeO5x+OxK3omdnoakjKDDN9ufKJSr8osHpLEMEgcPNEkTVzvIBcOpnOZin0gzzM5V1hoqZzbE7+KAbHLQzW8XNshLE4HDPXCZl5x18GVcXNFZIrqoodOZk9qBgeyGMZy4UYayI2qzO2w9PW6ajrhhSs7DKSOBv4M+YC0ves5RLDMC+fXqYt5OdG8N96vzvtuv0/2/x77NO9vRa678F6lvvlzuvL3xPrl08vlRMBoR4bnXXSBs8twf+yzfn533mlMFEYHq9Op7dYffO2d95YwfQVoJcoc9u6qYZvdZ60983WTy92W09fRqin76s44PPlrlxaTFvID6bgJIwq71uTf6u8Bpy9TF8TmF7LeG5kNW+XwXPb99OLOwAfRU79DSeJb15VTGo+X08A7bBX5BV9+f1/A27xr25ZJQAA -->
