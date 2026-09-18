---
name: tailwind-to-mui-conversion
description: "**MANDATORY** — invoke this skill whenever you have React + Tailwind reference code that needs to become React + MUI (Material UI) for this project. This includes output from `figma-design-to-code` (the `get_design_context` tool always returns Tailwind, regardless of target stack), Tailwind snippets pasted from docs/StackOverflow/other AI tools, or any existing Tailwind-styled component being migrated to MUI. Trigger on phrases like 'convert this to MUI', 'this is still using Tailwind', 'port this component to MUI', or whenever you're about to write `className` with Tailwind utility classes into a project that uses MUI. Do NOT use this skill for converting *to* Tailwind, or for styling systems other than MUI."
disable-model-invocation: false
---

# Convert Tailwind Reference Code to MUI

Use this skill to take React code styled with Tailwind utility classes — most commonly the reference code returned by `figma-design-to-code` / `get_design_context`, but also any other Tailwind snippet — and re-express it as idiomatic React + MUI for the target project.

This skill owns the **conversion step only**. It assumes you already have Tailwind reference code in hand (from Figma, docs, a pasted snippet, or an existing file being migrated) and a target project that uses MUI. It does not fetch designs — if you don't yet have reference code and are working from a Figma link, use `figma-design-to-code` first, then hand its output to this skill.

## Direction and Scope

- You MUST use this skill whenever you are about to translate Tailwind utility classes / `className` strings into a project whose styling system is MUI.
- You MUST NOT leave any Tailwind utility classes, `className` strings, `tailwind.config.*` references, or Tailwind-specific values (arbitrary bracket values like `w-[327px]`) in the final output. If the input has them, the output must not.
- You MUST NOT invent MUI-flavored code that ignores the project's actual theme — check the theme before converting (Step 1).

## Workflow

### 1. Load the project's MUI theme before converting anything

- You MUST locate and read the project's theme definition (`createTheme(...)`, typically in `theme.ts`/`theme.js`, or a `ThemeProvider` setup) before converting any styles. Every mapping below depends on knowing the real `palette`, `spacing` unit, `typography` variants, and `breakpoints` — not MUI's out-of-the-box defaults.
- If no custom theme exists yet, use MUI's default theme values and say so, rather than silently assuming a customized one.
- You MUST also check for existing MUI-based components in the project (buttons, cards, form fields, layout wrappers) that already encode the target styling, and reuse them instead of re-deriving equivalent `sx` from scratch.

### 2. Convert structurally, not class-by-class

- Do NOT do a mechanical find-and-replace from Tailwind classes to equivalent `sx` keys that just re-encode the same utility-class thinking (e.g. turning `className="flex gap-2 p-4"` into `sx={{ display: 'flex', gap: 2, p: 4 }}` string-matched blindly). Instead, understand what the markup is doing (a row of items with spacing, a card, a form control) and express *that* using the closest MUI primitive.
- Prefer semantic MUI components over generic `Box`/`div` + `sx` wherever one exists for the pattern (see Step 3). Fall back to `Box`/`Stack` + `sx` only for genuinely custom layout.

### 3. Element-by-element mapping

Apply these conversions as defaults; override with a closer match from the project's own component library when one exists.

| Tailwind pattern in reference | MUI target |
|---|---|
| `<div>` with `flex`, `flex-col`, `gap-*`, `items-*`, `justify-*` | `Stack` (with `direction`, `spacing`, `alignItems`, `justifyContent`) |
| `<div>` with `grid`, `grid-cols-*` | `Grid` (v2) with matching `columns`/`size` props |
| generic container `<div>` with padding/margin/background only | `Box` with equivalent `sx` |
| heading/text elements (`<h1>`–`<h6>`, `<p>`, `<span>` with font utilities) | `Typography` with the closest theme `variant`; only add `sx` overrides for what the variant doesn't cover |
| `<button>` | `Button` (map `variant`/`color` from visual style — filled → `contained`, outlined → `outlined`, text-only → `text`) |
| `<input>`, `<textarea>` + label markup | `TextField` (map `type`, `multiline`, `placeholder`, `disabled`, `error` state) |
| custom checkbox/radio/toggle markup | `Checkbox` / `Radio` / `Switch` + `FormControlLabel` |
| `<select>` / custom dropdown markup | `Select` (+ `MenuItem`) or `Autocomplete` if it's a searchable dropdown |
| `<img>` | `<img>` stays (per `figma-design-to-code` asset rules) but sizing moves from Tailwind width/height classes to `sx` on a wrapping `Box`, or `component="img"` on a `Box` |
| icon `<svg>`/icon font classes | project's icon set (e.g. `@mui/icons-material`) if the glyph matches; otherwise keep the exported asset per the Figma skill's rules — never redraw the icon |
| modal/dialog markup | `Dialog` / `Modal` |
| card-like container (rounded, shadow, padding) | `Card` (+ `CardContent`, `CardActions` as needed) |

