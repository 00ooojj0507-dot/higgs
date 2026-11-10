# Instagram Reels Production Rules (@space_scraper_) — v3.1

v3 replaces the flat "Navy Retro" look with the **Blueprint Print** look: navy blueprint paper, one-ink rough line art, halftone-dot shading, fine paper grain.
This file is self-contained: it is the only file the reels project needs. Where two rules seem to conflict, the more specific section wins.

---

## 1. Workflow

1. When I give you a topic or raw content, do NOT build the video yet. First reply with:
   - **Developed concept:** angle, hook, target keyword, reel type (story / single-fact), the main graphic per scene, closing question and CTA.
   - **Key facts with sources:** each fact gets a source and a confidence label (확정 / 통설 / 논쟁). Flag anything unverified here, not later.
   - **Full script as a table:**
     `scene | timing | on-screen subtitle | TTS narration (conversational) | syllables / budget | link word | emphasis/effect | visual`
   - **Cover frame proposal** (which frame, within the 3:4 grid crop).
   Then ask me to confirm.
2. As soon as I say OK (or approve with edits), build the reel immediately in that same turn. Ask no further questions.
3. Deliver the finished MP4 with: Instagram caption, alt text, cover frame (full 9:16 and 3:4 grid-crop preview), and the QA checklist results (section 14).

---

## 2. Length & Structure

- **Story/explainer reels: 40–60s. Single-fact reels: 20–30s. Never over 60s.**
- Build a story arc, not a fact list: context (who/when/why it matters) → story → interpretations/reveals → closing question.
- 3–4 key facts maximum. Each fact must connect to the one before it; start each new beat with a link word ("그래서", "근데", "그러니까", "문제는").
- Cut anything that doesn't serve the hook's payoff. Fewer facts, held longer, beat many facts rushed.
- **Loop:** the closing card keeps the hook frame's background and main graphic in the same position. In the last 0.3s, hard-cut the closing question, CTA and @space_scraper_ handle out and the hook title back in, so the final frame is identical to frame 0.

---

## 3. Format & Export

