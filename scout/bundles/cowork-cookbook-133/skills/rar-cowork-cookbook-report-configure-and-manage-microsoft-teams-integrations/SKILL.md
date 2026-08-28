---
name: "rar-cowork-cookbook-report-configure-and-manage-microsoft-teams-integrations"
description: "Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "bac9c98b973f564185040a2e053dea81f73a886ba75de4cbfdbee78621e7c372", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_microsoft_teams_integrations_agent.py` and in the RCI capsule.

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

Configure and manage Microsoft Teams integrations Summary Report — Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 bac9c98b973f5641…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_microsoft_teams_integrations_agent.py` first:

```bash
python3 report_configure_and_manage_microsoft_teams_integrations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_microsoft_teams_integrations_agent.py   # or on stdin
python3 report_configure_and_manage_microsoft_teams_integrations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage Microsoft Teams integrations Summary Report — Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations',
    "version": '2.0.0',
    "display_name": 'Configure and manage Microsoft Teams integrations Summary Report',
    "description": 'Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-configure-and-manage-microsoft-teams-integrations',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '727298e0809e4fea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-microsoft-teams-integrations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-microsoft-teams-integrations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConfigureAndManageMicrosoftTeamsIntegrations(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMicrosoftTeamsIntegrations'
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
    print(ReportConfigureAndManageMicrosoftTeamsIntegrations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZfixpbtX6GzP9huqhLNQ91113oMAoGEBJqFyyuteR7QLNz+7x0CMqvcbfd793Z/eNSqBKGIE+fsM+wTIX57sdomLKqXLy+yZ+WznZWmUehVMyt3Z+uiL6oEvBWJDf7PnCJvqshum6KqXz69uF7tVFHZREUOpq/aKHXrmTWrm6p1mrby3FndZplVjbPKK4uqmRX+JMKPAnDzvkBm5VbgzY6RUxV14TczxbOyehbljRdU1iQYCHSaqIuacdZHTThrisZK60+zpvJyF7xPUuzKsxK36PP6FWjlDVZWpl798uXnXz69RODzy5ffXpzUqsFXL9Jdk/W7FsvcPd51+FDhrsH+OwWAyNTKAzC3HAFSObguvcovqgx85Xr+7Hn1Y+2l/qfZv/1b0ltVUP/05Ws+e76+vkz/pDafNaEHTLDqBoDjWKVlRykw7XW2THtrrAFOALf8CWKUB6+Pmd8kFeXs79O9Hx+LvAZe8+PXlwKocFf268tPs6IC61Xt9Pl1klL++NNrWvRe9eNP3+TUrR17TjMJA1q/vj2vn2LBwG9DI/++6t+B1IfDbe/ry3fGTa+H3pOdYObLa1xE+Y8PwWVVdF5u5Y73409/JdYJPSdJo7r5f5L780Nw6FkusOmp+E+f7iD/Mps/DfqQ+dfLlsCt/4glYPj7cp9mT6D+SvYd//8kOo1yr/5A/E/F/dmE+d9nP/+lbf/dhE8z/+vLxkujDkSHnXpfZr+9ySdm/fMP7rcvf/jldyD6/ypGLtrKuUt4Azkb+V7dvL39/EN9//qHX37+oS1BrIHUeWur9M9k/hmu93X+gOBz1I9/nAvWV/MkBwk++4j02W9F+S/V768zzUoj99v39ZfZ9/kyveazyYj3RR8QfJczNdD1Oxx/evkdVI38UcTu+f/l5V//9bsSJTtF28yAg5so8ybllTACJau+53blAVzrCAD7HAfif/LwpDGofr/+H+deUj87z5K6eFTGt4+y+AYK2tujLL5l72u+NVNRevu+LP76OlPAekUVBVFupTNpeTp9nWblzaRLWXm1V3Wgythj430G9enz9AFU1tmv/+ySb3fpr+X4673qRo9qJq33UyWr29R7ndDQQy9/2u4APvEGz2nBwmnhAC39CBTmTwClukg7UAkn5OokStOZG1UApgJwxSQboPtlEvbrr7/aVh1+zR+lF509CKdegAEf6sw+fwbm+mkUhM3X3HPCYvbDb7//MPv32X836y58WuMEiOHpO6DhQRaFGcjFNgPDJiYCpdpy77777fcn6EBMDhgSeDryI+8xGcRy4rnvHpDZ5WcEJ2a2B5AHqGcT4qCez6Lmdbb3Zx/6PplxqvhhUTcz1ysBr3m5MwKpFjDnA8m8aGY1cETtj59mbe3dV/3Vrqy7ihkoClbz6+y4PgF+KVLwZ1LzPghMLvIIwP8RH4/vgZDqh3q2ehfxOhOm6J2VVmWVYWU91/Cth18Ar7xPB8KtWe71X/OJXr0JqnuIPOABgwAyztOlnyefA9oHjQAg7Pe172OsiQWVOxtWX/P6mSZWNbnCAbQBFg3ayJ3I42/PkKrDok3dO35A00nS0wvu0yv3GFz/w02G/GxUHu3B7GuLQDA2+/+ipZkMWu52ErNbKsxmxgiKZD6AntqxySGPDm6SB6LtkVTfeov3yvReoL/maQSiphr/9hh5d89zzHdmSkvpLh/EBgB6knsP3SkUq2oKeutr/s4EQOXZvewB74E8B3kwhd/7gtPdd01DkMzT9beu4O7qyp2MBuE5K1s7BaHje55rW04CtKqm9Hv6A8SxNyHeh5ET/sGqGZAOnALkz4ASEUgogN0dOqEAZoLM86si+zY8mnotoIXbOkBb0O96rzMdZNAURTVIW9AwTWMACj/cRc0yD2AMVPxAuA6t8qHM1CI/FbSevvge/+etbxF/12RSHsi0XKsBSPZTZXa94eHXDy2fngKqZlOO3if90dlPS2ffE9bfvuZ3DT/IAKR+OnH9d9DMQMqBqJxCbapcNag+mfcMHxAHd1p/fTDzg/o/dPnyX3YFP/5jG4c716p/9NuXWdg0Zf1lsXjw4zs9voK6ASjSiUqvflLl5490+wxW+vxIt88fvPX5zlufv0+3P6z3gO/L7B/T+Q8inqH+ZQa/Qq/QdIuPHG+K5ecLQLT+vDI/Y9Pdr7nkffM9WL7IgFqTS0bAzR/U9D4E8FNQecE0+EFV9cRwPSDVe20G3vmaf8THM3dA6c+DiVfr4rucvnM08PbDmR8UAm7lDVjbnTrAwJt2TOmkfu29fMnbNP30kluZ98/ulCbuAGENEJo2XSDBQJfVRN79ymrdaIJp+vzHraN4/2ClUw4WEw9PRPFRhe8muRXQd0raIJro4tMMmBGA4jlZ2U+JOzUbNrC6BgXacyezmrGc7HjspKau7qPl+68a3HMfFC23+DKVgE+zqT3/NPvotD/N3vc+9y1m3oLN389Tlz/ZDIaCt4+xHztj23v55U/UeDb9f63Esy49mMCyJ96bTPwTm4C0yru2gGjdSZ9vBn5bt3gs9vtdz+axbf3t5b30PL30bFHBcJDjn+uJahcgusGC4PoRh+De/1rz+pQLSihokoBgUOpph6ZsmkR9nMBgCocwyEI8CEddz6Jgn0QtiiJsi8RdD3Ns37U9j6QIBPZIByURIO8R5W9TnxFNuiKW5VAOCWMuTVqE46GQjToejMAuiQK5NOpTlIcB2D6mJqACPwF4GDyh+9FH3wP4gcNvLzaBgZEsVu+Xj9d6QWsWgWC2MNjzivADJV/s7SssZbmMVnZ5gdmda++X2ca71dtCrW7b/S09SoRwGM9H0oLDgplLh3mvkLwvepLjsqxcrqN+496sXcmx4dwfc4/ut4whYcez6pBIUUncOB4lbptz4bBsXb09HbsV16Vajxdmw/HWWDfrzBE52uCQ3MCSURtSO4JxesGo9DXXXVEWmatOOFq5M9ahnuvKTbglNolqMdfQB72F24OlQY2UqVVGJqGqherFL0U104zxGJ+M0KzZYC7kNwoX8wFZnDp4l/M45fuXDb/Fuq0O21drL9dXQh9KDmrtXaRnRa6mOZc5ZLlTcC3bjoa43Ks7TyIuV3auoWRkiN41c/ckRufDzmyNNl3rg1dctzVVrfmLzg1DEOxO19bYa/AKKBNfHXl+zjpHuY6VYkN6FOMwRxwMqK3sVA7lQV5JbTZkFwhb7jyYFJwS4VptYymErEFBIR8X2to8l7u0wh3CAKBI0HLMl+xlGVTFupq3azyuS4fFo0I3dfJ0PbRi4hxqWL/A6xuhj1xo+zyipvYS6W5bqa2yRIxjOjnrXGoKTQ2tKp3XjVJQWCRJdaX3cTqjT7fQ5MvLXmv0pSHvnENyiGq83dtCBN1cbzNHkMAwzkdV24hzt25zx9kQNV0TkXkqr/2hCPFsFdM54o1D7iBNutGORbRaZ62Two5YMRA36NHKwNBGhTR7bTOiv7hw8V46YObJy/gjfr4tIlO4Hc7dsNk2hb6nUjuhQheu6evYxKi8TRZZp6iDOFRcJSuOHacrLzM1xMka1aSsFY875ryBLo1ZID3kBDmcxdpBsIqiPlu0JFYdjqAoI1M5daHX8q4+zHllzrDUcn3yiVSSkP1lcTwuDsQxORUU1YubUAFUMTRautqj/Favb3p/1fQUV20BPsqtFpqNtTmslU4cZGNp7tPQZkpvZ0sSY+wTwymjwlyKt06SUwzfKJ05D8U536fK2rSiomb1bK9jKxS6LAdmJwtMZh9EbmhX6HkvcwYfbjtIlRitBP2ooF4wSpESiepwpgzdUwTTtFc4WtirzZ7gTGaMDFeG4qI0ZSf1ZUcI5qvAKHk6Wd6c03EOcaiIK+VV8Me53KCc5kInk1pQa2ToXJ9fy3pLGVWNEnKEOVpKHQO5hjeVJObHtFKzEDvsrRsSsPtcrZe+nM6h24lq5aKa1/WOw7LwtrUIaIkXiXbOjrLBcgF6Xnowd7ErVJRG85Rdqjlzzfk8hxqSysbS3ljashr8cVvrNYHw2NnbCvyyHhOoKE6bfjDhs+4JK7H2UqG6wmMURTWBkgp8OafkPkylWAxxeqNuSTTIchWnpUQLicSPNK3pzG7nq/tRVtbi5dpRQYSvtKZSznYlnMPqRkbVURYli6nkNY8KSZdXF973+n4X7UIoafdpXKHHzFGtQmEz17hxAY4PY8LjBuTN41VhntmTQTcWa2ixnxPREZkXsdY7ZE1WdebEXmcfqx0sMjS1HhfwNjYgOaUdXu+8UOdhg+AbeG5DqdnOkZMcE83S3Z7WSQ6xvpcGqEMOSb4zri2NJu2ZhlnusK5CCq57/myd2/OFJfxU3kdZMpwGfOmtFCXGVVwYYh7GFnGZ6Y11Xo7meQ+fEqLPImZcZcnaDOTc2qanoqu5IdyNw04LsdFhAs5IJIghufZwThrHXyflnGlMxmu4/R5SseMuyw8CeSzIMxrUgSTz6no+GqtdH/lW7YjXHqfP21A439yruUHW0Bou4JNQ9nTeaplwtW5xRdN+zhNUN0K9fM0d14YB0OnuolNHU7uQamwyyAARLHM7LcjD0iNbryDd1UrkkiMo5x3Zj+NCDUbK87lkno31ZRmpoJssIbxU0a3pMPVyQEpOZoWElnhJWl1L8uRqVR4c+QPfkRkT69TaDhg9AZUAXiUxd7tG5Wglokk7si5rrghtrw3bi4Vk2nq30s46kzVH3LyoUlVyR646XrmEgWjcucYxqgwomlcF7F/hXb00NV1x5wtcBjXSKeEDlxVBny+cvba6NvCo5hpsm6A4NRdeT4uONP1NZJt9zTpkyueim8duGa97xITxHSgm1aaIjzDkleIV3bY95RhbUluOIeIt+h1zuKa7nZq6g2Ipm06AYRfyI17eQ4SvZj7uHTnrfPTlMfW5itmb0nUgxSbfusLILhj0fAUMYoimZyCNvtNWQs1kknZqDL0HdVFtBrizMsNYrXE24KIsrfErfeCDqldX0faoGLAxOBASJERzTjRGEmRVWPFp5XDcPoS28GCAjCfLfQox3mknnAnm6ga96GuonsVSgNK7pL6lwlJDz2pWx2ca8LSi4rYsnhEhiOSMYc4Hb25hq3yd0nGk7Pd8XXWbzMqEIgiHgjKhwxp3w5j3kaIrdcdxTJ/WNYKKassie325LCTBG/ulgxRHrx62xODdoLUCEWXkbEJveeUWzDrWkRY6FXPB3IQq0kkLcpmQWNj2lrKtmZsgnQ9E1TAKu4m025wJjnsv3nbHU0vmUEzYjLA8CqsTarH6yA+e2GISdPRPK3VVL7cp6tFUavIkg16Jij+CxmJ1Oin0CaP9kAbZV2LH+TkdPLqCIIGJxI1t0Zzg8TfcNue5kY4XOyZIljwaDIHIG9sAmxJzm7EKs7503tjS5nkl4OelwyFkKGI06nKelNcbfHfZHpszPxdWTkde6b1EVMQOKvaJYLI5oeA5hwrMhqMXA77lb83ZSMsjpTHxmNMrLm1Wh722xvCrHWD8oEIHJcvHXWCqMYMVO6pkNZTX9vA+78TRqOGlv5RYgT2tbqwoIumV8/FyIychKsvXYncL0pXrBud6t+YsIV7F+k6J+MQ9YCxlCWxMRPvrpbfUQ7ktb33WXFGXaeq+PgWirFxyk9KL88DvoWE4bNGxJFf6bStQlGmHyrBFxiQkd7vL5uDwZnsS4wMowOUmiEOt0O1+mxUXZROMVxFZbQsGpJvvmFThkIV9LJXjTkdPeav2q32dx0rfckbNXNeF7q64AkZ4JRbHnZ8ecJ8MCToUnbPH432Qi2uWUeJYjY1Er0zsAGsbxVxXGo1HtdsXER+7R54TrVN0LijAqudNIGhyvOg1gWKwg3Qh1mxpYmYkyz26rR01SZcC5WDZLRiUYSydY71Mb+7QXreb+SVZuJiwAqALY0bSq3N2y217s/YXa1elZEGNz4t1lhwKXi9kbn2s05jMbsn2EnI8jh5HUjFWnNwu+wAR+xWkWwWsc7bg7668UrF5TOJVTywNSOIiIdo6e/4yusnyvDO7hbS4pBuH7ZpuzuwHkc0F3xTZ7Ibxl0DnnNbgPRRebpJjYt44HCnIlEYl5HpEGDTaJCRoNFhpb5fr8VpBBW1uXchKpPKQ8PmhjzVtM6w3sk8KUiaeLzXmJcQ57FxenMsFyhOSyJ+JReK29KUQb8cNSkOBB3GWbFX7vUFtIdAqbSESuvL5nFol7j6+rBRibR5QZ4Aou4W2R9aMY69gjleQgdb82Bp0x2ftMQSFcXuVx42fK7eutrJNlay311DYqv5SOSnDlcC8Lt6ucfLioXISH7cwTq7hsStOOo/4G5qWIJGMGqoZmrS207VFgp1QePPabnM1aMG1l7jYwG5r7NKG90YBZHWMbU9LvnKHBb0WVRiJdhC72UtLl3RwsHVbgd5sQdfBzm+ok3fLKTXfWFuIdjWpHpG1eFMKh3VuzK2ouvn+GMQLG+o2iR5wS6wxJBsmOpgbJYIRqZbWcBqTa8aPUAnrQrEdYm6x1AOhbskWpa4Yj0iVsunJOHZvPWQnl1vhbc77crHwNLBj3KQ42OasusWgLFjljPFByqxgnlhINR94+3C96bZSxWV7Vr1EfBrsBI/K6PP8TLInjMc3iNC08ZA6Q3UOjxjpLPn4xtLL9f509XEG0rfHRdSfNrGnE3bqi2461JpanEzVZ/WeRvdr7GAKc3HrnzvOcYpbUOLAvZmRQzTF7XXCSrZw059IuJLZGImRkAQMrPI7vs5pLOzz/GJo89A5akNOqMNlu+PYqyCgmUt3GMNyoSsc6C4DW/QTi3W6RLZ6sYBh1aoXcLyY73imJhSSWB6sFcfvWYWc85vKbfC5j94Y5Vy3GXxyzKitRQSrh9qXEOokQPC1XBjterPfLWQRQ9w2r33QcWZIJMdLZXG7yspZy7GI92SF4VWSUa48mkIs47KbE5W6Qt2bK0B3/YmFjAiuoyrZtYfSiuTSFNeilZHymll2gn0+dFjDukG+l3yPTXmU9RzD2zgqzWeQ3Ea8yqrYsKhWPeWdiluMnOiVtUGVG6eQsRzQacRbe2rUCmF1y13CNk87fdOcGnXH0vM+17YHutmFp8yAFJbToA11aGAU8hGfdcKy3SMb4yJ6Yw52sDZoO6gCgZ0M7CoOZRB1imVKaCYdXUqA612mIBgM9zcC3jtnvAUNICMG4xAQaMwbTS/Qom+b+u0qKmQF0cbQHPWChnnlqkakpbPG2bXJNoB7qbs246Ws6jlCnqMe3nR1EYfEbh9DQrc66ay33K4gKaWTgvV11Eyk5UU+USq92/ZekxzBNkKp5Yvrqrd55p6Jje8Xrj0shXWLdmm4P3W80FGrep0Y7mVBLE666yCVzzMaO2ety84vm9aUOiUOt+OFKkkFX0npPLSxK2T7kiS1qLbACEJu2jK2abZDRR7pGGTBzQO6wXgDGoIxDrb6kSuC7elqaxVPKGv4piBSo7ZmJYEd9rxI/RV98DFIWEJMgu0h+KifTjRWRru4Y8S0TlEYjWofb7SRNA92H5eLFiWCymZk0ykdlt5EEN6fgsUApREr3JTLiA8EQ2d6dbXVY5uhlX2DSYvMWaV2UHWbbcudgJwkJ1R4cs32mEsOtgpjGjrS8ZHtlwcjYpYGEnA3/yZGXEVL9mjCOiplFdSPFE+M6CWEKkIidafzanLcYtQY22RRjQGJzReevjz4pT4aGAkNQlOxh3Le9G3Q3CDStRPRQO2VmrG7cWOi2wvDXyEGYKj4ibGGeNjG86piu/aQtiY0UmxwFqCEEMrLSBVHdwV5EL9UUuoSVIsi4ct90i6hRcsz/dl1aOm2U0wC9W4LBDFMbL6as5sNUXRjAmrt3//+8ullOpx+HjH/j59ET6d3/2uHiI/zvvcHU/fzXdD0fbmv9eV/ruovn14qJwKKPg5W67QNnseN/+lY9fM/+6Bjkjo+HgZPz9uG5v1Ev7GC6edQL1HutnVTjW91kbb3A99PL3ZbTz/DqKdf6jjg/eUOQlZOx9gPRcAHy82i/H7w/tYUb49jZu9l+p3E9BzJc6Nvl09lpkPwEbg5cuo3lMDfvKqcEHg+O5kOaKeHJy+//wdt+k7pgCYAAA== -->
