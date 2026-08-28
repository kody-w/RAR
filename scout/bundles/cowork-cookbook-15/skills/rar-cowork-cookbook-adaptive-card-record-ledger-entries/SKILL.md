---
name: "rar-cowork-cookbook-adaptive-card-record-ledger-entries"
description: "Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_ledger_entries", "rar_sha256": "47765e95b93ddfcb4dd0514e896f83c0bd59c31448b741aedcddd355ee8e4264", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_record_ledger_entries`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_record_ledger_entries_agent.py` and in the RCI capsule.

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

Record ledger entries Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 47765e95b93ddfcb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_ledger_entries_agent.py` first:

```bash
python3 adaptive_card_record_ledger_entries_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_record_ledger_entries_agent.py   # or on stdin
python3 adaptive_card_record_ledger_entries_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record ledger entries Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_record_ledger_entries',
    "version": '2.0.0',
    "display_name": 'Record ledger entries Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-record-ledger-entries',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '786ec6c04ed8c6a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-ledger-entries'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-record-ledger-entries', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardRecordLedgerEntries(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecordLedgerEntries'
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
    print(AdaptiveCardRecordLedgerEntries().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebeiyLbnV7HP+yOznpkHmSXvums1KjKoiCgIVtbKYggGmWehur57B+o5Wfmq7utbvXqtJgeFiNjz/u0dgb+9WE0dZOXLl5cjsNIJb8VxGIByYqXuZJl1WRnBjyyy4b+Jk6V1GdpNnZXVy6cXF1ROGeZ1mKVwuVJmbuOAamJNStBUlh2DCetacLgFk6VVuhPpuJcnVWrlVZDVk8yD85wMPo+B60OOYCQO11e1VTfVxMvgo8QGrhum/iRMJ65VBXYGCVWf4IAVxvATzjkBK6leoTjgZiV5DKqXLz//8uklhN9fvvz24sRWBR+9vIkySqLe+W7vbLkHV7g+tlIfTsx7aI8U3ueghDIk8JELvMnz7mMFYu/T5D//M+qs0q9++vI1nTyvry/jH7VJJ3UAJnVmVTVwJ46VW3YYh3X/OmHjzuorqHbdlOloqAryTv3Xx8rvlLJ88s9x7OODyasP6o9fXzIogjUa++vLT6PiX1/KZvz+OlLJP/70GmcdKD/+9J1O1dhX4NQjMSj167fn/ZMsnPh9aujduf4TUn241QZfX/6g3Hg95B71hCtfXq9ZmH58EM7LrAWplTrg40//iqwTACeKw6r+t+j+/CAcAMuFOj0F/+nT3ci/TKZPhd5p/mu2OXTr39EETn9j92nyNNS/on23/38hHYcpjOE3i/8lub9aMP3n5Od/qdt/t+DTxPv6sgIxDO1yzLkvk9++HRVu+fMH9/vDD7/8Dkn/H8kcs6Z07hS+JVYaeqCqv337+UN1f/zhl58/NDmMNZhv35oy/iuaf2XXO58fLPic9fHHtZC/lkZp1qWT90if/Jbl/6P8/XWiW3Hofn9efZn8MV/GazoZlXhj+jDBH3KmgrL+wY4/vfwOISKF2jTOfRhm+X/8x2QXOmVWZV49OTpZU0+gg+swAaPwpyCsJvDvmNslgHatwhHhHvNg/I8eHiWGsPbr/3TuwPnZeQInYj3B55sD0efbA/a+PWDv2xP2fn2dnCDprAz9MLXiicoqytfU8uHwyDYvQQXKFgKK3dfgM4Siz+OXERd//Teof7sTes37X+/AHj4wSl2KIz5VTQxeRx3PAUifGjmwFoAbcBrII84cKJAXQmz9BHWvshgiej3ao4rCOJ64IeQJa0J/pw1t9mUk9uuvv9oQsb+mD0DFJ49iUSFwwrs4k8+foWZeHPpB/TUFTpBNPvz2+4fJ/5r8d6vuxEceCsT2p0eghPf6AjOsSeA06CzoXggfd4/89vvTvpBMCmsN9F/ojcVmXAwjNALum7GPAvsZI6mJDaCRoYGTPCvrewmqXyeiN3mXFzIdh0YcD7KqnrggB6kLUqeHVC2ozrslU1juKhiGldd/mjQVuHP91S6tu4gJTHWr/nWyWyqwamQx/G8U8z4JLs7SEJr/PRQezyGR8kM1WbyReJ3IY0xOcqu08qC0njw86+EXWC3elkPi1iQF3dd0rJBgNNU9QR7mgZOgZZynSz+PPodVP4Fo4FZvvO9zrLG2ne41rvyaVs/gt0pwL+pQlH7iN6E7loR/PEMKVv0mdu/2g5KOlJ5ecJ9euceg+pc9wfHRE/zYT3xtsBlKTP7/Nh6jzCzPqxzPnrjVhJNPqvmw5dgtjTZ/NFiwAbhTvufN96bgDVLekPVrGocwMMr+H4+Zdw885zzQqimhwVRWvdOH7ocKjHTv0TlGW3nXxfqavkH4J2iYO15BB8FUhqE+Rtgbw3H0TdIAKjrefy/nb5aC/ocROMkbO4bR4QHg2pYTQanKMcOejoChCkbrdkHoBD9odTdxP9KfQCFCmDMQ5u+mkzOoJjSzV2bJ9+nh2CTlD7+6E9iOgtfJGSbJGCgVzEzY6YxzoBU+3ElNEgBtDEV8t3AVWPlDmLGDfQpojb7IEhi7f/TAc/B7WN9lGcWHVCG21tCW3Yi0Lrg9PPsu59NXUNhkTMT7oh/d/dR18sda84+v6V3Gd3CH+R3fw/a7cSYwr5LqDqgjPFUQYhLwDCAYCfeK/Pooqo+q/S7Llz+17R//Xmd/L5Paj577MgnqOq++IMijtL1VtlcIDgiMkTAH1XuV+zzWoc+PyPn8yLHPzxz7gfTDUl8mf0+8H0g84/rLBH2dvc7GoW3ogDFwnxe0xvLzwvxMjKMjunx38zMWRnSNe1hW30vN2xRYb/wS+OPkR+mpxorVwSJ5x1roiK/peyg8EwVCeeqPdbLK/pDA95oLHfvw23tJgENpDXm7Y5/mg3ETE4/iV+DlS9rE8aeX1ErAv7V5GYEfhis0x7jpgakDG596HIJ3703QePPjpu2eVBAN3OzLmFufJmPD+mny3nt+mrztBu47rLSB26Gfx753ZAmnwo/3ue87Qhu8wA1Y3eej6I8tzthuPdvgPwsxphSUGEJ4NcrylqMjxz8RgV98qPifiezvX6z4CRQQy8fSHNZv6V1BOV3Y6EAIb8e0g5kEAbKBC/7MBvIpQdHAGuiO6n6333e1socuv9/NUD/2ib+9vAHG0wfPnhBOh5n5uRqrIAIDFTKE94+QgmP/N93ikwREOdiqQBoETVMkYEibwV3Xc2zCdWckSoA5Q3lz3JnZLsk4OEoQc5smUAu4juu6OEkCMAcERhGQ3iM2v43VPhzFwizLmTs0SrgMbVEOwGc27gAUQ10aBzOSwb05XAst9L40ghD51PWh22jI98Z1tMlT5d9ebMjyy4tAVCL7uJYIo1u0sbVvgcEMlGeK13kmHU9Zs0lg7a33a07HcDNyr1MNi1COoFjJjIJmcV6EdLS7FbK0F/qFkhyNsqGbzani+3Q2TTlifjg6itfgXn2jy3i7iLgOHLWjbpkVN435mBuiPFeXVdeuTpZxsZxsK1Lz9X66P0w9IzWY61YrdJ310/0xXudC4oaiYuDhlAE7CR8OyVQ3z5nc2Jxby7AgeotsTVSz2Ev4/tLHBs9cF5pOBYHrXFrf2BXzNT6Nu901ZqbtSZ+6ygmdel6l7IwSRRhuuzXOc+4Yq1V2Kbv+jOqbinapQb8Ucbtc3obN9YJc5cPWL+plEtj5Vmr2pxgpuZPBVc7NrNmMy3e6WWjtKWcurj4kjkxpYS33EnHZLOn64AXRDd+T67rcEZJaaucid3IrJ9mivJ4LLKMBmuqVE6VEe0y12smJNGvN48DspDR2b1Kwx9bhRgaGuE6o1WJxXBjNcdniyS2uGsy90Tl2orPLSmJ5hBkiR462gacsGlAfaT0P0u1BC8w66WH7ul4KtFdV8oaqnQoNIiq7RI7S57qjYmxJyhKBXpmLaQyBpBtxetorsUfbvmpYyCkhMHaOsHNXsw6ovhI0jCZI9gIGVLmh0bmvnLmwmJnh0hDhUpJADskNy7StXQNFYkysDbkWmwZp4uAqGiq7UNikvSuYIo0c7U2NdY2zFYtpsQuEjk92BlN5fLTUaA2xssssd29eqAj6TEzLfYpx26WH2ldNPCyNKjPtMEV3xmma3aal5FaWNr3GZi6YgRl76/5S1LMF33PbbOF5sax5fG7sDQmXjZMheycdl4co3jKpwLsngxDWVD/MdwJx2M9htCV+utUQgkuH5uIhwwphw+lCwNDO8/wYGLhCXPHT8RhtsxtAj7sDnqBSdVyF/c6VgkpzCmLQsPyw2CX+qVtc1hWwCZVl+Xqf6psbtSaalA0GIdpX8pqI1bpKHcklD5dgJS66qA+LzXDcYGxCpy4bsDlaRXq5iHwt3hIFKZ/BguucgRnodE/w+IxiHGt/QW0pJ9TFUeml6NIYAacE5Kmcy3RUH+bSGjkP6D4PiaHN8EJZdV6gZnLXttDL9LQzFm2sZUg1ta9RwTh2W69N7xStxbUq+jgW6bqt8pYzyNmsXB2G896XCsIKIbwLgnEWshwlNUrklOuaEzVrvdn06rBJKfWYqD7iVXwIYvyoOGLI3WbMzhU8IufO2s3AS5abB7VON3GWns4ycZ4Xp9g3+GNazXV+2vSlEKGFv+bnxflQyIttknAUZe0W5pKQnHS+mjErmgov64Ezdi2na1dfPU0DtGls1blOyVMtxVymBUhkFL6kw6SIy32N71UkvdH2RlvJADtQFLeTANm3tlaZ+/kQbaRtsrSyAkPV2NhFlXSs5WMZ4Rk1D8+ieMNdoB2zYzwoAuPqyfbcpkofab0LbYvKJ0wrZnUUrebXKD5fIsAyoZy7ulKlszhBM0Pz2O3+SjFThNYcdgr8vaCeyFbchXroXy3Z3h8GLbvSXSoYYn2bbtQs4K7d4sRax5m8W+inYNZ07Yare4kfdoiNrrrexjbSXuezgUSSAaXW8TE943WAMmUrVe3stGd1TYsCxMndPtAUStZjHveohuc7Z71fHmNJ2cxO0cl191gSDRXQgp3ESRceNXEu6crdaaHTfoin7tTsDoHs3PQzuGQiGw56qnp9knpBnW2OG9vtZgd+uO7OtxuataVYkVq7WQ7bkmTc1J4SzdY5aFRQ79QLQzPyZhp1yAbfoIBku1kAZhZn1MZARJ0l4oa2xAhH7HMW8ZBYlMTpcYFORWbXRpyBZNxca5dBqdXHFiZ4dTwsr0SkZRf0OgSJanKxsGHiKNFZsDwHVGg5xsnaN1x43urRdr6w5ueLwR/yQpUuOLrQsoMWh6vDVvGdBaw7S2F+OOGalWgzXS5WNDm7SjltrRn0tgmlK5fVCCuzkrbQ5smtOeZkSefXq1l2QKeokyhOw8aPdwHG3uwzjM5yuZ4hVpxn2dYu7RlVLasVIa43stSlW+p41myhIWdJKBnW6TwbTF0hpNJK6VRnLjhyxavWLk5N7Z70kNtxxubCnTF6EJm2uTon98pQ4eGyX9q0MKP0mu1dkKjYyrT2EJNyrZnKqXb2MBEiDxuzQ9HPMGV1bXgfnJcqLUZVfYnS4woVaJfRsro7GVXP7lPjFPYVses1ykeCrDJO9Qpn2iXn9IRepeccRPuMDb2DQnH11SCka8U7NREfXbvsplLJLNVlniy0GDM3+XmzPRdJhbHG0mWzRInVwZyeZbTRZ6rpkGYmt0vbprJoW1Nyst36gRJ4A5fspJuLeYkdXNi2RVvBlAutwdpgjiOltKPKKNJsDVspZGsLWsKVGJnMukTbFjOrxxIQ0yA7LnZ0GKiY680o6QhOu5MNsZJXDl45sDBal86mF3IQB/68XJpGKNiLKuNjiNaXNZccst6nZqFki7NFNrd3/C1j7LOXr8RwLfnb9KQQTssjHWKZ3qZ3DvEVFVgxO85TzRFM6jIUFrURQ4U63gQKSaZpiWCuvztr9TJbo+Js1+FkoQrbWdCsLxeGkhn0SqEXfcMgezsw0ZDku6I9z5VFsuF91SdZv8SycjY3xZOwY4XNIt7TqTVFOY4Srgd3q5tSbIlCIG1zAhgkf5hPtXi6GOQTrftDqReFTq6uW0W72F0QcGtBBwmbrfF1X2WFRmP6NWFQvKt3eXm4HivYk1qezw2sqV29rT09m7wZhRZ7zVH5LG4YaTrvCmNVq9IqjXboOdYrLreShZEtrjnvG3HElXSEh9skPaInY8dgx8FhszJNqsLbO67pnLa3IGm3ni9gvIalPCUmt2uyIalVNShgN9uJ0UIGx2YVkEvuuJ3mg2hJm6gjBeMUxbUdx6IC8nBDiW4hK9RVWM0XNctkc2VfHltmrydBt0oxV7ASM8Q3FlVL/Qzf76aOitd+mQKatpe2tp0dmNAN9/pU23tCChYra4VNb5XZefx5G+47rt3ZtiVTy3J6PB75a+KpaJKkIVVR6vS2R+JDxOSYu0/ThCYqFi+0IG3MnrvUx1UibdqNzR1MjmhmciEkwRSNYtXe1tlSE2yM7BR8KRxa0nMbc6ikE6Bqan7Qmf1t1sfCOiyobMl6eH46amziH6PzabjKvnuRdDcvYhL6o+CpYBlX9cqQuYJkJfQwuzDHPi5LG2CdMUW4WXDd61nP0YM/P4n6ZXdJlGOXAGNxq8mlb/omYIuGmMVH2ip2vSS40yFBuOzG4qp71YgUE7IjnRR1Ods4ez8pWSsZYMjsN4WDZ8vquOsuug3o6fKGBzznKet5hxLL4TqfFouCQiW3KdEEFcXNHpFbcL4s3URoz3mxbstGqskglV1OAXKoO2Sxl8oe2TmDFhR0sJAxHk0dZVfuEe26KMJm0YczAsTTfEOuNA4zV4EvaKw549ShWh4CTU+tbhuvlIjQkJifYZFSELG+FHR+y6zQnV1tFMLz6cXVBl0L7WkR3LrhBsTcK0J3US+Bqu7NC7FdHvKMxm+Ly4ZKPM1fY3gpRTZ3cnHRO9aSKaRXfwdqF9fque8v+Qwtk1ZJIHLvr2mgDpi4QnNg8QivBnB3263xZIrMFO8iS1Ok6EvApDHqlaszdUFww6ebG90YLuw8Y6sMe7d3sLMckDJ6S2f60hcFo10XMnmawS2An+grg+v2pMpWa669xXiIb61OEbSTvt2hqkstpVIMdViBiSBSDaVHWFBdCkqwpAIRCwYXfKN1idtsXW1Xtt/2i70HlkjBJ7U/dyylqL3zOsroShWQqqxlFUSDBgTfGipk05wcf0NEnmAeEdkANBohOkG0KVHSyPy6nfvnRXy2WqSkp1KbUwGDrvBtW5aLcnOgbxoeMYecCHAh2yjLPlmby0R1MZtNHYfXka7uDwtWTrwKG8KMXRxOdd9He1GYCfHO1PClSK7CxL258s2WarchPdG/sSu7qAYXm6e+eZjWsCFJlxufhiVgbpLD2lxtd+1xfUWrtTcTg3arNlMBeocq6ASZxp4/5acUtQAXaU27psfV87ZpfJtckjIO1ALu1VYqRwyFyZA4P/jmrFoXe+NghBfMqZYXPiCpK3LWQegxtSd3t0NMH1JPUxVW1kl2XnqB46xwPCVXdSM2Q6FiOHd2Dny5YarLybox8RoIp1LvXS2YK1mSgh3ReySJL+GG/dKwXDvsSp3gNwi8QzvhKuOhuievHFuoGs1bLa+QPZ7vA1GE/Xqt4JlRxUGoo32dpnW92A8rUGXRNe2KM91tLWwPXHa6i5ho15BEjAvAOew5x0KvOXE0h1UxlGRllB2xF1Y7dnBXzEEwk0SyU4evGwzuS5WNy3LnpVVigy9uF4NVBUUcQnOfdRl3g2zgenTO513qHuRQGeoZixGpK+nNDZuf6D1ItETa7fSibrSr6RW3vksHaQFanQyU6czEz2aZ76cnjKQp6uIS0UZ08APDKUsDEQJcEVbnnch6p6Tjl4y3OHvNrd1it/PKVC1sLpjrrjsLtnatbNmvqBm+AqSrobTDeHiWnYPhiumBpWyNQsS3M+/YspZPLHRGI7hpjpHKle194N8g3oiIlR8cYYYArQ+FMs35FFsQUoNiDadNxa1hXym9m4tyjBwQIp5jPV25a4aiSoUmUx+5dUM3NVbhTKH4nTlF+G3r0IXXKTye0wdiW1z3A01jZkH3Rl6p5G2KiwoyLyuT0Fee24W2obVeA7fjaj1T85C152s1n7nUenpmgitv6+JZnLk71CWDs9ieIdiQGe9HsUS1bZiTcyBz6s5qz/WNCVAyibEO8axmZtg7NweIy7M6VR9uR06hhEV265zO3B41cTdoK0NIVpmLXTZlUw9nslTqusbzvCFlSsjatb9dadc9LeAyyDXmuiCArEIbK0CaTh1gsuct63b1fp1X/M6eXTTyAAkUanLgXd69bFY3WDBpV1JPgIm2lgzLpXctRbnF6na3bkNaJzs2Zs4MX9+MLL+sbGEb7+MZpDkUns9YiIp6wOSv4uma6EMSHMn9jV6butcHi0KhpR2ZYAOi9/4qdd2GJQ/LyinXOdKZoZSL1YFNbSoJVqFqAg3AfVgmR61+6xmatJP9pts2dZrdJOM8BwfEWJfiYLA5y7L/fPn0Mh49Pw+Q/84r4vFA7//ZueLjCPDtddL98BhY7pc7ry9/S6pfPr2UTghlepygVnHjPw8b/8v56ed/4z3ESKB/vHsd333d6rcD99ryxx8QvYSp21R12X+rsri5H+J+erGbavwtQ/XteVj9clctyceT7x9UGU9nH8rU2bfHW+KX8ecG4zsd4IZWDZ63/vNc+dOL20NPhU71DafIb6DMR3WfLzfGs9jx7cbL7/8b9O6uxK0lAAA= -->
