import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import check_near_duplicates as rc  # noqa: E402


def entry(name, description, tags=(), display_name="", **extra):
    return {"name": name, "description": description, "tags": list(tags),
            "display_name": display_name or name.split("/")[-1].replace("_", " ").title(), **extra}


REGISTRY = [
    entry("@kody-w/copilot_studio_deploy_agent",
          "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, the pac CLI, "
          "the maker portal, and the solution zip.", ["copilot-studio", "deploy", "dataverse"]),
    entry("@kody-w/copilot_studio_probe_agent",
          "Sends a message to a deployed Copilot Studio agent over Direct Line and returns the bot's reply.",
          ["copilot-studio", "probe", "directline"]),
    entry("@kody-w/hacker_news_agent", "Top stories from Hacker News via the public Firebase API.", ["news"]),
    entry("@aibast/account_intelligence_agent", "Account intelligence for B2B sales.", ["sales"],
          _file="agents/@aibast/b2b_sales_stacks/account_intelligence_stack/account_intelligence_agent.py"),
    entry("@aibast/account_intelligence_orchestrator_agent", "Orchestrates the account intelligence stack agents.", ["sales"],
          _file="agents/@aibast/b2b_sales_stacks/account_intelligence_stack/account_intelligence_orchestrator_agent.py"),
]


def rhymes_with(manifest, registry=REGISTRY):
    p = rc.profile(manifest)
    out = []
    for q in registry:
        r = rc.rhyme(p, rc.profile(q))
        if r:
            out.append((q["name"], rc.declared(p, rc.profile(q))))
    return out


def test_tokens_drop_stopwords_and_short_words():
    assert rc.tokens("The agent uses a RAPP CLI to deploy it") == {"cli", "deploy"}


def test_rhyme_by_slug_tokens():
    m = entry("@someone/copilot_studio_parity_deploy",
              "Compiles caller-selected local agents into a provisioned, parity-tested solution.", ["parity"])
    names = [n for n, _ in rhymes_with(m)]
    assert "@kody-w/copilot_studio_deploy_agent" in names
    assert "@kody-w/hacker_news_agent" not in names


def test_rhyme_by_description_tokens():
    m = entry("@someone/dataverse_pusher",
              "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, pac CLI, "
              "maker portal, solution zip.", ["copilot-studio", "deploy", "dataverse"])
    assert [n for n, _ in rhymes_with(m)] == ["@kody-w/copilot_studio_deploy_agent"]


def test_unrelated_agent_does_not_rhyme():
    m = entry("@someone/weather_agent", "Current weather and a three day forecast for a city.", ["weather"])
    assert rhymes_with(m) == []


def test_self_is_never_a_rhyme():
    assert rhymes_with(REGISTRY[0]) == [] or all(n != REGISTRY[0]["name"] for n, _ in rhymes_with(REGISTRY[0]))


def test_distinct_from_clears_only_with_a_real_reason():
    base = entry("@someone/copilot_studio_parity_deploy", "Compiles agents into a parity-tested solution.", ["parity"])
    undeclared = rhymes_with(base)
    assert undeclared and all(why is None for _, why in undeclared)
    short = dict(base, distinct_from={"@kody-w/copilot_studio_deploy_agent": "diff"})
    assert all(why is None for _, why in rhymes_with(short))
    good = dict(base, distinct_from={"@kody-w/copilot_studio_deploy_agent":
                                     "deploy pushes an existing zip; this one compiles agents and tests parity"})
    assert all(why and why.startswith("distinct_from") for _, why in rhymes_with(good))


def test_supersedes_clears():
    m = entry("@kody-w/copilot_studio_deploy_v2", "Deploys Copilot Studio agents into Dataverse.", ["deploy"],
              supersedes=["@kody-w/copilot_studio_deploy_agent"])
    assert ("@kody-w/copilot_studio_deploy_agent", "supersedes @kody-w/copilot_studio_deploy_agent") in rhymes_with(m)


def test_dependencies_and_same_stack_are_designed_together():
    m = entry("@kody-w/copilot_studio_deploy_helper", "Helper for the Copilot Studio deploy agent.", ["deploy"],
              dependencies=["@kody-w/copilot_studio_deploy_agent"])
    assert ("@kody-w/copilot_studio_deploy_agent", "designed together (dependencies)") in rhymes_with(m)
    m = entry("@aibast/account_intelligence_scoring_agent", "Scores accounts for the account intelligence stack.", ["sales"],
              _file="agents/@aibast/b2b_sales_stacks/account_intelligence_stack/account_intelligence_scoring_agent.py")
    assert all(why and why.startswith("same stack") for _, why in rhymes_with(m))


def test_aggregated_family_is_designed_together():
    reg = REGISTRY + [entry("@cowork-cookbook/inventory_heatmap", "Generates a 3D HTML heatmap of warehouse bins.", ["dashboard"],
                            source={"aggregated": True, "source_id": "cowork-cookbook"})]
    m = entry("@cowork-cookbook/inventory_heatmap_by_value", "Generates a 3D HTML heatmap of warehouse bins by value.", ["dashboard"],
              source={"aggregated": True, "source_id": "cowork-cookbook"})
    hits = rhymes_with(m, reg)
    assert hits and all(why == "same aggregated library @cowork-cookbook" for _, why in hits)
    stranger = entry("@someone/inventory_heatmap_clone", "Generates a 3D HTML heatmap of warehouse bins.", ["dashboard"])
    assert any(why is None for _, why in rhymes_with(stranger, reg))


