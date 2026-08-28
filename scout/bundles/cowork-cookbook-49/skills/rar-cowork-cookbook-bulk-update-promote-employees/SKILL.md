---
name: "rar-cowork-cookbook-bulk-update-promote-employees"
description: "Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_promote_employees", "rar_sha256": "622df14da43090766996c376d663a372025bff86efc67be6a5ce0aa71d813191", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_promote_employees`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_promote_employees_agent.py` and in the RCI capsule.

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

Promote employees Bulk Field Update — Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_promote_employees_agent.py` and embedded as the fenced Python below (sha256 622df14da4309076…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_promote_employees_agent.py` first:

```bash
python3 bulk_update_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_promote_employees_agent.py   # or on stdin
python3 bulk_update_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Bulk Field Update — Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_promote_employees',
    "version": '2.0.1',
    "display_name": 'Promote employees Bulk Field Update',
    "description": 'Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '328b39f8330ede27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePromoteEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePromoteEmployees'
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
    print(BulkUpdatePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6Z5PjRpbtX8HWfmhpWV2EIWF6QhEPIAEagAYehFrRgjeE96Ce/vtLkKxqaTUzOxOxEY9tigAyb157zs1E/fZitU2YVy9fXmTPyqCNlSRR6FWQlbnQKu/z6gp+5Fcb/IOcPGuqyG6bvKpfXl9cr3aqqGiiPAPT6aJIIq+GLMhukyvkR17iQm3hWo0HWU6V1zVUVHmag0svLZJ89MDgynPyyq0hHzwBS0JRVrQNlER18wr1URNCbjV+rtoMTPW6yOsh2/PzygOapGnUvAElvMEC0rz65cvPv7y+ROD7y5ffXpzEqsGtFwaoot51OD/WZt+XBlMTKwvAmGIEDsjAdeFVQHgKbrmeDz2vfqi9xH+F/uu/rr1VBfWPX75m0PPz9WX6IwHtmtCDmtyqG8+FHKuw7CiJmvENopPeGicrm7bKJtfUwH9Z8PaY+V1SXkA/Tc9+eCzyFnjND19fcqCCNXn368uPUF6B9YAnwPe3SUrxw49vSd571Q8/fpdTt3bsOc0kDGj99u15/RQLBn4fGvn3VX8CUh9xtL2vL38wbvo89J7sBDNf3uI8yn54CAaR7LzMyhzvhx//kVgn9JzrFMp/Se7PD8GhZ7nApqfiP77enfwLNHsa9CHzHy9bgLD+O5aA4e/LvUJPR/0j2Xf//zfRSZSBRH73+N8V9/cmzH6Cfv6Htv2zCa+Q//Vl7SVRB7LDTrwv0G/f5DO7+vmT+/3mp19+B6L/RzFy3lbOXcK31Moi36ubb99+/lTfb3/65edPbQFyzbPSb22V/D2Zf8+v93X+5MHnqB/+PBesr2bXLO8z6CPTod/y4j+q398gzUoi9/v9+gv0x3qZPjNoMuJ90YcL/lAzNdD1D3788eV3gA4ZsKZ17o9Blf/nf0KHaEKm3G8g2ckB8oAAN1HqTcorYVRD4O9U2wB8vKqOgGOf40D+TxGeNM596Nf/49yR8rPzRMr5BIHfHuD37Yl63z5Q79c3SAFC8yoKosxKIIk+n79mVuBlzbQggLraqzoAJfbYeJ8BCH2evgBshH79p3K/3UW8FeOvd/SOHrgkrXYTJtVt4r1Ndumhlz2tcADieoPntEB6kjtAFT8CUPoK7K3zpAOYNvmgvkZJArkRwGoA/ONdNvDTl0nYr7/+alt1+DV7gCgGPRihnoMBH+pAnz8Dm/wkCsLma+Y5YQ59+u33T9D/hf7ZrLvwaY0zgPJnFICGe/l0hEBVtSkYBgIEQgog4x6F335/ehaIyQCFgZhF/kRJ02SQlVfPfXezvKU/o0v8nU4AbeRVA5AZAqQC7XzoQ1+w6PRowu4wrxvI9Qovc73MGYFUC5jz4cksb6AapF7tj69QW3v3VX+1K+uuYgrK22p+hQ6rM2CKPAH/TWreB4HJeRYB938kweM+EFJ9qiHmXcQbdJzyECqsyirCynqu4VuPuACGeJ8OhFtQ5vVfs4kQvclV96J4uAcMAp5xniH9PMX8TqggsPX72vcx1sRnyp3Xqq9Z/Ux4q/LuvA1UGaGgjdyJBv72TKk6zFvA+5P/gKaTpGcU3GdU7jl4/ksjMBE1xN17hgdfQ19bFEYW0P+PtmJSkd5sJHZDK+waYo+KdHm4buqAJhc/mibA8RCY9yiT77z/jhrv4Pk1SyKQB9X4t8fIu8OfYx6A1FbAPxIt3eWDaAPXTXLvyTglV1XdXfA1e0fpV+CPOySBeIDKBZk9JdT7gtPTd01DUJ7T9XfGfnpnqmOQcFDR2glIBt/zXNtyrkCraiqop/tBZnpTcfVh5IR/sgoC0kECAPkQUCICJQKQ/O66Yw7MBLV09/7H8GgKC9DCbR2gLWgxvTdIBzUx5UUNAgCamWkM8MKnuygo9YCPgYofHq5Dq3goM3WlTwWtKRZ5OqXDHyLwfPg9i++6TOoDqRZIHuDLfoJU1xsekf3Q8xkroGw61d190p/D/bQV+iOd/O1rdtfxA8VBOScTE//BORAoo7S+4+eERjVAlNR7JhDIhDvpvj1480HMH7p8+Usr/sO/163fmVD9c+S+QGHTFPWX+fzBXu/k9QaqYA5yJCq8+k5knx/l9vlZZ58/6uxPQh8++gL9e4r9ScQzo79AyBv8Bk+PhMjxppR9foAfVp+Zy+fF9PRrJnnfA/zMgglGkxEw5wenvA8BxBJUXjANfnBMPVFTD9jwDqogBF+zjyR4lgjA7CyYCLHO/1C6d3IFIX1E7AP7waOsAWu7UxMWeNPmJJnUr72XL1mbJK8vmZV6/9OmZAJ3kKPAE9M+BrgcNDRN5N2vPpqb6eLPu697JQEIcPMvU0G9QlMj+gp99JSv0HuXf980ZS3Y5vw89bPTkmAo+PEx9mNrZ3svYE/VjMWk9WPrMrVRz/b2r0pMdQQ0dryJsPOPwpxW/IsQ8CUIvOqvQk73L1byRIe6sSb6jZr3mq6Bni5oZl4hEDdQa6B8ACq2YMJflwHrVF7ZAp5zJ3O/+++7WfnDlt/vbmge+7/fXt5R4hmDZ68HhoNy/FxPTDcHOQoWBNePbALP/r0u8DkZgBpoRMBsHEVdH1m41gKDKZjAcYrCHYzAXRzHLIxAYXRp+z6Je76DE7aHW0vHgy2LQFwSwRAKAfIeCfntwWJApAf7HkYhqONiOLpcLiiEQC0KrEBYlguTJAETvgtw//vUK0DEp5UPqyYXfjSkkzeexv72YuMLMHK7qHf047OaU5qFY4J9DO1Zhft0HVPXhiivo4bjI4hR3DbXA3W6bmTfVWpfc1hWviaMwrCtqFWid5uL4SyXqGuHnWgj0hal7aJuUgwlktBxsDjt/c6nXZWl5RhZGGaa7PaNgyg14vNR6WpehHqWqaaLtiavUkzMHM8fuNQDAmL1KsJdKwxjjgnteq1H3UBrPBepo6RXazoyVyacJF4iC2qzR/lsXCC7qEPhcr2rNcW1CFW+aqUp7mLbruRlllNbk5x5BkfOz1iyJHfy0utsjHRB0dhpsOARTV8lqbZBzrkTzXq5EG1bVWtnyIpkT4TVwCslNeqhKdiqVcZiaBMDSkRy6ZVZvttr2qCHasUuXVCSSwdXe10IJSKSxIyRnG22RZEEdHZ8HK25WC7rY5HsFGM8IpZWNOVZ0uvZsWE6fNNbuGpmh0urNvSyvu5uY5cnyvZSaipbZ4tNXDBivU9v8JiGXLrHVHubUsslsxINb7lr8h3dknpr9LrcrQ+4UZnYMSVBMHdb6jqWmyxstHKfLczoKNBeY6drGDkty/ViQZnXY1Ci64t5vFjIZnklFHUYblaxr6u5qQYMXLGL2OqNeGFkUbJaNTt1EWmtlDN4k0VGlZ2PWb5cwuu97fSdcRQwApuFXNxgtH5DSSdGrmg7OlU9V2SNlW62fpXVEnTlh1hBRx5v0H3UkB27ui3bMmL0el+L9rwJ8jpcZ2FO4XY9IOF5zo5Sy7Fb/CQoSj0M/FYl4zC8LIOk5j2xtQ1fI5uBv9QO0V5u6NHbnBvkQCrEltmEDmpkCbdUEiRUMmSr7MsTfiiQJdcKRunq2oI/YjsFd89mQPWHyDglFzXzF769pWe+XzXUjrxsObRESswjzaruJF8ymmgBb5NiOddVlSeMUKuU5X5FXVB/ub1uDhd94IuQREBJFuwG1FhionRBwYdCPonAYXHOr2tyVPt0l/MEh+QR165FZxMIe2lztJabix1FduDCMrvaoKSoHbgVszMO5JhWB9LbB4urfZtJ+sVQyNY48835wnvjHs6CiNqTwoZFT3O0aUVmPbKcMmuy0beWZeaEhAGvybVplsm47KRoPsx3Ot5Fl3yEZ1tN0kqyW7pFRLnq5aTNGWzeiWklR9cFnF3CQeNiphK0KzakFC5d/b188610P59hp3AVWup+hRgRe8OkjaejciX7ojHrWAPxvIrfEoZW97A7nyenPMpGkmIrLhVIdDDxE6JlCn9G1nsx4/tkV53jyiwOVV/sl2LJkCW+YdaJi4m4aR0X2I6zD03U7lqPWVLKcIBjyzBqOFr36o2Uq2VjHZjznMzVSFmLY37uDX83qPx5t0I7XUjPfnWBF8l+dzGaXK1NFu9qRmu6lN/ikmSyHLVujnJxHRJtk7NswfZ8p/KD62QrT7QTw+cXu004bpy5zxW61WyOrV8GiomHHp3D5yVlmIdd5O5up2pX6nuqZ1IX4ZqMWqWIWenYpY0kxJ+R+cUPj8zWNFw6KDfoabwmN8E48bFhbcNrtpHKpU+K25WeVxlbnDaUdwvMfbneb4xqe15LDG0sZ36E284qxWh5GO3Q2mbLRYseRpVyAwHgDYzqROjtDgh9zXcHbiunqLxbzvPeVjkT48Yjn5yD5f5yiS/V7nw+5vqCd/CT3igOzYxXVjV25o5RaifDhs3GGS7GmmGDghUk8xrlRN7L3a0H4VJaT4ePIDDbrcAyFaFwld8QN3wNQFSRs5rE5/6Wm5FedWQuVwAFe32B3whstDRzr4yZkx2o63p1vUSRSM6rmX3uhMu6qtrz5RwNYrge8BmXwTg/q27DgvJKWqZ8ujsnazIvGUbXiGXVyiK9qpi4kGfwyTIVHo6co1wlF7zi+BV6YgEI8TyLBKwhli3n0WoUFVwzKSCCqiFWBynfoTV8kyvahQtx6/L5qQ4yl6aEXV8QZlTS+nbZrCUlnhnCDTDBhvXTnjuY7Fa2SnTPHcQYZInQF223Ig7Vcb6mj8lsOK6KWT90zbAd/A1xGcYMO6HNQc9kF3GSsEMvycw1SEDQwqq/VphuqdW2lbCts7uZcZVY0ZqtWZ8tBIrg+EzdlBvQhiitrmzmZlYxt2jLi/nRUo29tEP85ujHjsSMOzLW2RBNk0W2EBNzN7j0ATATexA6xNPNwR011xxm4Vbx1iv32gxRjKl5IUprumdZZEzq0wWWjB1+niOr4nKd7Q70pkV4tS4bJg38g3S4cbqgDVJPzk7X1V7rolW026S8S0fjaVjJwc5l1qQqgJ1LGd1cb3sV7PxAXE+B1vncUY8UMzKyk9EagUKjs1XkzTp/PVugy0htCmYnb27B3mCZ/VDZVO5J10hVDn1WDgcCNXF7FpSZ2awvx+hSY12do1S6bylOUDThUDLezcdPhbo/7sfjUB53W4WxBjR0ljIujiOLtVbKHzTFy6SNAl/43NQNwG54l8ghDxAu2MOGdNl4gawuJUIUuADr95s86ZMVSDoljDSjWAXL1cJcwOIWs26lNj9utM0BXuG464eX3blXqOLkrKWx1w5WTiMOFltSQBFi6ko62LYoIUEsByoBXUlwc1ZSjkXbVqb9Sr/BrITP1pkhA2KOzoVJ+SkqzjEHMyN8q5T+Cj17YcTYxWWgox1itehi8NiWo5kebKCOsc9p0TUL5nDIhsd4c6kcm5FBN4QMSofxOmMGlqJeEBdGlnKpHBeewMGhoPNH9SQhxh6mXRCE9ZXjXZzWMZD8bpVIvG0YhZrDwvJ2FhkpOCzsVjoOBRmh9gq/xIVEM6HulyxjEY5GA6YrvVROYnrjq/uTyUtEjIvrPEuVWe46jZAcYyMuhOO4IiOfh4v5QrytYTjjgN3UKg5vco4laR1ucbFPDgMzLMRuHYOelEU8awNobMXJPF8kfCmm13651W7XsB7iMSYSfuBsh6zja7wWyE1vEuLFcms5A82t1PZRjLqGGe/Klt/stZS6pUoprHa2b+uKb85PzFlfll0tOOEMdmZ0VZPWgOzNYSD5ozEThTy6XZFGPemw4ZcEoMfb1jq1CYwiynZ1ml8V2FBAL9uqlj27Bn5gmAo7cP31kpz4/pLQhwVBi5fdotNd9ZTQCqqG4QB6pp4VW45cbIgQMEne6W1OwBXjred57YEetFEB1LLLTYj5heAJRJ0dpCa+BYh7bmitWWhtKV5FCa/2LZ2J58OCucjrTbMfVUa4drfdcomc19uEO7jsaE5kL/NxWvkW2XNtLptarCq9YlIJg2/kFJAU7B2jQ2us9wlc40F/SE2uNwcKcHt+DUh30S0VDXfq1UyhnFSbp7JIlHUlnFVm8B0jLVl2pW4T+7RbFZtGPCxYRejCcTiQQ3weS3XWCTAT96ejwWCJu5+fV4Sih7tAvfXtwU7Ny428XDq1KLmuwwt3FsaCzfPCqZfP1/RU5PJ8xd6OaUoYHIeMp1KgbTmmZAfP5YssnONiqe3DKnHVYBCJNa3XWynPyWy3S3jS7LSci8J0dNJ0aHBb3s7kS9muy4T26RXF33hq5E/1XNVlIV/Rxp416LPcXQ5GhgbhLJQ177pbKII+XOCLFMAYFbMlXOFOELYLfKDmC+Mo1yQvNo29nDFXTpQxOvHdndrPK69oUYqZa/0Qu56EN0hxKzB+fl7MrfIozWYVUnmUnhB+omjRfo6FvaUZ1I1oy3i22PJEjRnXI5fZm7CtL3vJkOGz3Qr7YuBLE6Z0HzTC26tDm0686gvMNI622BkXyiGOWqt0Q3IAabbXtXWt5PFi0ZHHiKXYtcc6dVRWTUWeqFNnEXjA9BgrzAO/xLj6sI50hPI4Gk5nDQc7aBs30QWjwqRbJfrmHObKgeBncyvg+37uSTCSNz2HddRlDbueScxImJwvAp/lSY3H53PS8AeYbBICA1yPDwjOH7u9NfIIAtPLhgXYZc4EATTBFkLgi33eznNptgvAduiMbIpQC+liQBe5cj6cYXZ3ne87letP0XG+jLys0zV8qV3adQI6eh7lbzv0xEzAK2jSIefWmJ2SyxBLNttkf1Dc1ViOqw7fkli8Bxla0NSZb4mglbveX/uay3SXePCydNuf3MRFUG7OGfvZOB5zcedQYoZT6Vl3h3qxEQTGiVmYgxGCBPvZc1zC2xPa1XBF2XMsjuONcnIRMSPpkWUNdHFKsN7LRDddzgZ4ZA0D7bYKqzviCuV0N12gXbf0wDbTRUk00DysDG/bNSC2AcfG0b/sS5o+Y17FkZzsr/hWy1mxuQXSaZF5RyOXRoojkmrWAhTbndb8dumlRGoHybY1EjxPMndPn+KNc3K8/TrQrm3OIiQaX3ulFrrK7BMs8xxxRpNqxei93kUbjVCvs1nJ9KR3Lm5Hs12skQu3OxBYQ9UmyDqpl/bxsZcQBj7i9kU4Meu6CUthPcMucllSrRif46VGcqaydpQ5QzhH++JiCLov7OjYmVis5OUydbgRFTF+GRk8DfqeSy4ZGewv3KETeox2KR0ZUaTGiHBniMWopCTL+gR6rt0TU18up/mWiQ5ItFjVhO3OBvJKcPn5aHub62p5EdZ1sUHNtNddoSo7J20t6mp1NqxvcoegOOcsafJcBDLji7ZYq1tmb9zaQCPnTSSxTLKb3YgFdlLCPCxwLzbgSBWRE5VvHSO7ysRWX0jrPm6oSFXXGQ664xnqN2yNE4uozVx3rpre+iSszwA0T41I5ozTz088VxEZbqB+qA9aqREuTJFup7n9EUGPrX0uZus5IQiIfQg7fhY0zUIw0L1YBztP9S5BGtMqetQ82E87ZD8cQefKWqfQmuGysPA7eb4hcj2b2Re5iwA4+RwtwpaiuQO2reLsDBeYo6OkPpLwzegT2UY84XC+husZgJ6Ds4U3KzjZrPQ0RIZlgG/dVC6rykFa61bZiktYdp25CqmXIheWEjBymZ3V0esD8pRJpIqAHbmxZJBsndNcFa48IRa5ZRemEqfO1A2ZHsUD7iBiugFtE2otj16iyB6SCbB9dnqM03vJbwTdEeZHtFIWgNGTxZ7ommM0smhriK7QU6GdpXNGA902Ys76+ipuhXMVH1dJpIWDNd/NwQ5anS/lQmmqzI23dLZZLElmDDKpr3WsYSJzk54GeuV2VbqeD1xISeZmW2ak5hRKiy/TG9jG2ZlDnLes6RoFvp5Hc6lh9+OVpumffnp5fZnOnp8nyP/aa+DpWO9/7XTxcRD4/g7pfnjsWe6X+1pf/kV9fnl9qZwIaPM4O62TNngeNv63k9PP//S1wzR1fLxTnV5yDc37+XpjBdPvAb1EmdvWTTV+q/OkvR/cvgKX1dPvJdTfngfUL3dz0qK5P/tQH1yFUeV9a/JvldeAby/Trw1ML248N3o8ny6D5zny64s7gphETv0Nw5ffvKqYjHy+xwC2oW/wG/Dd/wM0c3t9ZiUAAA== -->
