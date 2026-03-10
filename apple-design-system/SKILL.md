---
name: apple-design-system
description: "This skill provides design guidelines, typography hierarchy, and UI patterns inspired by Apple's philosophy of minimalism and sophistication."
risk: safe
source: user
date_added: "2026-03-08"
---

# Apple Design System: Minimalism & Sophistication

This skill codifies the design principles used by Apple to create premium, high-impact web experiences. It should be used when designing new interfaces, auditing existing UIs for "premium" feel, or applying Apple's specific aesthetic standards.

## Core Principles

1. **Prioritize Content Over Chrome:** Eliminate unnecessary borders, heavy backgrounds, and decorative elements. Use whitespace and subtle separators to define structure.
2. **Generous Whitespace:** Use extreme whitespace to create a sense of luxury, confidence, and focus. Whitespace is a deliberate design element, not just empty space.
3. **Typography-Driven Hierarchy:** Lead with clear, bold typography. Let the hierarchy of font sizes and weights guide the user through the information.
4. **High-Craft Imagery:** Use high-resolution, sharp product imagery. Focus on macro details and materials. Place products on neutral (pure white or black) backgrounds to make them the "Hero".
5. **Purposeful Motion:** Animations should be smooth and communicate meaning (e.g., scroll-driven scaling) rather than being purely decorative.

## Design Foundations

### 1. Typography Hierarchy (SF Pro)

* **Hero Headers:** Extra Large, Bold (64px - 96px). Used for product names.
* **Sub-headers:** Medium/Large (24px - 48px). Used for slogans or secondary info.
* **Body Text:** Regular/Medium (17px - 21px). High readability, generous line height.
* **Action Links:** Small (14px - 17px), usually in Apple Blue (#0066CC) with a chevron icon (`>`).

### 2. Color Palette

* **Primary:** Pure White (#FFFFFF), Pure Black (#000000).
* **Secondary:** Shades of Gray for subtle depth (e.g., #F5F5F7 for backgrounds).
* **Interactive:** Apple Blue (#0066CC) for primary buttons and links.
* **Materials:** Use translucency (Blur/Glassmorphism) for sticky navigations.

### 3. Layout Patterns

* **Modular Sections:** Divide the page into full-width sections. Each section should have a single focus.
* **Grid Systems:** Use a clean 2-column or 3-column grid for secondary products/services.
* **Safe Areas:** Ensure content respects margins and safe areas, especially on mobile.

## UI Components

| Component | Standard |
|-----------|----------|
| **Primary Button** | Pill-shaped, Solid Color (Blue/White/Black), centered text. |
| **Secondary Link** | Text color #0066CC, followed by `>`. |
| **Header** | Sticky, Translucent (System Material), minimal items. |
| **Cards** | Rounded corners (unusually large radius, e.g., 20px-30px), no borders, soft shadows. |

## Implementation Checklist

* [ ] Does the page use a single, strong font family (like SF Pro)?
* [ ] Is there enough whitespace (at least 80px-120px between major sections)?
* [ ] Are the images high-resolution and centered on the product hardware/details?
* [ ] Are interactive elements (buttons/links) using the consistent blue accent?
* [ ] Does the navigation bar blur the content behind it?

## Examples

### CSS Pattern for Apple-style Blur Nav

```css
.nav-bar {
  position: sticky;
  top: 0;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}
```

### Typography Scale

```css
h1 { font-size: 80px; font-weight: 700; letter-spacing: -0.015em; }
h2 { font-size: 56px; font-weight: 600; }
p { font-size: 21px; line-height: 1.5; color: #1d1d1f; }
```
