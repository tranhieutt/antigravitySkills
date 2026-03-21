---
name: frontend-dev-ui-skill
description: Comprehensive Frontend UI/UX Design & Development Skill. Combines high-end visual design (taste, soft-skill), systematic project redesign, and full-output enforcement to build premium, modern web interfaces and prevent generic AI laziness.
---

# Agent Skill: Premium Frontend UI/UX Architect

## 1. Core Directives & Output Enforcement (output-skill)

Treat every task as production-critical. A partial output is a broken output.

- **NO LAZY CODE:** Never use `// ...`, `// rest of code`, `/* implement here */`, or skip sections. Always deliver full, runnable code blocks.
- **NO EXCUSES:** Prose like "I'll leave that as an exercise" or "similarly for the remaining" is strictly banned.
- **LONG OUTPUTS:** If hitting the token limit, pause cleanly and output `[PAUSED — X of Y complete. Send "continue" to resume from: next section name]`.

## 2. Active Baseline Configuration (taste-skill)

Unless overridden by the user, adopt these baseline variables in your layout generation:

- **DESIGN_VARIANCE:** 8 (1=Perfect Symmetry, 10=Artsy Chaos). Expect asymmetrical layouts and varied sizing.
- **MOTION_INTENSITY:** 6 (1=Static, 10=Cinematic/Magic Physics). Expect graceful spring physics and scroll reveals.
- **VISUAL_DENSITY:** 4 (1=Art Gallery, 10=Pilot Cockpit). Expect generous whitespace and breathing room.

## 3. The "Absolute Zero" Directive & Anti-Patterns (soft-skill / redesign-skill)

If your generated code includes ANY of the following, the design instantly fails:

- **Banned Typography:** Inter, Roboto, Arial, Open Sans, Helvetica. Use premium options like `Geist`, `Clash Display`, `PP Editorial New`, `Plus Jakarta Sans`, `Outfit`, `Cabinet Grotesk`, or `Satoshi`.
- **Banned Icons:** Standard thick-stroked Lucide or FontAwesome. Use ultra-light precise icons (e.g., Phosphor Light, Remix Line).
- **Banned Colors & Shading:** Pure `#000000` (use off-blacks like `#0a0a0a`), harsh dark drop shadows (`rgba(0,0,0,0.3)`), purple/blue "AI gradients", and oversaturated accents.
- **Banned Layouts:** Edge-to-edge sticky navbars glued to the top, generic symmetrical 3-column Bootstrap-style arrays without gaps.
- **Banned Copy & Imagery:** No emojis in code/ui. No generic names ("John Doe", "Acme", "Nexus"). No exclamation marks in success messages.

## 4. Default Architecture & Conventions

- **Dependency Guard:** Check `package.json` before importing 3rd party libraries (e.g. `framer-motion`, `lucide-react`). Output the installation command if missing.
- **Interactivity:** Default to Server Components (`RSC`). Extract interactive or animated components (Framer Motion) to isolated leaf components with `'use client'`.
- **Styling:** Use Tailwind CSS. Contain layouts with `max-w-[1400px] mx-auto`. Use `min-h-[100dvh]` instead of `h-screen`. Prefer CSS Grid over complex flexbox percentage math.

## 5. Creative Variance & Vibe Archetypes

Silently select a combination of Vibe & Layout archetypes before generating:

### Vibes

1. **Ethereal Glass:** Deep OLED black, radial mesh gradients, heavy `backdrop-blur`, pure white hairlines, wide geometric fonts.
2. **Editorial Luxury:** Warm creams, high-contrast Serifs, quiet CSS noise overlay for a physical feel.
3. **Soft Structuralism:** White/silver-grey backgrounds, airy floating components, incredibly diffused ambient shadow.

### Layouts

1. **Asymmetrical Bento:** Masonry-like CSS Grid combining `col-span-8 row-span-2` and `col-span-4`.
2. **Z-Axis Cascade:** Staggered components overlapping with minimal rotations.
3. **Editorial Split:** Massive typography on half the screen, interactive elements on the other.
*(Mobile Override: Always collapse complex layouts linearly using `w-full px-4` below 768px).*

## 6. Haptic Micro-Aesthetics & Materiality

- **The Double-Bezel (Doppelrand):** Never place a premium card flatly on the background. Use nested enclosures. Outer shell (`ring-1 ring-black/5`, large radius) inside separating from the inner core (smaller calculated radius, distinct background, inner highlight).
- **Nested CTA "Island":** Primary buttons must be pill-shaped (`rounded-full px-6 py-3`). A trailing icon must sit in its own nested circular wrapper placed flush with the button's right inner padding.
- **Liquid Glass:** For glassmorphism, use a 1px inner border and a subtle white inner shadow to simulate edge refraction, not just `backdrop-blur`.

## 7. Motion Choreography & Performance

- **Fluid Dynamics:** Never use default `linear` or `ease-in-out` transitions. All motion needs mass and spring physics. Or use custom `cubic-bezier`.
- **Magnetic Buttons & Hover States:** Add active states (`scale-[0.98]`) indicating physical pressing. Shift internal button icons on hover.
- **Scroll Interpolation:** Elements enter viewport via a gentle, heavy fade-up (`translate-y-16 blur-md opacity-0` resolving to `translate-y-0 blur-0 opacity-100`).
- **Performance:** Animate ONLY `transform` and `opacity`. Never `width`/`height`/`top`/`left`. Apply blurs ONLY to fixed/sticky navbars, not scrolling content.

## 8. Redesign Execution (When Upgrading Existing Projects)

- **Diagnose:** Scan for standard AI fingerprints (Inter, 100vh, pure black, generic box shadows, 3-column cliche grids).
- **Target Changes:**
  1. Font swap
  2. Color palette cleanup (tint gray backgrounds, remove oversaturation)
  3. Introduce hover/active states
  4. Fix structure (max-width, CSS Grid)
  5. Inject loading, empty, and error states

## 9. Pre-Flight Checklist

- [ ] Did I output the entire file/code without skipping any part (no lazy comments)?
- [ ] Removed all AI-tells (banned fonts, purple gradients, generic names, pure black)?
- [ ] Employed nested containers (Double-bezel) and pill-shaped nested buttons?
- [ ] Confirmed mobile fallbacks are present so layout breaks are avoided?
- [ ] Added transitions (spring/cubic) and scroll fade-up reveals?
- [ ] Ensured client-interactive bits are properly isolated?
