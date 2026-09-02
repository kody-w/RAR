---
name: "rar-cowork-cookbook-configure-map-value-streams"
description: "Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_map_value_streams", "rar_sha256": "1458777452e6cca9511e50bae53cf570a089687150c4980dd9134d4856d01bf0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_map_value_streams_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-map-value-streams:86ebe937676e2b4ab48dc5a732d7ef829a9a72cc16c22c7a8f10791287c2e909", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_map_value_streams`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_map_value_streams_agent.py` is
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

Map value streams Configuration Bulk Setup — Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-map-value-streams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 1458777452e6cca9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_map_value_streams_agent.py` first:

```bash
python3 configure_map_value_streams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_map_value_streams_agent.py   # or on stdin
python3 configure_map_value_streams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map value streams Configuration Bulk Setup — Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-map-value-streams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_map_value_streams',
    "version": '2.0.0',
    "display_name": 'Map value streams Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to map value streams from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-map-value-streams',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-map-value-streams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ffb53fe67eb4147',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/map-value-streams'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-map-value-streams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureMapValueStreams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMapValueStreams'
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
    print(ConfigureMapValueStreams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZPaSJ7vv6Kt/aG7F9tI6EKemIgHEiBA6JYQtCfKOtF93739v28KqLK9Pd1vJuJFPDlcpSPzex+fzKzfXsym9rPy5fOL4poptDPjOPDdEjJTB6KzLisj8CuLLPAfsrO0LgOrqbOyevnw4riVXQZ5HWQpmL7K8zhwK8iErCa+j/WCW1Oa02fI9s305kJ1BiVmDrVm3LhQVZeumVSQV2YJYAcFad7U0Ka33Rjygtj9AHVB7U+DA+dBZZKpzOLYMu0Iqpo8z8r6ExDE7c0kj93q5fOv//jwEoD7l8+/vdixWYFXL/RTEvdk5vrEWXkwBhNjIBUYkQ/ABCl4zt3Sy8oEvHJcD3o+/Vy5sfcB+q//ijqzvFW/fP6SQs/ry8v0T25SqPYn7cyqdh3INnPTCuKgHj5Bq7gzhwoq3bop08k4QOsgvX16zPxGKcuhv0/ffn4w+XRz65+/vGRAhLvqX15+gbIS8Cub6f7TRCX/+ZdPcda55c+/fKNTNVbo2vVEDEj96fX5/CQLBn4bGnh3rn8HVB+etNwvL98pN10PuSc9wcyXT2EWpD8/COdl1rqpmdruz7/8GVnbd+0oDqr6X6L764Ow75oO0Okp+C8f7kb+BzR7KvRO88/Z5sCt/44mYPgbuw/Q01B/Rvtu//9FOg5SEPdvFv+n5P7ZhNnfoV//VLe/mvAB8r68MG4ctCA6rNj9DP32qogb+tefnG8vf/rH74D0/5WMkjWlfafwmphp4LlV/fr660/V/fVP//j1pyZ/5OlrU8b/jOY/s+udzw8WfI76+ce5gL+WRmnWpdB7pEO/Zfl/lL9/gvQp77+9rz5D3+fLdM2gSYk3pg8TfJczFZD1Ozv+8vI7qA0p0Kax759Blv/nf0KnwC6zKvNqSLEzUH+Ag+sgcSfhVT+oIPWZ1F+V457jPiXOVwi8ndIdlAiziWtoV5pBDIF8mDw+aZB50Nf/Y99r50f7WTvnb/XQBXbOX+8V8PVZAb9+glQfcMzK4BakZgzJK1GEzJub1hOve1RUTfKxndgBUYJHuZHp/VRqqiZ2/wZ9/Qv6r3dSn/JhEv1LCnxhAgc5UO0moIKaZRAPkHkv3EPtfgTFFNSP9zI7/WjyT5M9zr6bPq1kg3rt9q7d1C4UZ7b5qNjVB+DoKotbUAsn21VREMeQE5TAMFk5POp3k36eiH39+tUyK/9L+ii+KPToJdUcDHgXGPr4MS9dLw5ufv0ldW0/g3767fefoP+G/mrWnfjEQwQN4G4qYIYYOigCD4FsbBIwrIKmUACl5u6t335/+GCSLgXND+RQ4E3NrJ788p3rJw0ejnnzCtB5EtEtn5x+tBvU+cAuUFADa4G8rj58SScSGRhadkHlvhnxMflh+jc3P/hMPqmeNgR+ujfLaew96iZn2lnpfIL2HvRuKaDu1Bknj/pZVYNAzd3UcVN7ADPN+psL06yGKpArlTd8gJoKqDpR/moB0pNxElCQzPordKJF0NuyeGrf5bPXgdlZGkyOf8bp4zUgUv4EYmz9RuITxLvAmlBulmbul2bl3sd55iMiQE97mw+Im1DqdtDUv93JR/csvkfe6Q+ggf4BXqwnxKGAGpNDX5oFjGDQ/y80Mkm72u3kzW6lbhhow6vy5RFaE3iaNH3gLQAOIAAuHnnyDTC81Za3qvsljQPgjnL422Okd4+mx5hHJQMZ74CCId/pT3ld3ukGNYiJyclleTfDl/StvH8ANgEeqSYVQOpGUyHI3hlOX98k9UF+Ts/fWj30CLdJdRDIUN5YcWBDnus6dyPUfjll1NMFIEDcKbtACtj+D1pBgDpwPqAPASECEKmgBdxNx4PMAPDo4YX34cEEoIAUTmMDaUHquJ+g8xTJIBoryHIBCprGACv8dCcFJS6wMRDx3cKVb+YPYSZA+xTQnHyRJWbtfu+B50cQlVMfAfzeUw5QNYHvgS074ASQUf3Ds+9yPn0FhE2m8L9P+tHdT12h7/vQ36a0AzJ+K/gAg08t/DvjgFpdguCcQg4016gCiZ24zwACkXDv1p8eDffR0d9l+fwHFP/zvwf07y1U+9FznyG/rvPq83z+aHNvXe6TnSVzECNB7lbfOt5HkGUf71n28ZllP5B8WOgz9O+J9QOJZzx/hpBP8Cd4+sQFtjsF7PMCVqA/ri8fsenrl1R2v7n3GQNTLQP11RreW8rbENBXbqV7mwY/Wkw1daYONMN7Zbu3iPcQeCbIo8KA3lBl3yXupNPk0Ie/3isw+JROtd2ZsNvNnVY08SR+5b58Tps4/vCSmon71yuZqb6C+AR2mJY+IFcACqoD9/70joimhx8XbfcsAunvZJ+nZAK9DKDXD9A7EP0AvS0N7uustAFro18nEDyxBEPBr/ex7ytCy30By7B6yCeZH+udCXs9MfEfhZhyCEhsu1O3zt6TcuL4ByLg5nZzyz8SEe43ZvysDFVtTh0QNN5nPldATqeZ6jjwGsgzkDqgIjZgwh/ZAD6lWzSg5zqTut/s902t7KHL73cz1I9F428vbxViun8AgEfEgAn/Cj6brPnWV18nmuY0846i7sa9481XoFgw9c/vPt0mMPD6iL2Xz6CyuB9eJhOWAWhX431h/PIQBGjwDakCCqBGfKwmPDAHqQMogS6dT9JHoL59x2B6HTj38dPN5z+Ht39M9s9LwrVcCiUJknAXFmZa2NKxcZNEFw7pessFZVImubBthLAXC5s0lx4CkxSyWJL2wqVgCvCfvJeYT/5zZLI7kPzduP8O2n55TAUdYYETYC6C4UuSJDF84RK2bVI4grg4bJkujtoeTsImvKSIJYngsI1RS9hxKATFHGyJEw6MWN7daE8U8JDn9Q1gv3nike6voDYmwSTtwjTtpU0imEORJmG7KGyhtossEIdEXRinUG+5dDEw/33q0xuTsx4qTyEK8B5AW+3E57end6ewIzAwksWq/epx0XNKN63zPJLX3EwsZ8GIDpe1YG4dQr0OWCStSltpCIZnb8E2OqeWqPK8uCPDOrTJLWwE8nzFzRQD1dkzSnrbU1UxubPb68NJdgwdcUp4ph+wIoBV/hrE9mDhSueYRoRkGacRI9wUcVRqsC8m7bBDdzFRXLR2jg7FeGsHpCuPhLw3adbJYBit4lupyU0vujRRVP152HBZlvSF7UWEbsUXQu/5/rhoeFipTktnu82TTD1g6amE5TqIOY06j7AbLoeB8gwWx+ctN9goi8+FM0cuvADXTHnFaYUZ7Cw3ORWGO98MsRKgCeAbp0dZ8GCGnev7HX48LOEMgaO4oGBVhv1gvd5L/C51dDpTuSXundgmpxGtPyOo2PMnMzw2R0dlzCE6tvERTuGTXep6pIijlzPGlaHdDXa+IYNVqA7MU/FVJ3IJ4JJNrh/VqyHXmoOhgYKrlX4sLmNrLOar/VnUt8RV6opxQ2pmmpAoSbN041SyJa3WDkY59eqqUTzpe5VhEhYW9zBc+vNjf9i7zk4/Z0lbt/tzLPMX7RzYKc/xXDhL1smhvByaCtmVZ66R86u40Rm7SgKVSohFpevzsuYOZ21NuFcY20d+WR02XS2TnuTmuxxZEkppjK6wXg80pZHVbLAQaik1+ALPWIu8npRhUPU8MRcePh7XF7Xhg22uLzfqUCKdwSPXatxecQ9jY1UXYjrOVCzL5nW2rzbrwxKR6tDyueUBJprtdsSVfvAzdZ4ItOTfEJu46VnhdoU7pwoU0Q4VURZwMI+W+GWRo6PDjcZFCCk6rtqTZJyLo3vIB3GDUKKo4UKjVf16qRbVfD2b4XTLOKQzvzR6SSqFwnmUOLvdLm1+pcDwpRoQe6MIhZIvo9QScLbyN3BpONcFG/lBo+OGGaGbk9PuxipzjHXICQdJExcZT3bi+ipvyJumE0stNfZqRZyWu6V83hYXa6shzI2AFzTqt1GAc7LM7r19uOP7Q4PvnH26z/0G0zlJ0hSDs6syGFk2NAXuTJOxfl4jcyLqBka1cnJFL652vwg42OlTokWGde3hFLw74OkiN3H0dF5TM0qsB5jFDbVovNl8k66kfowsxeNYlEarcmaYl9ZDdkfWk7irY21AJeLSMJBvaaidF7V63XlR2Sc46WOkWRE6X65Rwh6GY6O63bhTUWWtnbEhVG3OGyinKHyRPDnlca3u0Hm31Ny+qMoerhrtluJ14aNOUbpp7KWpHB/oYNHUM8Hcw2dExTbRreBVMTQJLdSNPggI1NohxjFRsH1mbAk2hY9G6oqH7TkfMHsfzYm4DZJSuo1L89Ru0V2ykVIkHFcauS30rala3EKbmQe8U+jtSuROtUvvaKrKLcTWajX3hY2E5ozuc6kKQJUpjqF4iPUm0pUC43YZhtLCjB7EeLWjeGxeHgrkKFv2XOnHfAio2yH3NjcDS7ibAKBwMmRpF3nKNaVUeENVy4VVy2zUxT3pUDMr9CL3LFYFHg+lSxDa8VBlOYkUaXRd9yHRqQyJKv1c8TKrpLOd0tnmepfHclix43pTOpc1g/e2spnNEPK22ZPAaWp1tGdum3f9fBXFyamFkbWKW7eNJ8FZb7OXVZQUXCfeUCKiM8Lud0hAFrYWD5LnxzYzWnFzXIhM3W2c1VrbhFxQHxXJzI+qFYVbQYQ5vSNWB/vIxHXUWPuRbvBOp/wa5URrFw2mLyBxZM7PYozy3NyqBI0aouWYl63QpjFug75DHA7XlWJfC5Q1UJy8KSFSzPjMuLLpCsMiCiaM5JbOkSiygBMwy1G7NNrLs1avYpYlRq3HZxl+ElGxHTcCVnpbTjvEqTsr6yiODrub3OWOIgrb8bgI+qNvHHF4IciciYU0h/uHmGd8mzlGZyxMbsetuVA1ZBdq6VB5zkapRv7s83qC0qnC+aoybRMhfBAOdWiGTSJF9MHbFpaphdHQY7p+qUNZPJ2W9AbNvZll7JEgbPeY1qDL05o2rA01ZIwfzebbQNuyS7eES0EviKYWdlaQloyy5HM2gtdneu5fuSq08bGpRkfY687IWidfO56yS7AhlzdkocPzQmQIKxhxp+iFgol3B9uXrknRyIOaY30xT7Ebs40W1416CA81c2Znp1XDDTxj52a71bebWW1a3nKzIurCidoVs3fTedZpeokrJwMhYAqLnWzmrAnHXlxY98ojl7wgo+JGrCn/iu7LdaOex7pSzDLO6KvEsQGNoFc3zwIh7rmlIYSFv4jrVaRciJBRLrywsWkk4+QYsQ/6VRxtrSi52JwnxdE0Jf98Iml0pZ9UruPCoLD9WCMka+xmvakDIjjMzLekrpomn6w8mwdQ4ygfEl7cgMUBlVujneSDEF3PYyqoLLGnR7e2gkMUaoyCRGs+P5KzsFYDXKa9sOKLYLsg7Cvjb69eKDSuqeyRAslXc9Dr1EimDdENYck/bcnRuOmcsZ3LUuSsrVWOBic0h9WI2tHVVkaa/XUVgJq/G+anTTiLkfO2z2xc0Hh4119rvBo1pVL6dUxwWC+US187rXmpN5WWNzWHm2N+JPtqxgqhgZ0PVlYRxDW9wHaFqztC5hJuLG+dV5f6Ke/O5W55VnxyDnBMzYn7MOyv9i0C7oloz3OOeR+WXQL6VVld926dUsTFYlwqtU76ZXBU3NBJeH/jeIHrNiZDA2ApSTFzuK38G5/fzvaWamNjv1ysseA0JItMK0W5ZXUetw2EVfirdN7vrEO+W6+6MAAAzOOIg71XFoWvK46nJxfOR7UVu3eMES3Mm6PUxrHwDpKA0KHSzrfLFamtQ9sZeM+8rLdZpsqYI1yPAmv0oOswW1fYbjBhVnfwTj1hctdXSieFNUInAyPPtWIpRwOxMK/46hQ06M0d8KxdGYYX+5vzLL5qK6E7UKpDdgm1lUjZjmjjonb+Gd2ZV5Jblxqb09ubpJTbY+EIcYCz57BK65sGAOy6wAa/WexkUh78WejiNyl3nSooKVHT89W+Xjis42+KptCX44FINd8mbHlhF6XniSAoeq3cZHoCLMcSEtfqfrlY9wWGmtyO8jZbVL5q6i4iEtfCaVdHUokaS1MQxnPdaR52YJflvm3MBpldZ2OkRwBWbnAZTjOfGSQ7XeWrVZidVrbBicUuuBWcoGCZWnqSTnOhLqxnmLJaJ5xk1vtwCDq9TPCrFwNMRxJrt7epmbzwl5uSkZCTcnTRrZkF0u0gF0iJpsEazcdI4fNVZUkuLZVSqaEcXO9WRq4J6XZjR70jnMxWLvq+WYp1uRIEczyhW5dl/ONFz0VJFY5dHxDI2PFwZ2iistWHUK7rCBHcPSl6wRVg4FVEYsIYaoM7wDfjNmySVmnXA3fedcgq00TgFmG8rGNfkTjNSlvvdroS8tqAO08iNd+6ho7MbPeGZJBFd4gVJdt4ljNwgxsojTu3JMuzdLXEtjy3O+55YaSFZSOsM9ozhGuiuvxK1vnrumuX540ynKRDZHP4joeXhU0Ix+jAXUAI3047OhhOe1zi0MA6wUF0mklhyqsljTpUSBPyildxUlpt98zi3KZn2vAMxMN2xfYgpdENw2Y2GcP98nwCoBRRm6VbddXpIqyHs32u9uOxCho3u8oxC6DBYgmABYwzbKvEuu4diVNGt7UzuxKwr8xPiZX5ncksRsPfOKQ0UEPet10hsv2hEtki4+p5rbtwt0iaq9qaxhoRiHkbdm5K9YIz4DxYuVrCUDOe04uxtJesCj0nqVGcRyXnj51mioe9ZJyCLsjRs5qXUXu6UF5Sa65aqnHd3ZZDNdDzVGY2vTe3HAaW93oyNh13sebUxb1ROpptVmrZO0m4lHBqB3vLIC86iU1FvLqq/gCLsMx6DW5U5tggFiMtxIVT4yhTJ6u5IMN143lj6y1SDxhizeIWOZ/dfGpVrjuy9OYjN2fVYHFtnctstBakzDmxq6/5ZavtdhLMw5s0Nim6khnCyG+Lpp2tT4Q/SuaFPaFwSISZZx4uI8bMpPiS5gc8m/mw3F4qFSbRukn0BRlhJ4ZVTOSkW6kGu1xg5OH1eA3prMFdo6Vt+4rACsAR0unYZiSAeA42sGXn5a4ReULGVCzFduhW0/h01xg1ySyN1PL05U2kdFzh+UuRrXfjUkWWebhApU3DOHHWyEERLENhjOQyg0Ue9hLC5NU5EpLNLuSvcMBQ60O2PlJ7NqIoNodFR/AKNwl8lNTbOuCO2bwUGoE5WGcA2bluphNNQNPqMNfcJRGm3FxsCM1B1yd5hc8w49JmhY7JyNDuA7ax6dNiU8IXShnOWecuvP5EyOoKkypxSYnICV3vdst0RPrjCbc3rnCd9x0WL9YbBVcSNGidBWv729koaPDSOaBMzybRBWAtq/NDd3tNxVFtwTWbkeJ1ZBc3IV9nfmlRXB5yNywQTtwptmlxtbiAlui3+2o9EHTVegzhS+jlKvU878kzOx8VBgPIvLwYzaLpr5x9dQjRdKkNCzgbYHGyLBeGvVyTx1hpeHsWtnR7OZgsGZYmskwdtMR7lvSlPoxxXmE6azh2TphLSE2v2n5+YRizybK2obvNskICeNu0yapfNbukI4lrGTqR0BoUZjQ6z/NkayHDMc0cIgpqUaauRFhjNYsyXZQJt62nuTSayyiPXViNGQUvPBLCLrmmB0JA/VXmEzmhFNRV3MuLAzWu2RljolY1GGJ/W8xxg+6tum4Jstx4qK8spWC/nTeCy54xV5HnShPwS3mprcs5WaEiM/P1VOe0EZ+tXDk5azOscBLUncued6sjvlFR3h537iyyWHifBEx7PHqrncjoZ8c5dfP5QswQHEmYrdkI1s5V9MrAmjmz6ZiOllLKMHrSskU6OJg1w6QCY0niiWpxGydq3W9SNsVkHHEuO/YIFo9SR60EhmDWBM2sOcZFAcQmd3yxLvR1uyJvJ8q6eK2h2mc3ZDehtuJWrDzXGUxgtZOLphhFB2QdmMvAoXp8T8Pd2qA77Lzo1t08PDJHElcsyYZXoz/GipTN9NJklIwaXJ9GWA7l9r2fbg3UHVWB7PmlZwdHnFvPY4wjTrUcJgffbbCZ7idxNSsjNkEpQT+Mt+uh8kDBYio4LaqGASuWIVsVyTxPRs6xyeqCH/qZ4K0uGS0Icb6Y7U/yHu6UzSasKU1KF1nUFvuMoGDvZrGDLY6JLlyHnbLoRcHYDE7YYgwRaSTCw6CLr/7+8uHlfoj78hmBSYT88DKdBTx39P/FXeHbGOSvTyIoiS8+vPy/2758bCW+nfDdt/dd0/l85/75X5LvHx9eSjuYZLlvIVdxc3tuVv6vbdmPf7FLPE0cHofO0/FjX7+dfdTm7b5/HaROA8YOr1UWN/fda2DXppr+1KR6fR4fvNxVSfLpLOKd1/Oo4rXOXp9niC/TH4JMJ2quE5j12+Ptucn/4cUZgHsCu3pFCfzVLfNJw+cR07R9O50xvfz+P2cAjqw6JwAA -->