- 1080x1920 (9:16), 30fps.
- Video: H.264 High, `yuv420p`, 10–12 Mbps (grain and halftone need the higher end), `-movflags +faststart`.
- Audio: AAC, 48 kHz, ≥192 kbps.
- Build with code-rendered graphics (my colornote.py approach; if that script isn't attached, write equivalent Python with Pillow/cairo + ffmpeg). No Gemini/Veo AI video for reels.
- No watermarks or third-party app logos.

---

## 4. Safe Zones (Instagram UI)

- Keep clear of the Instagram overlay: **top 220px, bottom 420px, right 150px**.
- Side margins: left ≥120px, right ≥150px (buttons sit on the right).
- **Main graphics: y 260–1280.** At least 60px clear above the subtitle box.
- **Subtitle box: vertical center y ≈ 1380–1420.**
- **Profile grid cover (3:4):** the key text and graphic of the cover frame must sit inside the center 1080x1440 area (y 240–1680).
- After building, check one frame from each scene against a safe-zone overlay.

---

## 5. Target Keyword

- Pick ONE target keyword per reel (e.g. "렘브란트 명암법").
- It must appear in: narration within the first 3s, on-screen text, caption line 1, alt text.

---

## 6. Hook (first 3 seconds)

- The hook text and main graphic are **fully rendered and static at frame 0** (no fade-in, no logo intro). Motion (zoom, pop-in, slide, halftone reveal) may start from **0.3s**.
- Narration starts within 0.2s.
- Use a provocative question, a surprising fact, or a one-line payoff promise. It must make sense with sound off.
- **Hook title: Pretendard ExtraBold 80–110px**, ivory with one key word highlighted (section 7). Restrained, not shouting.

---

## 7. Emphasis

- Every key moment gets one of:
  - zoom / push-in
  - **highlighted keyword: navy (#11192D) bold text on a rounded box in the reel's accent color** (as in "같은 [벽]에서")
  - simple animation: pop-in, slide, **halftone reveal** (dots grow from 0 to full size), **line draw-on** (the ink outline draws itself)
- At most one main emphasis per scene. Vary the type between consecutive scenes.
- Motion is crisp with ease-out.

---

## 8. Narration (TTS)

- Spoken, conversational Korean (해요체: ~잖아요, ~거든요, ~했대요, 근데, 그러니까), following the subtitles' meaning.
- Voice: `ko-KR-SunHiNeural` via edge-tts, rate `+30%`.
- **Syllable budget:** about 7–8 syllables per second of scene time. Fill the `syllables / budget` column in the script table before building; anything over budget gets rewritten.
- Each line starts ~0.1s after its subtitle and finishes before the next. If it doesn't fit, shorten the wording; never speed up further.
- **Spoken forms (rewrite in the text; edge-tts has no custom SSML for pronunciation):**
  - Numbers: 98개 → 아흔여덟 개
  - Years: 1642년 → 천육백사십이 년
  - Percent / units: 30% → 삼십 퍼센트, 5km → 오 킬로미터
  - Foreign names: write in Hangul pronunciation (Rembrandt → 렘브란트)
- The narration reads the closing question and the CTA (**≤25 syllables combined**, to fit the 3.5s ending).

---

## 9. Sound

- Short SFX (whoosh, pop, click, paper/pencil scratch for line draw-on) on transitions and emphasis, **max 1–2 per scene**, mixed at ~45% under narration. Never mask the voice.
- No BGM baked into the MP4; I may add quiet music from Instagram's library at upload.
- **Master: -14 LUFS integrated, true peak ≤ -1 dBTP.**

---

## 10. Subtitles

- Font: Pretendard only, for all text in the reel.
- Bottom-center, 36–44px, one line where possible.
- Ivory text on a semi-transparent darker navy rounded box (#080C18, ~85%). The box is clean: no grain, no halftone.
- Vertical center y ≈ 1380–1420 (see section 4). Never overlap main graphics or emphasis captions.
- Subtitles use the clean written form; narration uses the conversational version.

---

## 11. Ending (max 3.5s)

- Closing card: central question → ONE CTA → @space_scraper_.
- Layout follows the loop rule in section 2 (same background and graphic position as the hook frame; the last 0.3s returns to the hook title).
- Choose the CTA by reel type:
  - Shareable/surprising → send ("친구에게 보내주세요")
  - Reference/tips → save ("저장해두세요")
  - Opinion/taste → comment ("댓글로 알려주세요")

---

## 12. Design Tone — Blueprint Print

### Concept
- A blueprint (청사진) printed like a 1960s two-color magazine illustration: **navy paper, one bright ink, halftone dots for tone, slightly rough hand-inked lines.**
- Calm and restrained overall; the texture gives warmth, not noise.
- Style reference: a vintage two-color print portrait (blue ink on yellow paper, halftone shading, rough brush outlines, white offset underlay). Our reels invert it: **bright ink on navy paper.**
- Approved sample frame (`reel_sample_wall.jpg`, uploaded to this project as the visual reference; match it when in doubt): navy grain background, ivory title with the key word on a yuzu box, a `#222F4C` rounded panel with a rough yuzu outline, a navy hand silhouette with a yuzu outline, halftone bands along the panel's bottom and right edges, a radial halftone halo behind the hand, a few loose construction dashes.

### Palette (HEX)
- Paper (background): Deep Navy `#11192D`
- Panels / secondary planes: `#222F4C`
- Text: Ivory `#F4EEDC` (secondary text: `#A9AFC0`)
- **Ink (accent): ONE per reel.** Default Yuzu `#F2C230`. Alternatives by topic: Custard `#F3D68C` or Soft Red `#E2614A`. Never mix inks in one reel.
- **Soft Red check:** red halftone on navy has low contrast. For a Soft Red reel, render one test frame first and check it at 1/4 scale; if the halftone doesn't read, raise minimum dot coverage to ~30% and use a solid red line around the shape. The emphasis box uses the same ink.
- Ratio per frame: navy tones ~75–80%, ink (lines + halftone + fills) ~20–25%, ivory mainly for text.

### Line art (ink)
- Line art is drawn in the **ink color**, not ivory. Ivory line art only for a "contrast object" that must stand apart (max one per scene).
- Weight 10–14px at 1080 width, round caps and joins, with **slight hand-inked roughness**: low-frequency wobble (±1.5px) and ±20% weight variation along the stroke.
- **Broken lines:** 1–3 small gaps per main shape (e.g. at a corner or the top edge), like a pen lifting off.
- **Construction marks:** up to 3 short loose dashes or tick marks near the panel edge per scene. They are part of the blueprint motif, not decoration everywhere.
- Fix the random seed per shape so lines don't jitter between frames (no "line boil").

### Shapes & fills
- Silhouettes stay **as simple as possible**: a few basic shapes, readable at 1/4 scale. Detail comes from line roughness and halftone, never from extra interior lines or hatching.
- Fills are flat navy (`#11192D`) or panel (`#222F4C`). A solid ink fill is allowed on one small element per scene.
- Small cutouts in navy.

### Halftone (the only way to show tone)
- Tone, light and shadow are shown **only with halftone dots in the ink color**. No smooth gradients, no soft glows, no blur, no drop shadows.
- Dot grid: 45° (or 0° for architectural/blueprint subjects), pitch 14–18px, round dots. Tone = dot size, from ~15% to ~85% coverage.
- Uses:
  - **Shadow bands:** a halftone band along one or two edges of a panel (bottom/right = shadow side, keep it consistent within a reel).
  - **Halo:** a radial halftone behind the main subject to pull focus (replaces "glow"). Max one per scene.
  - **Form shading:** halftone on the shadow side of an object instead of a second solid plane.
- Halftone never sits behind text or inside the subtitle box.

### Paper texture
- One static fine-grain layer (monochrome, ~4–6% opacity, grain size 1–2px). Same texture in every frame; do not animate it (keeps the file sharp and the bitrate sane).
- **Layer order (bottom → top): background → panels & illustrations → grain → titles, emphasis box, subtitle box & subtitles, @handle.** Graphics get the grain; text never does.
- Optional speckle: a few tiny ink-colored specks at ≤3% opacity on panels only.
- No other textures, scratches, or paper folds.

### Optional print effect (max one scene per reel)
- **Misregistration offset:** an ivory or `#222F4C` underlay of the main silhouette shifted 4–8px down-right, like the white offset in the reference. Use for a hero moment only.

### Blueprint motifs (max one per scene)
- The default main-graphic frame — a rounded panel with a rough ink outline, its halftone shadow band and construction marks — is the base layout and does **not** count as a motif.
- Motifs (pick at most one per scene on top of the base):
  - Faint grid in `#222F4C` (pitch 60px) on the panel
  - Dimension line with end ticks and a short label
  - Corner crop marks
  - Stacked horizontal stripes that thin out

### Photos & artworks
- Images must be public domain or CC0. Credit the source in the last line of the caption.
- Default treatment: **halftone duotone** (ink dots on navy) inside a rounded panel with a rough ink outline, so photos match the illustrations.
- Show the original colors only when the scene is about color; then use a clean 24px-rounded photo with a 12px ivory frame.

### Typography
- Pretendard only. Hook title ExtraBold 80–110px; other titles Bold/ExtraBold 56–90px. Ivory, centered, the key word on an ink box (section 7).
- Text is always clean: no grain mask, roughness or halftone on letters.

### Layout & motion
- Generous whitespace. Safe zones and positions as in section 4.
- **Max 2 text elements + 1 graphic per scene.** Subtitles and the @handle don't count; an emphasis caption counts as one text element.
- Scene changes: hard cuts, a stripe wipe, or a halftone wipe (dots sweep across). No soft fades.

---

## 12-B. Illustration Sources

Use these sources, in this order of preference. Whatever the source, the result must be redrawn into the Blueprint Print style above.

1. **Code-drawn shapes** — the default. Simple silhouettes + rough ink outline + halftone.
2. **Open-source line icons** as a starting silhouette (people / objects / symbols)
   - Lucide (ISC) or Tabler Icons (MIT). Keep the license notice with any icon files.
   - Scale the stroke to 10–14px, recolor to the ink, add roughness and gaps, add a halftone or navy-fill treatment. Never use an icon as-is.
   - If the repo is available: `tools/icon_restyle.py` and `assets/icons/lucide/` do the basic recolor/stroke step.
3. **Gemini app sketches** for complex compositions
   - The Gemini Pro subscription has no API access, so this is manual: I generate the sketch in the Gemini app with the prompt below and upload it to the chat.
   - The sketch is reference only: trace the silhouette, then redraw it in the reel style (ink outline, halftone, palette). A raw AI image never appears in a reel, and no AI mark may survive into the final frame.
   - Gemini/Veo AI **video** is still not allowed.

**Gemini sketch prompt template** (replace `{subject}`):
```
1960s two-color print illustration of {subject}. Bold simple silhouette, rough brush-ink
outlines, halftone dot shading, only two inks: yellow ink on a dark navy background.
No gradients, no text, no small details. Centered with generous empty space. 1:1.
```

---

## 13. Caption & Alt Text

- Line 1: hook + target keyword, within the first 125 characters.
- 3–5 short lines in 해요체 summarizing the insight, emoji sparingly.
- A line matching the reel's CTA.
- Image source credit (if any).
- 3–5 hashtags only (hard max 5), mixing Korean and English.
- Alt text: one line, ≤100 characters, includes the target keyword.

---

## 14. QA Checklist (report with every delivery)

- [ ] Length within the range for the reel type, ≤60s
- [ ] Target keyword in narration within 0–3s, on-screen text, caption line 1, alt text
- [ ] Frame 0 fully rendered; narration starts ≤0.2s
- [ ] Every narration line fits its subtitle window (no overlap)
- [ ] Subtitles don't overlap graphics or emphasis captions; nothing in the safe-zone margins
- [ ] One ink color only (lines, halftone, emphasis box)
- [ ] Tone shown only with halftone: no smooth gradient, glow, blur or drop shadow
- [ ] Grain is static and subtle and sits under all text (layer order in section 12)
- [ ] Lines don't jitter between frames; ≤3 construction marks per scene
- [ ] Max one main emphasis per scene; types vary between consecutive scenes
- [ ] Last frame is identical to frame 0 (hook title back in, closing text out)
- [ ] Soft Red reels only: test frame checked at 1/4 scale
- [ ] Cover frame readable in the 3:4 grid crop
- [ ] Each illustration still reads at 1/4 scale; no raw AI image or untouched stock icon
- [ ] Loudness: -14 LUFS integrated, true peak ≤ -1 dBTP
- [ ] Hashtags ≤5, alt text ≤100 characters

---

## 15. After Posting

- 48h after posting, I'll share: 3-second hold rate, skip rate, average watch time, sends, saves, non-follower reach share.
- Keep a running log (topic, hook type, length, ink, metrics, what to change). If a `reels_log.md` file is available, add a row there; otherwise give me the updated row so I can paste it into the project.
- Decision rules for the next reel:
  - 3s hold rate < 60% (or high skip rate) → change the hook type (question ↔ surprising fact ↔ payoff promise).
  - Average watch time < 50% of length → cut the next reel by 5–10s.
  - Sends > saves → lean into shareable topics and the send CTA; saves > sends → reference/tips and the save CTA.
- Before proposing a new concept, check the log for what worked.
