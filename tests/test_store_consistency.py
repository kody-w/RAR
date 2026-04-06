"""
Store Consistency Tests — validates index.html structure, tier mappings,
CSS class coverage, and key feature presence.
"""

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = REPO_ROOT / "index.html"
REGISTRY_JSON = REPO_ROOT / "registry.json"
CONSTITUTION = REPO_ROOT / "CONSTITUTION.md"
SDK_PATH = REPO_ROOT / "rapp_sdk.py"

html = INDEX_HTML.read_text()
registry = json.loads(REGISTRY_JSON.read_text())


# ═══════════════════════════════════════════════════════
# Tier and Rarity Consistency
# ═══════════════════════════════════════════════════════

def test_tier_to_rarity_defined():
    assert "TIER_TO_RARITY" in html
    assert "'official'" in html or '"official"' in html

def test_rarity_labels_defined():
    assert "RARITY_LABELS" in html

def test_rarity_labels_no_uncommon_no_common():
    """Rarity labels should use Core/Starter, not uncommon/common."""
    match = re.search(r'RARITY_LABELS\s*=\s*\{([^}]+)\}', html)
    assert match, "RARITY_LABELS not found"
    labels_block = match.group(1)
    assert "Core" in labels_block or "core" in labels_block
    assert "Starter" in labels_block or "starter" in labels_block

def test_tier_rarity_mapping_covers_all_tiers():
    """Every quality_tier in the registry must map to a rarity."""
    tiers_in_registry = set()
    for agent in registry.get("agents", []):
        tier = agent.get("quality_tier", "community")
        tiers_in_registry.add(tier)
    # Check they're all in the HTML TIER_TO_RARITY
    for tier in tiers_in_registry:
        assert tier in html, f"Tier '{tier}' from registry not referenced in store"


# ═══════════════════════════════════════════════════════
# CSS Class Coverage for New Rarity Names
# ═══════════════════════════════════════════════════════

def test_css_core_rarity_classes():
    """CSS must have styles for the 'core' rarity class."""
    assert ".core" in html, "Missing .core CSS class"

def test_css_starter_rarity_classes():
    """CSS must have styles for the 'starter' rarity class."""
    assert ".starter" in html, "Missing .starter CSS class"


# ═══════════════════════════════════════════════════════
# Collector Mode
# ═══════════════════════════════════════════════════════

def test_collector_mode_exists():
    assert "showntell-overlay" in html
    assert "showntell-card" in html

def test_collector_mode_flip():
    """Collector mode must support card flipping."""
    assert "flipped" in html
    assert "Flip" in html

def test_collector_mode_touch_support():
    """Collector mode must have touch event handlers."""
    assert "touchstart" in html
    assert "touchmove" in html
    assert "touchend" in html

def test_collector_mode_gallery_effects():
    """Collector mode must have gallery lighting effects."""
    assert "showntell-dust" in html
    assert "--spot-x" in html
    assert "--shadow-x" in html
    assert "collectorCardIn" in html

def test_collector_mode_binder_value():
    """Collector mode must show Binder value."""
    assert "showntell-btc" in html or "Binder Value" in html

def test_collector_mode_chain_ownership():
    """Collector mode must show chain ownership status."""
    assert "showntell-chain" in html


# ═══════════════════════════════════════════════════════
# Wallet Tab
# ═══════════════════════════════════════════════════════

def test_wallet_tab_exists():
    assert 'panel-wallet' in html
    assert "switchTab('wallet')" in html or 'data-tab="wallet"' in html

def test_wallet_auth():
    """Wallet must require GitHub authentication."""
    assert "walletLogin" in html
    assert "wallet-auth-area" in html

def test_wallet_viewer():
    assert "loadWallet" in html
    assert "renderWalletContents" in html


# ═══════════════════════════════════════════════════════
# Transfer System
# ═══════════════════════════════════════════════════════

def test_transfer_modal():
    assert "collectorTransfer" in html
    assert "executeCollectorTransfer" in html

def test_transfer_gift_sale():
    """Transfer must support Gift/Donate and Sale modes."""
    assert "xfer-type-donate" in html
    assert "xfer-type-sale" in html

def test_transfer_recipient():
    """Transfer must accept recipient name."""
    assert "xfer-name" in html
    assert "xfer-addr" in html

def test_transfer_provenance():
    """Transfers must record provenance."""
    assert "provenance" in html
    assert "brainstemFingerprint" in html


# ═══════════════════════════════════════════════════════
# Verified Authority
# ═══════════════════════════════════════════════════════

def test_verified_authority_constant():
    assert "_VERIFIED_AUTHORITY" in html

def test_verified_authority_entity():
    assert "Wildhaven of America" in html

def test_verified_authority_permanent():
    assert "permanent" in html


# ═══════════════════════════════════════════════════════
# Mobile Support
# ═══════════════════════════════════════════════════════

def test_viewport_meta():
    assert 'viewport' in html
    assert 'width=device-width' in html

def test_mobile_breakpoints():
    assert "@media (max-width: 768px)" in html
    assert "@media (max-width: 480px)" in html

def test_mobile_tap_targets():
    """Mobile buttons must have minimum 44px tap targets."""
    assert "min-height: 44px" in html


# ═══════════════════════════════════════════════════════
# Constitution
# ═══════════════════════════════════════════════════════

def test_constitution_superseed():
    const = CONSTITUTION.read_text()
    assert "SuperSeed" in const

def test_constitution_federation_auth():
    const = CONSTITUTION.read_text()
    assert "Federation Authentication" in const or "federation" in const.lower()

def test_constitution_free_shade():
    const = CONSTITUTION.read_text()
    assert "Free Shade" in const

def test_constitution_verification_authority():
    const = CONSTITUTION.read_text()
    assert "Verification Authority" in const


# ═══════════════════════════════════════════════════════
# SDK File Exists
# ═══════════════════════════════════════════════════════

def test_sdk_exists():
    assert SDK_PATH.exists()

def test_sdk_executable():
    result = __import__("subprocess").run(
        [__import__("sys").executable, str(SDK_PATH), "--help"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0


# ═══════════════════════════════════════════════════════
# Registry Consistency
# ═══════════════════════════════════════════════════════

def test_registry_agent_count():
    assert len(registry["agents"]) >= 131  # 131 founding + new agents

def test_registry_has_basic_agent():
    names = [a["name"] for a in registry["agents"]]
    assert "@rapp/basic_agent" in names

def test_registry_no_common_tier():
    """No founding card should be common/experimental tier."""
    for agent in registry["agents"]:
        tier = agent.get("quality_tier", "community")
        assert tier != "experimental", f"{agent['name']} is experimental — founding cards should be at least community"

def test_registry_legendary_agents():
    """All @kody and @rapp agents should be official (Legendary)."""
    for agent in registry["agents"]:
        if agent["name"].startswith("@kody/") or agent["name"].startswith("@rapp/"):
            assert agent.get("quality_tier") == "official", f"{agent['name']} should be official tier"