def test_aggregated_mirror_rhyming_across_libraries_warns_instead_of_blocking(tmp_path):
    root, base = _repo(tmp_path, REGISTRY)
    (root / "agents" / "@cowork-cookbook").mkdir()
    (root / "agents" / "@cowork-cookbook" / "copilot_studio_deploy_recipe_agent.py").write_text(
        '__manifest__ = {\n    "schema": "rapp-agent/1.0",\n    "name": "@cowork-cookbook/copilot_studio_deploy_recipe",\n'
        '    "version": "3.0.0",\n    "display_name": "X",\n'
        '    "description": "Deploys Copilot Studio agents into Dataverse via pac CLI and solution zip.",\n'
        '    "author": "t",\n    "tags": ["copilot-studio", "deploy", "dataverse"],\n    "category": "devtools",\n'
        '    "source": {"aggregated": True, "source_id": "cowork-cookbook"},\n}\nclass X:\n    def perform(self, **kw):\n        return "x"\n')
    _git(root, "add", "."); _git(root, "commit", "-q", "-m", "mirror")
    code, doc = rc.gate(root, base, REGISTRY)
    assert code == 0 and not doc["findings"]
    assert [w["rhymes_with"] for w in doc["warnings"]] == ["@kody-w/copilot_studio_deploy_agent"]


def test_report_clusters_the_family():
    doc = rc.report(REGISTRY)
    assert doc["agents"] == len(REGISTRY)
    assert doc["clusters"] == 1
    assert doc["cluster_list"][0]["members"] == ["@kody-w/copilot_studio_deploy_agent", "@kody-w/copilot_studio_probe_agent"]
    assert doc["by_publisher"] == {"@kody-w": 2}


def _git(root, *args):
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)


def _repo(tmp_path, registry):
    root = tmp_path / "repo"
    (root / "agents" / "@t").mkdir(parents=True)
    (root / "registry.json").write_text(json.dumps({"agents": registry}))
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "t@t")
    _git(root, "config", "user.name", "t")
    (root / "README.md").write_text("x")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "base")
    base = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return root, base


def _agent(root, slug, manifest_extra=""):
    (root / "agents" / "@t" / f"{slug}.py").write_text(
        '__manifest__ = {\n    "schema": "rapp-agent/1.0",\n    "name": "@t/%s",\n    "version": "1.0.0",\n'
        '    "display_name": "X",\n    "description": "Deploys Copilot Studio agents into Dataverse via pac CLI and solution zip.",\n'
        '    "author": "t",\n    "tags": ["copilot-studio", "deploy", "dataverse"],\n    "category": "devtools",\n%s}\n'
        'class X:\n    def perform(self, **kw):\n        return "x"\n' % (slug, manifest_extra))
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "add " + slug)


def test_gate_blocks_undeclared_rhyme_and_prints_the_fix(tmp_path):
    root, base = _repo(tmp_path, REGISTRY)
    _agent(root, "copilot_studio_deploy_again")
    code, doc = rc.gate(root, base, REGISTRY)
    assert code == 1
    assert doc["checked"] == ["@t/copilot_studio_deploy_again"]
    assert [f["rhymes_with"] for f in doc["findings"]] == ["@kody-w/copilot_studio_deploy_agent"]
    out = subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "check_near_duplicates.py"), "--base", base,
                          "--repo-root", str(root)], capture_output=True, text=True)
    assert out.returncode == 1
    assert '"supersedes": ["@kody-w/copilot_studio_deploy_agent"]' in out.stdout
    assert "FAIL 1 undeclared rhyme" in out.stdout


def test_gate_passes_declared_rhyme_and_unknown_supersedes_is_an_error(tmp_path):
    root, base = _repo(tmp_path, REGISTRY)
    _agent(root, "copilot_studio_deploy_again",
           '    "supersedes": ["@kody-w/copilot_studio_deploy_agent"],\n')
    code, doc = rc.gate(root, base, REGISTRY)
    assert code == 0 and doc["cleared"] and not doc["findings"]
    _agent(root, "copilot_studio_deploy_third", '    "supersedes": ["@kody-w/does_not_exist"],\n')
    code, doc = rc.gate(root, base, REGISTRY)
    assert code == 1
    assert any("unknown agent" in f.get("error", "") for f in doc["findings"])


def test_gate_ignores_pushes_without_agent_changes(tmp_path):
    root, base = _repo(tmp_path, REGISTRY)
    (root / "README.md").write_text("y")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "docs")
    code, doc = rc.gate(root, base, REGISTRY)
    assert (code, doc["checked"], doc["findings"]) == (0, [], [])


def test_live_registry_report_runs():
    reg = rc.load_registry(REPO_ROOT / "registry.json")
    doc = rc.report(reg)
    assert doc["agents"] == len(reg)
    assert doc["thresholds"]["name"] == rc.NAME_THRESHOLD
