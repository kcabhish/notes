# Fluent UI (React) Cheat Sheet

## 🔧 Installation

```bash
pnpm add @fluentui/react
```

---

## 📦 Basic Imports

```tsx
import { 
  DefaultButton, PrimaryButton, IconButton,
  TextField, Checkbox, Dropdown, IDropdownOption,
  Stack, IStackTokens, Label, ThemeProvider
} from '@fluentui/react';
```

---

## 🧱 Common Components

### ✅ Button

```tsx
<PrimaryButton text="Submit" onClick={handleClick} />
<DefaultButton text="Cancel" />
<IconButton iconProps={{ iconName: 'Add' }} title="Add" />
```

### ✍️ TextField

```tsx
<TextField label="Name" placeholder="Enter your name" />
<TextField label="Password" type="password" canRevealPassword />
```

### ☑️ Checkbox

```tsx
<Checkbox label="I agree" />
```

### ⬇️ Dropdown

```tsx
const options: IDropdownOption[] = [
  { key: 'A', text: 'Option A' },
  { key: 'B', text: 'Option B' },
];

<Dropdown
  label="Select an option"
  options={options}
  placeholder="Choose..."
/>
```

---

## 📐 Layout (Stack)

```tsx
const stackTokens: IStackTokens = { childrenGap: 10 };

<Stack tokens={stackTokens}>
  <TextField label="First Name" />
  <TextField label="Last Name" />
</Stack>
```

---

## 🎨 Theming

```tsx
import { createTheme, ThemeProvider } from '@fluentui/react';

const myTheme = createTheme({
  palette: {
    themePrimary: '#0078d4',
    themeLighterAlt: '#f3f9fd',
    neutralLighter: '#f3f2f1',
  },
});

<ThemeProvider theme={myTheme}>
  <PrimaryButton text="Themed Button" />
</ThemeProvider>
```

---

## 🖌️ Custom Styles

```tsx
const customStyles = {
  root: { backgroundColor: '#f4f4f4' },
  label: { color: '#0078d4' },
};

<TextField label="Styled Field" styles={customStyles} />
```

---

## 📛 Icons

```tsx
import { initializeIcons } from '@fluentui/react';

initializeIcons();

<Icon iconName="Mail" />
<Icon iconName="AddFriend" />
```

[List of icon names](https://developer.microsoft.com/en-us/fluentui#/styles/web/icons)

---

## ♿ Accessibility Features

- All controls support keyboard navigation
- `ariaLabel`, `aria-describedby` available in props
- Supports high contrast mode

---

## 📚 Resources

- [Official Docs](https://developer.microsoft.com/en-us/fluentui)
- [Component Gallery](https://react.fluentui.dev/)
- [Theming Tool](https://fluentuipr.z22.web.core.windows.net/theming/)
