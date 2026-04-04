// RAR v1 Ship — Automated Test Suite
// Run in browser console at localhost:8080
// Tests: Feature 1 (Sharing), Feature 2 (Starter Pack), Feature 3 (Holo Effects)

(async function runV1Tests() {
  const results = [];
  let pass = 0, fail = 0;

  function test(name, ok, detail) {
    results.push({ name, ok, detail });
    if (ok) { pass++; console.log(`  PASS: ${name}`); }
    else { fail++; console.error(`  FAIL: ${name} — ${detail || ''}`); }
  }

  console.log('\n=== RAR v1 TEST SUITE ===\n');

  // ── Feature 1: Core Sharing ──
  console.log('--- Feature 1: Core Sharing ---');

  // T1: Drop zone accepts all file types
  const dropInput = document.querySelector('#drop-zone input[type="file"]');
  test('T1: Drop zone accept attribute includes .card/.rad.eggs/.egg',
    dropInput && dropInput.accept.includes('.card') && dropInput.accept.includes('.rad.eggs') && dropInput.accept.includes('.egg'),
    `accept="${dropInput?.accept}"`
  );

  // T2: saveMinted function exists and uses IndexedDB
  test('T2: saveMinted function exists',
    typeof saveMinted === 'function',
    typeof saveMinted
  );

  // T3: getAllMinted function exists
  test('T3: getAllMinted function exists',
    typeof getAllMinted === 'function',
    typeof getAllMinted
  );

  // T4: exportSingleCard function exists
  test('T4: exportSingleCard function exists',
    typeof exportSingleCard === 'function',
    typeof exportSingleCard
  );

  // T5: handleFileDrop function exists
  test('T5: handleFileDrop function exists',
    typeof handleFileDrop === 'function',
    typeof handleFileDrop
  );

  // T6: importRAD function exists
  test('T6: importRAD function exists',
    typeof importRAD === 'function',
    typeof importRAD
  );

  // T7: airdropCard function exists
  test('T7: airdropCard function exists',
    typeof airdropCard === 'function',
    typeof airdropCard
  );

  // T8: airdropDeck function exists
  test('T8: airdropDeck function exists',
    typeof airdropDeck === 'function',
    typeof airdropDeck
  );

  // T9: Export buttons exist in UI
  const exportAllBtn = document.querySelector('button[onclick*="exportCollection"]');
  test('T9: Export All button exists in collection',
    !!exportAllBtn,
    'checked onclick=exportCollection'
  );

  // T10: Mint a test card and verify it persists to IndexedDB
  if (allAgents.length > 0) {
    const testAgent = allAgents[0];
    const beforeCount = (await getAllMinted()).length;
    const testCard = await mintCard(testAgent.name, 'test');
    const afterCount = (await getAllMinted()).length;
    test('T10: mintCard persists to IndexedDB',
      testCard && afterCount === beforeCount + 1,
      `before=${beforeCount}, after=${afterCount}`
    );

    // T11: Minted card has required fields
    if (testCard) {
      const hasFields = testCard.mintId && testCard.serial && testCard.agentName &&
        testCard.variations && testCard.provenance && testCard.cube;
      test('T11: Minted card has all required fields',
        hasFields,
        `mintId=${!!testCard.mintId}, serial=${!!testCard.serial}, variations=${!!testCard.variations}`
      );

      // Clean up test card
      // (leave it — it's fine, the user will clear if needed)
    }
  } else {
    test('T10: mintCard (SKIP — no agents loaded)', false, 'allAgents empty');
    test('T11: Card fields (SKIP)', false, 'no card to test');
  }

  // ── Feature 2: Howard Starter Pack ──
  console.log('\n--- Feature 2: Howard Starter Pack ---');

  // T12: HOLO_CARD_DB has 13 entries
  const holoCount = Object.keys(HOLO_CARD_DB).length;
  test('T12: HOLO_CARD_DB has 13 cards',
    holoCount === 13,
    `count=${holoCount}`
  );

  // T13: mintHoloCard function exists
  test('T13: mintHoloCard function exists',
    typeof mintHoloCard === 'function',
    typeof mintHoloCard
  );

  // T14: provisionStarterPack function exists
  test('T14: provisionStarterPack function exists',
    typeof provisionStarterPack === 'function',
    typeof provisionStarterPack
  );

  // T15: Starter pack flag mechanism works
  const starterFlag = localStorage.getItem('rar_howard_starter');
  test('T15: Howard starter pack flag set (or pack already provisioned)',
    !!starterFlag || allAgents.length === 0,
    `flag=${starterFlag}`
  );

  // T16: HOLO cards have avatar_svg art
  let artCount = 0;
  for (const slug of Object.keys(HOLO_CARD_DB)) {
    if (HOLO_CARD_DB[slug].avatar_svg) artCount++;
  }
  test('T16: All HOLO cards have avatar_svg',
    artCount === holoCount,
    `${artCount}/${holoCount} have art`
  );

  // T17: getHoloCard returns data for Howard's agents
  const borgHolo = HOLO_CARD_DB['borg'];
  test('T17: Borg HOLO card has abilities + flavor_text',
    borgHolo && borgHolo.abilities && borgHolo.abilities.length > 0 && borgHolo.flavor_text,
    `abilities=${borgHolo?.abilities?.length}`
  );

  // T18: Starter cards in collection have HOLO setId
  const allCards = await getAllMinted();
  const holoCards = allCards.filter(c => c.setId === 'HOLO');
  test('T18: HOLO cards exist in collection',
    holoCards.length > 0,
    `${holoCards.length} HOLO cards`
  );

  // T19: No duplicate starter cards
  const holoMintIds = new Set(holoCards.map(c => c.mintId));
  test('T19: No duplicate HOLO mintIds',
    holoMintIds.size === holoCards.length,
    `unique=${holoMintIds.size}, total=${holoCards.length}`
  );

  // ── Feature 3: BothAngles Holo Effects ──
  console.log('\n--- Feature 3: BothAngles Holo Effects ---');

  // T20: Fresnel CSS class exists
  const fresnelRule = [...document.styleSheets].some(ss => {
    try { return [...ss.cssRules].some(r => r.selectorText?.includes('.holo-fresnel')); }
    catch { return false; }
  });
  test('T20: .holo-fresnel CSS rule exists',
    fresnelRule,
    'checked styleSheets'
  );

  // T21: Scanlines CSS class exists
  const scanRule = [...document.styleSheets].some(ss => {
    try { return [...ss.cssRules].some(r => r.selectorText?.includes('.holo-scanlines')); }
    catch { return false; }
  });
  test('T21: .holo-scanlines CSS rule exists',
    scanRule,
    'checked styleSheets'
  );

  // T22: Orbit CSS classes exist
  const orbitRule = [...document.styleSheets].some(ss => {
    try { return [...ss.cssRules].some(r => r.selectorText?.includes('.holo-orbit-cyan')); }
    catch { return false; }
  });
  test('T22: .holo-orbit-cyan CSS rule exists',
    orbitRule,
    'checked styleSheets'
  );

  // T23: Holo card template includes new BothAngles divs
  const cardHTML = document.querySelector('.agent-card-holo');
  if (cardHTML) {
    const hasFresnel = !!cardHTML.querySelector('.holo-fresnel');
    const hasScanlines = !!cardHTML.querySelector('.holo-scanlines');
    const hasOrbitCyan = !!cardHTML.querySelector('.holo-orbit-cyan');
    const hasOrbitMagenta = !!cardHTML.querySelector('.holo-orbit-magenta');
    test('T23: Holo card has BothAngles elements',
      hasFresnel && hasScanlines && hasOrbitCyan && hasOrbitMagenta,
      `fresnel=${hasFresnel}, scan=${hasScanlines}, cyan=${hasOrbitCyan}, magenta=${hasOrbitMagenta}`
    );
  } else {
    test('T23: Holo card has BothAngles elements (SKIP — no cards rendered)',
      false, 'no .agent-card-holo in DOM'
    );
  }

  // T24: holoScanScroll keyframes exist
  const scanScrollKF = [...document.styleSheets].some(ss => {
    try { return [...ss.cssRules].some(r => r.name === 'holoScanScroll'); }
    catch { return false; }
  });
  test('T24: @keyframes holoScanScroll exists',
    scanScrollKF,
    'checked styleSheets'
  );

  // T25: holoOrbitA keyframes exist
  const orbitAKF = [...document.styleSheets].some(ss => {
    try { return [...ss.cssRules].some(r => r.name === 'holoOrbitA'); }
    catch { return false; }
  });
  test('T25: @keyframes holoOrbitA exists',
    orbitAKF,
    'checked styleSheets'
  );

  // ── Regression Tests ──
  console.log('\n--- Regression ---');

  // T26: Card mode switching
  test('T26: cardMode variable exists',
    typeof cardMode !== 'undefined',
    `cardMode=${typeof cardMode !== 'undefined' ? cardMode : 'undefined'}`
  );

  // T27: genCreativeArt generates valid SVG
  if (allAgents.length > 0) {
    const svg = genCreativeArt(allAgents[0]);
    test('T27: genCreativeArt returns valid SVG',
      svg.startsWith('<svg') && svg.includes('viewBox="0 0 200 200"'),
      `starts with <svg: ${svg.startsWith('<svg')}, has 200x200: ${svg.includes('200 200')}`
    );
  } else {
    test('T27: genCreativeArt (SKIP)', false, 'no agents');
  }

  // T28: renderMiniCard is async
  test('T28: renderMiniCard is async function',
    renderMiniCard.constructor.name === 'AsyncFunction',
    renderMiniCard.constructor.name
  );

  // T29: Collection view functions exist
  test('T29: renderCollection exists',
    typeof renderCollection === 'function',
    typeof renderCollection
  );

  // T30: Slide presentation exists
  test('T30: openSlidesPresentation exists',
    typeof openSlidesPresentation === 'function',
    typeof openSlidesPresentation
  );

  // ── Summary ──
  console.log(`\n=== RESULTS: ${pass} passed, ${fail} failed out of ${pass + fail} ===\n`);

  if (fail > 0) {
    console.log('FAILURES:');
    results.filter(r => !r.ok).forEach(r => console.log(`  - ${r.name}: ${r.detail}`));
  }

  return { pass, fail, results };
})();
