#!/usr/bin/env python3
"""RAPP Foundation SDK — Build agents, mint cards, track Binders. The open developer toolkit for the RAPP agent ecosystem."""

from __future__ import annotations

__version__ = "1.0.0"

# =============================================================================
# SECTION 1: CONSTANTS + CONFIG
# =============================================================================

import ast
import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]

VALID_CATEGORIES = [
    "core", "pipeline", "integrations", "productivity", "devtools", "general",
    "b2b_sales", "b2c_sales", "healthcare", "financial_services", "manufacturing",
    "energy", "federal_government", "slg_government", "human_resources",
    "it_management", "professional_services", "retail_cpg", "software_digital_products",
]

VALID_TIERS = ["experimental", "community", "verified", "official"]
SUBMITTABLE_TIERS = ["experimental", "community"]

REPO = "kody-w/RAR"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"
API_BASE = f"https://api.github.com/repos/{REPO}"

TIER_TO_RARITY = {
    "official": "mythic",
    "verified": "rare",
    "community": "core",
    "experimental": "starter",
}

RARITY_LABELS = {
    "mythic": "Legendary",
    "rare": "Elite",
    "core": "Core",
    "starter": "Starter",
}

RARITY_FLOOR = {
    "mythic": 200,
    "rare": 100,
    "core": 40,
    "starter": 10,
}

# Agent scaffold template — uses __TOKEN__ placeholders to avoid brace conflicts
AGENT_TEMPLATE = '''\
"""__DESCRIPTION__"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "__NAME__",
    "version": "1.0.0",
    "display_name": "__DISPLAY_NAME__",
    "description": "__DESCRIPTION__",
    "author": "__AUTHOR__",
    "tags": [],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}

from agents.basic_agent import BasicAgent


class __CLASS_NAME__(BasicAgent):
    def __init__(self):
        self.name = "__DISPLAY_NAME__"
        self.metadata = {
            "description": "__DESCRIPTION__",
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        task = kwargs.get("task", "default")
        return f"__DISPLAY_NAME__ performed: {task}"


if __name__ == "__main__":
    agent = __CLASS_NAME__()
    print(agent.perform())
'''


# =============================================================================
# SECTION 2: MANIFEST OPERATIONS
# =============================================================================

def extract_manifest(path: str) -> dict | None:
    """Extract __manifest__ dict from a Python file using AST parsing (no code execution)."""
    try:
        source = Path(path).read_text()
        tree = ast.parse(source)
    except (SyntaxError, OSError) as e:
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__manifest__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


def validate_manifest(path: str, manifest: dict = None) -> list[str]:
    """Validate a manifest and return a list of error strings. Extracts manifest if not provided."""
    errors = []

    if manifest is None:
        manifest = extract_manifest(path)
        if manifest is None:
            return ["No __manifest__ dict found in file"]

    # Required fields
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    # Name format: @publisher/slug
    name = manifest.get("name", "")
    if not name.startswith("@") or "/" not in name:
        errors.append(f"Invalid name format '{name}' — must be @publisher/slug")

    # Semver
    version = manifest.get("version", "")
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        errors.append(f"Invalid version '{version}' — must be semver (e.g., 1.0.0)")

    # Tags must be a list
    if not isinstance(manifest.get("tags", []), list):
        errors.append("tags must be a list")

    # Category
    category = manifest.get("category", "")
    if category and category not in VALID_CATEGORIES:
        errors.append(f"Invalid category '{category}' — must be one of: {', '.join(VALID_CATEGORIES)}")

    # Tier
    tier = manifest.get("quality_tier", "community")
    if tier not in VALID_TIERS:
        errors.append(f"Invalid quality_tier '{tier}' — must be one of: {', '.join(VALID_TIERS)}")

    return errors


def extract_card(path: str) -> dict | None:
    """Extract __card__ dict from a Python file using AST parsing."""
    try:
        source = Path(path).read_text()
        tree = ast.parse(source)
    except (SyntaxError, OSError):
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__card__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


# =============================================================================
# SECTION 3: CONTRACT TESTING (no pytest dependency)
# =============================================================================

