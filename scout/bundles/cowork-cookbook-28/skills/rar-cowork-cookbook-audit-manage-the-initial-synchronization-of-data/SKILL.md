---
name: "rar-cowork-cookbook-audit-manage-the-initial-synchronization-of-data"
description: "Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_the_initial_synchronization_of_data", "rar_sha256": "7c0aaffbc088825cc683ef111fce3f6cb26c8ea3c6ac8f6ab3f060d700b32bc3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_the_initial_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_the_initial_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the initial synchronization of data Completeness Audit — Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 7c0aaffbc088825c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 audit_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 audit_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Completeness Audit — Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_the_initial_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the initial synchronization of data Completeness Audit',
    "description": 'Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14a85acfb27fdc76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditManageTheInitialSynchronizationOfData(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageTheInitialSynchronizationOfData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V697PiyJbmv8Lc+aG7h6or7+rFi1hhZRACGZDo21EtkzIghwwyvf2/bwq4t6rf6zczPbsRSxkQyjz5Hfedkyl+e3GaOsrLly8vOnCyydpJkjgC5cTJ/Mk8b/PyAt/yiwv/Tbw8q8vYbeq8rF4+vfig8sq4qOM8g9P5xo/rapI6mROCSR2BSZzFdewkk6rPvKjMs3hwxrGTPJj4Tu1MSuDlpV9NgryEotMiATXIQFXd1y7yJPb6x/exk3lg4oROnFX1pGwS8Nl1KuBPvAh4l+oVYgGdMwqoXr78/Munlxh+fvny24uXOFX1jk25IzMiID5w6X+EpQYLCAqKSpwshHOKHtolg9cFKCHCFH7lg2DyvPqxAknwafIf/3FpnTKsfvrylk2er7eX8Y/WZHcj1LlT1SNUp3DcOInr/nXCJ63TV1D/uikzqO6kgmbNwtfHzG+S8mLy9/Hej49FXkNQ//j2kkMId8RvLz9NoOneXspm/Pw6Sil+/Ok1yVtQ/vjTNzlV456BV4/CIOrXr8/rp1g48NvQOLiv+nco9eFeF7y9fKfc+HrgHvWEM19ez3mc/fgQXJT5DWSjt3786V+Jvfssiav6vyX354fgCDg+1OkJ/KdPdyP/Mpk+FfqQ+a+XLaBb/4omcPj7cp8mT0P9K9l3+/+D6CSGofxh8T8V92cTpn+f/PwvdfvPJnyaBG8vC5DENxgdbgK+TH77qu+W859/8L99+cMvv0PR/6UYPW9K7y7hK0znOABV/fXrzz9U969/+OXnH5oCxhpw0q9NmfyZzD+z632dP1jwOerHP86F65vZJctbSBTvkT75LS/+rfz9dXJwktj/9n31ZfJ9voyv6WRU4n3Rhwm+y5kKYv3Ojj+9/A7ZArJK2Xj32zDL//3fJ0rslXmVB/VE9/JmpJysjlMwgjeiuJrAv2NulwDatYqhYZ/jYPyPHn6S3K//y7sT6GfvSaCIM/LQ1wdFfoUSvj4p8us/UOTXPPg6UuSvrxPIVzDJ4zDOIJNq/G73Nk7O6hFDUYIKlDfILm5fg8+Qlz6PHyDxTn79q0t9vUt9Lfpf7/QbP9hLm4sjc1WQcl9H7Y8RyJ66erBagA54DVwwyT2ILoghAX+CVqny5DaWAAixusRJMvFjyPWwavR32dCaX0Zhv/76K6Tx6C17UC0xeZSTCoEDPuBMPn+GagZJHEb1Wwa8KJ/88NvvP0z+9+Q/m3UXPq6xgwXg6SuIUNLV7QTmXpPCYdCN0PGQWO6++u33p7GhmAzWP+jZOIjBYzKM3Qvw3y2vC/xnnKInLoAWh9ZOi7ysIX9P4vp1IgaTD7xw0fHWyPBRDiuXDwqQ+SCDda2OHKjOhyWzvJ5U0B9V0H+aNNWjfv7qlveKB1JIAk7960SZ72A9yRP43wjzPghOhr6E5v+Ii8f3UEj5QzWZvYt4nWzHaJ0UTukUUek81wich19gHXmfDoU7kwy0b9lYRsFoqnukPMwDB0HLeE+Xfh59PhZpGGh+9b72fYwzVj3jXv3Kt6x6poVTgnvdh1D6SdjE/lgs/vYMqSrKm8S/2w8iHSU9veA/vXKPQeW/32HMv+8q7k3A5K3BUYyc/H/sVkYd+PVaW655Y7mYLLeGZj9sO/ZXow8eLRlsFe6L3fPoW/vwTj7vHPyWJTEMlLL/22Pk3SPPMQ9ea0q4uMZrd/kQFbTtKPcerWP0leUY585b9k72n2AA3JkNqg9TG4b+GHHvC45335FGMH/H62+F/2mn0SowIidF40LLTAIAfNfxLhBVOWbc0wswdMFo4DaKvegPWk2gdBghUP4EghhdBQvC3XTbHKoJky0o8/Tb8HhspyAKv/EgWtjAgtfJESbNGDgVzFTYE41joBV+uIuapADaGEL8sHAVOcUDzNjzPgGObr/FoP3e/s9b34L8jmQED2U6Y6y8Ze0YTz7oHn79QPn0FBSajtFxn/RHZz81nXxfk/72lt0RfvA+zPZkLOffmWYCsyx9xOJIVhUknBQ8wwfGwb1yvz6K76O6f2D58k9t/o9/bSdwL6fmH/32ZRLVdVF9QZBHCXyvgK8wQxAYIXEBqkc1/PxIwc8Q5udnCn7+hxT8nAefH2b9bp2H2b5M/hrWP4h4hviXCfaKvqLjrU3sgTGGny9omvnnmf2ZHO++ZRr45nO4fJ5CdKMrelh+P6rQ+xBYisIShOPgR1WqxmLWwvp5p2Go7lv2ERfPnIEsn4VjCa3y73L5Xo6hlx9O/KgW8FZWw7X9sbkLwbgJSkb4FXj5kjVJ8uklc1LwVzc/Y3mAYQwtM+6fYELBxqmOwf0KaghvxM74+Y97P/X+wUke4V7VELJT3knjmT5PNvw0ds0ZJJxxhzLWwEe9gPsqp0nqUYW6L0bMjw3R2Jx9dG7/vOo9v+Eafv5lTPNPk7HL/jT5aJg/Td63MPcdYtbAPdzPY7M+6gmHwrePsR/bWRe8/PInMJ69+78AEY8UM5LSQ13gf+OPuwsLp4Y0aWobCCn37t3HWHGr/l6Z/1ltuGAJrg0ssf4I+ZsNvkHLH3h+v6tSPzaov728M9DTec9mFA6Hqf65GossAoMdLgivH2EJ7/1ft6lPeZBBYVsEBTIe6jhB4Hooy7I45Xk0S4AAw7DAA0RAey5OeyxwCI92PDagHZcIUBr1GRR1Cdz1CCjvEexfx84iHjHiDhzqMRjpc4xDQzFwqAcwHPMZAqAURwQsC0horo+pF0jAT8Ufio5W/eiYRwM99f/txaVJOFIgK5F/vOYId3Bca+d2kTAdEq7TDG6vX7K9B2R0jwFfFq86iE+4Um5c4+Im4jII5RW55KvQt6VMc2Qbyctpe6ONHVMT0dndG9IUQ+lsFc/ds4tzjXWiOF/Jr3FvbU/9rEroK6o39RxLyrSd9hs/LTf7HVs4CWnm2142am1vUQ4jHxxUPjko6Q6SHxMIR1JII/U1vsOme/OYFEpc4YW2Kiw6rJRkfWhMhmDK9Kg51+VNWtPVxmwNh0kdPDlItVzrKVfvpNQLkCzBwNGiaLbZdcDaYJQfaM3mgPHhZl+LpXio6BQr/A2R5dNrXcfyITkMZSYx0ZaT8euxq5Ntt/VKFEebPmhy082cpp3xjVOvScUoSfqGbzpzeTmtrrfyuOhL0Q/t0poLc72Ptmx5VHph5eBmZRnoDcVuVVndcFXIXW7byQ1tBTKmTg/hIcDrVNwsNjMWt7c5GW/NOnGKMtjPNbGvM0pb5bkCmOBAW6dWaAXpdJn2M20frqgDMTMHPK8MLo6aTgHH5kj27jq3hqp3VllSJ4f5MK2Lw4XzZLn2yo2KXRc0yp0u27DAF45biw52xC6UYRZDT1+1HONK3weEauBI6KrbUlgqV5Sn91R8QaWzZwbahc6JwaYb32/RJROHR6Ag+yagpmEsrzL+eIYJYWBhF821ZmAQaMJGOA4RHR9SN+NjxOoc9IATchZsDJ7BD2czPLrzYK0HeHs46qI7lUXrZKVMlyExJR/1KAh1DY/sc39UE2rOnA8k4R+zSj4a0xOIi8I/H/3j0YpRS15jKrJB7WYz43dNIuGinrlUzJyoetYxxbbeXa44cNNThR6Ybog3G89iHP9qkcqWkg1aEdjjjlXtMtNz+YCwwqlM7QBxa2StstmqL4ZaIZu6mynWZmZdB6K9ntYH5uBH86N021w6OreP0rRt1zCXtcUBkNii7676dlawLn2wjzAuVFI+gb6WsH6TqT4yo8yTjlVCdMAWIY12M4KnuDW/4aRLrl0MTeqkhsx8MRP5hMKV5Cr3SnxNS4Wecy2ZlhkR+W1xk7ApfWvRBUn1wyX1vE7OM+GcSfNdJqlmKgJfuZmz26HYUCnfulkaOIcy86SpwFutdSwPi8RV2R0yQ+Y+txA73SxYgtbWgWux1SnmENNEt8tQuznSJlDXvsSonWD4xyVxlcw5sdohuoL05BUvad0oDVL0q4isXXK50hM0OXkHQ59j6F67RgpH0IhiyOKAuO35QtVsvcyMTkquTSY71CFGTKzgMv1GFNSR7lhHP81tbFV2hLZcguv2sKpJlzPV89mVJTlhDObg1EifQzLq9MOspoUMk033yp8s62rGQa8TbHlLLxs97qcsZ6a9offFjVRpe4Mqp+PMq7YyvSDYZKvseqCvGJ3f4IaTn6/uxju1bcZsM/FQXgkl8bZDuZsL/EDItBrYUudeJCoh+Ga+LdkO2VpFsh6YAnMzPKK3GpoQgdZaZmyZoPWOfmpnM2fKEwGTkhK3LCpiyxi3wBPI62YeYM3asm+IRhKFzeLLnUNEmpFGTQbQ+TniqIzU9rtAM6OLqGLUtizwJcau/K0YyHLJrXXhYuw62yKZVTPbD+cDOmzOqVBOmZWl7Oa1CXB7yTIbkUPrpchFduzueXZYMqftfNdKW17AYqWcYTwpiWYpnsOlLONlkNdLgq+kiNdQCVKFRKzT1mHL64BrEvCWpLZYXMJurqJx31mzdH2+zVNfBSzNhqdZOpg0Gm5s94z3m5hcG6tpw1pzWE7y5gYZ2rtlEaXr0qxDr6XnB9yG2spKWlJFPMiEvV6K6GqdYPSSCwRi1ZxxVNhVy0VLgjN9DIgwRmGQsoAljkHJGEQfTpeYFrNHlkWJrbgXqjBCi94RtisoLo5mpguZyw0keoehoE3Rxjx1i3Zu7WPYM+QsCIYZEjEoQO06MKlVZ5lG061OkskiIo9aW56T2hBPTF4OHUn2bo5xTUifP4RWEQwmPzve3IN54uipry6NS0tQwiWl7YQzvPkxOi176+ZtLgRnMXGp5jKG1XoCeuImH3P8yu3wgq9FE/YEhOoxZYsY+kpmb34iN/tUkS4O4y6oU21SHrVs/bPFYTuJkartglhK/aVfr5PTUDrbzW1bEYth1y2itcPt8gjpLycZPXcz44CdlSrWoittrPxMQOVDsbIXO7la5352sgfM3JjLU2ueVyuutEFBxlJEuFNnpZ0uHK+EihcZV8qteTHM98fZ7HTcHIhVt2UZPopbyfLW1wJPZ+IyhH0jvkRWJbuyOkPV+/A4ZXdrbRnr0pHWuiWXmlufOsVL+6zty07hDzttEAB/S1UOp2xK0NdaN5x5HZfw/aanaXxh6RcY6b6r51s2OiMVozDNAslsYCx3MXpFb6SDc6kQchijQ+/v55s0wnw910Xrahtze980OrfYOIBEfDvm5sz1rGNTsQWZrxqxKbEH90CeryR6mEburQ9nzSlY52IS6R6pEfYpiTFwwvN4SVtAh63PwZ3yYSVKp3g6zYhDSe/ROj7myybckVSwvRyjUm2OFKZYu4UJOVIGa8KlRYY+4L6OY/uw8wqKXnPILkMSrcWVDZacV8rep90Vp5JluN4ZdoWR55tPnWkaECfXCYiesGMyM3rr7AqZ4fAFituhXjGmSVw6fomt+Fl7cRf8mvFKS9y2OcOJrth3hmt2WazfdkPK5qJzlS9oLvKzKzYgBptd1xt2sdCNMKuiTEtNDDvoFvSnQNZZVuaitS/R2Wy7MKONaulph/JBUVyXILLNXd1cSqcxlurGC5syQ2eUc+x7I5EcpgX67mIDW0zDfh4WaTaXEq9oI6SwlTV+Pal+tYcVtgZ7UM/VLlTXasbhrG3vw+VtqnryDo8O7dLfNw4/BOTZzRXYaE9xHWmnCet7x7MgxL3tQJ6Ld6IIhiWt1dtIoirYEE3ZZm/IeX4tUPpQiWYFNFLpUsUplLQPUDZEjNZO+J6aizAHiBlhHQc07S4qF9vKNlOJ4uSqihVcjAO1uRVkKXB9e9n6ijmc94lplcYgSjW68EyH4qqTtmay4dAqFzKzy55b1426tppluJvKg1SA+SKNUH1qnFrpZi7XYhXcGhUXQi8t+rUnycw2rZMEWTBAO0jU3jkVO9iGpITaZwbXn8017sUu5wXG8QzWGJ7wnSgxjbAlvO6g1csZ3gpuKaTN5YaTHaPR0S2ncXrXl1w1H2R9g9W0796CGT5luMKvw1K5CrBeT7UCx5ErBXdXi7gvuzCcixa2hy1x5G9ivLre0K2034pYSFI7KUHwinDizUnnz8fV0C15FbuIZ3IhR+Y0pV1lv1vT5im9cnvTWJKlzMf7yIhUEfUP8kk+e7xJrGA+dmnb2CI+S8KNU8uJDE4Oe9sgkpYqx8vNtEC+5zGhshema/GFvapOdHShLgG/saVejofqYvADLRWwTpx1GHizGGvEBU5vvf30VBK7GBtmlXBcUzglVm5QdSh92eRheBWIeHbgO6fiUMUU1TNf4Rg1Y4+V0m37uQDk7ugB4TDbUjuQtAbrDPtwo1XKFrsynrvwsOvVjpltWNGHTBu2YUJXPXVtTl3tCQmduJiKnrx101+3aNhh+MqLtD1s+eZeqR7FmFdWWV+ItsGa86FcpC0VVfnSNRcIdi77lq7F6/6oXprVRTTt1VlphrydtemRadbngtt7FjiksPNyL/FqIyApUN2N6BEsuClUX3HSgdE4yaZjeg5VdeT9/GId0L1FNjN0f1aL6yCrbI4dkcPUgi0BQ7Pd0TdqZs03pCDMl8rMr8+namfl2AoEyIzcWT21blhvUOv1mrjdultlx7M134XkegMwRq5FlOyHE+MLFfSszfMy7mdqyp+GwCCqDCGDaHfiha5H7dyHe3m1y8twScrzxuLWwuoshyxSc0cZblFLlK2sUIiI6zQWDutcRgUBCy6YBDIx3nNCpu6EsEt3/KpanB01rBE1iqf7dY9CqkTX10bmfe2WFd3CUxGkzHYIbxmLhWA0NYK4CIm3ypoZjGBRDyB30mFn82GS4SVX60RmatMNiOJCbGTYRIu+LbBLtCjWOebMxcA/IVpE2hdDSHfU3NTBJWvO9GKfBpidFeS27vkANEbXQmYR7LYk/LNEq8s5W55E3hHYW0kkO3V/Qs2q58SjiaNwObNuB9dlgRggV9HYX/HTNGbd1JXXQyyWM3rPu22dg+k+Yy7scNqQlDlTDNLA6PqMZZ6g7voePebUNvJqdaiM0mbVjRlkNC1pCEYgzfq2hO1WuNdBu1jq2s46U3tiT9ewNyUGxdh7yN5BgZL4qrDC9+VQDUeMYzZXVD03mTWbHRhQCJ5fExIpEIHMEDNlJaxvndtYqFmyRtLdxFhoPH2LL88H26q0K1u4NUHq61Uoq+V6RU3j5ZFDdeV2aLci7HqTiBJp8bKbAXcXLtzOBsj8sDznlwHLYtf3qY4nz5hOG8F+i2rejW6G2+BshXOHCB7oprkq97P04m7BDT2KZR5v5rDfYusWyNriWnfXzWKK2HuYw5ni3AaanoZscVhKwXSRggYHDM2s9LrPiIoqNqzl9WmM0aGfTClB422llz2p1JcLVhrSsiXm/mKN9TsuJBhDAfuih7ZXVrdyN2s4Vas8W0V2sJhsYDODYaiFDiHqXXvuEBJdPoO+Obu6D7q6q6E+3Z7ySJSwo85ZHmGvRfFnIOQgWuSMV51tjeTlzTV28XIfITv/rC1niYh03PSsG0keFTQwMjQ295jC5SwX7mbQK1x7FqKFQ5h+0+zOs7pZWYLk1vWNzqwp4q0YehCXbkeeyMCNsFKol4IetLNlhfhRzUJDO86u4tNFY08FSzzXdKDouT89E0xSY0Jcuf2NNFygcyy7tOTtbb5V9oYRysZRY/yFGrRI4qz2vng5bTBuMC9GjbIWt0BRvpXNiLOCIQxJda6LWEy2HeGqFJ3ViDZV8FMEnEVwOUnGUdybB0fYyQsh19BgLyB70xbJgnRgP4TO032JbYvFxlwjDG7ehMw+rN0rto7mZtuUrLW7TP12RqpZRx4wzllmlERkiwu/KqM52JT7VXE+R93qMD0ltEJfTugphe1vxndsgStqoulHLoE5c2NDWq3Iy5RBnUoIFgRFk3zCmYzkhrdIJwRcNXTfzelokx2anhDZrMHZsFa7ZmYTM2e5SYllfGv6aY7O8uBaDoJ13LnBZglctCeFjN8SsbO1TnO0ULY8Zsy356LBhHaFYfoKzeLMOwXCIqHOlLBztK5vBmIY1tYJuj0om70gkdWV5/m/v3x6GQ9gnyfh/+Nn4uOp4v+zw83HOeT787L7kTRw/C/3tb78zyH+8uml9GII8HHAWyVN+Dz+/Ifj3c9/9bnLKK1/PIYeH/t19fsDhtoJxx9cvcSZ31R12X+t8qS5Hzh/enGbavzBRzX+JsiD7y93pdNiPGm/Axjf/RQuPT4g/lrnXx+n3OBl/EHG+DQL+PG3y/B5AP7pxe+hN2Ov+krQ1FdQFqPizyc54znx+Cjn5ff/A79zYaHXJgAA -->
