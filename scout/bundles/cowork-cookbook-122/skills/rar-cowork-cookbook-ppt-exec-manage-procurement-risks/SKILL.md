---
name: "rar-cowork-cookbook-ppt-exec-manage-procurement-risks"
description: "Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_procurement_risks", "rar_sha256": "4e7dc5ac0c56c7f9da8dc255564c4c63d533779ae24cb31d7209cf6d324e8971", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_procurement_risks`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_procurement_risks_agent.py` and in the RCI capsule.

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

Manage procurement risks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 4e7dc5ac0c56c7f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_procurement_risks_agent.py` first:

```bash
python3 ppt_exec_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_procurement_risks_agent.py   # or on stdin
python3 ppt_exec_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_procurement_risks',
    "version": '2.0.0',
    "display_name": 'Manage procurement risks Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01670af81f1563c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageProcurementRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProcurementRisks'
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
    print(PptExecManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bOjxpLuv6I580Pbo+6D2EXfcMSTAIEQAgkQSHI72izFvolFgPz8v79C0jndHl/PvY6YiKdejoCqrMwvM7/MKs5vL3bbhEX18vlFB3Y+Eew0jUJQTezcm7BFV1QJ/FEkDvw3cYu8qSKnbYqqfvn44oHaraKyiYocThdADiq7ATWcOgE9cNsmuoJPFbC9YbIrOlDtiihvJh5wk0mRTzI7twMwKavCbSuQAfioiuqkntSN3bT1R7haVqagAZMuasKJG9pVU9/Vauw0ifLgU3mXlxdwzVeoDujtcUL98vnnXz6+RPD7y+ffXtzUruGtl13Z8FCp7X3V3bdFtXFNODu18wAOKweIRg6vS1D5RZXBWx7wJ8+rH2qQ+h8n//VfSWdXQf3j5y/55Pn58jL+0dp80oRg0hR23QBv4tql7URp1Ayvk0Xa2UM9qUDTVjm0BBpaQTNeHzO/SSrKyU/jsx8ei7wGoPnhy0tRjuhCqL+8/DgpKrhe1Y7fX0cp5Q8/vqYjxD/8+E1O3ToxcJtRGNT69evz+ikWDvw2NPLvq/4EpT6c6oAvL98ZN34eeo92wpkvrzEE/4eHYOjCK8jt3AU//PhXYt0Quj2N6ubfkvvzQ3AIYwfa9FT8x493kH+ZTJ8Gvcv862VL6Na/Ywkc/rbcx8kTqL+Sfcf/v4lOoxwmwBvi/1TcP5sw/Wny81/a9j9N+Djxv7xwIIWZVtlOCj5Pfvuq73j25w/et5sffvkdiv6XYvSirdy7hK8wNyMf1M3Xrz9/qO+3P/zy84e2hLEG7OxrW6X/TOY/w/W+zh8QfI764Y9z4fqHPMmLLp+8R/rkt6L8j+r314lpp5H37X79efJ9voyf6WQ04m3RBwTf5UwNdf0Oxx9ffocEkUNrWvf+GGb5f/7nZBu5VVEXfjPR3aKFdNTmTZSBUXkjjOoJ/DvmdgUgrnUEgX2Og/E/enjUuPAnv/4f906bn9wnbSJl2XwdCfHrg/K+fkd5X++U9+vrxICCiyoKotxOJ9pit/syDoX0BhctK1CD6grpxBka8AkS0afxyyTKJ7/+S9lf72Jey+HXO3dGD37S2PXITXWbgtfRPisE+dMa952+wSQtXKiOH0FW/Qjtrov0CrltxKJOojSdeFEFDS+q4S4b4vV5FPbrr786dh1+yR9kik8eZaJG4IB3dSafPkG7/DQKwuZLDtywmHz47fcPk/87+Z9m3YWPa+wgqz+9ATWUdFWZwOxqR7uho6BrIXXcvfHb7090oRhYoCbQd5EfgcdkGJ0J8N6g1sXFJ4ykJg6AEEN4s7KoGsjQk6h5naz9ybu+cNHx0cjhYVGPJa0EuQdyd4BSbWjOO5KwOE1qGIK1P3yctDW4r/qrU9l3FTOY5nbz62TL7mDFKFL436jmfRCcXOQRhP89EB73oZDqQz1Zvol4nShjPE5Ku7LLsLKfa/j2wy+wUrxNh8LtSQ66L/lYG+8hck+OBzzBWL4j9+nST6PPxwoMw8qr39YOniXemxj3+lZ9yetn4NvV6AoXFgK4aNBG3lgO/vEMqTos2tS74wc1HSU9veA9vXKPwe1fNQT8WzPxfRvBjW3ElxabocTk/2/rMeq+EASNFxYGz014xdBOD0zHfmkU/mixYBMwgYH1yJ9vjcEbrbyx65c8jWCAVMM/HiPvnniOeTAW1NmDHKHd5cMwgJiOcu9ROkZdVY3xbX/J32j8I3T8nbOg7TClYciPkfa24Pj0TdMQ5u14/a2k371aeaP1MBInZeukMEp8ADzHhmg24YjymyNgyIIx67owcsM/WDWB0mFkQPmjAyIIJ6T6O3RKAc2ESeZXRfZteDQ2SlALr3WhtrAhBa8TCybLGDA1zFDY7YxjIAof7qImGYAYQxXfEa5Du3woM/awTwXt0RdFBmPlew88H34L77suo/pQqu3ZDcSyG/nWA/3Ds+96Pn0Flc3GhLxP+qO7n7ZOvq83//iS33V8p3iY5+lYqr8DZwLzK3tE3UhTNaSaDDwDCEbCvSq/Pgrro3K/6/L5T437D3+vt7+XysMfPfd5EjZNWX9GkEd5e6turzBXEBgjUQnqsdJ9GvPv0yPDPn2XYZ/uGfYHwQ+cPk/+nnJ/EPGM6s8T9HX2OhsfyZELxrB9fiAW7Kfl6RMxPv2Sa+Cbk5+RMHJsOsDS+l5w3obAqhNUIBgHPwpQPdatDpbKO+NCN3zJ3wPhmSaQK/JgrJZ18V363isvdOvDa++FAT7KG7i2N3ZqARg3Memofg1ePudtmn58ye0M/Bubl5H8YahCMMYtD0QdNj5NBO5X703QePHHLds9oSATeMXnMa8+TsaGFbLfW+/5cfK2G7jvr/IWbod+HvvecUk4FP54H/u+H3TAC9x+NUM5Kv7Y4ozt1rMN/rMSYzqNcQLGgl685+e44p+EwC9BAKo/C1HvX+z0SRKQx0fGjpq31K6hnh5sdj5OoOtgysEsgiHawgl/XgauU4FLC+ugN5r7Db9vZhUPW36/w9A89om/vbyRxdMHz54QDodZ+akeKyECwxQuCK8fAQWf/f1u8SkA8htsVqAEAtCeS9ruzCUpl/YZz557LkaSJEW4hEvhHonjNM3YACNcB0c9Gpsxrk95OEaAOUOjUN4jLr+O9T4alcJs2527NEp4DG1TLsBnDu4CFIOTcTAjGdyfzwEB8XmfCqui97T0YdkI43vjOiLyNPi3F4ci4EiRqNeLx4dFGNOmMMJRemdaUX5g5MjauZjaLKON0JEAKlqus15k3PlWr4pDZWySs56tGSGhhJyLLid7sZvpfp1MexxImbNi/fJUrQqCNYaE6+Y7yb/6axBv1qVww+MlSmzM9FBVetavTmaQMmczIzFmZYVXUqsWRyotDzJp8DNW1Y6V6PsIpuw0YXWRAy27CmxkLFEryADtFPI2vQRsdWbQG6yHq13FHq5mUw8rfjyOCFBZobtB4po4bL1jnYY7fWivByW4iQWq5reBVEVmmLbVnDcaBGmrKCQjBguC9WY/SGR1PF/4iy2abRmVmYKyt1QykU0u0aFC7CTPThRGwVQXFgogmzTF2u2ZpdkVPxSHTl1t8XMPMnHlEhln0aLeq0MZAPaSZLrIu0RhzjYOC3Z1bEezXk5vqUmGjSkqXry3GaXvrrbon84nvGiXq00apIfUTL3dWssbXz5uzrV00DGSYxPszC6r/XZj7qPMbHtqzSgKfeu2yaX2Bt3hdDLUjprbYUd1Ne/NqrlUh6bEtgl6YqeYh7LxDC/CdT/FaY44U9RM6Eo3NxUX5+a1duSbYIPdDrZy8i0hnRGG6eQnQtCQ5mDOvA2qrrHaV86pEVS6oEpk3838Yy1etMjx1YRAp3ic7t3gaqi0P8NBs4uUo3o0WNqPo6GNxOQkHCvEuOX6LcKafXArmgvFb5s0OMTuZYN38728u9DlZmnfBIy/0rW5Sm41ddiBy/mQejIimKLcWTqxyLBEZv3UiNx9QF3JpZRd/H1/3lEVTdUk1ocGdU3rtLmsLub8uB6aLFqEZ2h/pd/U1JBa6iiVmJulF5dKKpRMi1tMqo1N8OJ8dfPi6XTFINwgu8NK00MkQGqXcxiy8MvjjSfakG1sGr9JXjrvyRNdNsomTZxdV+p8xQDTUnZJL5YQ6IManPrQ4atMvB1bZposdmxsLWI2NHVPpow4MYBbqzK8z7FK4UoB1Q1rc4OH/SIglNlFTyRG6hL6dDsFKg/SWTBnN2Q0XMAqVSujuMG8tNudwDqdKfTonO5nA3eeBw57TGLXI9dqQ64rzheOxQZfdzmZs905zzw9veW+ZAli3PmRVkrd6mrTiDgNVT1OFyU3mzrBnlNr5Yi19TXsuJVQ8N1Aa5sLUsbqVhIGpuK0m4WVhYcw25uvDFaf08P1Iu7k+KQX5Eanp8HS5I9RNLuxmiriCoB5Zbm0yuuZes2j7gyky7bqu6g9nK6kbRrQ2ZmnFAhXZeFOlQ6nDcD6k2PWR7BcZ6YqobLehjwqzIvzthGuwFzUy2O5CSKGu1FZIvVNq9llRCDrGEF5xI422r6fztNjouuGvsBvPL5mVXNjrhyjMm+Rr+2ZJo5W8VVeNOetwFzt8ticsq1on42S96ilt3LJhM7q8kxqmWCYRyk9lcwKrcM9nlkmC4Nx8MW5aVqyblyzXF/fzlQIzgWOk8ThILiGEpxTFCY0rzLsrB3ik8SsyKt9RmnieILh61+nibhHwuVUm/Gtxyx5ri4llLNucbGMg+k26QYyKbx5YvOLjs6TqyicDDuZh3UgX3CPM/uFf8b8OuvnJ6USpHxTbbUau5UUEw3kkk0d2/Q3l43PeeJ1sZJWi7XPrlYNxAQp+IivM2TlqjtdJEDi8vq2Custy1jUBbCq3+3ZhS3rESsRh/hwyvQS10TdRc85tzxEJS/3qzRt96caPRMO2vd4U7Gb7Ihmtd3JMHq4A03hKdrUN9NNznl+xGlGvc2nbnPjgyQqHYO3jh5isJW03Q3NptEwY75ZXjYSd5vL86ngKgv52qjyacf1+5CZEshULcARwRvI49O0m051Xg2mvKkFtIaRZhPvO7lYco0uJKrT327HIFnqVXoaqqO6wPDOPxxVVQhrVi5WloucXGd5iDHmsj/0O/3Kqq22K6WssQO6Nwp1OM48J1R5iTnoYcKUpRwkOXpBpX3ne8J5j5qxPy+22Nm5+nCTLXTS1c7c0BSc620LVp5+XR209aaTA26lKhim9pvspjSCVeitqmX7mcKUBrHg2CXXoTdKb09kDpos30qcHbcYeVKV01lIdxbpoFmuTb3mQG6JtnM2RwVT2osjoNt68ItVmWz4o4BGNx2xSBHn6ZOorxPbTyifnG6Xtr49WnrS5EUWZ7sTppl+pnGLnAmyxe62DqTllbHFaZ8vOxVdikwaWljSG5qExpLNVAcwW2+iM687A3E+zWChG/o1F+9PLXURc6plD/LCaTpwWUX6IWBZhb1t1nG9PdUZqMvbUXOqfp4ty/AgHYZw2M4pq9xS+Uleso5wbM+LIooigKgwRsmryZOOK2gXL17o9NrMg7DD0Fm71IHQn+35PvLY29XLy5ZIQp+khKTniGajyHNVuep9D6JzeUmL8/Ja421cmJF3dOPkFLMS7jTaWd1p+XW7mGcNZV24XSuIJa4n5GrhQkLcHXZitrjO0vXc3O+s+aVZNhafQ+7FWHBSIAlFvSSJgcanQ8lb06BQ9pjuKkE4xd1psjNOablsAwpxXATjOUT3GhGu3YJ1x3JbMXX2NUWxg6cfTS+Nc5Se6iGNMOS0Lv0FGvLDmd3xIggQxFLWxSZGEUZVI7x1C5Ae0WnpcIDJ0+QqJVQ+NA1WdV5GrXltjS3BjbnSi+S8h4kZOApbYOTZZqerxBKnnbExT8skkrV5Lq+mXo6q2RbsD/YKWZSMah8upOOp7mKuoRUrJPbBW0FNjBjg9mE/s6ZxM5DFcaeawyYplYE2Hd5kuCWxDIbVXEEGZak4msEF3vaM9Xy+UmaRZxHbUtHOy9i/0JfboiA4eybg5y4QDancERk+8NkRY2CXOadZWV8iVRQzmaFu8wNxOeZKo+vM2jsQDXUuT9FREIjAOqnXrbmmT110Sipd011Z3EMC5YLNUA7riyskBSl6cZ12Jytdb0Sut2xMArKysURKMWIiXBN04zozCbPSRSueZiA7W1mpXR1Bb1ZDrHCZM+fPMWUZfmlYS39IWXa2VkPxpPp5rrWcLRJWb5xuV748LtDA9OYUdZGq0kUixtjP9RtQ23Rm9VbUq3RizI7GtVIaqUYYSRODjCyXB65zIiY6FDnHzrZB7EmLyGinpyFwN6Vh6nW1T5utBKNr43JeFx5kJMdP9pZhD7e24WWgnGeMaLD8CWzo6LgOG2Aq0p4fVjttudvztoRngRB2+7RQ5UKery6X2dST91q4l3XLWIjXtNRys2mcrYzsMsfkgkNp8LTsn9gCXSrnDbfqMNtaLhua0fdyJnps2SqllSFVvrzuDAnpN3N+jeYzSqnSorpNiYG+7EODnBGrfczriwOy0uHOWiu8BWr1GbeJHdTqrO18TSAkIyY8GazZK1PJGMnWcDd1DNfF/rYIEScP29PV0Y8V3BbgKMNjiDYIF+qyZlfHg5RjrrBgGMC3ZmXg5zbYQK5aCp2vV1N920mSK69WEgqLV1IcFie97nBuQWzZdL1A8mLrs0SlmIG1ERxpqE4XvGx213MvXAj14i5RcTar3DW+NgJ6ej2CRRnpvE7Usuvkauf6u2KmKyzsNfq+y/gw7vHBWiUVux2qZZVS080C9+Z0CIuP2/B0F6zz+GCmir++bAs2kWDNJOCWkIR1cLObifOdnpJ1Nd+qq1ZTF4CwcETwsAIVaaqSFBrbiIDWhTozEBjf+0tPH3H/LKLd1kRObbc4ySq24zztJC3PksZQRJvl/CU77tHLpqeLeT7luMBuLdm9uajCztMYvRWoRe6OsrWI1vEaLbsI8DK+unbo3kCjha21RHGJcLHz68Jd04tsETbdkdgdj+1y1zO6NVMwaTfTsCsbnNCWY+ITTjYpk1F17XP77IyZDYYu0DKcessbHjS31TFmTvEMgNhHphiFEAsH39SmTB+R+WFHYgcmpXFxd70IJabDEMIOnludlphd2Lv1bWZdgyuFNDwqk6uimnapt+8LBewSJ29cnsU5O9G24IQUmrakDEDtCpU9I2nii1fLHEjTURmIV7GBNFlg6jJgaEs+aLu1wuFONidDPJV3lH7KKD5dpSt/5mrXauVOxfUCXV+dbkfd/JnB+aanWYKmAVyQO9mXnareTM+t7qGJve+tE7XIKOaws7y+JgRF1k4xMVvNZrRqCUqMnBoNucpF6CAWMiVOc31erq+XNRoIRR0A71o2HjfM8vPV32pKaDJMtST6lbHl7CE7ZwR2vZKuNT142JxYQKWYPRmX1/OOQBzSUGrYCy9yOjfnWLzcZerxQkS9QN7WapEDDS+0iOHptJqvj/qaF6UwJt3cyZTZPkOkgXSNm5oEYp/WmQs0rjtK3n7Zwp1N0hmZ7Nu3VL6qNTGdL8lCYJsi9HmlGoqkRyqAuFPkNqgnBCypeqlbpezQp2UDLE5bWAK1XG9549jkQX3gRM3hDrJIef32YspuKCLiTaZ2RqoSPi03A0qTmC/60qrtMuZ4VtUhz86JLWuGW2S4WwJmyPVwBXyNDo84XzO1gqKyLxkW4rV847KioOJBl02VhomXs13MmTNi7RrZXGTNo2FdC4Az/fHWZ7sG37OHqHPkuKmEdpXvqfOR3oynygBppqk92yo6WTpS5ymJzAhOt5cCcbEuWmpTSwzkoZ3BR8Fu3SNpLhGXQHPzbg6SaURL18vGwag5d7PpI8uBRYAPtbAD8yvlIEZ+c+TWotY0ShxwJuv24pQmkWYTkqHA+LQI2aZPzeu8khGnDaXSOrV4W54udI+XsI63U5zaIfO6Ps5NDng46xwPjd8Iy3nkdLHB8zNik+tFNZPm6JRWl6E5JWJtxpl4CjywR5jSXhZrKbDKimh9vyqPvCLkodbu9iQ4l0iC4lh6XWWoY4vXXpuiHr8RNxDvPeGxKkdxS5tNl7miVuGCQFlhf0GVZiEnKkwoyNZHV59WQiosWatTw6ksDkAteE/kiOlmQ5UsmBoeGZCL5bkO/eWs0JMuvLnx5bpZgrTRt9TitsQsPdhPTdri9ICUwWAWat4e1LhSN2J1wDMd7zxqji90SlYHi6BnnBIycTLLrTm2BmTvzaxmt6ab69qICyewVp0ZsqTSy2vH9Kl0cYH1f86kaEwf552Yedt2SXZcQwqxhgXNJmY1L+jZbnYDHMHOodKD3nNXxb/sIkolnKzdEqWo3m6nVK5gB+l3y5bVzsZ5SBaLxU8/vXx8GY+gnwfJ//7r4vFo73/thPFxGPj2Sul+iAxs7/N9rc9/Q6dfPr5UbgQ1epyj1mkbPA8d/9sp6qd/+SZinD483sGO77765u3IHe6vxl8heolyr62bavhaF2l7P8j9+OK09fj7DPXX54H1y92srBxPv9/M+HYm2hRfS3sEMsrHdznAi+wGPC+D55nyxxdvgL6J3PorTpFfQVWORj5fa4wnseN7jZff/x8soeqzpyUAAA== -->
