---
name: "rar-cowork-cookbook-report-lease-assets"
description: "Builds a structured summary report of lease assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_lease_assets", "rar_sha256": "524ed9b52ef8681cced6d0c68ba0f5596706440c75a47e00752dc78cb4f00bd0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_lease_assets`. The original RAPP
agent is preserved byte-for-byte in `report_lease_assets_agent.py` and in the RCI capsule.

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

Lease assets Summary Report — Builds a structured summary report of lease assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-lease-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_lease_assets_agent.py` and embedded as the fenced Python below (sha256 524ed9b52ef8681c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_lease_assets_agent.py` first:

```bash
python3 report_lease_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_lease_assets_agent.py   # or on stdin
python3 report_lease_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lease assets Summary Report — Builds a structured summary report of lease assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-lease-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_lease_assets',
    "version": '2.0.1',
    "display_name": 'Lease assets Summary Report',
    "description": 'Builds a structured summary report of lease assets activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-lease-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-lease-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b4ed588bad8055b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/lease-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-lease-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportLeaseAssets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportLeaseAssets'
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
    print(ReportLeaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6abPayJbtX1Gf/mBXc3wEEpp8oyKeBAhNCCFAA+UKl+YBzSNSdf33TgE+dnVX3dc34j08gFDmzrWntXem+P3Fapswr14+vxw9K4O2VpJEoVdBVuZCq7zPqyt4y682+Ac5edZUkd02eVW/vL64Xu1UUdFEeQamM22UuDVkQXVTtU7TVp4L1W2aWtUAVV6RVw2U+1DiWbUHWXXtNWCs00Rd1AxQHzUh1OSNldSvUFN5mQveJwR25VlXN++z+g0s6N2stEi8+uXzL7++vkTg88vn31+cBIgDANT7ItK0AH2XD2YkVhaAW8UAdMzAdeFVfl6l4CvX86Hn1cfaS/xX6D/+49pbVVD/9PlLBj1fX16mP2qbQU3oAYRW3QC1HKuw7CgByN8gOumtoQYaAo2zp/pRFrw9Zn6XlBfQz9O9j49F3gKv+fjlJQcQrMmAX15+gvIKrFe10+e3SUrx8ae3JO+96uNP3+XUrR17TjMJA6jfvj6vn2LBwO9DI/++6s9A6sNVtvfl5QflptcD96QnmPnyFudR9vEhuKjyzsuszPE+/vR3Yp3Qc65JVDf/K7m/PASHnuUCnZ7Af3q9G/lXaPZU6F3m3y9bALf+K5qA4d+We4Wehvo72Xf7/zfRSZR59bvF/1LcX02Y/Qz98re6/bMJr5D/5WXtJVEHosNOvM/Q71+Pymb1ywf3+5cffv0DiP6/ijnmbeXcJXxNrSzyvbr5+vWXD/X96w+//vKhLUCseVb6ta2Sv5L5V3a9r/MnCz5HffzzXLD+ObtmIH+h90iHfs+Lf6v+eIM0K4nc79/Xn6Ef82V6zaBJiW+LPkzwQ87UAOsPdvzp5Q9ACtmDfqbbIMv//d+hXeRUeZ37DXR08raBgIObKPUm8KcwqiHwd8rtygN2rSNg2Oc4EP+ThyfEgLd++z/OnQw/OU8yhB+c9vVOaF8fhPbbG3QCovIqCqLMSiCVVpQvmRV4WTMtU1Re7VUdIBB7aLxPgHo+TR+gKIN++wtpX+8T34rhtzsVRg8OUlf8xD91m3hvkw566GVPxA7gb+/mOS2QmeQOAOBHgC1fgW51nnSAvyZ962uUJJAbVUC5HHDzJBvY5PMk7LfffrOtOvySPQgThR4EX8NgwDsc6NMnoImfREHYfMk8J8yhD7//8QH6T+ifzboLn9ZQgHZPiwOEwnEvQyCD2hQMA84A7gP0cLf473887QnEZKAiAf9EfuQ9JoMIvHruN+MeOfoTguGQ7QGjAoOmkzEBC0NR8wbxPvSO91mJJp4O87qBXK8AxcbLnAFItYA675bM8gaqQZjV/vAKtbV3X/U3u7LuEFOQylbzG7RbKaAq5An4b4J5HwQm51kEzP/u+sf3QEj1oYaYbyLeIHmKOaiwKqsIK+u5hm89/AKqwbfpQLgFZV7/JZtqnjeZ6p4AD/OAQcAyztOlnyafg0oNCi+oot/Wvo+xptp1utew6ktWP4PbqiZXOIDswaJBG7kT5f/jGVJ1mLeJe7cfQDpJenrBfXrlHoPSj0X9+Kz5j3IMfWmR+WIJ/f/uDiYY9Harbrb0abOGNvJJNR/mmZqWyYyPPmeSB2LkkQrf6/g3FvhGhl+yJAK+roZ/PEbejfoc84MGKq3e5QOPAvNMcu8BNwVQVU2han3JvrEugAzdKQbYHGQniN4paL4tON39hjQEKThdf6/AdwdV7qQ0CCqoaO0EONz3PNe2nCtAVU1J8zQ1iD5vMmYfRk74J60gIB3YG8iHAIgI2BjY7m46OQdqgnzxqzz9Pjya+hqAwm0dgBZ0hd4bpIO4n3xfg2QDzck0Bljhw10UlHrAxgDiu4Xr0CoeYKZG8gnQevriR/s/b32P0zuSCTyQablWAyzZT1TpereHX99RPj0FoKZTZt0n/dnZT02hH4vDP75kd4Tv7AwSNpnq6g+mgUCipPU91Ca+qQFnpN4zfEAc3Evo26MKPsrsO5bP/6N3/vivtdf3unb+s98+Q2HTFPVnGH7Uom+l6A1kOyhHTlR49bMsfbpn0qdHJv1J1MMyn6F/Dc6fRDyj+DO0eJu/zadbUuR4U5g+X0D71SfG/LSc7n7JVO+7W8HyeQrIa7L2AOrge634NgQUjKDygmnwo3bUU8npQZW7kyUw/Jfs3fXPtABcnAVToavzH9L1XjSBIx9+eud0cCtrwNru1EgF3rSvSCb4tffyOWuT5PUls1Lvb/YTE1eDgAQGmHYeIDVAL9JE3v3Kat1ossL0+c9bo/39g5VM2ZNPdW8i5ndqvCN2KwBnSrcgmuj5FVBhFgDam5Top5Sbirt950ZQKt0JdTMUE8zHfmPqfd4bo/+J4J61gG7c/POUvK/Q1MS+Qu/96Cv0bYdw32dlLdgi/TL1wpPOYCh4ex/7vvOzvZdf/wLGszX+exBPRnlwuGVPdWZS8S90AtIqr2xBYXMnPN8V/L5u/ljsjzvO5rG5+/3lG2k8vfRs5MBwkJ2f6qm0wSB4wYLg+hFm4N7/psV7TgG8BvoNMAdDlp5L2Rji+SROLhxAlLg7d3DStuY+hlE4MceXy7lDYNaS8OZzAkNchyAde+nP57Y7QXjE59epZEcTDG/ueyi1QBwXxREMW1ILArEoF8y3LHdOksSc8F1A/d+nXgEtPnV76DIZ7r3bvMfmQ8XfX2x8CUZyy5qnH68VTGkWoRO2GtpUhXsm5uMHVCvOaayyudUbrtZnW5yR6bElVG8joqsNdi2tdE8PXCPOF2vlEM5ylbrGKDp2zDrZD/N2FilMmsTXUUaJ1gNKLM/Mjsu3g95sGsHStOR2tmCjbgbeWehmHYow3A2Sx2aVJGmrVdJqriYBFCVLOY3YkH2typbBF7JozJqSR7B5o4paqatpPFe1Mh7ZbhQUVetL76JbKTVsc4oTcMrPLjiloAVFSQ7hdTEM8+qp0+b5VSipsxEkF21oTtfqyIpnfTFPzGtdrG5jG1z8su3bFR5kF6k6W3a8KUrKoWtjnyjytSBwbPAziSVKQzjXWuKFHiszDpuUzEHeWlhWhTavLRjDKKuTha34cVA1RMNNKm6WiFfiV8PlOlVPW+1IjOpuQ0XH5LTLog2G6g5+PtTJpohT7cYI85BHHB0b1DNG6lZypXRdOYjHpe7zbMLQPeH3W21EFvVq5q+ueqElaIRsCj4RrWaDB9i81MTw5FfIIRniEuUT69Jam8WOg3dBrVq97Rclp9eGk60sXRLFxQX0pTDqnwkl6cv2etP3pqrxlz46ldZ4xWlzNi7kBT6TTEB5a/pmGI7US0N26TsDNQmTZwuqNnjqspPqjOOUur6O3ArpkrUmFo5O4tVp7xpaOe70LqkP7k02jqaohEoUZFTNXlLhTO63WViMrLeDHWMVXlaYt+wDmSC4zVLlRRfP4jYWE8U87XwE46zoomuaYSLG0SJ39obo61ONLSMOPYaEfNRGU60urVAWESzs9XPqF+TgH64zE/GjGmaEGa12XbMV8nyc+8gaw71TssYUhTSEeVUVwTKNxgSkhIRQm47ZIKKhqYiejoIgSRcr1Zt1HKVy1B8EpCOZkrvWMmc7DDUDe8/0SGqrZmYZiX7cqweYveEb2aFk4XjzMFXfn2JjI6lbhGboRVSKKVfKPMe3xEa9qsj2yGp0kfJRmJzPNzM7Xut1TjizxdCyLr7vUDFM18cbqeAKosxUEoZNAt56ObJQlnanpK1XNNdzKi82MXnjzrbk5NjYd0QOb+fexUzGxXzZwlKGXGDh4ujtAHPlfmO16TKyCNGqmMCPDNbRl6u0UdlAqLcwRfdwlbeiH5UUTaqmEFKlYZX5LtxiYxKyJ1TbF1ZxjP1b4SdkVNlj79IKitfqdiSwJVemw3Y3o05BpktzBOOtBvcWpatQx+N1lZbNVpI2Z52ar4oGLTyxsbfqUMJCkwFSDsSZuj3T1D7BSEZL5vFR1yKn7Q57mBLhyDC7KvcjlEFRM6yHFs6Rs5qXhnrIkiZsj9KSN4yVwHsrql5r1/OQ4SexqvEbnZ5WNk+0ppCXIAt3uLnjm5tkanNtFknBLOeGKgqdVXVYRK3fDYvcdT3YmV3jUwlvg93OAoRQkBxy2meFtkhdbqXOVl2HZ7cTchy9a0ZQ6TpCu7OvzEw1kedVrfnDWvApVQWRnp09i2HGEW7zox26Pu7nURAEjB47FW0fyxO7yap9KpkyvS4GLyoceMWMK+xSmslaiZHR7w6D2Zy87krF+c2zrQtvebRI28JaLdQq2XBwv+1lCTFvTiyyp3RXCOqaiy3h0tQ6Ul00tQebsYBo53webdb84igAtq0PVCbM2BLFePGyDbxLXgSRpCJ5sYyN7qZfBZ4z9o60ZwrcZUF5zrUbkjqpEYrNFYc9Q8apzo6qzcYoEa7CstnpGPOlpzdDTeFqvfKUYR8W9UiQw0GMiaxlUNOkh2KdkZ5T+j6RJAS769ARRGZWb0itWyU5iV0QlLWczYYOZwUrsnI5o4ll0Z9XpL4v09GK9x5hCqnQbLbp8ijljLEoI1fpsID0Thg2K256tW/FIGxV5oTcmHMhkzC/tVYOjQRXpjrLN7o75jJtsYcApU04uu6K3bafeVToHnIuCVBbxbG6aNqFt3IO8xTbjPpSKYiFt3RhXZ+LVSG2nX1IdDIsVQtGMmlA8YrT+hBGjqlzwY0ePYW0WN+wUboxccoMo6h7aOSUTmIio9TC22t5zff90osPa0Q8FcJNRbiEG50GdrlluFHT7oRfucXuFt6OPttIreKybLxth0vUItQc7cxiKc9CkTngZNPV2+hargx+S0Sahzfy+Xo4LzG6Q0Kt1bfBnuYdWZiXRLzV6COeJPubPmqjf2hguw+CXasRXFbui+DI8Vy9voVcb400QZ4v17rGT8nF4+L1JRdMY39Qrm0ZV5p67W0n5jW2TwIhjgewmo8imC6Uu1jY5wcGDQVU3AuBYceG2F/PR0cdbtI1G6TWtiyG57mZ24jLsD4kIkXxOkreZn6izxfiWNLqar6vSm2lWk5MWvGRmd+y+iKt5zaRbTiQoTt8QRzzm4zvEomvcP6IIsJmuB23Letsr1yiJ+WakHZXNm/q3oI3qXaoVfVUGfmO5rT0LDF0RM2smMVIuZV8JBSO24ZmZ6mPXvymZmYov2hzjJWyOqcvzHqw29xec8q+sM02yvvtJa8OFEwuPQ/O7NziWeZgLDtzl3FL5IAK9fpy4zrrOqDputIWToqeb20RjuywT85eA7exMF+Zgzsw8ljYJy9Y9YJV0kwYkKlZLKIqERSGVFfF0abl7jh3VNXvxitWLJhY2lyPdX8UuKpMzPQyx+C9YkfXW8nVq0Jikea6p9nk4uSXVcKADkxjb2d0XuirIjpla/ksqUO1ZYgtaNrPUljm6qB33qKtTWGj9Wqs2MdwDpe79kgWsH5lpKNRbEQ8vDBHhwZxmI6mWOVXbiOHtnRQuUzIIj+sEV8p99s83puNftX0LFz5C8NiTUo4SsW4VaS0t63eHFVy5ZqloMOJWXaitTXP9slf4WdS9eqLmJ7pxSiQnuZ6WH+aWc1xlOnVjlwpa5TtWoMO9JpDGSFf2mffJ/114ox5UsuHHWiglY2nz280mZ7UoRVPIj9ntC5SpZzFpdNpq+jj2ZLEJsfhIGN4ZUNSZyFoufFW1Nqm9yL0uAn3WK75/HnGSXUaxqfIT5XFJs+xHbXJLwROXE/soTDozmgTe431A6XuLPhSRvBtE6+ds1Ac1fOBwMdooaxlER52o7aal2NjtIaIattCv8WykCwOiHxzVxxPWNhOI89KXa14L7gBFoxCid4iQhGouADv5RaRjyY9Cz1pFyyo5SGT+BW+y4JsPa5z2c2TE3MqNPc6mqYCl5gQL7DVuDxZQxaxC15qwpXab3aeYud8fW2aAh61jOdv/mId2yqxDvOUYYvV6Eu2OsqH8y41x/1lBpr3U3fSk73NGCNtafPFNsnP8jI8LTQCa51jC7rwq6XnlD+77Fj3QCqrc6YQmhaHbkKUweIcdiNfzI65sccPrXTGybNbUKZJsOIakRGwnR4uR6/iu2zJDqnNUkM3L6Ur6jBGsxtNEDz+zrJbxzLAPkMO1ld1zOZr0NvKboOKc9ZAImfHkjiulIo9FMxGCfr5bh83MbK8BZ6M5Ow4X7GrriIuCEHhsFX5JWkSeH7j1oTetDiSLpoRbWRx3ySkUmVrsLsrDWSAsx5b2PKYAgst0B6d7/S+4k3CT0nYpFxVx7uYd/o9k7u9sWLIqEYVY8N2sRsbdQYv2ACRDtTidr4Qi5xHcXcdYFGRulsX9GmJAhM+3bWqtV25N6sljW42UyuGyw94zy1O2eGw9nmYnZ1uJ5LSOFGbHxt6aYdEi5DEQkRunbjuUbqitAVil/64dMITklDwTE3gXtsOQVbOZrCmkLZr4OtlnpWhh+prp5aQlQBjaHGyz0GwXHU3a8MN8tA7PewoOwHuT+W0uJPVTY1VNH3dEM5OWEvrGT1sFND4sv2W5cloqawrfYEvDXvvXgVHjI97VJq7axVreTcSebezsZPRiY5jnvgSk/HTju9C2wa7gQ1ZSbQWK8StFjN/SW0FnFgJhRzL4+ghh6VNdJ04O3SbGzHILK5ZqxOXcgrquaS75Nci0ymXOYvMCSU0mzVnUergVrBswTZ3c3RrUwPORwJ5yZQSzxEjqcSBM6vxhiBSId+eCStrHVU/sr6ja4hjWyqazvDFEa2ClElGv0w9WbebLj511/OtP56XottSw2BGc5jFjvxhGSx157LOnfHQmTGGm0pLXJrjKlgvKl3AZ2sQ4/PzstNuCnemNYnpT+PAGcF5yV1Ei5F92Ry3gt0Xo7Lf9LNL3beOt6gsPgu5YreX9h1+8zvpiru7fi3PlVC2bpeQcLhBKWr1xHAp2EvQrIfvTwwd1Ny+HrjSkXCqb0vrhK2TVjKM3sxWB/QG02mX9gJR2/XZQbeGtyazThVGcalgnTA7E2dH3C+H/CQwHjIf1yh8UlxKXjR75NTigGlGfME7B6xlljW5PRhEv+TGMN+SknvKSG6rGmvLN4jdAZ7VsRag5maPmdK6yYXGQHqwmTIuNuYsF6hnGE3oXMKsMJQDSIBFK6AV4YAdmkzTRkbxG9x31pZu9rucy3f+yIMNT8RyDL5XEj5vcQw/ED6RJQixmeGH9TxuiGh32Ur4aPvtCWdTovJhdbAUIq1n7u1Iw7BocGNjhVjAAnre+KC+AGuahuzHI5rpTGm27WAES6dwGQkNzkiOESQH2oEj7QxdvTe9PUXRZybP10a8yngmHqafAlCnTvBZKrI1u+XnLr9wb5TOK5Y2k5WDzDC7YyL57AhjF9EJzaxYF5XsU82cz9ID6qR7SodvHIKqhHqVfZ7kz+04BGDL6HL9GiaGkEmFq72se2rdorwmy90WlS6U3MwoV7jdSHTDljVj6lcTNWdYtdhlNe+vQ7RjmxMamrCE7HqfpjOHP918i6kUeCfyZbdgOyE+r/eVbAhxsjSopjWkwpjn+/pikU2MrhzVZxYuyZm0AcOLkAt2GXUOuq4dU1AGLMy5wbKbCjVMXLc6Cu81A6V7ZueTYuTOrZOso6ADkIYzv7Cpa9EobXuZyzvR99dxz+GMyZEk5p+34hU3xE0gIDN0KSyvlw0eD7wvK1jUO1yrOosQEdRehCuTdZUQl0ghFhkDwKNp+uefX15fpqPf5wHuP3umOh2e/T87w3sct317WHM/OfUs9/N9rc//FMWvry+VEwEMj9PIOmmD50HefzuL/PQX5/rThOHxMHJ6cnRrvh1gN1Yw/UbmJcrctm6q4WudJ+39APT1xW7r6eF9Pf2+wwHvL3foaTEd6z7WAB8s537o+rXJv7pRXeS19zI9Wp8eh3huZDXfLoPncezrizsAo0dO/RXFsa9eVUyaPZ8TAIWQt/nb4uWP/wIiFJJ2bSQAAA== -->
