---
name: "rar-cowork-cookbook-d365-case-to-resolution"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution", "rar_sha256": "6d6c4607359940256d05529333b3364954082a28375a4e65209f5f13a7a12f24", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_case_to_resolution`. The original RAPP
agent is preserved byte-for-byte in `d365_case_to_resolution_agent.py` and in the RCI capsule.

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

D365 Case to resolution Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_agent.py` and embedded as the fenced Python below (sha256 6d6c460735994025…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_agent.py` first:

```bash
python3 d365_case_to_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_agent.py   # or on stdin
python3 d365_case_to_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Case to resolution Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution',
    "version": '2.0.1',
    "display_name": 'D365 Case to resolution Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-case-to-resolution',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c365a36303644e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution', 'uses_skills': {'custom': ['d365-case-to-resolution'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365CaseToResolution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolution'
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
    print(D365CaseToResolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9VaabObyHr+K+SkKp6J7CMJBALfulURCCEJEDsIxlMe9n0RixBM5r+nkXSOPZmZ3NyqfIlslwR0v/2uz/N2419f7K6Nyvrl84vi2wXE2FkWR34N2YUHUWVf1in4KlMH/IPcsmjr2Onasm5ePr54fuPWcdXGZQGmb6DtUNh57DYQgqHQLi7swvWhf4OUrqqyAaIiOy4g3i7s0M/9ooX8W+XXLdS4ZeV7UFtCbeRDlN340+/ab8qsm0RDfuF9astP4Auq6tL1mwb6BFS5+nUDoRAHQ3bt281dYWQNccjbKL+BgrrM72L52K3LpgxaiOyauJhkiE9ZlN3aWRm+AoP8m51Xmd+8fP7p548vMfj98vnXFzezG3DrZQvMmtRTS/ldOTAps4sQPK0G4MbpGhgVlHUObnl+AD2vfmj8LPgI/fu/p71dh82Pn78U0PPz5WX6I3fFXdG2tJsWuMO1K9uJs7gdXqFN1ttDA1zSdnUBDIUaEIUifH3M/CaprKC/T89+eCzyGvrtD19egHdre9L1y8uPUFmD9epu+v06Sal++PE1K3u//uHHb3Kazkl8t52EAa1fvz6vn2LBwG9D4+C+6t+B1Ec2OP6Xl++Mmz4PvSc7wcyX16SMix8egkGgrv49TX748a/EupHvplnctP8ruT89BEe+7QGbnor/+PHu5J+h2dOgd5l/vWwFwvrPWAKGvy33EXo66q9k3/3/30RnU1K+e/xPxf3ZhNnfoZ/+0rb/acJHKPjysvWzGJSR7WT+Z+jXr4pIUz998L7d/PDzb0D0PxSjlF3t3iV8ze0iDvym/fr1pw/N/faHn3/60FUg13w7/9rV2Z/J/DO/3tf5nQefo374/VywvlakRdkX0HumQ7+W1b/Uv71Cup3F3rf7zWfo+3qZPjNoMuJt0YcLvquZBuj6nR9/fPkN4EIBrOnc+2NQ5f/6r9+hi+KWXQuBALdx7k/Kq1HcQODvVNu1P2FWDBz7HAfyf4rwpHEZQL/8h3vH20/uE2/nHkCcry6AnK9t+fUbIv7yCqlAXFnHIQDZDJI3ovhlglUAqmCpCoz06ysAEWdo/U8Afj5NPyCAvr/8hcSv98mv1fDLHUbjBxbJ1GHCoabL/NfJFiPyi6fmLqAK/+a7HZCblS5QIogBcH584PYV4Nhkd5PGWQZ5cQ2MLOvhLhv45vMk7JdffnHsJvpSPIATgR5c0szBgHd1oE+fgDVBFodR+6Xw3aiEPvz62wfoP6H/adZd+LSGCID76Xmg4VERToArwm5iHxAUEEYAE3fP//rb06dATAHID8QpDmL/MRlkYup7bw5W9ptPMIpBjg8cC5yaV2XdAjSG4vYVOgTQu75g0enRhNdR2bSQ51eAwvzCHYBUG5jz7smiBCwI0q0Jho9QN/EfWPUXp7bvKuagpO32F4inRMAOZXZnxydbgMllEQP3v4f/cR8IqT80EPkm4hU6TbkHVXZtV1FtP9cI7EdcACu8TQfCbajw+y/FRH93or4XwsM9YBDwjPsM6acp5oCJc1D1XvO29n2MPXGYeuey+kvRPJMcEDXwyp26ByjsYm+C/r89U6qJyi7z7v4Dmk6SnlHwnlG55+BEwn/WJNCPZuJLBy+WK+j/ey8yWbphGJlmNiq9heiTKpuPCEwt2KTwo2sD7QEE0vBRbd9ahjfAecPdL0UWg3Sqh789Rt7j9hzzwLKuBmbLG/kuH/gGRGCSe8/pKUfreqoG+0vxBvAfQZrc0Qw4BQBA+vDa24LT0zdNI1Dl0/U3sr/nQO1NXgJ5C1Wdk4GcCnzfc2w3BVrVU10+QwkS3J9qtI9iN/qdVSAYLcgjIB8CSsSg0gAJ3F13KoGZoCTvLn8fHk8tFNDC61ygLehx/VfIAKU1pVcD6hn0QdMY4IUPd1FQ7gMfAxXfPdxEdvVQZmqLnwraUyzKHGT89xF4PvxWDO/hB1JtD8T5S9FPmOz5t0dk3/V8xgoom0/le5/0+3A/bYW+Z6K/fSnuOr7TAECFbCLx75wDgWrMH9k5gVoDgCn3nwkEMuHO168Pyn1w+rsun/+wF/jhn9su3ElU+33kPkNR21bN5/n8QXxvvPcKIGUOciSu/ObOgZ8mxprq7lsl/k7cwzufoX9Opd+JeObyZ2j5unhdTI+42PWnZH1+gAeoT6T5aTU9/VLI/rfQPuM/4TDAFmd4J6W3IYCZwtoPp8EPkmombusBnd5RGTj/S/Ee/mdxANAvwolRm/K7or2zMwjmI1bv5AEeFS1Y25s6t9Cf9jLZpH7jv3wuuiz7+ALQ0P/rPczECyAvgQ+mDQ+okQkNY/9+9d4LTRe/3/LdqweUvVd+noroIzT1rR+h9xb0I/S2KbjvrooO7Ip+mtrfaUkwFHy9j33fTzr+C9h8tUM16fvY6Uxd17Mb/qMSU+28YfHEXs9inFb8gxDwIwz9+o9ChPsPO3siQtPaE3PH74TSAD090Ad9hEDEQH2BkgFI2IEJf1wGrFP7lw5QpDeZ+81/38wqH7b8dndD+9gu/vryhgzPGDxbQzAclOCnZiLJOchOsCC4fuQRePa/bRqf0wCEge4FzMM8zF1hizWCEsRqAe55CxSFCQRBHATBVgS6WuCwDePIGrVXPobCCyJAgyVir+0lHMArIO+RhF+nBiCeVPEXgY8QS9gFKsAouiKWa9gmPHu1tm1vgePrxTrwAMp/m5oC/Hva97Bnct57/zr54Wnmry8OtgIj96vmsHl8qDmh2xi8duTImdWYb6LSoe4sozzR+RhyR3+5Z1znsEm3/tjsSq12D0GqHC/2Ktm4fLk2+BO1x0gRVgJz7Q50FReOzV2t/WbtwwITCIV4RceMJOnD4ItIPZzUa2bUJNvoxzLzDF3fpuvZUjk0OTufi9IowHvRG4tgSKXxUKwiF10V4RXenT15l/qIiZkOV3BIJOgzrnbD+tjdAB9GVMUrCFzGEb9Q/DEul/1AGBlVykbNWwoh7zWjhk/nK5GKO8XlF6tlNCcyZzlD2Zy2Lq3iSIhzGg9Vptt1nMB16w7H23jdY6h8Fndi7W4lzA+KYS6M2RB0Izobm3VwHdcLEd5njZrpbspdZnWiVFlr8LVustWSGiPSJDK5mfexi1XUcknm3aJMkf1xIJaqso6VPNikBzZWLzEW4fPi2Bm02K8SpTnq+rBDdXM3GPSVGxeWU7ixvjgZhpu6VprSfaYTVjxPIps4H7vutJasZRKV682MpY14qKTmxHOj0KBpn1lUtQVGxBtVYFUmcgqW1Pnaq2F5MCxxP8YRWwR0vqA3hr8/exKmXvWzxC0JRxoDesFJmrCdtTQeo7StHeCz65xrZhgTg5Ntu4sl55L0i6SNjN5Rq8uWbZArRykXkWNj3jnO85pjCWYpXOCGNIc9Che142wT1uuxrnR0fCnjTYU26F4UQot08hOGWd6MUFOxaTuMgoOzmlr0aSU1NTMjCsacR/DJjGuSy5alFR+vfD2q1oVdDngvChcu4snLuIPNAG3IXd5rsK6J+vnCNtbc2R8in0f9VRgeZ7dcCOTj4FNZkrNnTZ5t0RFZBpwX55fwQuQ8rjbj7jbDj7Tj+wdqlx5EbSZfap4WNNdadpaboc1yPHDEqWSw/W50uTY6r0yx3+iWPyxk6cxV84WILohuXMMG3yQNusOW28JNcwOpd6toWcnDhVPcBa7ggYHtmCZOylvg7ZKG5lDzdtmlxG6feEeXHkynsDGmwGmzOC1SD7/slrQ+OGh/ySitRSP7pFJnq+4odMPJt13qzlmW4fZrxqKVUMJghXLDUOOUbKXxgyjsyXKvrTsBjuNeuK6ZLhfzubHD6SMtlmm1q6U541SzcZ8vCUpsCdSaFVrkWsjC8NfzBYDENKs3C+82EtgisC6wssmSM+rkYk3sdKJecyu3XI4adYy8JXchE+OEBIJCV0ywcpetljqYYmh2oEnRTjnjvG+xJIdqTKrV9OU6w+UwXqOejB7so0kz2u2c1CTdUlfdSZOlWq2Zhp4vj/3F1OWj6Sn70NfZuFWu2ey45ZQdexRZsRKoITZ56prSRtkgEj7bOHFboSOn8w5V7pKrKlp79axoHOwQXl5mUhxj1fyAwJKa67JUJ8SuC5X1JTvKg3I21+aOg9XgnDUNjI57yuEtPs7RTd50PN6MdW4YWrU8lfpC70pp7KQ6ciTOFpjksrGwOQc3N8dzm0CRK9u7cf2Vjgp3Vp+vIa+drEwuVSQ7XbtjPgsUJljmV8fTTH5PIOPswhMakTJdIR8TpVDOLHsCLcciC46abxwIfEUitqhpSBSLR804iYlfXm45iToXuW02bbwKFE0MOn8lU2q3yljVVHA/0Gan/fbYwqO6zN3LiJjcjbQ2mckKm+02212Lfo9KedLTPLNcW8nBV3b7y0G+EX2XF56qdojJK+eDTRlRayxvdHnyWZvd27Rvw22u9Mwq2ySayMP0Ns6Lq73uYSdJmtEwl9z+lml2a9StclLnHj7T8DGT8OMSKerlzCtqmBAowZB2OqvMYmyGLN1YC3YilrmOhK+2vKSwKoIQAiMy3W6EkX0TxHlI7XPlINSrElDOPrlh+DW++YJE3YwFm3fHi1dgF5WOQ7phhIxjJTQ8iy1LYuzOrXNPtlq5uW7Ltri1OyxwSVD1FbZaCXsVNsVrtSICGkDKuozRhZ1KpteGlqJGbX9GyDyjZN01CLbqUj/TKs3XRtccjkQWoRR2K5aLU7KKz7hYIax16jj9oqMR3Wz3C8s7CXnbNz6nRWHDJ+sUvTm0m7QOfCS53jquqTUcVdaaqHabVLz5zIDJvGdko5c4EdU3csMzl31ewWGZGSle8VuiqmGvKVpTOXILaW6i+7TtXW/R8sqiXxTkTfUvS9WfG+0wULMFud/ZW0QPiRMfafsiPLmkIFWeqnP07mAk56GUnTwREnJ3CnYnFlvdkpCO0EqtjfjWzHBOPHnGXuUSIyLMhHXWpLLDt4Ek54xBKVfjYNXzU7qah1FJapgS02PJD9wlxTKz4EVdcJpDyuiUbXXb4jSu5jpjnSVavgHW4oNjy5TU1V+4jNQIvhpzG4cxY4kpeHwRRWyyGI8dA1Oas1zgjn9Lw+XhcA2Hzqt3Fi3FPlIS9EElvbzGcn1bkshho6jw4kByKpbIQ7CwKGl2tNkSJq98VBUbQoyo0mD9TNHyLS8eAat4DZOwqlIZ3KFKOYD3x2WVsmN44M61nQl+klXOjNayw+6wLQkBBNMu6tsMoQWytlZsqtnhzUVCzLnKhZJnkqqy1rFQxwWiEgJSdyQC+qAdzc/gzZLv8lUq77eN6tTqmGyc9Xq7zIdOX+fO2Z2Ju4GvNKEFexCu4RcDGpPk9uKcm7FnE0EKpR5bIalVJIaUhf4twhtdyuHSMXblLIkRL61U1UvOISvO1DqrEGrrbfIclo6rKFLok1LJwMBhd6bwq6qTSmHELY5W50DQBybB63y45GcH3cQbkkzFlXON9pQh77L9BjOjciQF1u5o/NSjWrZUZbqhR/1i7PowGs1dGjF5MpO2l3yR4mGBsurJkWtbMazohG7mOqrORrJm0qNwWC57h9hUi+JEm13sHDQ92+LycIAXeF3auX3Y3Y59e0wP0qbEMjwuUUbOyM7hpbZxV3w3pweu7CPhQM+IJNniTEZiSlMLCZV7xeUm9eRhvajgyjhch3LGpKhaF7mjHZyZomdXj+AzIeJWUnDkIyLl18YZXSFJswxPiWDnh/S2q50Rt45XR7vKXjAkClUp41J2TmgeNWIKYNFFazNpjPEE483NIy+7WXY7R9ytOwpHOQYNdN/Fpz6lSGNdbTGSuGS8ftDyAbXDluRNz2T0MFusFjpSU0d0MG8wId9mtVoNRmcfpFTbckTRd5WkVxI16Fs1EmmjVZODZvMbAr6sehI/kpdkay1ikmo3F0s7YZLGEoqdD3XhFSHB4IqpRIyE2Mq+l5m6qg8llWK65AR6Z7OUccJI7Up629sRy2GP9sKbtZ5H+uooa+fgCDNK3AXb8NR5+LaupRD0lbFERQvWy3egqBeqttmt+Oo0M2PSnN+S7ZinnYvim66f+WVoI/CF626WBlckT4l45++snXPgXKxQnD1IUn+luyXsHiRAhPRa7U1QJivQAXa5oHqkXi00yqqGFKQUn9yOjXPc566dd7KAcumeNneiJCQbHRU24rCzTYwBBGU1CZO79TmvJWKkLKMnNIuzt7U5NzWnxjbrKF4To7PJDuNFyvtLwNnjzRUyzVQtCZYEKjBV2xgiFb6x8Zlgtl4EK+saLZXOJGYXPDwLalsa2DUK6dAjamNuLOwzCwe6KOOn01jjsx3aojXgZKTLMWS1wvYReRHX3WV+Qq4e7M30kzQUM7wjLti8C7wxm3fscEXE6+zSIY0jGggcXIp0e8EcZB3ltgfHJ2+uFMnIgBzfMMiiga2rgaG2dO1hHt2M3j41l7y/CgjQAEZ+1csZHsxyjp5ZHF7mKq37DkI4TBB4yNZaa/DWcYtVONZINrdI1ZjToiAi/jYh+4UAbxJvmekw2E2TJUegiAWfC4fMpRPeZHJHBs7p6sDhXC/R4xbhxvk8IonNxR5CZYGscWl+W+BZiiLGvsJmHS+fKzU1VZVbUpYrhnyfupxvKluR3TH6hhIWtnUdN9GRpsUQmaeGhugbGnMMwYwGygt9Te22JpsAWrTUwxpum1xHnHTlbvesnSGg2M+av47OZWJTAOvKpdsekWgv6LtGGVlM4tlr6MAxeuod5Hx1WPzKGYc5slgv9nNkdw5PaGpfndtudWzbdgmTyPG8P1sOo4WF5puj5eMJRoSkExVKfxbVk2yo+xs23hb2PsP2g7WccXMMlK3chFyXwX6/PYZyYPYoF5CaR8BZjSbHS+XNliuHJ51lAPaPKZqfahQ+ZyuPac+qT5rr4MIKQuWN5xu6Ho7m6sjypLj20V3DyEHTtHp/Ck+n7VEoa59PGn3w+AD2kFVMHniSaU4iUjpNVFPqauiKbXOWZzc15N3Dib65LNnmccsxVyGstvRc9IesjrlCE6iZt+mX5W7dR46wc/YiIU09Fc4c7GhuiphE9adKWAodZhINQ21yBdvs+j27Toe+oYJtE+EX+Yp20rXolqUbJdfVINBFWTcMvuDYxG48JIPHoxMdCxRTVLMyB4PC1pKX45ttvhFB84Cf6j3tY8RNPPRnOlif6sKCx6DbRP5FOAqiKB0R1ZwtSxR4OVzjhEvlLULrBWddlzji3VjuZuwbcSMwFFJbR6GXEGasRtxZH2qjsIV1RbBoOSy5XOa7c+nGcynHDZIX3R27jQvuNkqXmWeYC2mDGuKqRDm0YnaDt1UxlT24eVfqV/PU46fcB+5cSUyMcCgVzngGngfBIoYthxjO4jW44gwCyLSfr+d7sj7P2c35ooAtfpKv8noeD2NelDKj72vPJmYCvO3qCrZNOPDW+JaYVQrX4PPGcJLTGvMbNeGDg4CVVbwxcV2/LNrluhtuylY76yYvX1bWZQ52S/HMLHAz39gbRdtfZt3hfL71C/lwK+YFmmACNxy5ay7MEB7sjzYOtUZtth65nXwDjRfGnED/JfUmp0gHHtFPOZdvSwU28StihItr4KyvloK73gxJm12CbFbR3tuuC07Du15b+SLZpkvR343zgy1v8AuFyRuBS6STdQ37ML7MtXy1tYuqt6pNwZzj0jl36rZgMXqt8VhxEG9ZuhuJdj2snd4b8FHTB4NA2B6BbzbBdKCNCW54veU5f4aUwj5oLC3JRYUzEUwHMFEdKscDSSIepa1+RcJ8MbfR81W+qLXrCZtRosOAW2YryYzViih5VkCQkZyv4qOh+bKLVmjeSCm+X+esKFnIfjv3knxB7MvrGOitfIxZabN5+fgynSs/T4f/0dvh6eDu/+z88HHU9/ZO6H4w7Nve5/tan/+hJj9/fKndGOjxOBFtsi58HiT+t/PQT3/xAmGaNDxer04vqm7t20l5a4fTfwB6iQuva9p6+PrdDOf5wu7r88D55W5CXrVf76+6wWXZRn49nWv/2QFsXEwvYHwvtlv/eRk+z4Y/vnjPN5ZfJ9P9uppMfL6VAJbBr4vX5ctv/wWyWhcnryUAAA== -->
