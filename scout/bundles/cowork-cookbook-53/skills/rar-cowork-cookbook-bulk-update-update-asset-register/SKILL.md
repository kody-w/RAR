---
name: "rar-cowork-cookbook-bulk-update-update-asset-register"
description: "Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_update_asset_register", "rar_sha256": "eba0a9a7cf9d54f377453283b6a860e45407fe8b73ba36454a458ac1c835ff21", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_update_asset_register_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-update-asset-register:97d5bfd0ce5fd1db73adb38c9a0904084aebad2d2918bea1b370cccd03b25db7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_update_asset_register`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_update_asset_register_agent.py` is
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

Update asset register Bulk Field Update — Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 eba0a9a7cf9d54f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_update_asset_register_agent.py` first:

```bash
python3 bulk_update_update_asset_register_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_update_asset_register_agent.py   # or on stdin
python3 bulk_update_update_asset_register_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update asset register Bulk Field Update — Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_update_asset_register',
    "version": '2.0.0',
    "display_name": 'Update asset register Bulk Field Update',
    "description": 'Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-update-asset-register',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-update-asset-register',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31a68c652a5292d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-asset-register'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-update-asset-register', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateUpdateAssetRegister(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateUpdateAssetRegister'
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
    print(BulkUpdateUpdateAssetRegister().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOi2LbvV+Hl/aO7L1klg0x14kQ8UBRERUFQ6DqRzbAZZJRJsF9/97dRM6v6dp+hI17EIyOVYe81r99ae+OvL07bREX18uVFB06OLJ00jSNQIU7uI7PiWlQJ/CoSF/4jXpE3Vey2TVHVL68vPqi9Ki6buMjhdL4s0xjUiIO4bZogQQxSH2lL32kA4nhVUdcfV3UNGqQCYVw3kFMFvKLyaySoigyyReK8bBskhQ9fkWvcRIhfDZ+qNkfKCnQxuCIuCIoKQGmyLG4+Q0FA72RlCuqXLz//4/UlhucvX3598VLICAomQHGMO+fHJz+y157c4ezUyUM4rBygHXJ4XYIK0s/gLR8EyPPqxxqkwSvy3/+dXJ0qrH/68jVHnsfXl/FPgwI2EUCawoF0fcRzSseN07gZPiN8enWGGiratFU+WqiGZszDz4+Z3ygVJfL38dmPDyafQ9D8+PWlgCI4o5G/vvyEFBXkB40Bzz+PVMoff/qcFldQ/fjTNzp1656B14zEoNSf357XT7Jw4LehcXDn+ndI9eFOF3x9+U658XjIPeoJZ758Phdx/uODcFkVHcid3AM//vTPyHoR8JLRm/8R3Z8fhCPg+FCnp+A/vd6N/A8EfSr0QfOfsy2hW/+KJnD4O7tX5Gmof0b7bv//QTqNcxj87xb/U3J/NgH9O/LzP9XtX014RYKvL3OQxh2MDjcFX5Bf3/SdOPv5B//bzR/+8Rsk/W/J6EVbeXcKb5mTxwGom7e3n3+o77d/+MfPP7QljDXgZG9tlf4ZzT+z653P7yz4HPXj7+dC/kae5MU1Rz4iHfm1KP9X9dtnxHTS2P92v/6CfJ8v44EioxLvTB8m+C5naijrd3b86eU3CBA51Kb17o9hlv/XfyGbeASoImgQ3Ssg+EAHN3EGRuEPUVwjh2dS/6Ir8nr9OfN/QeDdMd0hRDht2iDLyolTiFDF6PFRgyJAfvnf3h1AP3lPAJ2MyPj2QMH3rzsYvr2D4S+fkUME+RZVHMa5kyIav9shTgjyZuR4j426zT51I1MoUPwAHW0mj4BTtyn4G/LLv+Xydif4uRxGNb7m0C8OdJaPNCAri8qp4nSAID0i+dCATxBdIZZURZq6jpcg40dbfh5tc4xA/rSYB4Eb9MBrIb6nhQclD2KIyK/Q6XWRdhAXRzvWSZymiB9DyIc1ZLgXGWjrLyOxX375xXXq6Gv+AGISeRSXegIHfAiMfPoEq0CQxmHUfM2BFxXID7/+9gPyf5B/NetOfOSxg3a4GwwGc4qsdHWLwMxsMzisRsawgLBz99yvvz08MUqXwxoF8ykOxurWjN75LgxGDR7uefcN1HkUEVRPTr+3G3KNoF2QuIHWgr6oX7/mI4kCDq2ucQ3ejfiY/DD9u7MffEaf1E8bQj/dq+Y49h6BozPHavoZkQPkw1JQXejXZvRoVNQNDNoS5D7IvQHOdJpvLsyLBqlh3tTB8Iq0NVR1pPyLC0mPxskgODnNL8hmtoN1rkjhx2igO3s4u8jj0fHPaH3chkSqH2CMCe8kPiNbAK2JlE7llFHl1OA+LnAeEQHr2/t8SNxBcljvx4IORh/dM/oeecafdhJjpUcW98bjOeBrS2D4FPn/1ZuMovLLpSYu+YM4R8TtQbMecTW2UqOaj+4LdgkInPdIkm+dwzvIvMPv1zyNoS+q4W+PkcE9lB5jHpDWVjBONF670x+TurrThaIg8ujhqrqb4Wv+jvOv0CbQHfUIWTBvkxEFig+G49N3SSOYnOP1t5r/tM6YAzCKkbJ109hDAgD8e8A3UTWm09MFMDrAmFow/r3od1ohkDr0PKSPQCFiGKawFtxNt4VpAfukh/U/hsdjJwWl8FsPSgvzBnxGjmMYQz/U0AGwHRrHQCv8cCeFZADaGIr4YeE6csqHMGN7+xTQGX1RZGMQfOeB50MYkmNBgfw+8g1SdWDIQFteoRNgOvUPz37I+fQVFDYbY/8+6ffufuqKfF+Q/jbmHJTxG+bDjnys5d8ZBwJ1ldV37IFVNqlhVmfgGUAwEu5l+/Oj8j5K+4csX/7Q0//419r+ey01fu+5L0jUNGX9ZTJ51Lv3cvcZZsEExkhcgvpe+j49kuz9655rn95z7XeEH3b6gvw14X5H4hnVXxD8M/YZGx+tYw+MYfs8oC1mnwTr03R8+jWHK4IPJz8jYYQzCLHu8FFV3ofA0hJCwcfBjypTj8XpCuvhHdzuVeIjEJ5pArEzD8eSWBffpe+o0+jWh9c+QBg+ykd498dWLgTjKicdxa/By5e8TdPXl9zJwH+wuhlxFoYqNMa4JoJpAzujJgb3q48uabz4/WrunlAQCfziy5hXsKbBjvYV+WhOX5H35cJ9AZa3cL3089gYjyzhUPj1MfZjqeiCF7g+a4ZyFPyxBhr7sWef/EchxnSCEntgrNrFR36OHP9ABJ6EIdT4D0TU+4mTPkGibpyxEsIC/EztGsrpw8bpFYGugykHswiCYwsn/JEN5FOBSwtrrz+q+81+39QqHrr8djdD81hI/vryDhbj+aMReIQNnPCfd2ujTd+r7NtI2Rnn33uqu4nvnegbVC8eq+l3j8KxNXh7hOHLFwg14PVlNGQVw/b6dl83vzzEgXp862EhBQgan+qxO5jALIKUYM0uRx0SCHjfMRhvx/59/Hjy5U8b33+Z/V84xqfcwMc8QAU+7rsM6fguyXqcg3HYFGOnDnAdn/AJDmdd4OAuyWCe5/kY6RIUHA6lGD2ZOU8pJvjoAyj/h6H/ejf+8iAAywVB0ZAClABzOIfxAs6npgHJMFOKJFjSpR2WxsCUmmJMAFgou+uQNLx0phTreLjHklQQEPhI79kOPqR6e2+9373yQIG3R/sAORKO47Eeg099jnFoD5CYS3oAJ3CfIQFGcWTAsmAK539MfXpmdNxD8TFoYXcC+7Bu5PPr09NjINJTOFKa1jL/OGYTznRoYur2/Qm90cByc2qv5/Eq1+2Cdi9ytYnb0A97W/GFQpi7hI9Fqr8YbEa9KVRhCuo+YguNSnImv6mD2ahDosiF1cSn9ra6Ut7ABKg3rcOBtwK7zutUmx0vjWI4Md5cjEu/2lw6zd41RnGY6gGLdptuGt92Bk3UyUyJWe24M3GKPwlRlWEc51lH5WAvrFqvNmYdbejZ0OnlIvZmK6JtBrncRrt4KA7AWbTN9rLSFXxTGFrdpI1/S5xzTQS7dYyCHMYQKpZeJ/U3NMA33TbfewvnUgn6oJxBhqkmsFZGseUuylG1BixOuCvt6QndeWlx1Al8eSkw+YhifjtNLvmlpGcz0/TMwlR69WSvrPakFjt0Jdh0rHqpIHgLgphhqZ0C5XCZLebgUm/LRD6f+q3pnMomU7Ws5rbcqqWlLciE1hz0/kielat+WM/YoVR8eK3HR+2soJE47BN3V21s8WKlftT461uZGz7vVWJO7GWFFuSJH6UbrlmHwTZ3CHewz6vNcdbVubm/clu63G8mkq/Vq5N5tCOuOdQOT6s7whasSxMSxMFYbu3WVqfYxjPwy+CuJpm9dlvOyg33OKvdOcvuy71ZznNRF4etqJo1q3O+TdWNtFOvvuJmC5qiHBRMsFXtX6gZ4ZBnzKkzfDikfs44enFW1w4ei7znxpi9zJsEx+36tnApIEv5wTyJs9Q6TM+nCRHHg6iC5Zks25t0FAN0nTSGLO/YzXHZ2efY25TUTphpN2FtGWzEci1a9XZsUA518m75Rkc3E7ewpzmhxtsZVedbpXbSdTkpJJs7YrfLpT0tQRwFUXPJjRTlIxDz4HYgQGC1WiXprWLsWMk/x8GuS1E08zbnmDJpvOoCESPIaVOsid6j1wPGkqWibP2KFofDfuLsc2AywlxZ1npmB5w+JWl/3q0k+9gkq8l2vTLOhQr8DTXDGHWTbpSYXtb91llFVYjnQsjjiR0dVT9fypU0zW0xukZ1Jy5CYV9ri/l6V9I3VZp56iqbsgneLrBgebqdpQNx3tVnf0YVASOQYVS504ETlpwkdsp+vUgmB+awNZhkR/cYKkrApbyLjVsdGgyLvrLo9ZaDNsZMr3Npw5l2pklswz1/ChhsW2FFqW4pWvZMzb4qNC5b/KVPODpKURKAdLnEg71Gt8pyql2Oq+Jq6PmCn5PmEhwZvdIDzZ6cYtGZ7BlFkkitvrIois57QztQANRmfFugrpVwEk335WKHlkmodZaTmBI1qY3MnBoJW+Aiaq7L/dY82fMVfiXm9dVkZ/R6erBpKe9X4iHeldtjr087/jDB5W5ZXa7YjR16sNtsJTnerQJ2buoFG66dLVRzS5PnW4wnswgQgjMkYsZZKcBQq/bLdJtop+sWM5X8kNmGs98b2HxTcnyxIGbGjuoJw2fzhL9IK/fQTwxcu2AFTaHOQs2VBT07GGi+8PM+FtBzPdRxuc/IUI1J44gHhuKaWeNwOJXs3Iqe2A26keQg9VnhHHr+VBVWynHZ+75TGsFZVjf5/irL5y6J9j668LyGnuYhiZlLFeqoc0vKmaHzcLLAUHTBxaJ4K6CIwTZG/c5Ohg3drjfCqb/UuT7ZrwdhF4rlWomU2jjqE6HFC4ch1qJznIf2VedLqV+GfrS2SiwhI7/Sz1RIhqspVuzjZH6DiNvFPjqlr600p3i9kMKbvTIILYH9LH4Ey4nH+lNnf7nI3dESrGW7O012tzwNcuN4iVUbxyfd6cZO21M1cPJqFx9qrcxhmUMvun5Ol9zWrixJLChxoeH0qUaDyTEULMnz+4kbhfo6qa/BEDMT8UTeUENiUFZhdwnLscUuWuwtddrtVs2gi4Ivy75iEdHNVO1jYoQX06sk0yuvS7yPlbjUllnDD7Rohl0vxntT5trLSgHLcpdb2iDz0jbLHdOad6nKM9SBx1mRkU+4tVzsnI1pLM9od8CSvjotOGKVygvgAbYNWIoztkRwvq5TtN/EJX2NOryXembJWP2Qk+rQSMdi8HsvjWpHvaxXAsYLwiKxBpyptopxIC3qjG78usevbC+EyziIwwXBndND4eKKw7YRvrZroTbLkNEkUzakUqnSZcJ2xLGjWpnvl4Cs+P1C6UjdjGZ9c17svQHfVNo1IEzKjxcnWyNa6SYdhGtyueoxwaXhwYAuVnfC3FDms7TZWBtgFSiGmkpniXNhx+s4aRfhxV/OwijRzDPurU11d/PF4ywZGl+yiVJOqdwPnY2442+EsqLX5sK2u50EsVxc2npwUo7nlGZWSiNIt6xmNj2orVrYbgK+y46s6/cXHYsMDVjhpoNrGKr2ByKyBmO9yjrd5Uu/siYbxghv2zhrjql8Wt96zQX9glPTBXXJstQorR23NGkv9uyYwY6hWOwbQN9iYHFXP48lbHv2F4rN7Ivblt6ksly5V2PN8ccyvGyn+GY+W2PFrNob601CFSlxdXZ8bui1FkXFRuH7XSWWJ0+YX1DlINDcllh3RKQcVIc3KHV3nUpLWpiQc2cNQ3idNzLvq/OhqVmvkSdquXYHbhWy3Bab3BpmeirRXsYWkzm5kLL0Fsx1eQoSsi23O0nL63oSrJ3VrivdmgIQ9NTIDZq9s6kwNYy1enY7Vc6JLxR+MZQ8ofAuxTC20ppJPedEK5PrPU24Z28Nc41RLzZmD1clqfZO2obL/LQ0Woqe93yWrBxqfynR3UXbwEitZVHxj6tTI3B0e0v1y8kAttfiboTuQrMKN+K+ixqqwJYTZ+Z45zJSNZmertrksKiiweilJFuhjpKJgs3taUqMlm1ECWqsOwG+7RJ70zZ0Gqwowjxic/S0kOgZ4Vl5Mr0wFy2Nw1rJzXXQ6pZqnMv5sB/Y0+7sbJbqvt/o5qpebRehci6KdWasElXDLUZmRBubEnTsmUeSP62o4nqdCCULMEXKXbmcHNKFm/Atl2uEpa9nQWkn3OFyuLiq7O4O5qGzOTXaGRRdtls24rANLVTs1elxJe9DbMNNVc3rTH6RryunAE0RceZpu+6XS8L315f9JVNFf6LkRZYH3mJTGiS7gynT6vEqWUdKr3inUFOEk4by4d6+gc1Q+BcZr8v5PL6maSiX3tq+bsnZ9lBqx8bvSfIYYyKjFbDumU5JBMvVsBXaiW6wJxJ2aZUt5cKFzmd8xVxL3yjl8IwbB1ZQQ2BfZ9da3DuHzJoFqyCzb7eLvtSUmUWX9TVew67I3G2PAGfCta8nQyUWUPAbMxOwTbMT51GBuhvHaNUDs6JIgdc2Q1XczjBq0n61nTJ9MBzDbBbYaHtwmEGyIuxopvllz7btmjRms4Uyj8tc1Iz4OF2eZ3ZEXEmvAnKfUws1OKWocCvmanVlhjZhsshvqn1iKHZxkLY3ubFRGSeZDTYjSc4gJhqelsnCzK3VadAlEVsFOLCys+lfZxktkKYYuo2OJmf1ImZifJvSwNQt2AWa8sZQr9dFJWCOslsNs/WsW7q4I1gFXJisytqFbX80STKlCmF3LF35Sr8OlZeo85bmuOlMd714L9Oyg81ofzKPxQEXW3qlH66DdDnYxG0WxbWSBYaVE5x2SLAtObS7yS4WUgAyWDFT2z1hylxW4kWrFKgDyiiwu4PfqvPkfD6rzPIsuM2hWHcLcBo6v91pLVERroPGeO9fzkBbBWR0VTgHtvXdZT7QkkLWJ6tQF7krRWptK5G+s8jEXG6waZqCqTR3azITbmqoqJpCH5meSZv9qauXlzRzJjK9H4pYPovruOVXmDlhSWxOaVuNvxXLqs4qhqBnEzucqfKcL5rhFO5XOKOzSlSubUUSz3Rnns6DaJMacatdTtS7OK3W8x6zsyA9ae1+4ThBvqHoPaDiqkfrctjt8HzCUceAFQJcqf01fSZRuaMIg0sZUtr1dIQxip8q7kXF8JpntliShxStnGbBGU1Jqq+0YBJdpvE8dNiJ4WQLT5zlkhtHG/Y62e/jA5tx+xNPy+QkW9GAs09VasZT9cQPYWVVm7M1Xc7JxmpMcQiNnd+6t0wChhXA4r3F1kolK5Nifw42KUCX4RxnL0w7L5WJwG45E1ty8WLBACvgIVyRJ+vEdl7GrGUi4pMbvnEr0uJscnkLrbpeDJvD/nQ4dexxvkfVau8xDnrTO7ybAFXd2BsYlW1wnct7LXBD+hQItC8Qbs5IB1nzA4f1N5rV865l2hC2HXSSUs5CI92bI5gMuEgbb8tsJ1IVrFdcmBU8P/Hp+nQ1V6x8oY6hNiNVQWRik1JAJK2xQ3vs6Auj8+F0UwQp7bZ2OzMICpwuMfDxhKc39mD300QVWp0OD4dbIQlhPrV99xatO7WeRp4wLY9KFy5ccbuGK6w5d8zzG8Wqqw6CFWcIw3q7WgeufNpS4kbUrIMlhVdtCwgwu+3hokIG0bUrSZG+tG6yQaetHwhHryeNyXVG7k5kbrP+cDxOzy7hF1NGAXYmwNX7dojd7VBLpAJk0aQ4qV0EYHbdXcmT0bBp43LEVMevsmdQrRDt2NNhsjyEwXJ5rq7Xab61VPGiLrmg77Zcf1n3R6khefU4u7rKockX7SLXaNpllOqYO4Ah0IWWLdXKt+aif+oMoRMKVAR7nL/qJrebSuDAeLkWavtdTaHbecE4lu7lBQOSIZbKvFTXN5k9kxZDzmQgbqsmGxJvshTsCXNCizQ/BkcfY5iKblzM6mWfCaoIu0gp7xK76XrfB353nHDsilQ4HXPbZJks0L6V2lbjboDbYWCyCoLrKtxSJ2zeTBYOWjmLRJCG85lfYNYs7y8VUdb9hENXhSlgsZZA2y7MYN6gp2nIzTGMvypGxJ2C23Q6VWfxnG66Tpz6TUqlLZOQ+eV2XNIRelT2RNU40SbZAWMm7W81GvLOudzrN1wd5A3pTRtYpHyXaIaj6btMZ+tczVVd2+s8JussWQR1xObniyBpV3SnX9rLPu8SEnjqnj+24mraNryRqaormidqvyZsHKLPbbG0bVU4225N0OZixRD7RmO5Yc76tmCiuE9hDSt53Z4X24Gs03bGzdaWa1HbFd7NB7EFJ26RHSjJ7KiZ7s+9zdBuMOW0ytaLyssnpizsJ6aaqVkWEKzBe0yVXiWV93Pl6qrYYmU4TpWIMqHm1T7gT5K5yi0Q+32Dduo6n0StjZkX/1az+DnF47yYsLzZ6O11UZc8z//95fXl/tr25QuOUSzz+jJu/T838P/S/m94i8u3JymSIYjXl/93m5OPjcL3l3v37Xzg+F/u3L/8BSn/8fpSeTGU6LFlDL0RPjck/8cG7Kd/uys8Th8eL57Ht5B98/7yo3HC+651nPtt3VTDW12k7X3PGlq6rcefntRvz1cHL3e1srK5P/tQY6QNqi72wFtTvD1/NPMy/jpkfLsG/PgxZrwMn7v8ry/+AL0We/UbSVNvoCpHZZ8vmsbd2vFN08tv/xde3MJxVCcAAA== -->
