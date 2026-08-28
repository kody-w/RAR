---
name: "rar-cat-agent-skills-work-brief"
description: "A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_brief", "rar_sha256": "9a295dbb76bd5acabb6141ccd43ef65992dc2e63b2a0553d06d6f30fb42f24d2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.4.0", "author": "Allan De Castro", "tags": ["productivity", "automation", "teams", "email", "calendar", "briefing", "multilingual"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/work_brief`. The original RAPP
agent is preserved byte-for-byte in `work_brief_agent.py` and in the RCI capsule.

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

Work Brief — A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-brief
  Upstream author: Allan De Castro
  Upstream version: 0.4.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_brief_agent.py` and embedded as the fenced Python below (sha256 9a295dbb76bd5aca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_brief_agent.py` first:

```bash
python3 work_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_brief_agent.py   # or on stdin
python3 work_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Work Brief — A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-brief
  Upstream author: Allan De Castro
  Upstream version: 0.4.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/work_brief',
    "version": '1.4.0',
    "display_name": 'Work Brief',
    "description": 'A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.',
    "author": 'Allan De Castro',
    "tags": ['productivity', 'automation', 'teams', 'email', 'calendar', 'briefing', 'multilingual'],
    "category": 'productivity',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'work-brief',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#work-brief',
        "upstream_version": '0.4.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '669d0b5ee44266f3',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WorkBrief(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkBrief'
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
    print(WorkBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjVpb9K0z2hyq3slLsoOzoiEE7QoAECIScjir2fd/l8X+fh6TMKnvsnpmIiRhVhY3gct+527n3PdWvT0ZT+1n59PrExLGRQksHWhhVXWZPz0+2U1llkNdBlo7PoSQr0yD1ILMMHBeqfaOGSsewK2jImhJKjCB+hiwjdlLbKJ8hI7UhxTGS6hmIOilUO3F8E4W68c3xIuscKHeyPHYg03Gz0hkloc5xIqiqjbKuXgAKpzcSIFE9vf78y/NTAK6fXn99smKjAreetKyM5iMeIAnwe+BWPgCLUvA9d0qgNAG3bID38e1z5cTuM/T3v0edUXrVT69vKfT4vD2Nf6QmvcGoM+AHxwYW5YYZxEE9vEBM3BlDBayumzKtIAPALIFHXu5vfteU5dA/x2ef74u8eE79+e0pAxCM0ZtvTz9BWQnWK5vx+mXUkn/+6SUGDik///RdT9WYoWPVozKA+uXr4/tDLRD8Lhq4t1X/CbTe42Y6b08/GDd+7rhHO8GbTy9hFqSf74rzMmud1Egt5/NPf6XW8h0rioOq/h/p/fmu2AcJAmx6AP/p+ebkX6DJw6APnX+9bA7C+r+xBIi/L/cMPRz1V7pv/v+D6jhInerD43+q7s9emPwT+vkvbftXLzxD7tvT0omDFmSHGTuv0K9f5cNq8fMn+/vNT7/8BlT/t2pkUIjWTcPXxEgD16nqr19//lTdbn/65edPTQ5yDRTl16aM/0znn/n1ts7vPPiQ+vz7d8H6pzRKsy6FPjId+jXL/6387QVSjTiwv9+vXqEf62X8TKDRiPdF7y74oWYqgPUHP/709BsggxRY01i3x6DK//Y3iA+sMqsyt4ZkK2sAPzVpHSTOCF7xgwoCf8faLh3g1yoAjn3IgfwfIzwizlzo279bRv3F8Jy0/lJFAeCtaQd45uuN+L69QApQkZWBF6RGDEnM4fCW3oRH9XnpVE7ZAuIwh9r5Aijny3gBBSn07buSrzf5l3z4duPJ4E450oId6aZqYudlhKyNvHkHaAFudnrHaoCqOAMsC7kBIMVnYEqVxe3InGDxG1jIDkpgS1YON93ABa+jsm/fvplG5b+ld37EoDu5V1Mg8AEH+vIFGODGgefXb6lj+Rn06dffPkH/Af2rt27KxzUOgJQfDgYId7IoQKBgmgSIAd+DaAE2uDn4198ebgRqUqeEQDgCN3DuL4OEixz73afylvmCEuR7hwANICvrsQ0F9QvEutAHXrDo+GikZT+rash2ctCKnNQabr3qLf3wZJrVUAWyqnKHZ6ip7m3nm1kaN4gJqFyj/gbxiwNoAlkM/jPCvAmBl7M0AO7/iPj9PlBSfqqg+buKF0gYUwzKjdLI/dJ4rOEa97gA8n9/HSg3oNTp3tKxtTmjq275fncPEAKesR4h/TLGHLKyBBS3Xb2vfZMxxlal3FpW+ZZWj1w2yjEUFuB2sKjXBPbI8P94pFTlZ01s3/wHkI6aHlGwH1G55yDIWejWYaG3BoURHPp/GQRGKMxmI602jLJaQitBkfS7i6wsrUdX3gcZ0KYhoOBeDt9b93vhv/PfWxoHIN7l8I+75M2xD5k7pzQl8IPESDf9IKrARaPeW9KNSVSWY7oab+k70QJDoRurAL+DCgUZPCbO+4Lj03ekPijD8fv3pnsLUmmPrgKJBeWNGYOgu45jm4YVAVSje9/9DzLQGYuo8wPL/51VENAOAg30QwBEAEoBkPHNdUIGzAQRc8ss+S4ejKMMQGE3FkDrO6XzAmm3aDZgujEdMI+MMsALn26qoMQBPgYQPzxc+UZ+BzOmyQOg8YjFj/5/PPqeqzckI3ig07CNGniyG1nSdvp7XD9QPiIFoCZjdd1e+n2wH5ZCP/aDf7ylN4QfxAwSMh5b6Q+uAalYJtUtQUfOqQBvJM4jfUAe3Lrmy73x3TvrB5ZXaMEoEHMnqFuHgD4n773n1qZOv4/JK+TXdV69TqcfYi9eUPuN+RJk0//Sbv42+vPLrb5+p+xu9yv0h2H9dzKPJHyF4Bf8BR4f7QPLGbPs8XmFmvSj1D//cP0I0i0Ijv0MaGnkMJAiYz5WvmPfpgDJ+R5FgCdLAF+Nzh1Ax/toD+8ioEd4peONwvd2UY1dpgM8cNMN/PyWfkT6UQWAflNv7G1V9kN13vokiNs9LB80Dh6lNVjbHkclzxl3DPFobuU8vaZNHD8/pUbi/GGnMNIyyDvgqHEvASoATBl14Ny+GY0djN4ar3+/AxJvF0Y8Fkn2YLygfvfaDaldAhhjVXnByMTPEEDn1f4N/I3txj5uAmOqCnRFe0RbD/kI776TGKeaj5HnvyK4FSdgFTt7HWv0GRrHU8C175PmM/Q++992TmkDNj8/j1PuaDMQBf/7kP3Y4JnO0y9/AuMx9P41iAdx3AneMMeWMpr4JzYBbaVTNKCH2SOe7wZ+Xze7L/bbDWd937b9+vTODY8oPUY0IA6K8Es1drEp8gKDBcH3e3qBZ/9qeHuIAtoCIwWQnRnojLBNkyJNmzAswzRJBEcsy8YxxyWJ2Qy1LdQhMRM1YILAbJi0SReDXRNHXRS3UaDvno9fx64cjMtbgLNJDIFdwyUt1DAoDHExyiZoy3VoZ4YiBkbCMA1/fzUCBfew6W7D6LCPOfKWk3fTfn0ySRxIbvGKZe6fxXSmXqY4Zfb+dpLCk/7iksdY9PH4euxP+/hMbAsU7ha1PgvP80pdn9ZmJNcFy+axTafKAtcZWtrhnTLbtZfcmuZnUV5HK6mjmJxqrhXFDxg/o6vuyvBtRQlqe1WN/Uk+TLEuozy5mfWRGDf7nUmXAsWepCpdBZHgbMyNIuYop3F6IZPyZZFHMR6Zu/SCLNSNFqiblMuS3YGfRD421FKx79lYDQpVw0+yXsxOce3LaMxtuvMckWy33WJEb5+FoXcDwmnMejoRewaJ8LArVVXntItmYmI4sEvGrihtPddVi8wVB5esvGRys6vndiQWceSYHcYkjSCYCOsvMrxkB85ft+WMHJwiul7UoN4Hh/5yTNdzv8GOnk4lTqJWwQnlHPJUKeVB2pVbje4aGtWJTYHV2CqgMnuyHpzZaVcKendWe9PfDSd8iSHKXq1UL4/lPm5ZVSDWKeoQl1RujqWzwrbJjJjMl7LJTCKNXy3Ok83E7TSttSbdwVKLiytYnE7aG91FoyDZppIfqYFBE36sJrhLwxjB83U4CySNS3Ghiox5D+Kw62Kf6Yalkk/tKSKaiMtRvhjHwUaRF2Z26pIqP86PBXmVBJQSl6Y2sZeMJDKZBW/z+cxtl5RgV+Icnlx7b5jIhssPvYKIhLT2TbebY5fEuoRGKtbxpaJzbDBWW8uze73T7EUrHrZ9vrg0e5JcqU41sRFthZlbsUdBjIzS8vaEOzVCfi6aVQBy7DDQkV5qTd2fBjhMCWpVXWchx9MNeQ1pb0dQveyUhRU3TiC3FdvzbbwPtA2fUKxPdDy2klwpt3VRacVYX3GHWborMp5Pixh3Zz1BREFHEudBlaJFQ+9WzJFukO1ux4ROEV46fqG4g8opUjcLHIlBhTLLqHNUV/myrNV1uYqp7pr0py0zlwlFWTanlXJmpoizEK/1iZ1U2zSdr3cRt9abNeP7caPF1Tzk5GCwDc43Wfjon2Ku0wQpNanVMZ6wfjZHt0KNM0Kz5v2VrvnnAzyxXElSfAQnUhD0QTyENMfAqt+pK91R0/bs76fJvLdaeALv1R2hCTKJNlddXoQpe51SU4JtDaSywjrgD/mu8FSu2euXVhrwMD5kIoF28NrgSXobb1o4G4I5lWmcCZ/mNX+lup7aLRwbUQ3WEyISLpKMit25S2jkrLOG3XJyTCja6cKQIPenIOuESMYHtzVDKUVcwzhUx0TFLiJKW+fTnMXnJLERSFC2oqfMXLmoQ582jwGGe1h4zIV+707SgZaXMqNt8XLY5vGiEOcYRjT2xZ9dM29zKNFhe5Z6b1kiHaVs50FjpccNT0tGgSuL1ELSXOA2p1hkojjfbvc8b/dhxTekh0hd2ZrwEOcNqkfILNv4mWApHbku+l6s+mAHH8uI2EclnbtnRUOuvY6WthEVFlLv6PMkmZ4mk3lip5pAwUqC7neS7JVKFSq6nfpzHdmIR3ehKiimTrfXICLr5HoYTueBnpwmraIoBD7TppjEYUNlndx4KSVhv0xtVBWQzWCj5Xme9HJdm9tIy2ccKbbqLLeG+eCHsr3GQxOJLnLDkmxH+IjV+6stTYikwuG9i8MXAx7oaxPp9nILxNbqhFPXl0t72JLewbfOorNW8nWNEaqapUIf+raF8dN1cw3aIV0WGjBBdmshrVkZ9oDXWtEQV+Rpum61en2UZ1HQx7wvbVeb6YUsqPUGodSy2SD8yXQHz3CxdaH7VRZfu81RX174/hLIzapUGpdZUHBpxSLXzthyng4elQhqLLLusGxyJojJWLUvdM3q63WoEcuro+Qegp/IY9lb+1RLTom5VsljIXXbxBBCKYGrUt723E5mWCRwcWpbdOmxWPjHaOud1vtE5lHWtJpg3ijsxCI06bKSGUM9ugcUK/r2oOOrLb/MO5X0qKPD0Ei34hxPatBknQ+dmLglJUT04TLNr8v6zKAbZ2qyfbHNPD6I5b3favhuD5fawV513LzqFAeUYhmTtSPgwUI+8EeMELpMo2Yk3XKX4ZCzG9Tk6fUmg3GEW7HVZe0jXLGVVllyQNNTKPqSfSoxY+X1ckVKJHeUCkJahhfaqY6OqGmhvkhzR4+UZWQVl2ySdewp7mJK4+I0sU3VZPOI9QM8BVSeswXJs8ZCWc4jn7pc+NPBYuWi38f5pkpYopkL1wUV9qZh5Eq9m+zJpUjLscSF7CWSqk4+sZzucSty2GnX9eBuKfwqsAnuWXPpeL5oh3zJZcfB34fhxWuW56VZp6uWW3qrKE5qfBvBgG8qru851ndFjVOCvVetLzVP1a20ZY5L2dqah7bgHB3hC81lDzo2N3zpPA/W3AZJIzijF+lxvdcEQdTXpOLlZgSGjDpmm015MV1WkqPUrySf58I+mZXBCbtSmxBebOPlhRFgC0s87qh7epIHM6nYNBq6QKrOUo3NrNvtF+15EoMRjIyZdFihSZriCSdcNGEhwDXNhHtma6LWbhcK+NGVkEyK1ALdWsXJmIang2vyIpZvT2dRmOsLW4j89WTOkAUZbMDsQaCkiLFnPKtwoUTnUrGMS2F9jlEFTpSl5WNzOThmuBbAizxBovWy3lXL/bRXQx0Xk8RezJxF4y2uVWqz7CrQtuEsK+wVqlZTfM30C/OMqDraOUd65fsnJjJBH56RFz0/e8xA5k19XRWohjao5rUdU9uqptaZZe72qsAlLmbg+yQ9dxtfrlBmUxSMjKv1ko6Fa79ce3zV1gzBCD6YMnMuOFB+19Nh3vdkphbrQGYx0KqX10m8SopmSnWLfDCWitXNmJJCwVi0LMuQYjbUkZ3kp2rnBUS0aZLjfFbKkX42s4Arztz1fOKx5Z7fkPuwoCNyQ9KTSRrXXLQr63IeZbqxrPJFv8WkwdirnLq3mVAtrnNvrcy0DHRCQNdNJlUNfLhes9DMBTRBptYSTNZOc5n7PKXTApFyp9Mqw2re8ZN0lbGCdCTmw2Bto8o788Ex1yrPKdNGt6XLxHQ596wJ1qAdYaRRqtP0clq47G43lXwLPdEsMU2u3WR9PmmX6akoMGO6byYuSD/hCk8MGpUnh2Lb06fjyWXFszU/nMUNo1NgUu57Y1hbyjYiva2ju+Ih71JPdgowK+PMlFxE3HG9PocYjbl9jR0YV2VoboY18EnRr9EqrUpbnQ8Z6BxLUEXGVgwa/Yo7DTlh0uhA49vl8iISsRYvjsd6vwYLrenl7qQU/sUX2ShLKxWH8yZRUSqhFuFKKtbHywaHN/trdTFwIUeD6R5sePprKDaarG+Gdag2G7dCOprfNvRWVtKJdhBiQpz6vICo6GoWKAdkOl+xBJoczrqIE2Dyhmte5wPPiic71K1KyvQ252LT4WmH2WAOPcckt4PNbWpsUVt1CizUp6YUHPdNvLp0V+EouYRHW3bHt7IdTSZ4oO72BzRL09U58rfYekeJu1qfDlMhyJUCFz3bOtt7M9wdWgps7mh/oy6YNkCSK7wnJmxomRXnn0MmDH3WZtJatYbljjSmhVsVgKr8blrC+nB0gs2FbC8Z7su5LiJsN0PscNmpSQb7Nd4cRL9cKW1DwGnqFyLt7GhY2mm42gYbCVcvrqvOrXOKdbJ0WVPZZpghfA+2SHDYXvTgwG35dbCguR6eOtYi8I7YlVUVfdqQ8yJrD9EOwSd223GFIabK5NDsjHZF1SYvWYfKta/YMg6UkLOuVOOZC2oW5sExOG7aQ33obGx71Slv415oeiYaQlPLG76icDNYeoOMbXaekC6PB3wg04MuskW7wadtutge0CpAUlPhF7ilzBvsqkXXzBbbWYQ0Z1twDFebDZsks0BmkU6AzqdSQjMKT3bHU1to7cmViGwG96vVMuXdrEFmCX5SuMt8ObueWMKeGWdqym8qtMA6ZtkxgIpsTrlMBA6bAq7XFLF1jD2BnVvkInXXDtdoPCx0cX+c5hmpUHYiHtp0P8wJyfZkck9VMr45s9iBnhAzJ90e3M5tKX99BFvotVXabb08CwbH2ESveIxB5yejapR2wGa5mDUZrl8l+Koik7Xuz7gzjgkMvIrgZUFOuO22x1VpK9WAuCjCVhAM0ci4c0tM2xOHDMxFYCNQIOeoV1YHcjvP+s4FE37NrbgzkYb+1Yd5io/PZ5TILaTVUAfL88ZqSB1pCkbb5BsbxhJlkirJKl3CM7FI6qKrprlIw1Y0N/BjGpDwXNZhvJJUN1nboQjeWVyia7nrDJezG0yOiMK5LOB0NmWdsOS5M6VggYYFFIIPbJnyGNnOXTdwlmdREUkynJw3RkJNXY8cpvhQtfwcT3p0ME/nS75aVA7dsId5phTn616V3da5ejqRI5V4YOzMtwSCHGh9pQXkmtuuFH/Cr+SpkfO4tuhpeNoeMTOYJbt4PbPnjRpP8KOi76fMepb165XKdgzz9Pw0Hs09Dtj+5Net8Yzj/+yo5X4q8n5kfjvYcgz79bbW658t/svzU2kFYOn7GVEVN97jmOWPJ0Rfvh+3joLD/Veg8bi+r9+PEWvDG/8NwtP92KsO2qAe7Xs/Ab39i4N6/JljPHkbfwMZD9seP4KAy5vy8TTs+Slp4jqIwXVjxCPIx4HtDSgOoP72n+jyQeyWIQAA -->
