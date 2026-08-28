---
name: "rar-cowork-cookbook-ppt-exec-maintain-open-service-requests"
description: "Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_open_service_requests", "rar_sha256": "0e26a42992a370a4e4d5761fc8c5f2a981491d44dd961e6545cb5095d47387cf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_maintain_open_service_requests`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_maintain_open_service_requests_agent.py` and in the RCI capsule.

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

Maintain open service requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 0e26a42992a370a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_open_service_requests_agent.py` first:

```bash
python3 ppt_exec_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_open_service_requests_agent.py   # or on stdin
python3 ppt_exec_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_open_service_requests',
    "version": '2.0.1',
    "display_name": 'Maintain open service requests Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e999649c50d10a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMaintainOpenServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainOpenServiceRequests'
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
    print(PptExecMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZebWLblX+HF+2DnIxxMYnKtWqsRoBExCgmRzuVkBjFPkiA7/3tfJIXtfFlVr7JXf2jZYQtx75nP3uei+O3F6bu4bF4+vxiBU0BLJ8uSOGggp/AhvryWTQr+K1MX/EBeWXRN4vZd2bQvry9+0HpNUnVJWYDty6AIGqcLWrAVCm6B13fJJfjUBI4/QGp5DRq1TIoO8gMvhcoCyh1wBX6gsgoKqA2aS+IFUBPUfdB2LdR2Tte3r0BnXmVBF0DXpIshL3aarr0b1zlZmhTRp+outSiB5jdgVHBzpg3ty+eff3l9ScD7l8+/vXiZ04KPXtSqE4Fpu6duBag2Hpr1p2IgInOKCKytBhCYAlxXQROWTQ4+8oMQel59bIMsfIX+67/Sq9NE7U+fvxTQ8/XlZfqj9wXUxQHUlU7bBT7kOZXjJlnSDW8Ql12doQXOdn1TAHeAtw3w5e2x87uksoL+Pt37+FDyFgXdxy8vIGAg0CDqX15+gsoG6Gv66f3bJKX6+NNbNkX740/f5bS9ew68bhIGrH77+rx+igULvy9NwrvWvwOpj/y6wZeXH5ybXg+7Jz/Bzpe3M8jAx4fgqikvQeEUXvDxp38m1otBBWRJ2/1bcn9+CI5BGQGfnob/9HoP8i8Q/HTom8x/rrYCaf0rnoDl7+peoWeg/pnse/z/m+gsKUAvvEf8H4r7Rxvgv0M//1Pf/tWGVyj88iIEGWi6xnGz4DP021dDFfmfP/jfP/zwy+9A9P8oxij7xrtL+Jo7RRKCxvj69ecP7f3jD7/8/KGvQK0FTv61b7J/JPMfxfWu5w8RfK76+Me9QL9ZpEV5vUPDo9Kh38rqP5rf36CDkyX+98/bz9CP/TK9YGhy4l3pIwQ/9EwLbP0hjj+9/A5QogDe9N79Nujy//xPaJd4TdmWYQcZXtl3EEhwl+TBZPw+TloI/J16uwlAXNsEBPa5DtT/lOHJ4jKEfv1f3h1BP3lPBEWqqvs6YePXd/T7OqHf1yf6fX1Hv1/foD0QXzZJlBROBumcqn4pnCgASAdUV00w7QCg4g5d8AnA0afpDQTA9Nd/U8PXu7C3avj1DqbJA6t0fj3hVNtnwdvk6zEG0PzwzPuG6gGUlR4wKkwAzL6CGLRldgE4N8WlTZMsg/ykAUEom+EuG8Tu8yTs119/dZ02/lI8gJWAHuzRImDBN3OgT5+Ad2GWRHH3pQi8uIQ+/Pb7B+h/Q/9q1134pEMFMP/MDLBwYygyBDqtz8EykDSQZgAj98z89vszxkAM4C0I5DEJk+CxGVRqGvjvATdW3CecpCA3AIEGQc6rsukAWkNJ9watQ+ibvUDpdGvC87hsJ6YDkfeDwhuAVAe48y2SgK2gFpRjGw6vUN8Gd62/uo1zNzEHLe90v0I7XgXsUWbgn8nM+yKwuSwSEP5v5fD4HAhpPrTQ/F3EGyRPtQlVTuNUceM8dYTOIy+ANd63A+EOVATXL8VElsEUqnujPMITTayeeM+UfppyPlEyQAW/fdcdPZnfh/Z3rmu+FO2zCZxmSoUHSAEojfrEn6jhb8+SauOyz/x7/IClk6RnFvxnVu41uPvXc4L4Pmn8OGMI04zxpcdRbAb9/zCXTH5wy6UuLrm9KECivNdPj/hOI9WUh8cUBoYDCBTZo5e+DwzvcPOOul+KLAHF0gx/e6y8Z+W55oFkfQOCqHP6XT5wBsR3knuv2KkCm2aqdedL8Q7vr6AI7lgGIgDaG5T/VHXvCqe775bGoIen6+9Uf89w40/eg6qEqt7NQMWEQeC7DohpF0+xfk8HKN9g6sBrnHjxH7yCgHRQJUD+lIYEhBNQwD10cgncBA0XNmX+fXkyDVDACr/3gLVgZg3eoCNonKl4WtCtYAqa1oAofLiLgvIAxBiY+C3CbexUD2OmMfdpoDPlosxBxfyYgefN76V+t2UyH0h1fKcDsbxOCOwHt0dmv9n5zBUwdiqtR5b+mO6nr9CPPPS3L8Xdxm+gD3o+myj8h+BAoNfyR9VNkNUC2MmDZwGBSriz9duDcB+M/s2Wz3+a7T/+tfH/TqHmHzP3GYq7rmo/I8iD9t5Z7w30CgJqJKmCdmLAT1MXfnrvs09Tn3169tmn9z77g/hHtD5Df83EP4h41vZnCHtD39DplgTUTcX7fIGI8J/mp0+z6e6XQg++p/pZDxPqZgOg3G8U9L4E8FDUBNG0+EFJ7cRkV0CedwwGyfhSfCuHZ7MAxCiiiT/b8ocmvnPxhDKPdL1TBbhVdEC3P81xUTCdc7LJ/DZ4+Vz0Wfb6Ujh58O+ebyZOAFULIjIdjUAHgdmoS4L71bc5abr44wHv3lsAFPzy89Rir9A00wIgfB9PX6H3A8P9HFb04MT08zQaTyrBUvDft7XfTo9u8AKOad1QTdY/TkHTRPaclP9sxNRZwGIvmHi+/Naqk8Y/CQFvoiho/ixEub9xsideAEifwDvp3ru8BXb6YAZ6hUD+QPeBhgI42YMNf1YD9Ew1C+jRn9z9Hr/vbpUPX36/h6F7HCV/e3nHjWcOnmMjWA4a9FM7ESQCahUoBNePqgL3/m8HyqcYAHhgkgFy0ACnnBnOsrhD0KgzC2Y+SVNY6DEeGeIOy2AzFvNnM99nKSygyBnpuSTKkv6MJhjaC4G8R4l+nYaBZDItQMOAYDHc8wkKJ0mwnwaCfGdGO46PMgyN0qEPOOH7VkCT/tPfh39TML/NtlNcnm7/9uJSM7ByNWvX3OPFI+zBoY+0q8cu21DBybaQtZuYNeXati6jLXWuFDnl9/PCxhNmfehFediImOwdzgq6po87mV9RcxU3QteDDa4yiqUhxe5pns4SD3d7QkpD4AV9mOuLkvS9LLKR3KnEwTXKBjfzI4/BbqnheYWzi0N2JqVD1LBHuV4wzbi0Vd1yF+Hlkh0Q28u2Uq7n56UxuDy2TLtAojuJiavIaGzyQsudssxRXTnWJnbgefV03utNVmOke0xWxTwLrF02yA7eYotNTBIRqhQFjKhjC3u521JhS8tHl7mxCZufuvVWQ7lGnp1Yp85yV8rqKrcTFBuI88LECm2H3PKdlFfdenXMMTFGycbCKcS7bc1W3yQ8b2J5njUprY4psW5Whql3N7PctzdvGfWdk54PyyVGbzfaDDvZNz/BKqmQSA3XD8cle+h1Sp6Po2U5SM3W3RHbrrJKsJVKqYP9GeEZQ+vt1jG1wKvifbPLd1hLZNvS3POEPR6qnCKJcScmfTcY7sizsV4c9tfcuCx2pAVQajhUXb9LSYeHh1C+Fai17pybMtLyPmjdtJHNbFkuyVqYzeBuLZ30donCToQ3GH0b8vrs6FpUwFQrn2r94uuVDfvnTaFvU9nb34p5C/fl6jBgA+PbZMuGqhLZa9PYzboeprENo9fkQJ0si8HaprktDoUdNEwZcM3Kj+1Y7zR3gW8X0pZBj1QvM+DsOVJ9PkZGe+uSBeJH9Q4M2ENMY4dt3ixWiI2eDtz2PK4WsYS3t+3KZM5xZ97iLCtDDT4hfoFiNt6dt2c8HPdbeqeqzSnfL4S5GG+pRXE4HvNsiezTxWI/1Ek1UnE1bBPYXwalErazedga4XxUcU+daeGVW7NsIs2qPXINj8oGgxlGRfnroIypVZzmDJ8mA2IH+ZFyhmPmL8cdb8U1ZnaHs0a2Fm147mGhLHennFzv9RzV4K3GbSut4VxBqwH4+fNxqK2dbS1QfrM5L81lfvU1Eq0z/2pr+3Q5HDaDvE5PJnKiT5EiBll7DvktmQx1cDjIzb4cCyFxenVpuFd9ecMYmkUHIWSigg9T0NHkZuCDDYumRihIuNdcMcPfF60SCowwWACJZ3JU0MiC4tze3Ng4jmAII9hceLDExDjEjJUtl+zM6GXM9s+ReBQYOcqPsSkXlsacAgVFvXnR6LvoWLoIpaewm1RnlcguaBBG61oxrLlmrhHNhKP1QefJuAkFmq/dcXbZdSqvjUU4kqgdbOrt5XbN+8MpJLfYoaUOOCvXiKUKhqft11eT7a9XwjlVjKHv1oq6PfaxmMk+ehGtxnCjSGec+CYLI7Xst+ii2HbezcNTHaaSsPUP3eJ0OV0sfGtY/OY8SrC2TRO/r+uYONIkwxRYZqLsZrO2ulJs4VVSbGTbD3NlRem6nWLYXN4Ei5RM8baNquiycaSUaFPmkm9snRgCJyl3GKuu2L2MS8bZLcjEG/zSOhluc0UkeL9bryJlXI51BGicoy1W90Q4MShnAUhFU6/sVlHZI8GkQ4x4leZdFjVNp9eGdwO0XegCfRXOm1TsyIFnyO3Z9PanmRezuYnjylqVQqejr8vW2lBDQ5PRUdznbG4POSperPG2aWxzW+njEdkWdTLgHqMFpWjGvMbZrHbaMDhiph6nNvO4X83pKJ0bTiL7Bx7H40YKMiJeHq7CnnMWlR4vgpqzDnvMPp1Sd8d6KDff7k2+965SgtWtanSMotCkx5nx/lix1WyRbq9s2rI7H9ChodXmqPSXFr8FhU0x/ZhG6XITGmIe+siZqjY79dpRlZmP6GaObyXhjEoMrITyTmibPjxZThLxasarK5qBZdE607vLCtbUFcJp2xWpY+L2YoXFEd9wnNkulUyWNDJOLx0vcNmuz8ZNyWtCGOpsAAbiYRWJfYTZA8vVxGLYnm6kbIiyAm9qkt+mtYMZwnUhpswm0QlNhE9Fd9isxW2pr4/9Lo8czUK03Eww8jYOs4YzmK7IVjLguc1gWlizM400L+fwLnDLgT65SufKFVo5BSCd2pU11DeVXCi1VSKvh6LBdR3lFpfbrWCqvX0+YufTUrU3tJvTeApLY0fmJTgc84UDX+bYOFBJNwbL3XxlpjopDl0FOjEgiYHFRcKQ+bQ6IQsY3rcn3mxP/X6U3cNtIWoKfcmNm8rDuuoqs/l2GQqz8542F3Gq7KKkH2x6c6y6Ko5jtOKsZU174mouJ9KC9PCaJzgabXl9QHOpo5IN43Kxoa1ob+VUeRqvuUg49cPAUULirq1Gmcu5g7PqInZKUz+00Xxx2c9lKT66c382nm6efeJzB966ikyJhINZ2iK+kckVZzaLC53sF8T+mNbKXLxml7UjaFeSIGE7r8od3HfVjsM3A+vAmhTibTPWlWNUTp6eaBmpqUxLL8WOWJZo5C9p61gIGC0RK8M+e4dtidPzjvLFjapH0vygF7hYYvna57dqpnC4pFB60SWbfbbyuUsu7ens1OaGvl53Gy/XF61pCKkkF7Q+C7tRrvYMunFO9kwNUQIBLXhNAl8hCkcx+NuQcGI2Br5DCXFn2AfBPxwOgru/0RTSM4WLjF10Oh4v23Rxm2NlTmBIEggnx26LizebEUepwjCvJlDyYneOlPhKxTau7wDkPOahyAtnu4YpJ9LFq3Y114DiiC5WLe0c2VjMtIdbfix1d1nC+4T106oz7bNVqtHcibbSnsjq/sAK50JNN841jsXD6hDmXEkSh1Ew58Rex0kNbS6ZsZD30pL0666ZwRzVc1edhx1i1mn+odxUg5LvSDt2o5zSd42n5Pm6jW4XAJ1udPRikRKlbNCEJkcLRndrCxO0s8dVknzlmSQ00ApE7XauSGUrYzdXiQbKOnBqP2yVUzXEAZcqIzFWCY/tTv3GEM9pwY/4ejUSFE+aTMzaqCpJLq+lvWSIG2kvghkB3bsos0EphBsTHyW2KVadmaq+7csbaSsjpm+NJZM5bloHwaK9Zr1c2TJbsCcRqcz1qKWkKJckrBwyii35uFG7c46eTXhRczVC3jJzTzgaknijxhhjoPQZOujH5KbQ6R619pdGYbc8whC6FOVEtRCFmZuwiVkWAo+q6dnfcMm+h09D5NfV+WCkXVUfcyWRrJUy72faVtmPYd0t4WptE0FEqsuOCs5NnIjyYnHL0ivZOcu05MltVnJEyXe72VYTtNM6QVc7dAHzmGWHywzQWr0Y+Xg0tqml+EeM9E89o/gX4IeW7dy2kq/SebHF0tMqF8jONvKxPdsAMvzZJj+RxRGAFp/PmD1BbJqrdj6qYYUrTnIxkFjqO35xabTooMj6eq4xC4U06kKjuJN39pamQ7RqxPgzPaZHKtyZG85Gwya3umFhkzh14XUzzucr2FJVHsymPNHmKE9grIgjczDc+3Yr8FK9GpGlwMHsZaHVRDmktDaC6ZprbKE6IJvlSUx7OUlSKsD6eJNx/KrZza9XReAOpCLy9iI7hdKpNneDdta6Q3M2fP8Mu0dOthajwfUlix8uyXG+9FcbGh65rZ3GXF/dwjihYEGosCXvp6ZZRDNFxIs2F9m6NDSmvEkt1VvN0M0zU4oucEQdL6s5ysjDeHWUvlJLamke9FTRtyyldUFNeeLMENniprH4hk4s57q9BLUnMfyZhS+z4ow2fcX0mEJfx4O3JSgwbA4zPehC9kD0QkItt0TYD9eTFOCq4Oun/dzfGDR2u3SKbKpKdjQP2UonVXZpcWTbgnMrSbhCNa6a+lB3g4sc4Vh0Fb3eNyKzdrZSiF3WRcNxuOCIup+BZNGJRmHEYcfz7jXEArjxeISg06aqWz6sWMxZcbeLv3J50NsXiQ4x24GX8Y5oG5quwWgrsJRwDhJLswL6Mg/O43BRB8IikLkwi4+RDY47SL2ClSLrwoCy2c6S4cT2eRj0kR5w4YT/2CJMKCpLk2N2xMJ156e4iZQrelNeZR4ceEVNbueVjpKzs5KtxFW2o0s8mZFn5qijPj0Me4P2h0vvJ9qS3Gc4icqrZMZhcXO1djNsQ0gOS+7HZH3bBvbS2GQZuwjMGfAnSZhVKuEzUIMc0vhlrzADX7ZtmCC9qMY4fgD2WLDAJKR0oqLlhsD5ywXXWB9dCqWNdptIHU1rX5xvcXNCcMkM6YFe6wh2QfqlKl62kkTz8mleS+tV4VIWmKO7De6Ck9z+5Ac9dp2dkjGZd7YlA762iLYH051CBZ64sDqq9G9XwkM8xq1CtRUxkbPo+tDC53nY7yxjdr7l5G3dt2lQryrduC1p7AwrF0MCBB6dK7Og8Q1u0ON2IM39iHDRSo8vinfUhaslBdGio5ery1VIwERm5ZK67GfwVSBnS7473QIRRq5lRTO4cJsxalF4+kALmLYy86JyG8bq+uNc1wKR0ipPLPddoaVHgdBPgqguqI5V64Xgx/VeHGl4tz9vqcTlLjiGnnFE9TeHHjD+6CpBn+Wb1pZ0ly2XY9jBV70UKiFQiIFXGceWxLCpZT9nx76ZX4hEa+OxW2Gn9RZhvfDEePOTdvVhRRJtaXFbViwuhatu3B0ZFutQQ5OyslWG0iFX7tzF++AQZiPAGcGn+oWB7tiAaqT5zacjnVKIKBq5HacHgNM1m6pZ3F/OFxysn5FqqZMYIEk1ptgNtsL34ZG38my26zG8F01mLRk0i5kzWKYGwmHEUe4yxPLXLDWTJORirwXaYxA80xgUNAt7Jpjw5FCETzPj6XjTa2v0UQz3w66J3MZh25JWGxZOEES1l+pGX+1Psm+wiHkSbgswn+freXM9LAudOBUkjaPeeVuxt+W5ypuL6cFwg4wcKmjGPur21s1kEMLo147s8oQXxA6D72elfen2gdS1OHoBp6NVAq9N2YQFOL45O2+FLudoxnM9tT3w51sp7mKrdg3eKn0ab8kAD24S1R60HS92kS/ARzWF/et8pqxujImxjsgyKT3OrxxP23wgNdqiOgv5bXGATZ6VnNRGN7mwawsuZip8p2RzI2BTSQtVL0JWR9NW+/EiC5czvSBRLmOOrNgNVq3YgruSKiWj2ys7JmHUOfAec2EtW2kE1zZoxWejneAOXiOZIZgqvl+M0qXoLyS3UinSm4/Rkhw65dzOjcMy7Umel8+VgVrXA75FBFJLibzAjzd/tSLmlncbVsWSJoJ+O1DEGV1dh5oUahIc67mX15fpqfTz2fJf/WZ5etD3/+x54+PR4Ps3TvcHy4Hjf77r+vyXLfvl9aXxEmDX4wlrm/XR80Hkf3u++unf/LpiEjI8vrqdvia7de/P5Tsnmn4V6SUp/L7tmuFrW2b9/UHv64vbt9OvRLRfnw+0X+4u5tX0dPzdpUnw042u/Pr8TY6X6VcWpu9+Aj9xuuB5GT0fPL+++ANIWeK1XwmK/Bo01eTv8wsQ4Cb+hr5hL7//H/KM6WL6JQAA -->
