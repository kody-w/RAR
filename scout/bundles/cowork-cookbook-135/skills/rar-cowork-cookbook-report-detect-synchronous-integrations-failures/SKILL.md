---
name: "rar-cowork-cookbook-report-detect-synchronous-integrations-failures"
description: "Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_detect_synchronous_integrations_failures", "rar_sha256": "b3ac1bd5846d20a48b233bcdb048895f9734f295f9ef4a21d570444a7049ce1d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_detect_synchronous_integrations_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-detect-synchronous-integrations-failures:b6870a70c9edf447daf407401ddf4830637611e931119a1e92592d67746536c3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_detect_synchronous_integrations_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_detect_synchronous_integrations_failures_agent.py` is
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

Detect synchronous integrations failures Summary Report — Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 b3ac1bd5846d20a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_detect_synchronous_integrations_failures_agent.py` first:

```bash
python3 report_detect_synchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_detect_synchronous_integrations_failures_agent.py   # or on stdin
python3 report_detect_synchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect synchronous integrations failures Summary Report — Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_detect_synchronous_integrations_failures',
    "version": '2.0.0',
    "display_name": 'Detect synchronous integrations failures Summary Report',
    "description": 'Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-detect-synchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93276d22e7a4ab66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-synchronous-integrations-failures'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-detect-synchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDetectSynchronousIntegrationsFailures(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDetectSynchronousIntegrationsFailures'
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
    print(ReportDetectSynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6a5OqSJfuX+HUfOjuce8SFBDqjTfioKCiggiKYO+O6gSSi9zvQk//95Ootffume450zMn4lhRJZfMdV/PWplZv72AuvLT4uXtRYMgwVYgigIfFhhIHGyRtmkRoq80tNAvZqdJVQRWXaVF+fLpxYGlXQRZFaQJmj6vg8gpMYCVVVHbVV1AByvrOAZFhxUwS4sKS13MgRW0K6zsEtsv0iStSyxIKugVYCBTYi4IIjQV0bGroAmqDmuDyseqtAJR+QmrCpg46HuQziogCJ20TcpXJAy8gTiLYPny9vMvn14CdP3y9tuLHYESPXpR7wLwd+baN97id6yXT86IVgQSD03KOmSZBN1nsHDTIkaPHOhiz7sfSxi5n7B//dewBYVX/vT2JcGeny8vw49aJ1jlQyQ7KCtkDBtkwAoipNMrxkUt6EpkF2Sn5Gm0IPFeHzO/UUoz7J/Dux8fTF49WP345SVFItyF/vLyE5YWiF9RD9evA5Xsx59eo7SFxY8/faNT1tZ1sDsihqR+fX/eP8migd+GBu6d6z8R1YeDLfjl5Tvlhs9D7kFPNPPl9ZoGyY8PwlmRNjABiQ1//OmvyNo+tMMoKKv/Et2fH4R9CByk01Pwnz7djfwLNnoq9JXmX7PNkFv/jiZo+Ae7T9jTUH9F+27/f0c6ChIUxx8W/1NyfzZh9E/s57/U7T+b8Alzv7zwMAoaFB1WBN+w3941RVj8/IPz7eEPv/yOSP9fyWhpXdh3Cu8xSAIXltX7+88/lPfHP/zy8w91hmINgvi9LqI/o/lndr3z+YMFn6N+/ONcxP+UhAnKbOxrpGO/pdn/Kn5/xXQQBc635+Ub9n2+DJ8RNijxwfRhgu9ypkSyfmfHn15+R3CRPEBreI2y/F/+BZMCu0jL1K0wzU7rCkMOroIYDsIf/aDEjs+k/lXbirvda+z8iqGnQ7ojiAB1VGGrAgEKhvJh8PigAUK/X/+3fYfUz/YTUscPZHx/wOL7d7D4/j0svn/A4q+v2NFHUqRF4AUJiDCVUxQMeDCpBv73SEGg+7kZREDiBQ8IUhfiAD9lHcF/YL/+TZ7vd/KvWTeo+CVBPgPIkQ5WwRjRAUUQdRgYMMzqKvgZ4TDCmSKNIgvYITb8qbPXwW5nHyZPa9qo0sAbtOsKYlFqIz3cAGH3JxQQZRo1CDMHG5dhEEWYExRIzBRVkQH0kR/eBmK//vqrBUr/S/IA6Sn2KEXlGA34KjD2+XNWQDcKPL/6kkDbT7Effvv9B+zfsP9s1p34wENBteNuPhToEbbR9jKGsraO0bChaiH/A+fu1d9+f/hlkC5BtRPlWuAG8D4ZUfsWIoMGD2d9eArpPIgIiyenP9oNa31kFyyokLVQ/pefviQDiRQNLdqghB9GfEx+mP7D9Q8+g0/Kpw2Rn9wije9j79E5ONNOC+cVE13sq6We1XrwqJ+WFQroDBVdmNgdmgmqby5MUlTIUbCUbvcJq0uk6kD5VwuRHowTI+AC1a+YtFBQDUwj9Gcw0J09mp0mweD4Z+w+HiMixQ8oxuYfJF4xGSJrYhkoQOYXoIT3cS54RASqfR/zEXGAJbDFhtIPBx/dw/geefx/tenQnv3Ko13AvtQTnCCx/5+dzSA+t1qpwoo7CjwmyEfVfMTa0IwNqj/6t4Ee6koeifOt0/gApQ+4/pJEAfJP0f3jMdK9h9djzHfaqZx6pz8kenGnG1QoSAavF8UQ2OBL8lEXkMhDwJcDxKFcDgdkSL8yHN5+SOqjhB3uv/UI2CP+BqVRZGNZbUWBjbkQOvckqPxiSLGnG1DEwMHQKCds/w9aYYg68gWijyEhAhS6yHZ308koVVBf9Yj7r8ODofNCUji1jaRFuQRfsfMQ2ig8S8yCqH0axiAr/HAnhcUQ2RiJ+NXCpQ+yhzBDg/wUEDx98b39n69QkA7lB3H7moGIJnBAhSzZIhegBLs9/PpVyqenkKjxkA33SX909lNT7Pvy9Y8hC5GE32oC6uiHyv+daRB0F3F5DzVUk8MS5XkMn+GD4uBe5F8fdfrRCHyV5e0/rAl+/HvLhnvlPf3Rb2+YX1VZ+TYeP6rjR3F8tdMYFUg7yGD5LJSfH1n2+bss+/x9ln3+yLI/sHlY7Q37e6L+gcQzwt8w4hV/xYdXu8CGQwg/P8gyi89z8zM5vP2SqPCbyxH7NEbyDZ7oECJ/rTofQ1Dp8QroDYMfVagcileL6uUd/O5V5GtYPFMGYWviDSWzTL9L5UGnwckPH34FafQqGeDfGdpADw7rpWgQv4Qvb0kdRZ9eEhDDv71OGlAZhTEyzbDWQgmFeqwqgPc7UDvBYJ/h+o8Lxf39AkRDzqVDbUXYGnwF27suToEEHZLUQ1UPFp8wJL+HwHJQrx0SdWggLKRuiXAYOoM+VZcNCjzWUUNP97Xh+48S3HMdgZSTvg0pj0owas4/YV/77E/Yx8rnvrJMarT0+3no8Qed0VD09XXs13WwBV9++RMxni3/XwvxxKEH8gNrqK2Din+iE6JWwLxGtdwZ5Pmm4De+6YPZ73c5q8ei9beXD6gZrh+NxSPM0IT/bi84mOCjhr8PfMBA7d6x3S1y74HfAQqHoVZ/98obGo/3RxC/vCHYgp9e0GTUMaHGvr+v318ewiGtvnXPg6ig+FwOvccY5SCihDqCbNAoROD5HYPhceDcxw8Xb3/Rcv+XkeTNopkZDma4zULHJcmZA1wSn5E44aBbZorT0xlNEJCdEgTBAnQxodiJQ89mJE1NaXuKZCpRuMTgKdOYGPyDtPnqhP/pquDlQQ4VpQlFI3rWFNiE5VAMSTsTHJCMNZlOLduxcJJhWMplZ1PSnQwX0CXBhHCoGU6SJNKRZG1IOAO9ZyP6kPH9o+n/8NgDX94RQMfBoMEEAJuxZwTpsDNA23CKW1NECZGeTSFOsVOXYSAJB8rPqU+vDU59mGEIb9SDog6wGfj89oyCIWRpEo1ck6XIPT6LMasDekJa8s0aFbTrHZOxaOWEGifqsdhtILE+25bITXjYl8vwlB+34UWLRXYVzsSVU4EW51xkZnPDJs16Ldb1NTB2abbkZnDi10eftCKG6ktb1QUcbtM80q1FYVY4OBE+CBz8BOJldDlNfFXuc1cB28Cu6UrfTooTqdPnW+Req4gYL4mZsZc6GNqbc4W3xVGq1wt5XyexlYhKcljHukVrkVPYYFJkwJc2hjzdLHK0uOvGl8tqE+tGJ10VwzfLtUcpSc+MlSQbMUpS5n1Ej5SG8Zf5yNDyw6pMq223y8AqbDSqBFuQx462OmWXPk8uY/9kGhvnkEiRTsp233W4W4tJn5zrOIjZlJq4yU4m80MVnUFXm80q8OJ5IauEV262yySojINO3DLQ89xJr/GwLouwm61NfAIDOjqzuwRHIavbXqAf5w6Ib6v5bebB43TnaEWsxac+1qnFBr+KE6VbbtXDZbTOM3xkrODhELYtPOzAgisavqhTfmP4uV0QgVgfz4V13ewXMXsJ2VPGLts8n+xuY31zbqtL2+N9RGVFTCo+vwzU86Kw5HlO+FN9ezZ8+bojQmIFe7fqQ9boAvMYWaYfnbxEW0qXYqt5k8ZspOvp6jrXnCBaXlft1uXh9tLseejyoGbKIE8Tjr1Iu/K6miklE/V7srL263yjOnuTLow5NI5BL2upnnoOK1u6tIzb6NYao0kQ9kIOV3ziZ/3elsdkPV90J5G53UxAxPvNhFDEqW4pdJmZThtcxmyBE8KhzOkMD8cCSZl6dp7D5HLVV8re12prqeSXtZIRQpPgFuvOU2LkHN2bWpXildrjFi0IEn5kjIQR1zQXnlk8D3zQ9qxJGUecPYyuu54j90vopLMVcT4JBFPOQS9bi0wHRqSW09NtS52XAZFK4WbENMvNce4F52WplaRZScLhFMhOF299jiv2LL89X8P9iAU035HNglvbrb48mvtKOlTkfCcyPBSFGBgCrtnarZ5PNbHb6jt/GeLCZaVfjlHg2CZpG8fw1tbUyfcctzYceVUwy3V3hDITKg4Tuuj3eh6tDjrdbtOI0daXKoldEFmRvWGIUXPbR+fpervqiZJ1x8LsZEZrahX2tru87Paj0KvXBJrfii2gCC/p6wMBjiYjlPJlduC1PjhzlaqNaTUZGZuTPj6fedtGQRpUDuDsUFvkx3gj8qFnpdkaRFI1na0Far+eSYSylY9Rf6PHsiNMDJHkz3kU75jWCfE1TdTFya2q3SGUQjwtlGvfQeJkQHkjlagPKs5rXZ3rhrOjMpoRNTY8rlKHPzAjDzX5/O3I586o0DZtpSq3bT2JymOQEfM0DNurSeduuMjEtV4BsHMuc0HuFLg+HTpxaWqNKCbuZEErFeOXs6tgiXFz7DYkKe6m8ko4XcyYCNlitD0Ym844yWQStyNebtzbeHeuCF2YUrWd7Jv9ahIGJAlpZhPBSRq7Si8XsawITihXLiF7iW0g/Fif3MCWZxeLcH1ntBkl1ZRm1hLVT0zyFFKkde2juDy4EkN2zrxvbFY5ibh9JElHLvbzZpWKaOHIBJlVievLHgWwobR+2eYxjNP2SlelUUyk+CxMLpcubaXwPEoC7uzp2irdmq2TnoSRx3D5SJB3wuW8DuatxmX6bcUc0y1ZsR2+ZBQtMjXe2wM85a7zo8cuLnaIM51bcXCvcUux4XbFxhbMbsPmfUtZfNK1Z4HglUl62OO7w7a7npipy3eQOpuTrNjvm2l0g43VkfltvsmdG9EYDfJzt01ifrS8VprsHc3pMbWP0nhchfPpnqKv1UTg0/zQ9AQ92hvX2X7Js8BgDiUJlZaeC/5luVOtvsvq7aHdifNjpQXh3rrQnhx481M/shHoSNx0cjAsY78pq1YwuG21qcWoW1ArPUEZGBIiQ9GkkMcZ0PNdv5A8hgwOE00aL821sIr2lKieZb5x1pEaEjU/rnpg0HYzPjF2eqIWVijil7PlaTgRXndLZ2UI2qZTpcN0DmhF6f1bNrqNF0UQ5tqO1yzW9O1lbhjICu657F1Z08MSTPJxr3bSZsM35iSa5srCuU456ljLsPSjzrjN+TjZreQ+prTIaHrZpEi7r09Hybhs3fnZK7fHFGS6ocxSfj+eTNiJCkVbPBo52ztMYrZpdrix4lZlGtsM3EmzLLcjRxdGI9eWpXkfnX1ODyjXIU7Is/Bwmi0l1JTIp1TNdtQMLsui7i7h/iCO5LPe67kUzedMteAndtx4iyBji0N2Q93bdkfmdmZ2vGiYykjlW4lGy9Jg2Z/t5eowv9kXYqdq1GiBL4mzAzRlxesSCMjyVM9Pjq+TLbudGRqlHJf+dnM9TBabhblTd6uZgZZeF0Fn7IVZ7X22c3qvd05Sxq7h9XY9hLtosgqqGQioxKyoPI6TMDIV9qzTTCAAbdaeOS5VZdiNPIte08qNC1izmVHyEadTzeZ9yOXbsVCNKtlOTZm9pPz8wqJubrLcTP2144XhztzEIGgPgiEq13Uf6P1I8EJRuy4bTqlnCX6lLUHmJJlzp2B9boubsTaqllwpiZdzrLboZvXZoesjq10IR09iZ1lx66YYJR1sWvrEc/hodRP3pOIQEyC06nreOGy0arILymxXKzRqX6msc2XjXeBYu3l1LdkK55Wr6s0Do7lMT6R4iOmUWy0tot3Z7bWOGq6f+IwvBfEpjRrBqw2fcMKcJZZzIEniKuv7Y4bforj21QiwuZ0nFJsuO7y2t4sLdYRppJ29SNxm0NaX3SVqcxBmbX/hD1KuevZNyM/XmDLy0Az7aXQpJhdPMcVrHEcu5UVrS5suFQb3N8gHm7lx4i/tolEupefpR7W0JRAGp1qz6iN0KIFnaVb08ljKsxSoF0dKj2Jlgd1gVrJq/Fjt5QhIcbCaK9JEdaSV0UXkTXWXrJCaM9Vpo+0oUeNpKUpZVy1ali5jX449eVEvGnTBnBd+KNXKNt2ZwvngNr7Dtssu62rItZGNW1Y5sSleWJuatlc0JoUcyLfzCy4gMDHlxX6WnuXT1B/VSYNLF2pONle4kPCd7a8UOVgeVTrzvbV5kqpw4yfjcOH3fGDWCs6lBWXSO+aIIjVlZC5yREWRpSl39KNllS1HWeDL/m55tU8b/6zKvhNYe16RVnTVgsPCkNeI92lHLfqM8HClD7WZaLlksNihTp0RtmNmOT36wk2r1sl2e4g8GQRiKjRdvKt2rHcCQlgaZb9B4S1kdMvRVyPfXp1jzusgO91YYPr7cgTkZtIs0pt7EGhhIkakX63nk4MvmoFCrIkJt2/hhHCZVA0kRQGj1kFaH84sV54yszmy6Y5bi6box3rP6pNdUV+rk1NtGm6VTQ0d7IPDdDUPdaNx6QPSJ5KuGi8ZCz5a5zkfCEdvNAGJbHu92SYy4fMm0FkyUkcGHtiaT4ylmZNPVfNsrpqimrPpAQ8JTT2MyW0mTbQdxacnQ5mTR4lWVx1yNXfTIBVk6dRJgb2/rRfMwXRO7bojGMcuxpEVp4Gs7aYpQ0exdzo4zuVQRJs0D8jFnIby4cyjNio9N5YwGevXzG+K5nKuIjKiCXgjT3a693tbH2W13Ga+3SbnWbLH99aNcNjzGKzrfn+8OkYR3Y7WmSh5iDpp2udDiFu13KXqJNFCdQpT4Kz9adWn/I6z9npDNBdO6i3zPE6UNuNiYpdtu+h64ZrZaKqmJ97shVkeKvQW9eFjy0y4MI52HBnpatHTNdzf1JxTKMieqeX4ONV2vUWSestSBloTXApvRUxZwoKOtrTMcTE3rU5d8iQtMwplz+cpsxqNx6noMpuc2WxmnjImMzdJD8Km1br9NJL19ESQ0oJMOwOERER33NZmhTAVmKbWa9EVxrxLruqMFc4iWrrBE95yue3AvXDLfJajFks9WXj0VYpdyl77t6vIsl2Z7Dt6sijPMbPd84VpW5PdJYy5cbLIimm0UuxNaTCLRdhfxxRcrde7jXKUl+Vcmd0KkLj4dVJR0/X1vFvtJ4lD+q2RWIbeXW0g3xJwuF2WG/YqS9as2DNTRuCjtI7CCdHiM9c3K34GKrWvCrICY2s9YmwoXk6x0R9gywuaqhhX2jA00jqW4waVPS+7yMUIvy19wa58PbnUTUHujayI1mwjmcuDQ3vOrR3bY4lxM1cpBULgjFmu46Mgd32p2UTrQ9UH6r4NYSOYqtCu2e42Jiw1EXbzhC+bozNbkRuQAmpVBBuQhbQ596xK2h8Cr03bM8oJdjZnLpvR5qxXjMre2HDZX/HIUhGM5qKmzqfjM8+SjDL315I74vFdEZ+terpiWFSqTrhK+YWnZknd4FNP21VTzbRSe0uzrJJvLdJS9oaksLKz2Wgkg5YP62kyURRn1Qt6NYlbm8120pHp43A2OzjxiGcTX7telnCFd1d3AcwitYpUlmP2VhfzZpIfcL8v1zqRqlzILyf16lxaB2e0V4zL+Roox6I0ZslNlVYhS1yN6LSYgXNiHVjrWnnRzKrpqLtQRd3G/THwbnyD2iM/l6Yrcg35mtwwLeDSRKHn3pZ1ILW/coHnirexXKQkEE/22pvBsAtmWZLNi5u3mI3N2XQhQkEunFF3sN2Ve6HyZobKUTmezJIE1iAaL4NtP1uoqM3H46ksTjOlrdn1aH7JGKqsxvMNo4PNMaVLwsqvzNwRj1bGTMbqjL2yoy7YuZF7gFNGL2jV01VU/VZL4cAnkdgTBDX3IWvMxElu2GpKX/LxoWv8EV4w4OyBxcJcAhDskilNn268SnRrbaLNZpaPSmpcU04plKSFs1PLV/dsIEr7U82P/BuQmHWrMDPN5xMqS0mbZHnY73RCrlcGbxFVNmIrmbjhs7VMzC8+UK/OFTfEUzdqfWa/hsyZkOGSZRqznzPcQid9bsmmi3LK9GmQujkPj3GAI43teGX47uRMSXXkag24RTMiga2xjnFHqU+FyI8bSt7Y82gUkptxWe1RwpVMHdLJfraYKkdnGR8pRa+Xi4NrkUvUHaeH2rK17ZlQRjdzcxjrTbyva1gz4ZlqjrsD5LgpVNNJFe40r8WNS3ko5b3h1lyzzw91GBzIq8Xotsvdor5e2xfFngFrrZT4fo6KJCF28LRkMo7j/vny6eV+8PvyRuAUS3x6GQ4Hnlv8/4MdX68PsvcnYbS+wz+9/L/bcnxs/30cDN732yFw3u7c3/7bMv/y6aWwAyTfY8u4jGrvuen477ZcP//NXeGBWPc45B5ON2/Vx0FKBbz7HnaQOHVZFd17mUb1fQcb+aQuh3+BKYf/krLR98td5TgbDhEe/NEFcOIguR97vFfp+2OTH74M/6MynNpBJ/h2+5Rq2HDvkHcDu3yf0tQ7LLJB8eeR1bA7O5xZvfz+fwDDVojT7CcAAA== -->
