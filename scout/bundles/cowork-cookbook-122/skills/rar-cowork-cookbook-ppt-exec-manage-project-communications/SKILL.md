---
name: "rar-cowork-cookbook-ppt-exec-manage-project-communications"
description: "Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_project_communications", "rar_sha256": "4fe3d419c55626916d21d37421323bf8c1f0e54ea9134c99f0fc2dced26d1b73", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_project_communications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-project-communications:60df3423d794103a659bbbda4b83a9ef4a1da0c0803a1bab0b6e00e9c7a22f65", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_project_communications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_project_communications_agent.py` is
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

Manage project communications Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 4fe3d419c5562691…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_project_communications_agent.py` first:

```bash
python3 ppt_exec_manage_project_communications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_project_communications_agent.py   # or on stdin
python3 ppt_exec_manage_project_communications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project communications Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_project_communications',
    "version": '2.0.0',
    "display_name": 'Manage project communications Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-project-communications',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '048444c389f30da8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-communications'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-manage-project-communications', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageProjectCommunications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProjectCommunications'
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
    print(PptExecManageProjectCommunications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjxpruX2FqPtgeVRcgNqlOOGIQoJVFQhII3I5qlmQTm9iRr//7TSRVdffY54w9MR9GFV0l4M3n3ZdM+rcnq66CrHh6fdoDK0UWVhyHASgQK3URLmuz4gz/ZGcb/kOcLK2K0K6rrCifnp9cUDpFmFdhlsLlC5CCwqpACZcioANOXYUN+FQAy+2RbdaCYpuFaYW4wDkjWYokVmr5AMmLLAJOBbGTpE5DxxrgSqSsrKoun4fbeQwqgLRhFSBOYBVVeZOtsuJzmPqf8htomkHGL1Am0FnDgvLp9Zdfn59C+P3p9bcnJ7ZKeOtpm1cClEy6sd7eOXPfMYYQsZX6kDbvoV1SeJ2DwsuKBN5ygYc8rn4sQew9I//xH+fWKvzyp9fPKfL4fH4aftQ6RaoAIFVmlRVwEcfKLTuMw6p/Qdi4tfoSKUBVF1BXC2pbQF1e7iu/ImU58vPw7Mc7kxcfVD9+fsrywc5Q2M9PPyFZAfkV9fD9ZUDJf/zpJR6M/eNPX3HK2r7ZGIJBqV/eHtcPWEj4lTT0blx/hqh399rg89M3yg2fu9yDnnDl00sEPfDjHRg6swGplTrgx5/+GawTwACIw7L6S7i/3IEDGEVQp4fgPz3fjPwrMnoo9IH5z9nm0K1/RxNI/s7uGXkY6p9h3+z/X6DjMIWp8G7xP4X7swWjn5Ff/qlu/2rBM+J9fuJBDHOusOwYvCK/ve23AvfLD+7Xmz/8+juE/m9h9lldODeEN5iloQfK6u3tlx/K2+0ffv3lhzqHsQas5K0u4j/D/DO73vh8Z8EH1Y/fr4X8j+k5zdoU+Yh05Lcs/7fi9xdEs+LQ/Xq/fEW+zZfhM0IGJd6Z3k3wTc6UUNZv7PjT0++wSqRQm9q55//r07//OyKFTpGVmVcheyerKwQ6uAoTMAh/CMISOTyS+st+sxLFl8T9gsC7Q7rDEmHVcYUsCiuM34vboEHmIV/+07kV1E/Oo6CieV69DaXy7V4M3x70b98Xwy8vyCGAzLMi9MPUihGV3W4RSA8LH2R7C5CyTj41A2coVXivPCq3GqpOWcfgH8iXv8bq7Yb6kveDQp9T6CELug1WW5DkWWEVYdwj1lCx7L4Cn2CxhVWlyOLYtmBRH37V+ctgJT0A6cN2zkc7AEicOVB8L4QF+hm6v8ziBlbIwaLlOYxjxA0LKFNW9LcSD63+OoB9+fLFtsrgc3ovyQRybzslCgk+BEY+fcoL4MWhH1SfU+AEGfLDb7//gPw/5F+tuoEPPLawQdysBsM6RtZ7RUZgjtYJJCuRIUBgAbr58Lff7+4YpIMND4GZFXohuC2GaF8DYtDg7qN3B0GdBxFB8eD0vd2QNoB2QcIKWgtme/n8OR0gMkhatGEJ3o14X3w3/bvH73wGn5QPG0I/eUWW3GhvsTg408kK9wVZeciHpaC60K9DS0WCrByacw5SF6ROD1da1VcXwgaLlDBGSq9/RuoSqjogf7Eh9GCcBJYpq/qCSNwWdrwshr8GA93Yw9XZEGDxe8jeb0OQ4gcYY7N3iBdEBtCaSG4VVh4UVgludJ51jwjY6d7XQ3ALSUGLDP0dDD66Re8t8qR/OVYI73PJtxMJP0wkn+sxhpPI/4EpZtCCXSxUYcEeBB4R5INq3ENumL8GC9xHNjhKIHAUuefP1/HivRK91+jPaRxCNxX9P+6U3i3K7jT3ulcXMIRUVr3hD/le3HDDCsbK4PyiGOLb+py+N4NnaH7oqXKoazClz0OByD4YDk/fJQ1g3g7XXwcD5B6Gg/YwwJG8tuPQQTwA3FsuVMFg6ndvwMABQ9bB1HCC77RCIDoMCog/eCGE5oQN42Y6GWYMNOk9/D/Iw2HcglK4tQOlhSkFXhB9iHAYpSViAzgzDTTQCj/coJAEQBtDET8sXAZWfhdmmIkfAlqDL7IEBsy3Hng89B+x5H5NRYhquVYFbdlCJ8BM6+6e/ZDz4SsobDKkxW3R9+5+6Ip827X+MaQjlPFrT4Bj/NDwvzEOrOFFco862IrPJUz4BDwCCEbCrbe/3Nvzvf9/yPL6h43Aj39vr3BruMfvPfeKBFWVl68oem+K7z3xBeYKCmMkzEE59MdPQxJ+uqfZp0eaffo+zb5DvxvrFfl7En4H8QjtVwR/wV6w4ZEYOmCI3ccHGoT7NDM+kcPTz6kKvnr6EQ5DuYMl2O4/us47CWw9fgH8gfjehcqhebWwX96K362LfETDI1dgwUj9oWWW2Tc5POg0+Pbuuo8iDR+lQ/l3h6HPB8OmKB7EL8HTa1rH8fNTaiXgr26GhmIMgxZaZNhHQfvDQaoKwe3qY6gaLr7fDN5SC9YEN3sdMgw2PjgAPyMfs+wz8r67uG3a0hpur34Z5uiBJSSFfz5oP3aaNniCe7qqzwfp71umYXx7jNV/FGJILCixA4bWnn1k6sDxDyDwi++D4o8gyu2LFT/KBazoQ+2GXfqR5CWU04Uj1jMC/QeTD+YTDNYaLvgjG8inAJcaNmh3UPer/b6qld11+f1mhuq+7/zt6b1sDN/v08I9doZt6t+b6wbDvvfjtwHeGkBu09fNzrfp9Q3qGA5995tH/jBEvN0D8ukVVh7w/DRYswjhSH69bbif7jJBZb7OvRAB1pBP5TBHoDCfIBLs7vmgCGx87jcMhtuhe6Mfvrz+2bD8F4rBK425HkGOCZeZkjhGWDQ1tW3btUh7QlhT4JEW7lqYg03gM9y2bMymAYaBqcNY47FHU1CUwaeJ9RAFxQdvQCU+TP4/HOOf7iiwj4wpGsKQHiBcEp86FEWP6SlOu2PcJRhyjBNjwvYmDu5hgCKBNcUJ0plOPcxzxi5sX2PaxW2GGPAeI+RdtLf3cf3dP/fKcBMjHAQfW5YzcRicdKeMRTuAwGzCAThkyxAAo6aEN5kAEq7/WPrw0eDCu/ZDDMPpEc5uzcDnt4fPh7ikSUi5JMsVe/9w6FSz6DFpd91pdKWBYafUbg/r05kJ4EyuzufzeMw7e2UlljKbnQx+CZaUcBBT76QUC1UX1tyyn22TvXdxa9DL1aJPNzJrlGeiSvn4WlQTyqRMdb4agwm5aWb7spja8oo/Npoblyep1haX8+ZaXp2wMMaTed05hBFdTlLKlZITNvoGRb1VAfpsczwJkaxIc4GcY7qfAMbObKm6+FxhTad9V9WbFA9m9Kk+cBxxDK8GSBYaaSj9OgpG5rHEq+1eCrEjn1HLjFLSQ48qaU5PlLSRrjE9qRs/MC+TMXtuNyuMn1uMrMaHHVPFK03q6lx3crHJd9TWkZtZqeKX3VggMqqvrY6svGYjWNRZ9FdrTimO+Pq0GkundaCftmt7T9gbfT0+wOGUrjbnaL44zvd1wBuHrkrwC3/ADCbeFAxvXxSD1H28t4sIYMqovdrHDKyFjZbFR02N820pXkGeivFmLPRrw8GjnV0WIr67CJvW3W8IvTvXdZq3E44aB/OmLGhh4WoyayrTo8w1uihruW1U0mFfzSRmSwdqb593sdHY0yCodNzjlWN9uARJ6KOV3xtxORuPragrZnSLlWlo5Y6/5PpmmoWqmOs5peM8RUgcVMjviG2tLKIFHk57aWdTk3ixrScOJyZz2sTtUc3gi2RDOB2Y45oTbbom5GNrTJTTa5OpkU6W7Yq+VBwzd+YxsGxX1UfLcEbhmpvv1rox6mPU9VcS3E30lxxSHjQhRU3sWM8Oy3Cz6g+leT0reycKYu3KievjaFZO0WmK4WZXRfto7F21DSN5J8ZIDnN+JgR7ep6aepLEC+oQ47NDivMH77zGk0PJXN1k2bteTEoyeY1oeTnZbcvtpjqw+vziTXiD6pQGjYNRwIlZ26ijyl363IFnpkHfEarVu2Km72fr0TJ3w8NRXU9NWQkpIlwYJYnzfWuFa9acHNiVFooGq+mpto/dXRBfL9vWlebSap2Ls+NCHXtsnmTyAbPYRlvsA06VhcZaEQa1Co9husDUk7xw1c6peqvUzR2QM7IyxCbQjOUJrRpekplwcVor+30nns+TPbUehaQJrjZIpEMuXdcpWFPrEzAnMalGXuiQ8qgXSuaI0s2ELTL5LAbU+sKOxF7kvYl4WjBl2fmb9cJW2n3hbazZrNqOl4FpjbkrXu/n8y16kIirE5fmaHJh+gM9tiNOtGJ7JwgzwK741VonTx7eHbeEKLkEJx/S03XUQXsczVMUqM4mDuaFBvBV4dBAraOTvPcme7I9aqnWHEVJnK018uRUG1rYHXH64GbNPNrsuJVqFJddOYqK/kybWF2bIN+vm815ySyvecYLDOd6J3MtreJGOmD+IRdwTcu5+oTGEyPFY6yloDXiqt2VNROf+AusHCnPuatku98wfCKlziRmTpJEXrxivSoEtBHK6LwmtXFY72fZJGC2J1zHE1EtoohWk4N8FKfpYkTsAmNndQ7J9UW6ChvWjWuq5jx14+LjxpoSzA5Q/LzG0JG0bFEg+Ev9wFSrVRn3ftJVtnxolYynJypf1LugGO8y7MRe65PgXLik68YzyjC0ZhHkQl+f89HIWAZnudQvzqVEl1dUTorx1txlBmPr0VRTbdpeoRt202Y5K/ZZdQ5PHq1wgWSzZb1c+LvFMZdmQrUhbZ1t8GaTdsVZWos700ogI9/UL5x72Cxtjbs2Bynb7UmNjaJVWVamOF9oTNASy2WwOF8v+Ul3Z1lfbY0COhpWqD1+rcxeLQq5SakxaE4BpYZX1QrPVQaaekoI8TKz0KNxsphUIIX55TzlrrvuOi12cux2zHyabdgV8Pi2J53tkrY8D01POHC2UkPHfLdHN3re4iNqYoy7FbtxfRXLs/1WESg8252kQttfTJzPQ5sZy8U1XrC7CRufF4VyunBe51zGcn04BtyhKblaDdfiahH0gM1AGkiScm3T9oxleTZxjytBrBf8CedENMPmgqsc2/FipIJ1Kl6WhHUdEXJvaLhYmnvBifi6lSzydLAYrDZlnQqtNUdTY7hd8DW+CdvOzxOB8fanazrbT5aW28bTi2JrWmBQQWp5Wt1fqUpJ60NYteZmHVGT1JbsvVsddpS35vxwsb8cS0uXYjHyYLU9uP5E3Gub0bVC50Yr1EbnwPLmCZU60usaxi8tUivYgbPVuaflETGqWNLkQ3rH701mlZSy0C+F5U7uR6WFhicnmXMEWZ0ra9JhNFeKrW9U1IU0yBosJuxejq4lHxy7/Tbj1OCsmebaU/0CWkNx8bNOTrZ4YGUHWpPObjOqxGOiqeU8vYDFqTbZXA9DFU3Q7YwqcYFaOgu1iiLWYTbzFC9iNwhc7szIc7zpuUyCkGhxkGSJa1JcXoeL8eZonyjMBtME0MX5fCyOPb81G3N5DI+FfJW7i9wu1XqK5+VUx5m8nwdOXF/6YtbQsrDequf1bO7m46UkJWLKcttcYPXl9uLn1xCczkt5Xie818ars7bvNmstjNdRcVhpBLvjGvrse9sozu2RIMTSfBGVtI1OO8tQtotiea2Wq5kxVVtuTzZr3JiRSibRCfTnJnXMyWS6xdBDzFB6K4miFruczTISxzC1Ks4wtT6tqfEaiCmPX0aNJlo2UfblvJPS40ir6qvTS+RVCmcCZnKoRbfaomZbtV20LT4t1ye2CcA8QEuhj8crc79YjfbxyE3z6+4QnZI5E5KspkbxRnMrbAR2E7LbCZpmx5t9fWV3DkNTwGLNLGOc2poT19gJ8iByalzvKM/YJKxv8qMFQ1bHvafmaqskK9roT2FSBFtRUrQVpu/8K3VydcNMV7s84CjrzNJmtUaFxWh/7uGQgQpxQh6s3RYHR7RszS7fHELedcY4aTQnU2lHtaUHh4iXjqK85aWYZIw23K00akU7jLjz0VAUUYqbOyONizdbZmlyEdvYEamai5VnWsaZ0EsRs5hDIuBrwsqIXNb1eNeAbjUawzEgV09apegXUkyj2p4IZkifIm991Wden3KmsFKC5U7x0lSteWtJgr40em+Vn1jc19wJTV/WRe4eXcyfhgxQFByvg33YrYmkCpWWUUi7J+RJztpUfjjvUXMsqQG+Oh6CYOFlO+VYHtZLbUvtJB1Tzxe9yk19Je7ia5WyG2PObWtUsfa7JnEX1ankrnmopAZJktpyz+8O1uRi7YO1wIEwtPw1xhcy6woZtjgzeiCd5SkXH0wvCch9d9wkMX8+46Ii0VV+Ma8uiZrVUZntY+lQ5lN/Ex0F/GxsRd6wjUhurGQfGC1DqlI3VTCiMiiZoWTPoZsZJxvTUWpQm810owg1ja30UcXNjiQu+HO+PTKxdbwsVVnLsFks1wx7lJa1ZAKnT69jBZOUKNGIilpQa5wpaes4W3ALsNzyzlS+zhmrp4Iko6cN6ROJjmGnhc21+5FfKl3UorHRaeOavgQyZowyiz3UALug50hmz7Xsh1cTaHWwnrPcspA431iK/pFSBKexN+1o0c2ztR8sRuCiL5q9G41gj8NPFLNn62xqak24nol5FCnTyufOJumIeyPtRw7KB1gfzSpu3ROoIAvjtFTyURyYYhsJl/ZCeWluzZnV0j24CmO1rgxkIjrGseqtaSnj8s6hTRJTYYw65GYnrcstHVOlPZkoWq0pc0Dp5HbBqGq/JWLLtYkaV6Y9KoM2RcFphmopEdWjvmF8g6k7N95hY7eyFqO+TbjLPmYqvJKV6rhVzvRRi5cqBR1f+I6ubx3coSpuQkUyLuAqtUXF0y6UoxWe4yE4bhTR65pVWrDsmLcEVZs32/Ya7micKAx2TnT2ZQoHxzlaEIp90owVemBoTJm1NK2MZ5HHLPSxU1+7cs2bhDkmiuNMN7YTmo9q1b6IzYlul9l0ckIZu2BQf0biepQTFopeliMlPVceoBnGgsnKXukjNTp2MjNzD7y+3B2BlkuiKZR7qLi6YFZlPmm39EHNBAWl0lges1y6PKQJ3C5u2+3GIGbVvLsuqfLa0kwyPmwY99rUbrhbUO5cp3B5GRks3cvk7Awj+NCfUyCUWCD5xVkTEkNDd0Q8ks1xZzp8P2ec4HD2R0SJbZeOFhwxvenguLrsobhkcRanLDDruNRg7hFjofbGu6mLzfjMxKq1v70etXPU0V139pj4sr2a2kJEaRxNZ1knjs7JqA11dl/3Qa+jIUkvq3SLLQ+S6jb61C1nBj6TDX2aSjbsHo19NWT6EnE906KC4cKJPz51U6KH8/r6smK3hM5Q0wXnOata6+ZRNeVXShYDc5np4XRuV/loCVRB4quZ4TWr2iy8o0YkI6deMdslu4Q7aECW4dKvcZrVocIkw2HSfsQRig7WJT2azKhswVVZur0o175Qr6jOd9RkGp+dbkTyuLGIKwWv3c4aU8Z8PqOiXCgwOFJZxDr2J+eF0PGzY+FdQbBLj7Yc6gCNVvQenJO2oM4uKZcdAU62NK+PYzSt1nIYRWtLFPPZ2O7KsV6zl+AQ4GASoXy96040GTXZuAZEtSAce45tnGxUznwbxbpp0bXzgJ8xFGpct0a9ypVx55HT2gyJNCybvc468twf4wKzihxbieXraXTQZQWTT9VoM88Meoof9SikGN8ly6UfXVmBV2enceprVFp1WcSGvkdSI01ckda69JYZ4Zz7gs7TSrB5dyrVnVwLu8mK8cx4rh688dRGNyU3Gbvm1CcOTdNwetoSYXslPOJ6OW434klqTDwSCZ1Op6euokNsG9K5XY5GNDMn9GAKN3duU40iFF3bC3SxIwi3Taa4SExnvrdKJiusm8kKl2OXzVRAtx5+9Q3Nq1eYrRZMLG4bqxm1jJpbPJvvl7iLbqOoMTYrY084ntrTeHRd22igAEbOFOxqbzDOmuxWogYYgjUxMG6O/ILnrTjkFdrSuPx6XF21fVbRC4rf6uOEwTFiI7VRT8yzhbBeuuNt4EwPHcPx7cRZjg9HnNSICZ86is9q9urUM9hsb7Skq17QDXCqOjErXlkq6noWUccqk9c8saatqdsf1y4D8k6biuEUG/ezhmhU7jQzCamZeSeYXeUuiWkm6g6MJAKayJSTV5rHVJldOIOYa4KYYQJkoHlJyvmE1hB+XaIWlfqTNsdLxWPRnXAGIh6TOyM85GK2Z1ObkmfLkXqGGz2hnmAjShczFJCXa6LsMJIwr3g/Ph0nIx/FF7jcwD0ny7I///z0/HR71fv0imM0gz8/Da8DHof6f/842L+G+dsDj2DGEO5/74Tyflr4/urvdsQPLPf1xv3174r66/NT4YRQrPsxchnX/uNo8r+cx376ayfFA0Z/f3c9vK3sqvf3I5Xl346zw9Sty6ro38osrm+H2dDwdTn8P5by7fFi4emmYJIPbyneFXr6OAB/q7KB0AuHx2E6vIEDbmhV4HHpP87/n5/cHjowdMo3gqbeQJEP2j7eQw0Ht8OLqKff/z+2bHBtrScAAA== -->