def run_contract_tests(path: str) -> list[tuple[str, bool, str]]:
    """
    Run the RAPP agent contract test suite against a single agent file.
    Returns a list of (test_name, passed, message) tuples.
    """
    results = []
    agent_path = Path(path)

    def record(name, passed, msg):
        results.append((name, passed, msg))

    # 1. has_manifest
    try:
        manifest = extract_manifest(path)
        if manifest is not None:
            record("has_manifest", True, "__manifest__ dict found")
        else:
            record("has_manifest", False, "No __manifest__ dict in file")
            manifest = {}
    except Exception as e:
        record("has_manifest", False, f"Error reading manifest: {e}")
        manifest = {}

    # 2. manifest_fields
    try:
        missing = [f for f in REQUIRED_MANIFEST_FIELDS if f not in manifest]
        if not missing:
            record("manifest_fields", True, "All required fields present")
        else:
            record("manifest_fields", False, f"Missing fields: {', '.join(missing)}")
    except Exception as e:
        record("manifest_fields", False, f"Error: {e}")

    # 3. name_format
    try:
        name = manifest.get("name", "")
        if name.startswith("@") and "/" in name:
            record("name_format", True, f"Name '{name}' is valid @publisher/slug format")
        else:
            record("name_format", False, f"Name '{name}' must be @publisher/slug format")
    except Exception as e:
        record("name_format", False, f"Error: {e}")

    # 4. has_basic_agent (uses importlib to check class inheritance)
    agent_module = None
    agent_class = None
    try:
        # Add known BasicAgent locations to sys.path
        rapp_dir = str(agent_path.parent.parent / "@rapp")
        templates_dir = str(
            agent_path.parent.parent.parent
            / "agents"
            / "@aibast-agents-library"
            / "templates"
        )
        for extra in [rapp_dir, templates_dir, str(agent_path.parent.parent)]:
            if extra not in sys.path and Path(extra).exists():
                sys.path.insert(0, extra)

        # Also try adding the project root so `from agents.basic_agent import BasicAgent` works
        project_root = str(agent_path.parent.parent.parent)
        if project_root not in sys.path:
            sys.path.insert(0, project_root)

        spec = importlib.util.spec_from_file_location("_rapp_test_agent_", str(agent_path))
        agent_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(agent_module)

        # Find class that inherits BasicAgent
        import inspect
        found = False
        for obj_name, obj in inspect.getmembers(agent_module, inspect.isclass):
            bases = [b.__name__ for b in obj.__mro__]
            if "BasicAgent" in bases and obj.__name__ != "BasicAgent":
                agent_class = obj
                found = True
                break
        if found:
            record("has_basic_agent", True, f"Class '{agent_class.__name__}' inherits BasicAgent")
        else:
            record("has_basic_agent", False, "No class inheriting BasicAgent found")
    except Exception as e:
        record("has_basic_agent", False, f"Import error: {e}")

    # 5. instantiation
    agent_instance = None
    try:
        if agent_class is not None:
            agent_instance = agent_class()
            record("instantiation", True, f"{agent_class.__name__}() succeeded")
        else:
            record("instantiation", False, "Skipped — no agent class found")
    except Exception as e:
        record("instantiation", False, f"Instantiation failed: {e}")

    # 6. perform_returns_str
    try:
        if agent_instance is not None:
            result = agent_instance.perform()
            if isinstance(result, str):
                record("perform_returns_str", True, f"perform() returned str ({len(result)} chars)")
            else:
                record("perform_returns_str", False, f"perform() returned {type(result).__name__}, expected str")
        else:
            record("perform_returns_str", False, "Skipped — no agent instance")
    except Exception as e:
        record("perform_returns_str", False, f"perform() raised: {e}")

    # 7. standalone_execution
    try:
        proc = subprocess.run(
            [sys.executable, str(agent_path)],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if proc.returncode == 0:
            record("standalone_execution", True, "python agent.py exited 0")
        else:
            record("standalone_execution", False, f"Exited {proc.returncode}: {proc.stderr.strip()[:120]}")
    except subprocess.TimeoutExpired:
        record("standalone_execution", False, "Timed out after 15 seconds")
    except Exception as e:
        record("standalone_execution", False, f"Error: {e}")

    # 8. has_docstring
    try:
        if agent_module is not None:
            doc = getattr(agent_module, "__doc__", None)
            if doc and doc.strip():
                record("has_docstring", True, f"Module docstring present ({len(doc.strip())} chars)")
            else:
                record("has_docstring", False, "Module docstring missing or empty")
        else:
            source = agent_path.read_text()
            tree = ast.parse(source)
            doc = ast.get_docstring(tree)
            if doc:
                record("has_docstring", True, "Module docstring present (parsed via AST)")
            else:
                record("has_docstring", False, "Module docstring missing")
    except Exception as e:
        record("has_docstring", False, f"Error: {e}")

    # 9. no_hardcoded_secrets
    try:
        source = agent_path.read_text()
        suspicious_patterns = [
            'API_KEY = "sk-',
            "API_KEY = 'sk-",
            'password = "',
            "password = '",
            'token = "',
            "token = '",
            'secret = "',
            "secret = '",
            'api_key = "',
            "api_key = '",
        ]
        found_patterns = [p for p in suspicious_patterns if p in source]
        if not found_patterns:
            record("no_hardcoded_secrets", True, "No hardcoded secret patterns detected")
        else:
            record("no_hardcoded_secrets", False, f"Suspicious patterns found: {found_patterns}")
    except Exception as e:
        record("no_hardcoded_secrets", False, f"Error scanning source: {e}")

    return results


# =============================================================================
# SECTION 4: REGISTRY CLIENT
# =============================================================================

def _get_token() -> str | None:
    """Get GitHub token from GITHUB_TOKEN env or gh CLI."""
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


def _fetch_json(url: str, token: str = None) -> dict | None:
    """Fetch JSON from a URL with optional GitHub auth header."""
    try:
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def fetch_registry() -> dict:
    """Fetch registry — prefers local file (local-first), falls back to GitHub."""
    # Local-first: use local registry.json if it exists
    local = Path(__file__).parent / "registry.json"
    if local.exists():
        try:
            return json.loads(local.read_text())
        except json.JSONDecodeError:
            pass

    # Fall back to remote
    url = f"{RAW_BASE}/registry.json"
    token = _get_token()
    data = _fetch_json(url, token)
    if data:
        return data

    return {"agents": [], "stats": {}}


def search_agents(query: str) -> list[dict]:
    """Text search across name, display_name, description, tags, author, category."""
    registry = fetch_registry()
    agents = registry.get("agents", [])
    q = query.lower()
    results = []
    for agent in agents:
        searchable = " ".join([
            agent.get("name", ""),
            agent.get("display_name", ""),
            agent.get("description", ""),
            agent.get("author", ""),
            agent.get("category", ""),
            " ".join(agent.get("tags", [])),
        ]).lower()
        if q in searchable:
            results.append(agent)
    return results


def get_agent_info(name: str) -> dict | None:
    """Find an agent by exact name in the registry."""
    registry = fetch_registry()
    for agent in registry.get("agents", []):
        if agent.get("name") == name:
            return agent
    return None


def install_agent(name: str, output_dir: str = "agents") -> str:
    """Download an agent .py file from GitHub and write it to disk. Returns the output path."""
    agent = get_agent_info(name)
    if agent is None:
        raise ValueError(f"Agent '{name}' not found in registry")

    file_path = agent.get("_file")
    if not file_path:
        raise ValueError(f"No _file path recorded for '{name}'")

    url = f"{RAW_BASE}/{file_path}"
    token = _get_token()
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode()
    except Exception as e:
        raise RuntimeError(f"Failed to download agent: {e}")

    # Reconstruct output path relative to output_dir
    parts = Path(file_path).parts  # e.g. agents/@kody/my_agent.py
    if parts[0] == "agents":
        parts = parts[1:]  # strip leading "agents/"
    dest = Path(output_dir) / Path(*parts)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    return str(dest)


# =============================================================================
# SECTION 5: CARD + BINDER OPERATIONS
# =============================================================================

def seed_hash(s: str) -> int:
    """Deterministic, reproducible hash for card generation."""
    h = 0
    for c in s:
        h = ((h << 5) - h + ord(c)) & 0xFFFFFFFF
    return h


def mulberry32(seed: int):
    """Return a callable PRNG producing 0.0–1.0 floats from a seed."""
    state = [seed & 0xFFFFFFFF]

    def _rand():
        state[0] = (state[0] + 0x6D2B79F5) & 0xFFFFFFFF
        z = state[0]
        z = ((z ^ (z >> 15)) * ((z | 1) & 0xFFFFFFFF)) & 0xFFFFFFFF
        z = ((z ^ (z >> 7)) * ((z | 61) & 0xFFFFFFFF)) & 0xFFFFFFFF
        z = (z ^ (z >> 14)) & 0xFFFFFFFF
        return z / 0xFFFFFFFF

    return _rand


# ─── SEED MNEMONIC (7 words = 64-bit seed, full fidelity, memorizable) ───
# 1024 words → 10 bits per word → 7 words = 70 bits (covers 64-bit seed)
# Say 7 words. The card appears. An incantation that summons an agent.
# DRAFT: word list will be curated for incantation feel before first public mnemonic.
# Once locked, the list is PERMANENT — changing it breaks all existing mnemonics.

MNEMONIC_WORDS = """FORGE ANVIL BLADE RUNE SHARD SMELT TEMPER WELD CHISEL BRAND MOLD CAST STAMP ETCH CARVE BIND FUSE ALLOY INGOT RIVET CLASP THORN BARB SPIKE PRONG EDGE HONE GRIND QUENCH SEAR HAMMER STOKE FIRE FROST STORM TIDE QUAKE GUST BOLT SURGE BLAZE EMBER PYRE ASH SMOKE SPARK FLARE FLASH FLOOD GALE DRIFT MIST HAZE VOID FLUX PULSE WAVE SHOCK BURST CRACK ROAR HOWL ECHO BOOM THUNDER VENOM BLIGHT SCORCH SINGE CHAR WITHER ERODE CORRODE DISSOLVE OAK PINE MOSS FERN ROOT VINE BLOOM SEED GROVE GLEN VALE CRAG PEAK RIDGE GORGE CLIFF SHORE REEF DUNE MARSH CAVE LAIR DEN NEST HIVE BURROW STONE IRON STEEL GOLD JADE ONYX RUBY OPAL AMBER PEARL CORAL QUARTZ OBSIDIAN FLINT GRANITE BASALT COBALT CHROME BRONZE COPPER NICKEL RELIC TOTEM SIGIL GLYPH WARD CHARM BANE DOOM FATE OMEN ORACLE SAGE SEER MAGE DRUID SHAMAN WRAITH SHADE PHANTOM SPECTER GOLEM TITAN DRAKE WYRM GRYPHON SPHINX HYDRA CHIMERA SCROLL TOME CODEX LORE MYTH FABLE SAGA EPIC VERSE CHANT HYMN DIRGE OATH CREED VOW AURA MANA ETHER PRISM NEXUS VORTEX RIFT WARP BREACH PORTAL GATE VAULT SHRINE ALTAR CRYPT SPIRE STRIKE SLASH THRUST PARRY GUARD SHIELD HELM LANCE MACE PIKE STAFF WAND DAGGER BOW ARROW QUIVER ARMOR PLATE GAUNTLET VISOR CLOAK CAPE MANTLE AEGIS BULWARK RAMPART BASTION CITADEL KEEP TOWER FORT RALLY CHARGE SIEGE FLANK AMBUSH ROUT VALOR MIGHT FURY WRATH RAGE SPITE MALICE GRUDGE HAVOC CHAOS DASH LEAP SPRINT LUNGE DIVE SOAR GLIDE PROWL STALK CREEP SWIFT FLEET BRISK RAPID SPIN WHIRL TWIST COIL SPIRAL ORBIT ARC CURVE BEND LOOP DAWN DUSK NOON NIGHT SHADOW GLEAM GLOW SHINE BEAM RAY HALO LUSTER MURK GLOOM DREAD FELL GRIM STARK BLEAK PALE ASHEN DIRE GRAVE SOMBER EBON ABYSS SHRIEK WAIL RUMBLE HISS GROWL SNARL BARK BELLOW DRONE CHIME TOLL KNELL CLANG CLASH SNAP THUD RING PEAL GONG HORN DRUM FLUTE LYRE PIPE BOLD KEEN FIERCE STERN VAST DEEP GRAND PRIME NOBLE ROYAL SACRED ANCIENT PRIMAL ELDER PURE VIVID SHARP BRIGHT DARK WILD CALM STILL SILENT STRONG PROUD BRAVE WISE JUST RAW DENSE SOLID WHOLE CORE APEX ZENITH NADIR CUSP BRINK VERGE CREST STAR MOON SUN COMET NOVA SOLAR LUNAR ASTRAL COSMIC NEBULA QUASAR PULSAR ECLIPSE AURORA CORONA PHASE WANE WAX WOLF HAWK EAGLE RAVEN SERPENT VIPER COBRA FALCON STAG BEAR LION TIGER LYNX PANTHER CONDOR OSPREY CRANE HERON OWL CROW BULL BOAR RAM HORSE MARE STALLION AX ORB AWE OAT EEL URN ELK ELM ION IRE ORE AIM ZAP JAB JAW JET JOT JAG HEX HEW HUE HUM DIN DUB DYE FIN FIG FOG FUR GAP GEM GNU SOUL MIND WILL FORCE POWER CRAFT SKILL GRACE POISE NERVE GRIT METTLE VIGOR ZEAL VERVE PLUCK GUILE CUNNING WILE LURE TRAP SNARE BAIT DECOY RUSE FEINT GAMBIT PLOY MESA TARN FORD PASS BLUFF KNOLL MOOR HEATH STEPPE TUNDRA DELTA BASIN PLATEAU FJORD ISLE ATOLL STRAIT CHANNEL HARBOR COVE BAY GULF SOUND CREEK BROOK RAPIDS FALLS CASCADE ARCH DOME PILLAR COLUMN BRIDGE WALL MOAT RAMP LEDGE STEP STAIR HALL NAVE ALCOVE NICHE SILL TRUSS BRACE STRUT JOIST FRAME PLINTH DAIS THRONE QUEST HUNT TRIAL ORDEAL RITE RITUAL PACT BOND PLEDGE DECREE EDICT MANDATE LAW RULE REIGN CROWN SCEPTER BANNER EMBLEM BADGE MARK SEAL TOKEN GUILD CLAN TRIBE ORDER SECT COVEN LEGION HORDE SWARM PACK FLOCK BROOD CLUTCH CRUX JINX GLINT DINT STINT KNIT SLIT SPLIT WHIT CLEFT DEFT HEFT LEFT THEFT WEFT BEREFT SHAFT GRAFT RAFT DRAFT TUFT LOFT CROFT DROIT BRUNT BLUNT STUNT RUNT GRUNT FRONT FONT HAUNT GAUNT FLAUNT JAUNT TAUNT SALT MALT HALT JOLT COLT MOLT SMOLT QUALM BALM PSALM FARM HARM ALARM DISARM FOREARM PLUME FUME LOOM ZOOM GROOM BROOM VROOM SCARCE TERSE MORSE COURSE SOURCE NORSE REMORSE WRENCH CLENCH STENCH TRENCH DRENCH FRENCH BENCH TORCH PORCH MARCH LARCH STARCH SEARCH PERCH BIRCH CHURCH THATCH CATCH MATCH BATCH HATCH LATCH PATCH WATCH SCRATCH SNATCH HEDGE WEDGE DREDGE SLEDGE FRIDGE DANCE TRANCE GLANCE STANCE PRANCE CHANCE ADVANCE ENHANCE BLISS MISS KISS DISMISS AMISS REMISS WHISK DISK RISK FRISK TUSK MUSK RUSK HUSK CROAK SOAK STROKE SPOKE BROKE WOKE INVOKE EVOKE PROVOKE VEIN CHAIN PLAIN STRAIN GRAIN TRAIN BRAIN DOMAIN TERRAIN REMAIN TREAD SPREAD THREAD SHRED BRED SLED STEAD INSTEAD COST LOST HOST GHOST MOST POST ROAST TOAST COAST BOAST STREAM DREAM TEAM CREAM SCHEME THEME SUPREME EXTREME SWAY FRAY PRAY STRAY ARRAY DECAY RELAY CONVEY OBEY SURVEY BETRAY THROW FLOW SNOW GROW KNOW BELOW HOLLOW CLIMB RHYME SLIME THYME SUBLIME PARADIGM PROWESS DURESS FORTRESS MISTRESS COMPASS BYPASS SURPASS AMASS CRIMSON LINDEN MAIDEN WARDEN GOLDEN MOLTEN FROZEN CHOSEN WOVEN SCYTHE CRUCIBLE TORRENT TEMPEST MAELSTROM CINDER INFERNO TYPHOON CYCLONE GLACIER ICECAP PERMAFROST MONSOON SOLSTICE EQUINOX MERIDIAN TWILIGHT MIDNIGHT DAYBREAK SENTINEL WATCHER HUNTER RANGER SCOUT TRACKER SEEKER FINDER KEEPER BINDER ARBITER HERALD ENVOY REGENT PREFECT CONSUL MARSHAL VASSAL SQUIRE KNIGHT PALADIN CHAMPION PARAGON MONARCH SOVEREIGN OVERLORD WARLORD CHIEFTAIN PATRIARCH MATRIARCH PROPHET MYSTIC HERMIT ASCETIC NOMAD PILGRIM WANDERER EXILE OUTCAST ROGUE REBEL VAGRANT DRIFTER MARAUDER BRIGAND CORSAIR BUCCANEER RAIDER REAVER SLAYER BERSERKER GLADIATOR CENTURION LEGIONNAIRE TEMPLAR CRUSADER INQUISITOR ZEALOT HARBINGER AUGUR PORTENT PRESAGE AUGURY PROPHECY DIVINATION REVELATION EPIPHANY REMNANT VESTIGE ARTIFACT FRAGMENT SPLINTER SLIVER MORSEL CRUMB PARTICLE MOTE FILAMENT STRAND FIBER SINEW TENDON LIGAMENT MARROW ICHOR ELIXIR POTION TONIC SALVE REMEDY ANTIDOTE CURE PANACEA CATALYST REAGENT COMPOUND TINCTURE DISTILL INFUSE IMBUE ENCHANT CONJURE SUMMON BANISH DISPEL REVOKE ANNUL NEGATE NULLIFY SUNDER CLEAVE REND SHATTER FRACTURE RUPTURE PIERCE IMPALE SKEWER GORE MAIM RAVAGE DEVASTATE OBLITERATE ANNIHILATE ERADICATE PURGE EXPUNGE EFFACE EXTINGUISH QUELL SUBDUE VANQUISH CONQUER PREVAIL TRIUMPH ASCEND TRANSCEND EVOLVE AWAKEN ARISE EMERGE MANIFEST EMBODY HARNESS WIELD MASTER COMMAND PROCLAIM SANCTIFY CONSECRATE ANOINT BESTOW ENDOW BEQUEST LEGACY HEIRLOOM COVENANT COMPACT TREATY ACCORD ALLIANCE FEDERATION DOMINION REALM KINGDOM EMPIRE DYNASTY EPOCH AEON CYCLE HELIX MATRIX LATTICE TAPESTRY MOSAIC CIPHER ENIGMA RIDDLE PUZZLE LABYRINTH MAZE CAULDRON CHALICE GOBLET GRAIL TRIDENT MAUL FLAIL HALBERD GLAIVE RAPIER SABRE KATANA MACHETE SCIMITAR CUTLASS BROADSWORD GREATSWORD LONGBOW CROSSBOW BALLISTA CATAPULT TREBUCHET MIRAGE ILLUSION REVENANT LICH BANSHEE GHOUL VAMPIRE WEREWOLF GARGOYLE BASILISK KRAKEN LEVIATHAN BEHEMOTH COLOSSUS JUGGERNAUT MONOLITH OBELISK ZIGGURAT MINARET PAGODA DOLMEN BARROW CATACOMB DUNGEON PARAPET TURRET BATTLEMENT DRAWBRIDGE PORTCULLIS BARBICAN PALISADE CONDUIT PYLON TORQUE RATCHET LODESTONE KEYSTONE CAPSTONE BEDROCK SEQUOIA REDWOOD CYPRESS HEMLOCK WILLOW ASPEN HICKORY JUNIPER MAGNOLIA HAWTHORN SAFFRON MYRRH MANGROVE ORCHID THISTLE POPPY HEATHER JASMINE VECTOR SCALAR TENSOR FULCRUM PIVOT CRESCENT PINNACLE VERTEX""".split()

# 10 bits per word, 7 words = 70 bits (covers 64-bit seed)
# The word list is the protocol. Once locked, it's PERMANENT.
# Future: locale-specific word lists map same indices to different languages.
_MNEM_BITS = 10
_MNEM_COUNT = 1 << _MNEM_BITS
assert len(MNEMONIC_WORDS) == _MNEM_COUNT, f"Need exactly {_MNEM_COUNT} words, have {len(MNEMONIC_WORDS)}"
_WORD_TO_IDX = {w: i for i, w in enumerate(MNEMONIC_WORDS)}


def seed_to_words(seed: int) -> str:
    """Encode a 64-bit seed as 7 memorable words. Full fidelity. Offline forever.
    This is the hero use case: memorize 7 words, reconstruct the exact card anywhere."""
    words = []
    remaining = seed
    for _ in range(7):
        idx = remaining & (_MNEM_COUNT - 1)
        words.append(MNEMONIC_WORDS[idx])
        remaining >>= _MNEM_BITS
    return " ".join(words)


def words_to_seed(mnemonic: str) -> int:
    """Decode 7 words back to a 64-bit seed. Lossless round-trip."""
    words = [w.strip().upper() for w in mnemonic.replace("-", " ").split()]
    if len(words) != 7:
        raise ValueError(f"Mnemonic must be 7 words, got {len(words)}")
    seed = 0
    for i, word in enumerate(words):
        if word not in _WORD_TO_IDX:
            raise ValueError(f"Unknown word: {word}")
        seed |= _WORD_TO_IDX[word] << (_MNEM_BITS * i)
    return seed


# ─── AGENT TYPES (the color identity — like Pokemon types or MTG colors) ───
# Every agent has a primary type derived from its category.
# Tags can add a secondary type. Dual-type agents are rarer and more valuable.

AGENT_TYPES = {
    "LOGIC":  {"color": "#58a6ff", "icon": "brain",   "label": "Logic"},
    "DATA":   {"color": "#3fb950", "icon": "stream",  "label": "Data"},
    "SOCIAL": {"color": "#d29922", "icon": "people",  "label": "Social"},
    "SHIELD": {"color": "#f0f0f0", "icon": "shield",  "label": "Shield"},
    "CRAFT":  {"color": "#f85149", "icon": "gear",    "label": "Craft"},
    "HEAL":   {"color": "#ff7eb3", "icon": "heart",   "label": "Heal"},
    "WEALTH": {"color": "#bc8cff", "icon": "coin",    "label": "Wealth"},
}

# Category → primary type mapping
CATEGORY_TYPE = {
    "core":                     "LOGIC",
    "devtools":                 "LOGIC",
    "pipeline":                 "DATA",
    "integrations":             "DATA",
    "productivity":             "SOCIAL",
    "general":                  "SOCIAL",
    "federal_government":       "SHIELD",
    "slg_government":           "SHIELD",
    "it_management":            "SHIELD",
    "manufacturing":            "CRAFT",
    "energy":                   "CRAFT",
    "retail_cpg":               "CRAFT",
    "healthcare":               "HEAL",
    "human_resources":          "HEAL",
    "financial_services":       "WEALTH",
    "b2b_sales":                "WEALTH",
    "b2c_sales":                "WEALTH",
    "professional_services":    "WEALTH",
    "software_digital_products": "DATA",
}

# Tag keywords → secondary type (first match wins)
TAG_TYPE_HINTS = {
    "LOGIC":  ["ai", "ml", "algorithm", "compute", "analysis", "ast", "parse", "model", "intelligence"],
    "DATA":   ["data", "pipeline", "etl", "sync", "migration", "import", "export", "extract", "transform"],
    "SOCIAL": ["email", "chat", "meeting", "communication", "demo", "presentation", "coach", "assistant"],
    "SHIELD": ["compliance", "security", "audit", "governance", "risk", "regulatory", "permit", "license"],
    "CRAFT":  ["inventory", "supply", "maintenance", "production", "manufacturing", "field", "dispatch"],
    "HEAL":   ["patient", "clinical", "care", "health", "wellness", "staff", "credentialing", "intake"],
    "WEALTH": ["sales", "revenue", "pricing", "deal", "proposal", "billing", "financial", "portfolio"],
}

# Type effectiveness chart — weakness and resistance
# LOGIC > DATA > SOCIAL > SHIELD > CRAFT > HEAL > WEALTH > LOGIC
TYPE_WEAKNESS = {
    "LOGIC":  "WEALTH",   # gold corrupts pure logic
    "DATA":   "LOGIC",    # logic deconstructs raw data
    "SOCIAL": "DATA",     # data exposes social spin
    "SHIELD": "SOCIAL",   # social pressure overwhelms bureaucracy
    "CRAFT":  "SHIELD",   # regulation constrains craft
    "HEAL":   "CRAFT",    # industrial demands strain care
    "WEALTH": "HEAL",     # care costs erode wealth
}

TYPE_RESISTANCE = {
    "LOGIC":  "DATA",
    "DATA":   "SOCIAL",
    "SOCIAL": "SHIELD",
    "SHIELD": "CRAFT",
    "CRAFT":  "HEAL",
    "HEAL":   "WEALTH",
    "WEALTH": "LOGIC",
}

# Evolution stages — tied to quality tier
EVOLUTION_STAGES = {
    "experimental": {"stage": 0, "label": "Seed",       "icon": "seed"},
    "community":    {"stage": 1, "label": "Base",       "icon": "sprout"},
    "verified":     {"stage": 2, "label": "Evolved",    "icon": "flame"},
    "official":     {"stage": 3, "label": "Legendary",  "icon": "crown"},
}

# ─── STAT DERIVATION (deterministic from manifest, never random) ───

def _derive_types(category: str, tags: list) -> list:
    """Derive primary + optional secondary type from category and tags."""
    primary = CATEGORY_TYPE.get(category, "SOCIAL")
    types = [primary]

    # Check tags for secondary type
    tag_str = " ".join(t.lower() for t in tags)
    for type_name, keywords in TAG_TYPE_HINTS.items():
        if type_name == primary:
            continue
        if any(kw in tag_str for kw in keywords):
            types.append(type_name)
            break  # max 2 types

    return types


def _derive_stats(name: str, tier: str, tags: list, deps: list,
                  env_vars: list, version_str: str, description: str) -> dict:
    """Derive 5 stats (HP, ATK, DEF, SPD, INT) deterministically from manifest data.
    Each stat is 10-100. The seed ensures unique distributions per agent."""
    rng = mulberry32(seed_hash(name + ":stats"))

    # Base stats from tier
    tier_base = {"experimental": 15, "community": 30, "verified": 50, "official": 70}
    base = tier_base.get(tier, 30)

    # Version multiplier (higher version = more refined)
    try:
        v_parts = [int(x) for x in version_str.split(".")]
        v_bonus = min(15, v_parts[0] * 3 + v_parts[1])
    except (ValueError, IndexError):
        v_bonus = 0

    # Tag/dep/env contribution
    tag_bonus = min(20, len(tags) * 3)
    dep_penalty = min(20, len(deps) * 5)
    env_bonus = min(15, len(env_vars) * 5)
    desc_bonus = min(10, len(description.split()) // 5)

    def clamp(v):
        return max(10, min(100, int(v)))

    # Each stat has a base + deterministic seed offset + manifest bonuses
    hp  = clamp(base + v_bonus + tag_bonus + rng() * 25)
    atk = clamp(base + tag_bonus + desc_bonus + rng() * 30)
    dfs = clamp(base + env_bonus + v_bonus + rng() * 20)  # "def" is reserved
    spd = clamp(base + 20 - dep_penalty + rng() * 25)
    itl = clamp(base + desc_bonus + tag_bonus + rng() * 20)

    return {"hp": hp, "atk": atk, "def": dfs, "spd": spd, "int": itl}


def _derive_abilities(name: str, tags: list, category: str, tier: str) -> list:
    """Generate 1-3 abilities deterministically from agent identity."""
    rng = mulberry32(seed_hash(name + ":abilities"))

    # Ability templates by type
    ABILITY_POOL = {
        "LOGIC":  [
            ("Analyze", "Inspect target data source. Draw insight."),
            ("Compute", "Process input through algorithm. Return structured result."),
            ("Parse", "Decompose complex input into structured components."),
            ("Reason", "Apply chain-of-thought to derive conclusion."),
        ],
        "DATA":  [
            ("Extract", "Pull data from connected source into working memory."),
            ("Transform", "Reshape data to match target schema."),
            ("Sync", "Synchronize state between two systems."),
            ("Pipeline", "Execute multi-step data flow. Each stage feeds the next."),
        ],
        "SOCIAL": [
            ("Assist", "Guide user through task with context-aware suggestions."),
            ("Draft", "Compose human-quality text for target audience."),
            ("Coach", "Observe performance and provide actionable feedback."),
            ("Present", "Format findings into presentation-ready output."),
        ],
        "SHIELD": [
            ("Audit", "Scan target for compliance violations. Report findings."),
            ("Enforce", "Apply policy rules. Block non-compliant actions."),
            ("Monitor", "Continuously watch for anomalies. Alert on deviation."),
            ("Certify", "Validate against standards. Issue compliance attestation."),
        ],
        "CRAFT":  [
            ("Build", "Assemble components into deployable artifact."),
            ("Optimize", "Tune process parameters for maximum throughput."),
            ("Schedule", "Allocate resources across timeline. Minimize conflicts."),
            ("Dispatch", "Route work to available capacity. Track completion."),
        ],
        "HEAL":  [
            ("Triage", "Assess priority and route to appropriate handler."),
            ("Screen", "Evaluate against criteria. Flag items needing attention."),
            ("Support", "Provide contextual guidance through complex process."),
            ("Track", "Monitor progress against care plan. Alert on gaps."),
        ],
        "WEALTH": [
            ("Prospect", "Identify and qualify potential opportunities."),
            ("Forecast", "Project future values from historical patterns."),
            ("Negotiate", "Propose terms optimized for mutual value."),
            ("Close", "Execute final steps of value exchange. Confirm settlement."),
        ],
    }

    primary_type = CATEGORY_TYPE.get(category, "SOCIAL")
    pool = ABILITY_POOL.get(primary_type, ABILITY_POOL["SOCIAL"])

    # Number of abilities: 1 for experimental, 2 for community, 3 for verified/official
    tier_count = {"experimental": 1, "community": 2, "verified": 3, "official": 3}
    count = tier_count.get(tier, 2)

    abilities = []
    used = set()
    for _ in range(count):
        idx = int(rng() * len(pool))
        # Avoid duplicates
        attempts = 0
        while idx in used and attempts < len(pool):
            idx = (idx + 1) % len(pool)
            attempts += 1
        used.add(idx)
        ab_name, ab_text = pool[idx]

        # Damage/cost derived from seed
        cost = int(rng() * 3) + 1  # 1-3 energy
        damage = int(rng() * 40) + 10  # 10-50

        abilities.append({
            "name": ab_name,
            "text": ab_text,
            "cost": cost,
            "damage": damage,
        })

    return abilities


# ─── FLAVOR TEXT + TYPE LINE ───

_FLAVOR_FRAGMENTS = [
    "Built for the ecosystem. Ready for the edge.",
    "One file. Infinite possibilities.",
    "Runs anywhere the RAPP runtime breathes.",
    "Forged in the registry. Trusted in production.",
    "A single-file agent. A single promise: perform.",
    "When the network calls, this agent answers.",
    "Data in. Insight out. No drama.",
    "The pipeline starts here.",
    "Born from a manifest. Raised in the registry.",
    "Your code, your agent, your card. Permanent.",
    "Not just code. Identity.",
    "The forge remembers every agent it ever touched.",
]

_TYPE_PREFIXES = {
    "core": "Foundation",
    "pipeline": "Pipeline",
    "integrations": "Integration",
    "productivity": "Utility",
    "devtools": "DevTool",
    "general": "General",
    "b2b_sales": "B2B Sales",
    "b2c_sales": "B2C Sales",
    "healthcare": "Healthcare",
    "financial_services": "Financial",
    "manufacturing": "Industrial",
    "energy": "Energy",
    "federal_government": "Federal",
    "slg_government": "Government",
    "human_resources": "HR",
    "it_management": "IT Ops",
    "professional_services": "Professional",
    "retail_cpg": "Retail",
    "software_digital_products": "Software",
}


def mint_card(path: str) -> dict:
    """
    Mint a card from an agent file. The canonical path:

      manifest → forge_seed() → resolve_card_from_seed() = the card

    The seed IS the card. mint_card just reads the manifest, forges the
    seed, and resolves from it. Both mint_card and resolve_card_from_seed
    produce identical output for the same agent. This is the protocol.
    """
    manifest = extract_manifest(path)
    if manifest is None:
        raise ValueError(f"No __manifest__ found in {path}")

    name = manifest.get("name", path)
    category = manifest.get("category", "general")
    tier = manifest.get("quality_tier", "community")
    tags = manifest.get("tags", [])
    deps = manifest.get("dependencies", [])

    # Forge the seed FROM the manifest data
    seed = forge_seed(name, category, tier, tags, deps)

    # Resolve the card FROM the seed — one canonical path
    card = resolve_card_from_seed(seed)

    # Enrich with manifest metadata that doesn't affect the card identity
    card["name"] = name
    card["display_name"] = manifest.get("display_name", name)
    card["version"] = manifest.get("version", "1.0.0")
    card["description"] = manifest.get("description", "")
    card["author"] = manifest.get("author", "")
    card["tags"] = tags
    card["power"] = card["stats"]["atk"]
    card["toughness"] = card["stats"]["def"]
    card["name_seed"] = seed_hash(name) & 0xFFFFFFFF
    card["_resolved_from"] = "manifest"

    return card


def card_value(name: str) -> dict:
    """Fetch registry, find agent, compute floor value based on tier."""
    registry = fetch_registry()
    agent = None
    for a in registry.get("agents", []):
        if a.get("name") == name:
            agent = a
            break

    if agent is None:
        return {"error": f"Agent '{name}' not found in registry"}

    tier = agent.get("quality_tier", "community")
    rarity = TIER_TO_RARITY.get(tier, "core")
    floor_pts = RARITY_FLOOR.get(rarity, 10)

    # Floor BTC: 1 BTC = ~10,000,000 pts (illustrative peg)
    floor_btc = round(floor_pts / 10_000_000, 8)

    return {
        "name": name,
        "display_name": agent.get("display_name", name),
        "tier": tier,
        "rarity": rarity,
        "rarity_label": RARITY_LABELS.get(rarity, rarity),
        "floor_pts": floor_pts,
        "floor_btc": floor_btc,
    }


def forge_seed(name: str, category: str, tier: str, tags: list, deps: list) -> int:
    """
    Forge a seed FROM agent data. The seed IS the card's DNA.

    Packs the agent's identity, types, tier, and hints into a 64-bit
    integer. Anyone with this number reconstructs the exact card —
    no registry, no network, no lookup. The protocol is permanent.

    Bit layout (64 bits):
      [63-32] name_hash      (32 bits — identity, drives stat variation)
      [31-27] category_idx   (5 bits — 0-18, maps to primary type)
      [26-24] secondary_type (3 bits — 0-7, 7=none)
      [23-22] tier_idx       (2 bits — 0-3)
      [21-17] tag_count      (5 bits — 0-31, influences ability count)
      [16-13] dep_count      (4 bits — 0-15, influences retreat cost)
      [12-0]  tag_hash       (13 bits — drives ability selection)
    """
    name_hash = seed_hash(name) & 0xFFFFFFFF

    cat_list = list(CATEGORY_TYPE.keys())
    cat_idx = cat_list.index(category) if category in cat_list else 0

    # Derive types the same way as _derive_types, then encode
    types = _derive_types(category, tags)
    type_names = list(AGENT_TYPES.keys())
    secondary_idx = 7  # 7 = no secondary type
    if len(types) > 1:
        secondary_idx = type_names.index(types[1]) if types[1] in type_names else 7

    tier_map = {"experimental": 0, "community": 1, "verified": 2, "official": 3}
    tier_idx = tier_map.get(tier, 1)

    tag_count = min(31, len(tags))
    dep_count = min(15, len(deps))
    tag_hash = seed_hash(" ".join(tags)) & 0x1FFF if tags else 0

    seed = (
        (name_hash << 32) |
        (cat_idx << 27) |
        (secondary_idx << 24) |
        (tier_idx << 22) |
        (tag_count << 17) |
        (dep_count << 13) |
        tag_hash
    )
    return seed


def resolve_card_from_seed(seed: int) -> dict:
    """
    Reconstruct a card from a seed number.

    Two modes:
      - 32-bit name seed (< 2^32): the card's PERMANENT identity.
        Resolves to the CURRENT version via registry lookup.
        This is the number you memorize and share.

      - 64-bit full seed (>= 2^32): a SPECIFIC version's DNA.
        Resolves to the exact card from that version, offline.
        This is the versioned snapshot.

    Share the short seed. It always points to the latest card.
    """
    # 32-bit name seed → lookup current version in registry
    if seed < (1 << 32):
        try:
            registry = fetch_registry()
            for agent in registry.get("agents", []):
                name_hash = seed_hash(agent["name"]) & 0xFFFFFFFF
                if name_hash == seed:
                    return resolve_card(agent["name"])
        except Exception:
            pass
        # Not found in registry — fall through to generate a preview
        # Pack as if it were the top 32 bits with default lower bits
        seed = seed << 32  # name_hash only, defaults for everything else

    # 64-bit full seed → unpack exact version
    # Unpack the seed DNA
    name_hash = (seed >> 32) & 0xFFFFFFFF
    cat_idx = (seed >> 27) & 0x1F
    secondary_idx = (seed >> 24) & 0x7
    tier_idx = (seed >> 22) & 0x3
    tag_count = (seed >> 17) & 0x1F
    dep_count = (seed >> 13) & 0xF
    tag_hash = seed & 0x1FFF

    # Reconstruct category → primary type
    cat_list = list(CATEGORY_TYPE.keys())
    category = cat_list[cat_idx] if cat_idx < len(cat_list) else "general"
    primary_type = CATEGORY_TYPE.get(category, "SOCIAL")

    # Reconstruct tier
    tier_list = ["experimental", "community", "verified", "official"]
    tier = tier_list[tier_idx] if tier_idx < len(tier_list) else "community"
    rarity = TIER_TO_RARITY.get(tier, "core")
    evo = EVOLUTION_STAGES.get(tier, EVOLUTION_STAGES["community"])

    # Reconstruct types (secondary encoded directly)
    types = [primary_type]
    type_names = list(AGENT_TYPES.keys())
    if secondary_idx < len(type_names) and type_names[secondary_idx] != primary_type:
        types.append(type_names[secondary_idx])

    # Stats — same derivation as _derive_stats using only seed-encoded fields
    # We pass empty strings for version/description since those aren't in the seed
    # but the core stat inputs (name, tier, tags, deps, env_vars) ARE encoded
    fake_tags = ["x"] * tag_count  # count is what matters, not the strings
    fake_deps = ["x"] * dep_count
    stats = _derive_stats(
        chr(name_hash & 0xFF) * 4,  # reconstruct a name-like string from hash
        tier, fake_tags, fake_deps, [], "1.0.0", ""
    )
    # Override with name_hash-seeded stats for full fidelity
    rng = mulberry32(name_hash ^ 0x57415453)  # XOR with "STAT" for unique stream
    tier_base = {"experimental": 15, "community": 30, "verified": 50, "official": 70}
    base = tier_base.get(tier, 30)
    tag_bonus = min(20, tag_count * 3)
    dep_penalty = min(20, dep_count * 5)
    clamp = lambda v: max(10, min(100, int(v)))
    hp  = clamp(base + tag_bonus + rng() * 25)
    atk = clamp(base + tag_bonus + rng() * 30)
    dfs = clamp(base + rng() * 20)
    spd = clamp(base + 20 - dep_penalty + rng() * 25)
    itl = clamp(base + tag_bonus + rng() * 20)
    stats = {"hp": hp, "atk": atk, "def": dfs, "spd": spd, "int": itl}

    # Abilities from type + tag_hash
    pool = {
        "LOGIC":  [("Analyze", 30), ("Compute", 25), ("Parse", 20), ("Reason", 35)],
        "DATA":   [("Extract", 20), ("Transform", 30), ("Sync", 25), ("Pipeline", 35)],
        "SOCIAL": [("Assist", 15), ("Draft", 25), ("Coach", 30), ("Present", 20)],
        "SHIELD": [("Audit", 25), ("Enforce", 35), ("Monitor", 20), ("Certify", 30)],
        "CRAFT":  [("Build", 30), ("Optimize", 35), ("Schedule", 20), ("Dispatch", 25)],
        "HEAL":   [("Triage", 25), ("Screen", 20), ("Support", 15), ("Track", 30)],
        "WEALTH": [("Prospect", 20), ("Forecast", 30), ("Negotiate", 35), ("Close", 40)],
    }.get(primary_type, [("Perform", 25)])

    tier_count = {"experimental": 1, "community": 2, "verified": 3, "official": 3}
    count = tier_count.get(tier, 2)
    ab_rng = mulberry32(tag_hash | (name_hash & 0xFF00))
    abilities = []
    used = set()
    for _ in range(min(count, len(pool))):
        idx = int(ab_rng() * len(pool))
        while idx in used and len(used) < len(pool):
            idx = (idx + 1) % len(pool)
        used.add(idx)
        ab_name, base_dmg = pool[idx]
        abilities.append({
            "name": ab_name,
            "text": "",
            "cost": int(ab_rng() * 3) + 1,
            "damage": base_dmg + int(ab_rng() * 15),
        })

    weakness = TYPE_WEAKNESS.get(primary_type, "LOGIC")
    resistance = TYPE_RESISTANCE.get(primary_type, "DATA")
    retreat_cost = min(4, dep_count)

    flavor_rng = mulberry32(name_hash ^ tag_hash)
    flavor_idx = int(flavor_rng() * len(_FLAVOR_FRAGMENTS))

    dual = f" / {AGENT_TYPES[types[1]]['label']}" if len(types) > 1 else ""
    type_prefix = _TYPE_PREFIXES.get(category, "Agent")
    type_line = f"{type_prefix} Agent — {AGENT_TYPES[primary_type]['label']}{dual}"

    return {
        "seed": seed,
        "display_name": f"Agent #{name_hash & 0xFFFF:04X}",
        "tier": tier,
        "rarity": rarity,
        "rarity_label": RARITY_LABELS.get(rarity, rarity),
        "types": types,
        "type_colors": [AGENT_TYPES[t]["color"] for t in types],
        "hp": hp,
        "stats": stats,
        "abilities": abilities,
        "weakness": weakness,
        "weakness_label": AGENT_TYPES[weakness]["label"],
        "resistance": resistance,
        "resistance_label": AGENT_TYPES[resistance]["label"],
        "retreat_cost": retreat_cost,
        "evolution": evo,
        "category": category,
        "type_line": type_line,
        "flavor": _FLAVOR_FRAGMENTS[flavor_idx],
        "floor_pts": RARITY_FLOOR.get(rarity, 10),
        "seed": seed,
        "name_seed": name_hash,
        "_resolved_from": "seed",
    }


def resolve_card(name: str) -> dict:
    """
    Resolve a card from an agent name via the registry.

    Looks up the agent, forges the seed from its manifest, then resolves
    the card from the seed. Same canonical path as mint_card:

      registry lookup → forge_seed() → resolve_card_from_seed() = the card

    Enriches with metadata (display_name, description, author, version).
    """
    registry = fetch_registry()
    agent = None
    for a in registry.get("agents", []):
        if a.get("name") == name:
            agent = a
            break

    if agent is None:
        return {"error": f"Agent '{name}' not found in registry"}

    # Forge seed from manifest data
    category = agent.get("category", "general")
    tier = agent.get("quality_tier", "community")
    tags = agent.get("tags", [])
    deps = agent.get("dependencies", [])
    seed = forge_seed(name, category, tier, tags, deps)

    # Resolve from seed — one canonical path
    card = resolve_card_from_seed(seed)

    # Enrich with registry metadata
    card["name"] = name
    card["display_name"] = agent.get("display_name", name)
    card["version"] = agent.get("version", "1.0.0")
    card["description"] = agent.get("description", "")
    card["author"] = agent.get("author", "")
    card["tags"] = tags
    card["power"] = card["stats"]["atk"]
    card["toughness"] = card["stats"]["def"]
    card["name_seed"] = seed_hash(name) & 0xFFFFFFFF
    card["_resolved_from"] = "registry"

    return card


def binder_status() -> dict:
    """Check local registry.json and count agents by tier, computing total binder value."""
    local = Path(__file__).parent / "registry.json"
    if not local.exists():
        return {"error": "No local registry.json found. Run build_registry.py first."}

    try:
        registry = json.loads(local.read_text())
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse registry.json: {e}"}

    agents = registry.get("agents", [])
    by_tier: dict[str, list] = {}
    total_pts = 0

    for agent in agents:
        tier = agent.get("quality_tier", "community")
        by_tier.setdefault(tier, []).append(agent.get("name", ""))
        rarity = TIER_TO_RARITY.get(tier, "core")
        total_pts += RARITY_FLOOR.get(rarity, 10)

    summary = {tier: len(names) for tier, names in by_tier.items()}
    total_btc = round(total_pts / 10_000_000, 8)

    return {
        "total_agents": len(agents),
        "by_tier": summary,
        "total_pts": total_pts,
        "total_btc": total_btc,
        "registry_generated_at": registry.get("generated_at", "unknown"),
    }


def binder_transfer(mint_id: str, dest: str) -> dict:
    """Create a signed transfer intent for a card in the binder."""
    import time

    timestamp = int(time.time())
    payload = f"{mint_id}:{dest}:{timestamp}"
    digest = hashlib.sha256(payload.encode()).hexdigest()

    return {
        "action": "transfer",
        "mintId": mint_id,
        "to": dest,
        "timestamp": timestamp,
        "hash": digest,
    }


# =============================================================================
# SECTION 6: RAPP EGG — Sneakernet Brainstem Transfer
# =============================================================================
#
# A rapp.egg is the entire Brainstem compressed for sneakernet transfer.
#
# Three tiers of payload:
#
#   seeds:    [int, ...]     — Agent cards. Self-assemble from math. ZERO bandwidth.
#   payloads: [{...}, ...]   — Small custom content (< 4KB). Inline base64. LOW bandwidth.
#   refs:     [{...}, ...]   — Large content (cartridges). SHA256 hash = identity.
#                               Fetch by hash when online. Skip if already cached.
#                               Content-addressable = free dedup.
#
# The egg is the recipe, not the meal. Seeds self-assemble. Payloads travel inline.
# Refs are fetched on demand — the hash guarantees you get the right content
# from ANY source (binder repo, IPFS, USB stick, peer).
#
# 20 agents + 3 small configs + 2 cartridge refs = ~2KB. Fits in a QR code.

import base64


def forge_egg(agent_paths: list = None, agent_names: list = None,
              deck: str = None, config: dict = None) -> dict:
    """
    Forge a rapp.egg from a list of agents. The egg contains ONLY seeds —
    the minimum information needed to reconstruct an entire Brainstem.

    Args:
        agent_paths: list of .py file paths (reads manifests, forges seeds)
        agent_names: list of @publisher/slug names (looks up registry, forges seeds)
        deck: optional active deck name
        config: optional personality/preferences dict

    Returns:
        dict with schema, seeds array, and optional metadata.
        The entire thing is typically < 1KB for 50 agents.
    """
    seeds = []
    names = []

    # From files
    if agent_paths:
        for path in agent_paths:
            manifest = extract_manifest(path)
            if manifest:
                name = manifest["name"]
                category = manifest.get("category", "general")
                tier = manifest.get("quality_tier", "community")
                tags = manifest.get("tags", [])
                deps = manifest.get("dependencies", [])
                seed = forge_seed(name, category, tier, tags, deps)
                seeds.append(seed)
                names.append(name)

    # From names (registry lookup)
    if agent_names:
        registry = fetch_registry()
        agent_map = {a["name"]: a for a in registry.get("agents", [])}
        for name in agent_names:
            agent = agent_map.get(name)
            if agent:
                seed = forge_seed(
                    name,
                    agent.get("category", "general"),
                    agent.get("quality_tier", "community"),
                    agent.get("tags", []),
                    agent.get("dependencies", []),
                )
                seeds.append(seed)
                names.append(name)

    egg = {
        "schema": "rapp-egg/1.0",
        "seeds": seeds,
        "count": len(seeds),
    }
    if deck:
        egg["deck"] = deck
    if config:
        egg["config"] = config

    return egg


def egg_to_compact(egg: dict) -> str:
    """
    Compress an egg to a compact string for sneakernet transfer.
    Format: base64-encoded seed array. Tiny enough for QR code, SMS, NFC.

    A 20-agent egg compresses to ~220 characters. A 50-agent egg to ~540.
    """
    seeds = egg.get("seeds", [])
    # Pack seeds as 8-byte big-endian integers
    raw = b"".join(s.to_bytes(8, "big") for s in seeds)
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def compact_to_egg(compact: str) -> dict:
    """Decompress a compact string back to an egg."""
    # Re-pad base64
    padding = 4 - len(compact) % 4
    if padding < 4:
        compact += "=" * padding
    raw = base64.urlsafe_b64decode(compact)
    seeds = []
    for i in range(0, len(raw), 8):
        seed = int.from_bytes(raw[i:i+8], "big")
        seeds.append(seed)
    return {"schema": "rapp-egg/1.0", "seeds": seeds, "count": len(seeds)}


def hatch_egg(egg: dict, output_dir: str = "agents") -> list:
    """
    Hatch an egg — resolve each seed and install the agents.

    For each seed:
      1. Check registry for matching agent (seed → name → download .py)
      2. If not in registry, resolve card from seed (preview only)

    Returns list of results (installed paths or preview cards).
    """
    results = []
    registry = fetch_registry()
    seed_map = {}
    for agent in registry.get("agents", []):
        s = agent.get("_seed")
        if s:
            seed_map[s] = agent

    for seed in egg.get("seeds", []):
        agent = seed_map.get(seed)
        if agent:
            # Known agent — install the .py file
            try:
                path = install_agent(agent["name"], output_dir)
                results.append({"seed": seed, "name": agent["name"], "installed": path})
            except Exception as e:
                results.append({"seed": seed, "name": agent["name"], "error": str(e)})
        else:
            # Unknown seed — resolve preview card
            card = resolve_card_from_seed(seed)
            results.append({"seed": seed, "preview": True, "card": card})

    return results


# =============================================================================
# SECTION 7: CLI DISPATCHER
# =============================================================================

def init_binder(repo_name: str = None) -> dict:
    """Initialize a RAR-compliant binder in the current directory or a new one.
    Returns dict with paths created."""
    import subprocess as _sp

    cwd = Path.cwd()

    # If repo_name given, create subdir
    if repo_name:
        cwd = cwd / repo_name
        cwd.mkdir(exist_ok=True)

    # Run setup_instance if available, otherwise create minimal structure
    setup_script = Path(__file__).parent / "scripts" / "setup_instance.py"
    if setup_script.exists():
        env = os.environ.copy()
        github_user = env.get("GITHUB_USER", "")
        if not github_user:
            try:
                r = _sp.run(["gh", "api", "user", "-q", ".login"],
                            capture_output=True, text=True, timeout=5)
                if r.returncode == 0:
                    github_user = r.stdout.strip()
            except Exception:
                pass
        if not github_user:
            github_user = "local"
        repo = repo_name or cwd.name
        env["GITHUB_REPOSITORY"] = f"{github_user}/{repo}"

        _sp.run([sys.executable, str(setup_script)], env=env, cwd=str(cwd))

    result = {
        "binder_dir": str(cwd),
        "namespace": f"@{github_user}" if 'github_user' in dir() else "@local",
    }

    # Ensure minimal structure even without setup_instance
    for d in ["agents", "staging", "binder"]:
        (cwd / d).mkdir(exist_ok=True)

    return result


def _auto_register_binder(token: str, namespace: str, upstream: str) -> None:
    """Auto-register binder on the ledger if not already registered.
    Creates a GitHub Issue with register_binder action. Silent if already registered."""
    # Check ledger first
    try:
        ledger_url = f"https://raw.githubusercontent.com/{upstream}/main/state/binder_ledger.json"
        ledger = _fetch_json(ledger_url, token)
        if ledger:
            # Get GitHub username from token
            user_data = _fetch_json("https://api.github.com/user", token)
            username = user_data.get("login", "") if user_data else ""
            if username and username in ledger.get("binders", {}):
                return  # already registered
    except Exception:
        pass  # can't check — try to register anyway

    # Register
    body_data = {"action": "register_binder", "payload": {"namespace": namespace}}
    issue_body = f"```json\n{json.dumps(body_data, indent=2)}\n```"
    payload = json.dumps({
        "title": "[RAR] register_binder",
        "body": issue_body,
    }).encode()

    req = urllib.request.Request(
        f"https://api.github.com/repos/{upstream}/issues",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "RAPP-SDK/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15):
            pass  # registration issued — pipeline will process it
    except Exception:
        pass  # non-fatal — submit will fail with a clear error if not registered


def submit_agent(path: str, upstream: str = None) -> dict:
    """Submit an agent to the upstream RAR registry via GitHub Issue.
    Returns the issue URL on success."""
    agent_path = Path(path)
    if not agent_path.exists():
        raise FileNotFoundError(f"Agent file not found: {path}")

    code = agent_path.read_text()

    # Validate first
    manifest = extract_manifest(path)
    if manifest is None:
        raise ValueError("No __manifest__ found — validate your agent first")

    errors = validate_manifest(path, manifest)
    if errors:
        raise ValueError(f"Manifest errors: {'; '.join(errors)}")

    # Check snake_case
    stem = agent_path.stem
    if "-" in stem:
        raise ValueError(f"Filename '{agent_path.name}' uses dashes — rename to snake_case")

    upstream = upstream or REPO
    token = _get_token()
    if not token:
        raise RuntimeError(
            "No GitHub token. Run `gh auth login` or set GITHUB_TOKEN."
        )

    # Auto-register binder if not yet registered
    publisher = manifest["name"].split("/")[0]
    _auto_register_binder(token, publisher, upstream)

    body_data = {"action": "submit_agent", "payload": {"code": code}}
    issue_body = f"```json\n{json.dumps(body_data, indent=2)}\n```"

    payload = json.dumps({
        "title": f"[AGENT] {manifest['name']}",
        "body": issue_body,
        "labels": ["rar-action", "agent-submission"],
    }).encode()

    req = urllib.request.Request(
        f"https://api.github.com/repos/{upstream}/issues",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "RAPP-SDK/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            return {
                "ok": True,
                "issue_url": result.get("html_url", ""),
                "agent": manifest["name"],
                "status": "pending_review",
            }
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()[:300] if e.fp else str(e)
        raise RuntimeError(f"GitHub API error ({e.code}): {err_body}")


def scaffold_agent(name: str, output_dir: str = None) -> str:
    """
    Scaffold a new agent from template.
    name should be @publisher/my_agent (snake_case).
    output_dir overrides the default agents/ directory.
    Returns the path to the written file.
    """
    if not name.startswith("@") or "/" not in name:
        raise ValueError(f"Name must be @publisher/slug, got: {name}")

    publisher, slug = name.split("/", 1)

    # Enforce snake_case
    if "-" in slug:
        fixed = slug.replace("-", "_")
        raise ValueError(f"Slug '{slug}' uses dashes — use snake_case: {fixed}")

    # class_name: "my_agent" -> "MyAgent"
    class_name = "".join(word.title() for word in slug.split("_"))

    # display_name: "my_agent" -> "My Agent"
    display_name = slug.replace("_", " ").title()

    description = "A RAPP agent."
    author = publisher.lstrip("@")

    file_name = slug if slug.endswith("_agent") else slug + "_agent"
    file_name += ".py"
    base_dir = Path(output_dir) if output_dir else Path(__file__).parent / "agents"
    output_path = base_dir / publisher / file_name

    content = (
        AGENT_TEMPLATE
        .replace("__NAME__", name)
        .replace("__DISPLAY_NAME__", display_name)
        .replace("__CLASS_NAME__", class_name)
        .replace("__DESCRIPTION__", description)
        .replace("__AUTHOR__", author)
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    return str(output_path)


def _fmt_test_results(results: list[tuple[str, bool, str]], use_json: bool) -> str:
    if use_json:
        return json.dumps([
            {"test": name, "passed": passed, "message": msg}
            for name, passed, msg in results
        ], indent=2)

    lines = []
    passed_count = sum(1 for _, p, _ in results if p)
    total = len(results)
    for name, passed, msg in results:
        icon = "PASS" if passed else "FAIL"
        lines.append(f"  [{icon}] {name:<28} {msg}")
    lines.append(f"\n  {passed_count}/{total} tests passed")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        prog="rapp_sdk",
        description="RAPP Foundation SDK — Build agents, mint cards, track Binders.",
    )
    parser.add_argument("--version", action="version", version=f"rapp_sdk {__version__}")

    sub = parser.add_subparsers(dest="command", metavar="<command>")

    # init
    p_init = sub.add_parser("init", help="Initialize a RAR binder (agent workspace)")
    p_init.add_argument("name", nargs="?", help="Optional repo/directory name")
    p_init.add_argument("--json", action="store_true", help="Output JSON")

    # new
    p_new = sub.add_parser("new", help="Scaffold a new agent from template")
    p_new.add_argument("name", help="Agent name: @publisher/my_agent (snake_case)")
    p_new.add_argument("--json", action="store_true", help="Output JSON")

    # submit
    p_submit = sub.add_parser("submit", help="Submit an agent to the RAR registry for review")
    p_submit.add_argument("path", help="Path to agent .py file")
    p_submit.add_argument("--json", action="store_true", help="Output JSON")

    # validate
    p_val = sub.add_parser("validate", help="Validate an agent manifest")
    p_val.add_argument("path", help="Path to agent .py file")
    p_val.add_argument("--json", action="store_true", help="Output JSON")

    # test
    p_test = sub.add_parser("test", help="Run contract tests against an agent file")
    p_test.add_argument("path", help="Path to agent .py file")
    p_test.add_argument("--json", action="store_true", help="Output JSON")

    # search
    p_search = sub.add_parser("search", help="Search the agent registry")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--json", action="store_true", help="Output JSON")

    # install
    p_install = sub.add_parser("install", help="Download an agent from the registry")
    p_install.add_argument("name", help="Agent name: @publisher/my-agent")
    p_install.add_argument("--output-dir", default="agents", help="Output directory (default: agents)")
    p_install.add_argument("--json", action="store_true", help="Output JSON")

    # info
    p_info = sub.add_parser("info", help="Show details for an agent")
    p_info.add_argument("name", help="Agent name: @publisher/my-agent")
    p_info.add_argument("--json", action="store_true", help="Output JSON")

    # card
    p_card = sub.add_parser("card", help="Card operations")
    card_sub = p_card.add_subparsers(dest="card_command", metavar="<subcommand>")

    p_card_mint = card_sub.add_parser("mint", help="Mint a card from an agent file")
    p_card_mint.add_argument("path", help="Path to agent .py file")
    p_card_mint.add_argument("--json", action="store_true", help="Output JSON")

    p_card_value = card_sub.add_parser("value", help="Check the floor value of an agent card")
    p_card_value.add_argument("name", help="Agent name: @publisher/my-agent")
    p_card_value.add_argument("--json", action="store_true", help="Output JSON")

    p_card_resolve = card_sub.add_parser("resolve", help="Resolve a full card from just a name — micro-bandwidth self-assembly")
    p_card_resolve.add_argument("name", nargs="+", help="Agent name, numeric seed, or 7-word mnemonic")
    p_card_resolve.add_argument("--json", action="store_true", help="Output JSON")

    p_card_words = card_sub.add_parser("words", help="Get the 7-word mnemonic for an agent's seed")
    p_card_words.add_argument("name", help="Agent name (@pub/slug) or path to .py file")
    p_card_words.add_argument("--json", action="store_true", help="Output JSON")

    # binder
    p_binder = sub.add_parser("binder", help="Binder operations")
    binder_sub = p_binder.add_subparsers(dest="binder_command", metavar="<subcommand>")

    p_binder_status = binder_sub.add_parser("status", help="Show binder inventory")
    p_binder_status.add_argument("--json", action="store_true", help="Output JSON")

    p_binder_transfer = binder_sub.add_parser("transfer", help="Transfer a card to another address")
    p_binder_transfer.add_argument("id", help="Mint ID of the card")
    p_binder_transfer.add_argument("to", help="Destination address")
    p_binder_transfer.add_argument("--json", action="store_true", help="Output JSON")

    # egg
    p_egg = sub.add_parser("egg", help="Sneakernet Brainstem transfer — forge, compact, hatch")
    egg_sub = p_egg.add_subparsers(dest="egg_command", metavar="<subcommand>")

    p_egg_forge = egg_sub.add_parser("forge", help="Forge an egg from agent names")
    p_egg_forge.add_argument("agents", nargs="+", help="Agent names (@pub/slug)")
    p_egg_forge.add_argument("--json", action="store_true", help="Output JSON")

    p_egg_compact = egg_sub.add_parser("compact", help="Compress an egg to a shareable string")
    p_egg_compact.add_argument("agents", nargs="+", help="Agent names (@pub/slug)")

    p_egg_hatch = egg_sub.add_parser("hatch", help="Hatch an egg — install agents from compact string")
    p_egg_hatch.add_argument("compact", help="Compact egg string")
    p_egg_hatch.add_argument("--output-dir", default="agents", help="Output directory")
    p_egg_hatch.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    use_json = getattr(args, "json", False)

    # ---- init ----
    if args.command == "init":
        try:
            result = init_binder(args.name)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                print(f"\n  RAR Binder initialized!")
                print(f"  Directory: {result['binder_dir']}")
                print(f"  Namespace: {result.get('namespace', '?')}")
                print(f"\n  Next steps:")
                print(f"    python rapp_sdk.py new @you/my_agent    # scaffold an agent")
                print(f"    python rapp_sdk.py validate agent.py    # validate it")
                print(f"    python rapp_sdk.py test agent.py        # run contract tests")
                print(f"    python rapp_sdk.py submit agent.py      # submit to RAR")
                print()
        except Exception as e:
            if use_json:
                print(json.dumps({"error": str(e)}))
            else:
                print(f"  Error: {e}")
            sys.exit(1)

    # ---- new ----
    elif args.command == "new":
        try:
            out_path = scaffold_agent(args.name)
            if use_json:
                print(json.dumps({"created": out_path}))
            else:
                print(f"Created: {out_path}")
        except Exception as e:
            if use_json:
                print(json.dumps({"error": str(e)}))
            else:
                print(f"Error: {e}")
            sys.exit(1)

    # ---- validate ----
    elif args.command == "validate":
        errors = validate_manifest(args.path)
        manifest = extract_manifest(args.path)
        if use_json:
            print(json.dumps({"path": args.path, "valid": len(errors) == 0, "errors": errors}))
        else:
            if not errors:
                name = manifest.get("name", args.path) if manifest else args.path
                tier = manifest.get("quality_tier", "community") if manifest else "?"
                print(f"  Valid: {name}  [{tier}]")
            else:
                print(f"  Invalid: {args.path}")
                for e in errors:
                    print(f"    - {e}")
                sys.exit(1)

    # ---- test ----
    elif args.command == "test":
        results = run_contract_tests(args.path)
        output = _fmt_test_results(results, use_json)
        print(output)
        failed = [r for r in results if not r[1]]
        if failed:
            sys.exit(1)

    # ---- search ----
    elif args.command == "search":
        agents = search_agents(args.query)
        if use_json:
            print(json.dumps(agents, indent=2))
        else:
            if not agents:
                print(f"  No agents found matching '{args.query}'")
            else:
                print(f"  {len(agents)} result(s) for '{args.query}':\n")
                for a in agents:
                    tier = a.get("quality_tier", "community")
                    cat = a.get("category", "")
                    print(f"  {a['name']:<45} [{tier:<11}]  {cat}")
                    print(f"    {a.get('description', '')}")

    # ---- install ----
    elif args.command == "install":
        try:
            path = install_agent(args.name, args.output_dir)
            if use_json:
                print(json.dumps({"installed": path}))
            else:
                print(f"  Installed: {path}")
        except Exception as e:
            if use_json:
                print(json.dumps({"error": str(e)}))
            else:
                print(f"  Error: {e}")
            sys.exit(1)

    # ---- submit ----
    elif args.command == "submit":
        try:
            # Validate first
            errors = validate_manifest(args.path)
            if errors:
                if use_json:
                    print(json.dumps({"error": f"Validation failed: {'; '.join(errors)}"}))
                else:
                    print(f"  Validation failed:")
                    for e in errors:
                        print(f"    - {e}")
                sys.exit(1)

            result = submit_agent(args.path)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                print(f"\n  Submitted: {result['agent']}")
                print(f"  Status:    {result['status']}")
                print(f"  Issue:     {result['issue_url']}")
                print(f"\n  Your agent is now in staging for admin review.")
                print(f"  Once approved, it will be forged and added to the registry.")
                print()
        except Exception as e:
            if use_json:
                print(json.dumps({"error": str(e)}))
            else:
                print(f"  Error: {e}")
            sys.exit(1)

    # ---- info ----
    elif args.command == "info":
        agent = get_agent_info(args.name)
        if agent is None:
            if use_json:
                print(json.dumps({"error": f"Agent '{args.name}' not found"}))
            else:
                print(f"  Agent '{args.name}' not found in registry")
            sys.exit(1)
        if use_json:
            print(json.dumps(agent, indent=2))
        else:
            print(f"  Name:        {agent.get('name')}")
            print(f"  Display:     {agent.get('display_name')}")
            print(f"  Version:     {agent.get('version')}")
            print(f"  Author:      {agent.get('author')}")
            print(f"  Category:    {agent.get('category')}")
            print(f"  Tier:        {agent.get('quality_tier')}")
            print(f"  Description: {agent.get('description')}")
            tags = agent.get("tags", [])
            if tags:
                print(f"  Tags:        {', '.join(tags)}")
            deps = agent.get("dependencies", [])
            if deps:
                print(f"  Deps:        {', '.join(deps)}")

    # ---- card ----
    elif args.command == "card":
        if args.card_command == "mint":
            try:
                card = mint_card(args.path)
                if use_json:
                    print(json.dumps(card, indent=2))
                else:
                    print(f"  Card: {card['display_name']}")
                    print(f"  Type: {card['type_line']}")
                    print(f"  Rarity: {card['rarity_label']}  ({card['rarity']})")
                    print(f"  Power/Toughness: {card['power']}/{card['toughness']}")
                    print(f"  Floor: {card['floor_pts']} pts")
                    print(f"  Flavor: \"{card['flavor']}\"")
            except Exception as e:
                if use_json:
                    print(json.dumps({"error": str(e)}))
                else:
                    print(f"  Error: {e}")
                sys.exit(1)

        elif args.card_command == "value":
            result = card_value(args.name)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                if "error" in result:
                    print(f"  Error: {result['error']}")
                    sys.exit(1)
                print(f"  Agent:   {result['name']}")
                print(f"  Tier:    {result['tier']}")
                print(f"  Rarity:  {result['rarity_label']}  ({result['rarity']})")
                print(f"  Floor:   {result['floor_pts']} pts  /  {result['floor_btc']} BTC")

        elif args.card_command == "words":
            try:
                if args.name.endswith(".py"):
                    card = mint_card(args.name)
                else:
                    card = resolve_card(args.name)
                seed = card.get("seed", 0)
                mnemonic = seed_to_words(seed)
                if use_json:
                    print(json.dumps({"name": card.get("name", args.name), "seed": seed, "words": mnemonic}))
                else:
                    print(f"\n  {card.get('display_name', card.get('name', '?'))}")
                    print(f"  Seed: {seed}")
                    print(f"\n  {mnemonic}")
                    print(f"\n  Memorize these 7 words. They ARE the card.")
                    print(f"  Resolve anywhere: python rapp_sdk.py card resolve {mnemonic}")
                    print()
            except Exception as e:
                if use_json:
                    print(json.dumps({"error": str(e)}))
                else:
                    print(f"  Error: {e}")
                sys.exit(1)

        elif args.card_command == "resolve":
            # Detect: 7 words, numeric seed, or agent name
            input_str = " ".join(args.name)
            parts = input_str.strip().split()

            if len(parts) >= 7 and parts[0].upper() in _WORD_TO_IDX:
                # Mnemonic words
                seed_val = words_to_seed(" ".join(parts[:7]))
                result = resolve_card_from_seed(seed_val)
            elif len(parts) == 1:
                try:
                    seed_val = int(parts[0])
                    result = resolve_card_from_seed(seed_val)
                except ValueError:
                    result = resolve_card(parts[0])
            else:
                result = resolve_card(input_str)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                if "error" in result:
                    print(f"  Error: {result['error']}")
                    sys.exit(1)
                types_str = " / ".join(result.get("types", []))
                print(f"  {result['display_name']}   HP {result.get('hp', '?')}")
                print(f"  {result['type_line']}")
                print(f"  Type: {types_str}   |   {result['rarity_label']} ({result['rarity']})")
                print(f"  Stage: {result.get('evolution', {}).get('label', '?')}")
                print()
                stats = result.get("stats", {})
                print(f"  ATK {stats.get('atk','?'):>3}  DEF {stats.get('def','?'):>3}  SPD {stats.get('spd','?'):>3}  INT {stats.get('int','?'):>3}")
                print()
                for ab in result.get("abilities", []):
                    print(f"  [{ab['cost']}] {ab['name']}  ({ab['damage']} dmg)")
                    print(f"      {ab['text']}")
                print()
                print(f"  Weak to: {result.get('weakness_label', '?')}   Resists: {result.get('resistance_label', '?')}   Retreat: {'*' * result.get('retreat_cost', 0) or 'free'}")
                print(f"  \"{result['flavor']}\"")
                print()
                print(f"  Seed: {result['seed']}  |  Floor: {result['floor_pts']} pts")
                if result.get("_resolved_from") == "seed_only":
                    print(f"  Resolved from seed alone. Share the number — card self-assembles.")
                else:
                    print(f"  Resolved from name alone. Send \"{result.get('name', '')}\" — card self-assembles.")
        else:
            p_card.print_help()

    # ---- binder ----
    elif args.command == "binder":
        if args.binder_command == "status":
            status = binder_status()
            if use_json:
                print(json.dumps(status, indent=2))
            else:
                if "error" in status:
                    print(f"  Error: {status['error']}")
                    sys.exit(1)
                print(f"  Total agents: {status['total_agents']}")
                print(f"  By tier:")
                for tier, count in sorted(status["by_tier"].items()):
                    rarity = TIER_TO_RARITY.get(tier, "core")
                    label = RARITY_LABELS.get(rarity, rarity)
                    print(f"    {tier:<15} {count:>4} agents  ({label})")
                print(f"  Total value: {status['total_pts']} pts  /  {status['total_btc']} BTC")
                print(f"  Registry:    {status['registry_generated_at']}")

        elif args.binder_command == "transfer":
            result = binder_transfer(args.id, args.to)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                print(f"  Transfer Intent Created")
                print(f"  Mint ID:   {result['mintId']}")
                print(f"  To:        {result['to']}")
                print(f"  Timestamp: {result['timestamp']}")
                print(f"  Hash:      {result['hash']}")
        else:
            p_binder.print_help()

    # ---- egg ----
    elif args.command == "egg":
        if args.egg_command == "forge":
            egg = forge_egg(agent_names=args.agents)
            if use_json:
                print(json.dumps(egg, indent=2))
            else:
                print(f"\n  Forged egg: {egg['count']} agents")
                for s in egg["seeds"]:
                    print(f"    {s}")
                compact = egg_to_compact(egg)
                print(f"\n  Compact ({len(compact)} chars):")
                print(f"    {compact}")
                print(f"\n  Share this string. Recipient runs:")
                print(f"    python rapp_sdk.py egg hatch {compact}")
                print()

        elif args.egg_command == "compact":
            egg = forge_egg(agent_names=args.agents)
            print(egg_to_compact(egg))

        elif args.egg_command == "hatch":
            egg = compact_to_egg(args.compact)
            if use_json:
                results = hatch_egg(egg, args.output_dir)
                print(json.dumps(results, indent=2))
            else:
                print(f"\n  Hatching egg: {egg['count']} seeds")
                results = hatch_egg(egg, args.output_dir)
                for r in results:
                    if r.get("installed"):
                        print(f"    OK  {r['name']} -> {r['installed']}")
                    elif r.get("preview"):
                        card = r["card"]
                        print(f"    ?   Seed {r['seed']} -> {card['display_name']} ({card['rarity_label']})")
                    else:
                        print(f"    ERR {r.get('name','?')}: {r.get('error','?')}")
                print()
        else:
            p_egg.print_help()


if __name__ == "__main__":
    main()