### 4. Style-property mapping

| Tailwind concept | MUI target |
|---|---|
| Spacing utilities (`p-*`, `m-*`, `gap-*`, `space-x-*`/`space-y-*`) | `theme.spacing()` via `sx` (`p`, `m`, `gap`) or component `spacing` props (`Stack spacing={2}`) — using the project's real spacing unit, not an assumed `4px`/`8px` grid |
| Color utilities (`bg-*`, `text-*`, `border-*`) and raw hex from design tokens | `theme.palette.*` references (`palette.primary.main`, `palette.text.secondary`, `palette.divider`, etc.); use a literal hex only when no palette token reasonably matches, and call that out as a gap |
| Font size/weight/line-height utilities | The `Typography` `variant` that already encodes them; use `sx` overrides only for genuine one-offs, not to reconstruct a whole type scale inline |
| Border radius utilities (`rounded-*`) | `theme.shape.borderRadius` (via `sx={{ borderRadius: n }}`, where `n` is a multiplier of the theme value, not a hardcoded px unless the design truly diverges) |
| Shadow utilities (`shadow-*`) | `theme.shadows[n]` (via `elevation` prop on components that support it, e.g. `Paper`, `Card`, or `sx={{ boxShadow: n }}`) |
| Width/height utilities, including arbitrary values (`w-[327px]`) | Numeric/percentage `sx` (`width`, `height`); keep arbitrary pixel values only if there's no cleaner responsive/theme-based expression |
| Responsive prefixes (`sm:`, `md:`, `lg:`, …) | `sx` responsive object syntax (`sx={{ width: { xs: '100%', md: '50%' } }}`) mapped to the project's actual configured breakpoints, not Tailwind's default breakpoint values |
| State variants (`hover:`, `focus:`, `disabled:`) | `sx` pseudo-selectors (`sx={{ '&:hover': { ... } }}`) or, where MUI already handles the state via props/theme (e.g. `disabled` on `Button`), use that instead of hand-rolled CSS |
| Transition/animation utilities | `theme.transitions.create(...)` via `sx`, or `sx={{ transition: ... }}` matching the project's existing motion conventions |

### 5. Complex or unmapped styling

- If a Tailwind pattern doesn't map cleanly to a prop or theme token, use a `styled()` component (colocated with the component it styles) rather than a large inline `sx` object with hardcoded values, especially for anything reused across multiple places.
- Do NOT silently approximate — if the exact spacing/color/size from the reference has no clean theme equivalent, note the discrepancy (e.g. "used `palette.grey[300]` as the closest match; reference used `#e4e4e7`") rather than presenting it as an exact match.

### 6. Verify before finishing

- You MUST grep the converted output for lingering Tailwind residue — `className=`, utility-class strings, `tailwind.config` imports — and remove/convert anything found.
- You MUST confirm every color, spacing, and typography choice traces back to a theme token or an explicitly-noted exception, not a value copied straight from the Tailwind reference.
- You MUST confirm images/icons still follow the source skill's asset rules (real exported asset or matched project icon — never hand-drawn SVG).

## Error Recovery

- If you can't locate a project theme file, say so explicitly, proceed with MUI defaults, and flag that palette/spacing choices should be revisited once a theme exists.
- If a Tailwind pattern in the reference has no reasonable MUI/theme equivalent even after checking `styled()`, keep the closest approximation, note it inline as a comment, and surface it to the user rather than guessing silently.
