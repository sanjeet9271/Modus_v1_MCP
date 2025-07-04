# Modus Project Quick Reference Guide

A concise reference for GitHub Copilot to avoid common mistakes with Modus components.

## Modus Component Usage

1. **ALWAYS verify component availability**: Use the `get_list_of_all_modus_components` tool to confirm that the component exists before using it.
2. **Get proper properties**: Always use the `get_component_details` tool to understand the properties, events and usage examples.
3. **Follow provided examples**: Use the pattern shown in the example code provided by the tool.
4. **Prefer native Modus components**: Use Modus components instead of creating custom ones when available.
5. **Using ModusPagination**: Use a useRef with proper event listeners for ModusPagination instead of props like `onPageChange`.

## Image URLs

1. **Use provided URLs**: Always use the exact image URLs provided by the user.
2. **Fallback strategy**: If specific URLs are not provided, use placeholder services like:
   - Trimble assets: `https://modus.trimble.com/img/` or `https://modus-bootstrap.trimble.com/img/`
   - Default placeholders: `https://picsum.photos/[width]/[height]?random=[id]`
3. **Logo variants**: For Navbar:
   - Blue variant: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg` (white version)
   - Default variant: `https://modus.trimble.com/img/trimble-logo.svg` (dark version)

## Event Handling

1. **ALWAYS use native DOM events** (not onClick/onChange). Check with `get_component_details` tool.
2. **Core pattern**: useRef + addEventListener in useEffect with proper cleanup.
3. For Navbar hamburger menu, use 'mainMenuClick' event (not 'menuButtonClick').

## SideNavigation Implementation

1. **Location**: Always implement in Layout component for persistence across pages
2. **State Management**: Use context (NavigationContext) to manage expanded state
3. **Mode**: Use "push" mode with proper targetContent selector
4. **Height**: Account for navbar height with calc(100vh - 56px)
5. **Content Area**: Must have overflow handling and proper transitions

## Common Mistakes

1. Using React event handlers instead of native DOM events
2. Missing event listener cleanup in useEffect returns
3. Double event binding (form onSubmit + button onClick)
4. Creating custom properties already provided by Modus
5. Setting wrong button types (use "button" not "submit" with event listeners)
6. Implementing SideNavigation in individual pages instead of Layout
7. Using wrong event name for hamburger menu toggle
8. **CRITICAL: ALWAYS use ModusButton instead of HTML button elements** for any buttons in the interface
9. Not providing component implementation reviews after completing each section
10. **Don't Hallucinate and write `ModusAccordion.Item` instead of `ModusAccordionItem`**

## Best Practice Examples
```tsx
// Button with native event
const btnRef = useRef<any>(null);
useEffect(() => {
  if (btnRef.current) {
    btnRef.current.addEventListener('buttonClick', handler);
    return () => btnRef.current?.removeEventListener('buttonClick', handler);
  }
}, []);
```

```jsx
// ModusTabs with proper property naming and event handling
const ModusTabsExample = () => {
  const [activeTab, setActiveTab] = useState('tab1');
  const tabsRef = useRef(null);
  
  // Tab change handler
  const handleTabChange = (e) => {
    if (e && e.detail) {
      // Access the tab id directly from e.detail
      setActiveTab(e.detail);
    }
  };
  
  // Set up event listener without dependencies to prevent unnecessary re-renders
  useEffect(() => {
    const tabsElement = tabsRef.current;
    if (tabsElement) {
      tabsElement.addEventListener('tabChange', handleTabChange);
    }
    
    return () => {
      if (tabsElement) {
        tabsElement.removeEventListener('tabChange', handleTabChange);
      }
    };
  }, []); // Empty dependency array
  
  return (
    <ModusTabs
      ref={tabsRef}
      tabs={tabs}
      ariaLabel="Example Tabs"
      fullWidth={true} // NOT full-width
    />
  );
};
```

## Implementation Reviews and Component Priority

1. **Regular implementation reviews**: After completing each major component or section, provide a brief review summarizing:
   - Components used and why they were chosen
   - Any challenges encountered and how they were solved
   - Any optimizations or improvements made

2. **Component prioritization hierarchy**:
   - **First choice**: Always use native Modus components when available
   - **Second choice**: Compose using multiple Modus components
   - **Last resort**: Only use HTML elements when no suitable Modus component exists

3. **Component substitution guide**:
   - `<button>` → `ModusButton`
   - `<input>` → `ModusTextInput`, `ModusNumberInput`, etc.
   - `<select>` → `ModusSelect`
   - `<textarea>` → `ModusTextareaInput`
   - `<div class="card">` → `ModusCard`
   - HTML tabs → `ModusAccordion` or custom tabs with Modus styling

4. **Component testing**: Always use Browser MCP to test that components render properly and maintain proper alignment and width.

5. **Modus Icons Usage**:
   - **ALWAYS verify icon names**: Use the `f1e_get_modus_icons_by_char` tool to confirm that the icon name exists before using it.
   - **Common mistakes to avoid**: 
     - Using `user` instead of `person` for user/profile icons
     - Using `contact` instead of `contacts` for contacts icon
     - Using icons without verifying they exist in the Modus icon library

6. **Navbar Variant Logos**:
   - Blue variant needs white logo: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg`
   - Default variant needs dark logo: `https://modus.trimble.com/img/trimble-logo.svg`
