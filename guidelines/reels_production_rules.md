# Instagram Reels Production Rules (@space_scraper_) — v2

This version resolves the contradictions in v1 and adds safe-zone, TTS-budget, audio and QA specs.
Where two rules seem to conflict, the more specific section wins.

---

## 1. Workflow

1. When I give you a topic or raw content, do NOT build the video yet. First reply with:
   - **Developed concept:** angle, hook, target keyword, reel type (story / single-fact), illustration style per scene, closing question and CTA.
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
- **Loop:** the closing card keeps the hook frame's background and main graphic in the same position. The @space_scraper_ handle drops out in the last 0.3s so the final frame matches frame 1.

---

## 3. Format & Export

- 1080x1920 (9:16), 30fps.
- Video: H.264 High, `yuv420p`, 8–12 Mbps, `-movflags +faststart`.
- Audio: AAC, 48 kHz, ≥192 kbps.
- Build with the colornote.py approach (code-rendered graphics). No Gemini/Veo AI video for reels.
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

- The hook text and main graphic are **fully rendered and static at frame 0** (no fade-in, no logo intro). Motion (zoom, pop-in, slide) may start from **0.3s**.
- Narration starts within 0.2s.
- Use a provocative question, a surprising fact, or a one-line payoff promise. It must make sense with sound off.
- **Hook title: Pretendard ExtraBold 80–110px**, ivory with one key word in the accent color. Restrained, not shouting.

---

## 7. Emphasis

- Every key moment gets one of:
  - zoom / push-in
  - **highlighted keyword caption: navy (#11192D) bold text on a box in the reel's accent color**
  - simple animation (pop-in, slide, color reveal)
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

- Short SFX (whoosh, pop, click) on transitions and emphasis, **max 1–2 per scene**, mixed at ~45% under narration. Never mask the voice.
- No BGM baked into the MP4; I may add quiet music from Instagram's library at upload.
- **Master: -14 LUFS integrated, true peak ≤ -1 dBTP.**

---

## 10. Subtitles

- Font: Pretendard only, for all text in the reel.
- Bottom-center, 36–44px, one line where possible.
- Ivory text on a semi-transparent darker navy rounded box (#080C18, ~85%).
- Vertical center y ≈ 1380–1420 (see section 4). Never overlap main graphics or emphasis captions.
- Subtitles use the clean written form; narration uses the conversational version.

---

## 11. Ending (max 3.5s)

- Closing card: central question → ONE CTA → @space_scraper_.
- Layout follows the loop rule in section 2 (same background and graphic position as the hook frame).
- Choose the CTA by reel type:
  - Shareable/surprising → send ("친구에게 보내주세요")
  - Reference/tips → save ("저장해두세요")
  - Opinion/taste → comment ("댓글로 알려주세요")

---

## 12. Design Tone (Navy Retro)

### Mood & palette
- Calm, minimal navy and ivory, with one bold retro accent. 70s print feel, kitschy but restrained.
- Background: Deep Navy `#11192D` (secondary lines/panels: `#222F4C`)
- Text & line art: Ivory `#F4EEDC` (secondary text: `#A9AFC0`)
- Accent: **ONE per reel.** Default Yuzu `#F2C230`. Alternatives by topic: Custard `#F3D68C` or Soft Red `#E2614A`. Never mix accents in one reel. The emphasis caption box uses this same accent.
- Ratio per frame: navy + ivory ~80%, accent ~20%. The accent may be used as solid fills on the main graphic.
- Flat only: no gradients, glows, shadows, blur, grain, or noise.

### Illustrations
- As simple as possible, built from a few basic shapes (rectangles, circles, simple polygons). No fine detail or hatching.
- **Choose the style by subject and state it in the concept proposal:**
  - **Objects / shapes / scenes → flat planes.** Show form with 2–3 solid planes (accent = lit, `#222F4C` = shadow, ivory = contrast object). No outlines unless a shape can't read without one.
  - **People / icons / symbols → bold ivory outlines** (10–14px at 1080 width, round caps and joins). Solid accent fills allowed; small cutouts in navy.
- One style per scene.

### Motifs, photos, typography
- Retro motifs (stacked horizontal stripes that thin out, circles, rounded rectangles): at most one per scene.
- Photos: rounded corners (24px) with a 12px ivory frame. No color filters unless the scene is about the color change.
- Images must be public domain or CC0. Credit the source in the last line of the caption.
- Typography: Pretendard only. Hook title ExtraBold 80–110px; other titles Bold/ExtraBold 56–90px. Ivory with one key word in the accent color. Centered.

### Layout & motion
- Generous whitespace. Safe zones and positions as in section 4.
- **Max 2 text elements + 1 graphic per scene.** Subtitles and the @handle don't count; an emphasis caption counts as one text element.
- Scene changes: hard cuts or a stripe wipe. No soft glow fades.

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
- [ ] One accent color only (including emphasis boxes)
- [ ] Max one main emphasis per scene; types vary between consecutive scenes
- [ ] Last frame matches frame 1 (loop)
- [ ] Cover frame readable in the 3:4 grid crop
- [ ] Loudness: -14 LUFS integrated, true peak ≤ -1 dBTP
- [ ] Hashtags ≤5, alt text ≤100 characters

---

## 15. After Posting

- 48h after posting, I'll share: 3-second hold rate, skip rate, average watch time, sends, saves, non-follower reach share.
- Log them in `guidelines/reels_log.md` (topic, hook type, length, metrics, what to change).
- Decision rules for the next reel:
  - 3s hold rate < 60% (or high skip rate) → change the hook type (question ↔ surprising fact ↔ payoff promise).
  - Average watch time < 50% of length → cut the next reel by 5–10s.
  - Sends > saves → lean into shareable topics and the send CTA; saves > sends → reference/tips and the save CTA.
- Before proposing a new concept, check the log for what worked.
