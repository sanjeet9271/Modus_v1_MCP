# <ModusAccordion>

## Prompt 1
**User Question:** Create a webpage with an accordion containing three items, each with a different expand button type, and log messages when items are opened or closed?

**Agent Answer:**
References:
To create an accordion with three items where each item has a different expand button type and logs a message when opened or closed, we will use the `<ModusAccordion>` component. We will set the `expandButtonType` property for each item and add event listeners for the `opened` and `closed` events.

The approach involves:
1. Using the `<ModusAccordion>` component to create the accordion.
2. Adding three `<ModusAccordionItem>` components inside the accordion, each with a different `expandButtonType`.
3. Using `useRef` and `useEffect` hooks to add event listeners for the `opened` and `closed` events to log messages when an accordion item is opened or closed.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusAccordion, ModusAccordionItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const accordionRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const accordion = accordionRef.current?.querySelector('modus-accordion');
    if (accordion) {
      const handleOpened = (event: Event) => {
        console.log('Accordion item opened:', event);
      };
      const handleClosed = (event: Event) => {
        console.log('Accordion item closed:', event);
      };
      accordion.addEventListener('opened', handleOpened);
      accordion.addEventListener('closed', handleClosed);
      return () => {
        accordion.removeEventListener('opened', handleOpened);
        accordion.removeEventListener('closed', handleClosed);
      };
    }
  }, []);

  return (
    <div id="accordion-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }} ref={accordionRef}>
      <ModusAccordion>
        <ModusAccordionItem headerText="Item 1" expandButtonType="standardArrow">
          Content for Item 1
        </ModusAccordionItem>
        <ModusAccordionItem headerText="Item 2" expandButtonType="circleArrow">
          Content for Item 2
        </ModusAccordionItem>
        <ModusAccordionItem headerText="Item 3" expandButtonType="plusMinus">
          Content for Item 3
        </ModusAccordionItem>
      </ModusAccordion>
    </div>
  );
};

export default MyComponent;
```

# <ModusAlert>

## Prompt 1
**User Question:** Create a webpage with various alert types including default info, dismissible, action button, error, success, warning, and info with a link.

**Agent Answer:**
References:
To create a webpage with various alert types, we will use the `ModusAlert` component from the Modus design system. We'll display seven different alert variations: a default info alert, a dismissible alert, an alert with an action button, an error alert, a success alert, a warning alert, and an info alert with a link. The alerts will be stacked vertically with proper spacing between them.

```tsx
import React from 'react';
import { ModusAlert } from '@trimble-oss/modus-react-components';

const AlertExamples: React.FC = () => {
  return (
    <div id="alert-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px' }}>
      <ModusAlert message="Info alert (default)" />
      <ModusAlert dismissible message="Dismissible alert" />
      <ModusAlert message="Info alert with action button" buttonText="Action" />
      <ModusAlert message="Error alert" type="error" />
      <ModusAlert message="Success alert" type="success" />
      <ModusAlert message="Warning alert" type="warning" />
      <ModusAlert type="info">
        This is a info alert with <a href="#">an example link</a>
      </ModusAlert>
    </div>
  );
};

export default AlertExamples;
```

# <ModusBadge>

## Prompt 1
**User Question:** Create a webpage with 4 badges: a small primary badge with the text "New", a medium secondary badge with the text "Update", a large success badge with the text "Completed", and a small counter badge with the text "5".

**Agent Answer:**
References:
To create the webpage with the specified badges, we need to use the `<ModusBadge>` component from the Modus design system. The badges will be placed inside a `<div>` with `display: flex`, `flex-direction: column`, and `gap: 8px` to ensure proper alignment and spacing. The `<div>` also has `padding: 16px` and `overflow: auto` to enhance the user experience and ensure scrolling is enabled. The first badge is a small primary badge with the text "New". The second badge is a medium secondary badge with the text "Update". The third badge is a large success badge with the text "Completed". The fourth badge is a small counter badge with the text "5".

```tsx
import React from 'react';
import { ModusBadge } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="badge-container" style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '16px', overflow: 'auto' }}>
      <ModusBadge size="small" color="primary">New</ModusBadge>
      <ModusBadge size="medium" color="secondary">Update</ModusBadge>
      <ModusBadge size="large" color="success">Completed</ModusBadge>
      <ModusBadge size="small" type="counter">5</ModusBadge>
    </div>
  );
};

export default MyComponent;
```


# <ModusBreadcrumb>  

## Prompt 1
**User Question:** Create a breadcrumb component with crumbs "Home", "About", "Services", "Contact" and log the clicked crumb object to the console?
**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a breadcrumb component with four crumbs: "Home", "About", "Services", and "Contact". Additionally, we need to add an event listener to log the clicked crumb object to the console. We broke down the problem into creating the breadcrumb component, defining the crumbs, and adding the event listener.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusBreadcrumb } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const breadcrumbRef = useRef<any>(null);

  useEffect(() => {
    const crumbs = [
      { id: '1', display: 'Home' },
      { id: '2', display: 'About' },
      { id: '3', display: 'Services' },
      { id: '4', display: 'Contact' },
    ];

    if (breadcrumbRef.current) {
      breadcrumbRef.current.crumbs = crumbs;
      breadcrumbRef.current.addEventListener('crumbClick', (event: CustomEvent) => {
        console.log('Clicked crumb:', event.detail);
      });
    }
  }, []);

  return (
    <ModusBreadcrumb ref={breadcrumbRef} />
  );
};

export default MyComponent;
```

# <ModusButtonGroup>

## Prompt 1
**User Question:** Create a webpage with a button group that has three buttons labeled "Option 1", "Option 2", and "Option 3". The button group should allow only single selection, and the first button should be selected by default.
**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a button group with three buttons labeled "Option 1", "Option 2", and "Option 3". The button group should allow only single selection, and the first button should be selected by default. We will use the `selection-type` attribute set to "single" and the `selected` attribute for the first button.

```tsx
import React from 'react';
import { ModusButton, ModusButtonGroup } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="button-group-container" style={{ padding: '16px' }}>
      <ModusButtonGroup selection-type="single">
        <ModusButton selected>Option 1</ModusButton>
        <ModusButton>Option 2</ModusButton>
        <ModusButton>Option 3</ModusButton>
      </ModusButtonGroup>
    </div>
  );
};

export default MyComponent;
```

# <ModusButton>

## Prompt 1
**User Question:** Create a webpage with a disabled primary button that shows a loading spinner, a borderless secondary button, and an outline tertiary button.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three buttons with different styles and states. The first button is a disabled primary button with a loading spinner to indicate an ongoing process. The second button is a borderless secondary button for a minimalistic look. The third button is an outline tertiary button for a less emphasized action.

```tsx
import React from 'react';
import { ModusButton, ModusSpinner } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px' }}>
      <ModusButton color="primary" disabled>
        <ModusSpinner color="white" size=".5rem" />
        &nbsp;Loading...
      </ModusButton>
      <ModusButton buttonStyle="borderless" color="secondary">Borderless</ModusButton>
      <ModusButton buttonStyle="outline" color="tertiary">Outline</ModusButton>
    </div>
  );
};

export default MyComponent;
```

# <ModusCard>

## Prompt 1
**User Question:** Create a card with the title "Welcome", subtitle "Introduction", and content "This is a sample card." The card should have a height of 300px, width of 200px, border radius of 10px, and show a shadow on hover.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a card with a specified title, subtitle, and content. The card should have a height of 300px, width of 200px, and a border radius of 10px. Additionally, it should show a shadow on hover. The card is designed using the `<ModusCard>` component with the specified properties. Inside the card, there is a `<div>` with padding that contains the title, subtitle, content, and a button. The button is created using the `<ModusButton>` component with the primary color.

```tsx
import React from 'react';
import { ModusCard, ModusButton } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="card-container1" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusCard height="300px" width="200px" borderRadius="10px" showCardBorder={true} showShadowOnHover={true}>
        <div style={{ padding: '10px' }}>
          <h4>Welcome</h4>
          <h5>Introduction</h5>
          <p>This is a sample card.</p>
          <ModusButton color="primary">Go somewhere</ModusButton>
        </div>
      </ModusCard>
    </div>
  );
};

export default MyComponent;
```

# <ModusChip>

## Prompt 1
**User Question:** Create a webpage with three chips: an active chip labeled "Active Chip", a disabled chip labeled "Disabled Chip", and an error chip labeled "Error Chip". Each chip should have an image and a close button.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create three chips with different states and values. The first chip is active with the value "Active Chip". The second chip is disabled with the value "Disabled Chip". The third chip has an error state with the value "Error Chip". All chips should have an image and a close button. The image URL is set to "https://example.com/image.jpg" for all chips.

```tsx
import React from 'react';
import { ModusChip } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="chip-container" style={{ display: 'flex', flexDirection: 'row', gap: '16px', padding: '16px' }}>
      <ModusChip active imageUrl="https://example.com/image.jpg" showClose value="Active Chip"></ModusChip>
      <ModusChip disabled imageUrl="https://example.com/image.jpg" showClose value="Disabled Chip"></ModusChip>
      <ModusChip hasError imageUrl="https://example.com/image.jpg" showClose value="Error Chip"></ModusChip>
    </div>
  );
};

export default MyComponent;
```

# <ModusTreeView>

## Prompt 1

**User Question:** Create a webpage with a tree view that shows an email folder structure. Include main folders for "Inbox" (with sub-folders "Personal", "Work", "Social", and "More..."), "Archived" (with nested folders containing files), and "Spam". Make sure the tree view has a width of 400px and doesn't allow multiple selections.

**Agent Answer:**
References:
To create a tree view with an email folder structure, we'll use the `<ModusTreeView>` component with nested `<ModusTreeViewItem>` components to represent the hierarchical structure. The tree will have a width of 400px and will be configured to not allow multiple selections or checkbox selections. We'll create a main container with appropriate styling for the component.

```tsx
import React from 'react';
import { ModusTreeView, ModusTreeViewItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="tree-view-container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusTreeView style={{ width: '400px' }} checkboxSelection={false} multiCheckboxSelection={false} multiSelection={false}>
        <ModusTreeViewItem nodeId="1" label="Inbox">
          <ModusTreeViewItem nodeId="2" label="Personal" />
          <ModusTreeViewItem nodeId="3" label="Work" />
          <ModusTreeViewItem nodeId="4" label="Social" />
          <ModusTreeViewItem nodeId="5" label="More ..." />
        </ModusTreeViewItem>
        <ModusTreeViewItem nodeId="6" label="Archived">
          <ModusTreeViewItem nodeId="7" label="Folder1">
            <ModusTreeViewItem nodeId="8" label="File1" />
            <ModusTreeViewItem nodeId="9" label="Folder2">
              <ModusTreeViewItem nodeId="10" label="File2" />
            </ModusTreeViewItem>
            <ModusTreeViewItem nodeId="11" label="File3" />
          </ModusTreeViewItem>
        </ModusTreeViewItem>
        <ModusTreeViewItem nodeId="12" label="Spam" />
      </ModusTreeView>
    </div>
  );
};

export default MyComponent;
```

## Prompt 2

**User Question:** Create a webpage with a tree view that displays an email folder structure with an icon for the Inbox folder. The tree should include an "Inbox" with sub-folders "Personal", "Work", "Social", and "More..." as the last child item.

**Agent Answer:**
References:
To create a tree view with an email folder structure that includes icons, we'll use the `<ModusTreeView>` component with nested `<ModusTreeViewItem>` components. The tree will have a width of 400px and will display an inbox icon for the main folder. We'll set up the structure with "Inbox" as the parent folder containing sub-folders "Personal", "Work", "Social", and "More..." with the last one marked as the last child using the `isLastChild` property.

```tsx
import React from 'react';
import { ModusTreeView, ModusTreeViewItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="tree-view-container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusTreeView style={{ width: '400px' }}>
        <ModusTreeViewItem nodeId="1" label="Inbox">
          <svg slot="itemIcon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" height="16" width="16" viewBox="0 0 32 32">
            <path d="M28.79 12.39A1 1 0 0 0 28 12h-2V9c0-.55-.45-1-1-1h-9.59l-1.7-1.71C13.52 6.11 13.27 6 13 6H4c-.55 0-1 .45-1 1v17c0 .04.02.07.02.11.01.05.02.11.04.16.02.09.06.17.1.25.02.03.02.06.05.09.01.01.03.02.04.03.07.08.15.14.23.19.04.03.06.05.1.07.13.06.27.1.42.1h21c.13 0 .25-.03.36-.07.04-.02.07-.04.1-.06.07-.04.14-.08.2-.13.03-.03.06-.06.09-.1.05-.05.09-.11.12-.18a.31.31 0 0 0 .06-.13c.01-.02.03-.04.03-.07l3-11c.09-.3.02-.62-.17-.87zM5 8h7.59l1.7 1.71c.19.18.44.29.71.29h9v2H7c-.45 0-.85.3-.96.74L5 16.53V8z"></path>
          </svg>
          <ModusTreeViewItem nodeId="2" label="Personal" />
          <ModusTreeViewItem nodeId="3" label="Work" />
          <ModusTreeViewItem nodeId="4" label="Social" />
          <ModusTreeViewItem nodeId="5" label="More ..." isLastChild={true} />
        </ModusTreeViewItem>
      </ModusTreeView>
    </div>
  );
};

export default MyComponent;
```

## Prompt 3

**User Question:** Create a tree view with an action bar that allows users to add, remove, edit, copy, expand, collapse, and enable drag-and-drop functionality for tree nodes. The tree should display an email folder structure with "Inbox" (containing "Personal", "Work", "Social", and "More...") and "Archived" (with "Folder1" containing "File1" and "File3").

**Agent Answer:**
References:
To create a tree view with an action bar that provides comprehensive node management functionality, we'll use the `<ModusTreeView>` and `<ModusButton>` components. The action bar includes buttons for adding, removing, editing, copying, expanding/collapsing all items, and enabling drag-and-drop functionality. Each button has appropriate icon SVGs and initially starts disabled. The tree view displays an email folder structure with "Inbox" and "Archived" folders and their respective nested items. The implementation uses event listeners to manage button state based on selected items and implement the functionality for each action button.

```tsx
import React, { useEffect } from 'react';
import { ModusButton, ModusTreeView, ModusTreeViewItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const container = document.querySelector("div[id='tree-with-action-bar']");
    const root = container?.querySelector('modus-tree-view') as any;
    const addButton = container?.querySelector("modus-button[id='add']") as any;
    const removeButton = container?.querySelector("modus-button[id='remove']") as any;
    const editButton = container?.querySelector("modus-button[id='edit']") as any;
    const copyButton = container?.querySelector("modus-button[id='copy']") as any;
    const expandAllButton = container?.querySelector("modus-button[id='expand']") as any;
    const collapseAllButton = container?.querySelector("modus-button[id='collapse']") as any;
    const dragButton = container?.querySelector("modus-button[id='drag']") as any;

    const disableButtons = (disable: boolean) => {
      removeButton.disabled = disable;
      copyButton.disabled = disable;
      editButton.disabled = disable;
    };

    const getChildren = (element: any) => {
      const children = element.querySelectorAll('modus-tree-view-item');
      if (!children) return [];
      return Array.from(children).reduce((r, c) => {
        r.push(c, ...getChildren(c));
        return r;
      }, []);
    };

    const getItems = () =>
      new Map(
        Array.from(root.querySelectorAll('modus-tree-view-item')).map((i: any) => [
          i.nodeId,
          i.label,
        ])
      );

    const querySelect = (itemId: string) =>
      container?.querySelector("modus-tree-view-item[node-id='" + itemId + "']");

    addButton.disabled = false;
    expandAllButton.disabled = false;
    collapseAllButton.disabled = false;

    container?.addEventListener('itemClick', () => {
      if (root.selectedItems.length > 0) {
        disableButtons(false);
      } else {
        disableButtons(true);
      }
    });

    addButton?.addEventListener('buttonClick', () => {
      const nodeId =
        container?.querySelectorAll('modus-tree-view-item').length + 1;
      const selectedItems = root.selectedItems;
      if (nodeId) {
        const selectedItemId =
          selectedItems && selectedItems.length > 0 ? selectedItems[0] : null;
        const selectedItemElement = querySelect(selectedItemId);
        const selectedItemParent = selectedItemElement?.parentElement;
        const newNode = document.createElement('modus-tree-view-item');
        newNode.nodeId = nodeId;
        newNode.editable = true;
        const insertParent = selectedItemParent || root;
        const insertBeforeElement =
          selectedItemElement || root.firstElementChild;
        insertParent.insertBefore(newNode, insertBeforeElement);
      }
    });

    removeButton?.addEventListener('buttonClick', () => {
      const selectedItems = root.selectedItems;
      selectedItems?.forEach((i: any) => {
        const selectedItemElement = querySelect(i);
        const selectedItemParent = selectedItemElement?.parentElement;
        if (selectedItemElement) {
          selectedItemParent.removeChild(selectedItemElement);
        }
      });

      if (!Array.from(getItems()).length) {
        container
          ?.querySelectorAll('modus-button')
          .forEach((b: any) => (b.disabled = true));
      } else disableButtons(true);
    });

    editButton?.addEventListener('buttonClick', () => {
      const selectedItems = root.selectedItems;
      const selectedItemId =
        selectedItems && selectedItems.length > 0 ? selectedItems[0] : null;
      const selectedItemElement = querySelect(selectedItemId);
      selectedItemElement.editable = true;
    });

    copyButton?.addEventListener('buttonClick', () => {
      const nodeId =
        container?.querySelectorAll('modus-tree-view-item').length + 1;
      const selectedItems = root.selectedItems;
      const selectedItemId =
        selectedItems && selectedItems.length > 0 ? selectedItems[0] : null;
      const selectedItemElement = querySelect(selectedItemId);
      if (selectedItemElement) {
        const newNode = selectedItemElement.cloneNode(true) as any;
        newNode.nodeId = nodeId;
        newNode.editable = true;
        newNode.label = 'Copy of ' + selectedItemElement.label;

        let count = nodeId + 1;
        getChildren(newNode).forEach((c: any) => {
          c.nodeId = count;
          count++;
        });

        (selectedItemElement.parentElement || root).insertBefore(
          newNode,
          selectedItemElement
        );
      }
    });

    expandAllButton?.addEventListener('buttonClick', () => {
      root.expandedItems = Array.from(getItems().keys());
      expandAllButton.style.display = 'none';
      collapseAllButton.style.display = 'inline-block';
    });

    collapseAllButton?.addEventListener('buttonClick', () => {
      root.expandedItems = [];
      collapseAllButton.style.display = 'none';
      expandAllButton.style.display = 'inline-block';
    });

    dragButton?.addEventListener('buttonClick', () => {
      root.enableReordering = !root.enableReordering;
    });
  }, []);

  return (
    <div id="tree-with-action-bar" style={{ display: 'flex', flexDirection: 'column', width: '400px' }}>
      <div style={{ display: 'flex', justifyContent: 'end', flexWrap: 'wrap', marginTop: '1rem' }}>
        <ModusButton buttonStyle="borderless" ariaLabel="Add" title="Add" size="small" color="primary" disabled id="add">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0,0H24V24H0Z" fill="none" />
            <path d="M19,13H13v6H11V13H5V11h6V5h2v6h6Z" fill="#252a2e" />
          </svg>
        </ModusButton>
        <ModusButton buttonStyle="borderless" ariaLabel="Remove" title="Remove" size="small" color="primary" disabled id="remove">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0,0H24V24H0Z" fill="none" />
            <path d="M6,19a2.006,2.006,0,0,0,2,2h8a2.006,2.006,0,0,0,2-2V7H6ZM19,4H15.5l-1-1h-5l-1,1H5V6H19Z" fill="#252a2e" />
          </svg>
        </ModusButton>
        <ModusButton buttonStyle="borderless" size="small" ariaLabel="Edit" title="Edit" color="primary" disabled id="edit">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0,0H24V24H0Z" fill="none" />
            <path d="M3,17.25V21H6.75L17.81,9.94,14.06,6.19ZM20.71,7.04a1,1,0,0,0,0-1.41L18.37,3.29a1,1,0,0,0-1.41,0L15.13,5.12l3.75,3.75,1.83-1.83Z" fill="#252a2e" />
          </svg>
        </ModusButton>
        <ModusButton buttonStyle="borderless" size="small" ariaLabel="Copy" title="Copy" color="primary" disabled id="copy">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0,0H24V24H0Z" fill="none" />
            <path d="M16,1H4A2.006,2.006,0,0,0,2,3V17H4V3H16Zm3,4H8A2.006,2.006,0,0,0,6,7V21a2.006,2.006,0,0,0,2,2H19a2.006,2.006,0,0,0,2-2V7A2.006,2.006,0,0,0,19,5Zm0,16H8V7H19Z" fill="#252a2e" />
          </svg>
        </ModusButton>
        <ModusButton buttonStyle="borderless" size="small" ariaLabel="Drag" title="Drag" color="primary" disabled id="drag">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M11,18a2,2,0,1,1-2-2A2.006,2.006,0,0,1,11,18ZM9,10a2,2,0,1,0,2,2A2.006,2.006,0,0,0,9,10ZM9,4a2,2,0,1,0,2,2A2.006,2.006,0,0,0,9,4Zm6,4a2,2,0,1,0-2-2A2.006,2.006,0,0,0,15,8Zm0,2a2,2,0,1,0,2,2A2.006,2.006,0,0,0,15,10Zm0,6a2,2,0,1,0,2,2A2.006,2.006,0,0,0,15,16Z" fill="#252a2e" />
          </svg>
        </ModusButton>
        <ModusButton buttonStyle="borderless" size="small" ariaLabel="Expand" title="Expand" color="primary" disabled id="expand">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0,0H24V24H0Z" fill="rgba(0,0,0,0)" />
            <path d="M12,5.83,15.17,9l1.41-1.41L12,3,7.41,7.59,8.83,9Zm0,12.34L8.83,15,7.42,16.41,12,21l4.59-4.59L15.17,15Z" fill="#252a2e" />
          </svg>
        </ModusButton>
        <ModusButton buttonStyle="borderless" size="small" ariaLabel="Collapse" title="Collapse" color="primary" disabled style={{ display: 'none' }} id="collapse">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0,0H24V24H0Z" fill="none" />
            <path d="M7.41,18.59,8.83,20,12,16.83,15.17,20l1.41-1.41L12,14ZM16.59,5.41,15.17,4,12,7.17,8.83,4,7.41,5.41,12,10Z" fill="#252a2e" />
          </svg>
        </ModusButton>
      </div>
      <ModusTreeView>
        <ModusTreeViewItem nodeId="1" label="Inbox">
          <ModusTreeViewItem nodeId="2" label="Personal" />
          <ModusTreeViewItem nodeId="3" label="Work" />
          <ModusTreeViewItem nodeId="4" label="Social" />
          <ModusTreeViewItem nodeId="5" label="More ..." />
        </ModusTreeViewItem>
        <ModusTreeViewItem nodeId="6" label="Archived">
          <ModusTreeViewItem nodeId="7" isLastChild={true} label="Folder1">
            <ModusTreeViewItem nodeId="8" label="File1" />
            <ModusTreeViewItem nodeId="9" isLastChild={true} label="File3" />
          </ModusTreeViewItem>
        </ModusTreeViewItem>
      </ModusTreeView>
    </div>
  );
};

export default MyComponent;
```
    



# <ModusDataTable>

## Prompt 1
**User Question:** Create a table with columns "Name", "Age", and "Contacted". The "Name" column should have a width of 50%, the "Age" column should be right-aligned, and the "Contacted" column should have default settings. The table should have three rows with the following data: {name: 'John', age: 25, contacted: false}, {name: 'Jane', age: 26, contacted: false}, {name: 'Joe', age: 27, contacted: true}.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a data table with three columns: "Name", "Age", and "Contacted". The "Name" column should have a width of 50%, the "Age" column should be right-aligned, and the "Contacted" column should have default settings. The table should have three rows with the specified data.

```tsx
import React, { useEffect } from 'react';
import { ModusDataTable } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const dataTable = document.querySelector('modus-data-table') as any;
    if (dataTable) {
      dataTable.columns = [
        { display: 'Name', id: 'name', width: '50%' },
        { display: 'Age', id: 'age', align: 'right' },
        { display: 'Contacted', id: 'contacted' },
      ];

      const john = { name: 'John', age: 25, contacted: false };
      const jane = { name: 'Jane', age: 26, contacted: false };
      const joe = { name: 'Joe', age: 27, contacted: true };
      dataTable.data = [john, jane, joe];
    }
  }, []);

  return <ModusDataTable />;
};

export default MyComponent;
```

# <ModusDropdown>

## Prompt 1

**User Question:** Create a webpage with a dropdown that uses a chip as the toggle element. The chip should have the value "Dropdown Chip" and be in an advanced state. The dropdown should contain a list of options.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a dropdown that uses a chip as the toggle element. The chip should have the value "Dropdown Chip" and be in an advanced state. The dropdown should contain a list of options. The approach involves using the `<ModusDropdown>` component for the dropdown and the `<ModusChip>` component for the toggle element. The `<ModusList>` and `<ModusListItem>` components are used to create the list of options within the dropdown.

```tsx
import React from 'react';
import { ModusChip, ModusDropdown, ModusList, ModusListItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="dropdown-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px' }}>
      <ModusDropdown label="Dropdown" id="dropdown" toggle-element-id="toggleElement" animate-list>
        <ModusChip
          id="toggleElement"
          slot="dropdownToggle"
          advanced-chip
          value="Dropdown Chip"></ModusChip>
        <ModusList slot="dropdownList">
          <ModusListItem value="1" disabled borderless>Select Process</ModusListItem>
          <ModusListItem value="2" borderless>First Option (FO)</ModusListItem>
          <ModusListItem value="3" borderless>Second Option (SO)</ModusListItem>
          <ModusListItem value="4" borderless>Next Option (NO)</ModusListItem>
          <ModusListItem value="5" borderless>Another Option (AO)</ModusListItem>
        </ModusList>
      </ModusDropdown>
    </div>
  );
};

export default MyComponent;
```

# <ModusFileDropzone>

## Prompt 1
**User Question:** Create a file dropzone that accepts only PDF files. When a file is uploaded, log the file details and any error to the console. Also, provide a button to add a file programmatically and another button to remove a file by its name.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a file dropzone that accepts only PDF files. We will use the `acceptFileTypes` property to specify the accepted file types. We will add event listeners to log the file details and any error to the console when files are uploaded. Additionally, we will provide buttons to add a file programmatically using the `addFile` method and to remove a file by its name using the `removeFile` method.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusFileDropzone, ModusButton } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const fileDropzoneRef = useRef<any>(null);

  useEffect(() => {
    const fileDropzone = fileDropzoneRef.current;
    if (fileDropzone) {
      fileDropzone.addEventListener('files', (event: CustomEvent<[File[], string | null]>) => {
        const [files, error] = event.detail;
        console.log(files);
        console.log(error);
      });
    }
  }, []);

  const addFile = () => {
    const file = new File(["content"], "example.pdf", { type: "application/pdf" });
    fileDropzoneRef.current.addFile(file);
  };

  const removeFile = () => {
    fileDropzoneRef.current.removeFile("example.pdf");
  };

  return (
    <div>
      <ModusFileDropzone
        ref={fileDropzoneRef}
        ariaLabel="dropzone"
        description="Upload your PDF files here"
        dropzoneHeight="175px"
        dropzoneWidth="400px"
        label="PDF Dropzone"
        multiple={false}
        acceptFileTypes="application/pdf"
      />
      <ModusButton onClick={addFile}>Add File</ModusButton>
      <ModusButton onClick={removeFile}>Remove File</ModusButton>
    </div>
  );
};

export default MyComponent;
```


# <ModusIcon>

## Prompt 1
**User Question:** Create a webpage with three icons: a red "home" icon (size 30), a green "settings" icon (size 40), and a blue "user" icon (size 50). Log the name of the clicked icon to the console.
**Agent Answer:**
References:
To meet the requirements, we need to create three icons with specified colors, names, and sizes. Additionally, we will add an event listener to log the name of the clicked icon to the console.

```tsx
import React, { useEffect } from 'react';
import { ModusIcon } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const icons = document.querySelectorAll('modus-icon');
    icons.forEach((icon) => {
      icon.addEventListener('iconClick', (event: Event) => {
        console.log('Icon clicked:', (event.target as HTMLElement).getAttribute('name'));
      });
    });
  }, []);

  return (
    <div style={{ display: 'flex', gap: '16px', padding: '16px' }}>
      <ModusIcon name="home" color="red" size="30"></ModusIcon>
      <ModusIcon name="settings" color="green" size="40"></ModusIcon>
      <ModusIcon name="user" color="blue" size="50"></ModusIcon>
    </div>
  );
};

export default MyComponent;
```


# <ModusModal>

## Prompt 1
**User Question:** Create a modal with the header text "User Information", primary button text "Submit", and secondary button text "Cancel"? The modal should have a paragraph with the text "Please fill out the form below." and two input fields for "Name" and "Email".

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a modal with a header text "User Information", primary button text "Submit", and secondary button text "Cancel". The modal should contain a paragraph with the text "Please fill out the form below." and two input fields for "Name" and "Email". The primary button is used for submitting the form, hence it is given the primary color. The secondary button is for canceling the action, hence it is given the secondary color. The input fields are labeled appropriately for "Name" and "Email".

```tsx
import React, { useRef } from 'react';
import { ModusButton, ModusModal, ModusTextInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const modalRef = useRef<any>(null);
  const buttonRef = useRef<any>(null);

  const handleButtonClick = () => {
    if (modalRef.current) {
      modalRef.current.open();
    }
  };

  const handleModalClose = () => {
    setTimeout(() => {
      if (buttonRef.current) {
        buttonRef.current.focus();
      }
    }, 100);
  };

  return (
    <>
      <ModusButton id="btn-modal" color="primary" ref={buttonRef} onClick={handleButtonClick}>
        Open modal
      </ModusButton>
      <ModusModal
        ref={modalRef}
        headerText="User Information"
        primaryButtonText="Submit"
        secondaryButtonText="Cancel"
        onClosed={handleModalClose}
      >
        <p>Please fill out the form below.</p>
        <ModusTextInput label="Name" placeholder="Enter your name" />
        <ModusTextInput label="Email" placeholder="Enter your email" />
      </ModusModal>
    </>
  );
};

export default MyComponent;
```

# <ModusList>

## Prompt 3

**User Question:** Create a webpage with a dropdown that uses a chip as the toggle element. The chip should have the value "Dropdown Chip" and be in an advanced state. The dropdown should contain a list of options.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a dropdown that uses a chip as the toggle element. The chip should have the value "Dropdown Chip" and be in an advanced state. The dropdown should contain a list of options. The approach involves using the `<ModusDropdown>` component for the dropdown and the `<ModusChip>` component for the toggle element. The `<ModusList>` and `<ModusListItem>` components are used to create the list of options within the dropdown.

```tsx
import React from 'react';
import { ModusChip, ModusDropdown, ModusList, ModusListItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="dropdown-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px' }}>
      <ModusDropdown label="Dropdown" id="dropdown" toggle-element-id="toggleElement" animate-list>
        <ModusChip
          id="toggleElement"
          slot="dropdownToggle"
          advanced-chip
          value="Dropdown Chip"></ModusChip>
        <ModusList slot="dropdownList">
          <ModusListItem value="1" disabled borderless>Select Process</ModusListItem>
          <ModusListItem value="2" borderless>First Option (FO)</ModusListItem>
          <ModusListItem value="3" borderless>Second Option (SO)</ModusListItem>
          <ModusListItem value="4" borderless>Next Option (NO)</ModusListItem>
          <ModusListItem value="5" borderless>Another Option (AO)</ModusListItem>
        </ModusList>
      </ModusDropdown>
    </div>
  );
};

export default MyComponent;
```

# <ModusNavbar>

## Prompt 1
**User Question:** Create a webpage with a navbar that includes a main menu, notifications, and a profile menu with a user avatar, email, initials, and sign-out text.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a navbar that includes a main menu, notifications, and a profile menu with specific user details. The profile menu should display an avatar, email, initials, and sign-out text. The approach involves using the `<ModusNavbar>` component and configuring its properties to meet the specified requirements.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusNavbar } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const navbarRef = useRef<any>(null);

  useEffect(() => {
    const element = navbarRef.current;
    if (element) {
      element.apps = [
        {
          description: 'The One Trimble Design System',
          logoUrl: 'https://modus.trimble.com/favicon.svg',
          name: 'Trimble Modus',
          url: 'https://modus.trimble.com/',
        },
      ];
      element.logoOptions = {
        primary: {
          url: 'https://modus.trimble.com/img/trimble-logo.svg',
          height: 24,
        },
        secondary: {
          url: 'https://modus.trimble.com/favicon.svg',
          height: 24,
        },
      };
      element.profileMenuOptions = {
        avatarUrl: 'https://avatar.example.com/broken-image-link.png',
        email: 'modus_user@trimble.com',
        initials: 'MU',
        signOutText: 'Sign out',
        username: 'Modus User',
      };
    }
  }, []);

  return (
    <div style={{ height: '100vh', overflow: 'auto' }}>
      <ModusNavbar
        ref={navbarRef}
        id="navbar5"
        showAppsMenu
        showHelp
        showMainMenu
        showNotifications
      >
        <div slot="main" style={{ height: '300px' }}>
          Render your own main menu.
        </div>
        <div slot="notifications">Render your own notifications.</div>
      </ModusNavbar>
    </div>
  );
};

export default MyComponent;
```

## Prompt 4
**User Question:** Create a navbar with a search overlay, help tooltip, and profile menu with a user avatar, email, initials, and sign-out text?

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a navbar that includes a search overlay, help tooltip, and a profile menu with specific user details. The profile menu should display an avatar, email, initials, and sign-out text. The `ModusNavbar` component is used to achieve this. The `profileMenuOptions` property is set to include the user details, and the `helpTooltip` property is set to include the help text. The `enableSearchOverlay`, `showHelp`, and `showProfile` properties are used to enable the search overlay, help tooltip, and profile menu respectively.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusNavbar } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const navbarRef = useRef<any>(null);

  useEffect(() => {
    const element = navbarRef.current;
    if (element) {
      element.apps = [
        {
          description: 'The One Trimble Design System',
          logoUrl: 'https://modus.trimble.com/favicon.svg',
          name: 'Trimble Modus',
          url: 'https://modus.trimble.com/',
        },
      ];
      element.logoOptions = {
        primary: {
          url: 'https://modus.trimble.com/img/trimble-logo.svg',
          height: 24,
        },
        secondary: {
          url: 'https://modus.trimble.com/favicon.svg',
          height: 24,
        },
      };
      element.profileMenuOptions = {
        avatarUrl: 'https://avatar.example.com/broken-image-link.png',
        email: 'modus_user@trimble.com',
        initials: 'MU',
        signOutText: 'Sign out',
        username: 'Modus User',
      };
      element.helpTooltip = {
        text: 'Help',
        ariaLabel: 'Help Tooltip',
      };
    }
  }, []);

  return (
    <div style={{ height: '100vh', overflow: 'auto' }}>
      <ModusNavbar
        ref={navbarRef}
        id="navbar6"
        showAppsMenu
        showHelp
        showMainMenu
        showNotifications
        showProfile
        showSearch
        showShadow
        showPendoPlaceholder
        enableSearchOverlay
        reverse={false}
        variant="default"
      >
        <div slot="main" style={{ height: '300px' }}>
          Render your own main menu.
        </div>
        <div slot="notifications">Render your own notifications.</div>
      </ModusNavbar>
    </div>
  );
};

export default MyComponent;
```

# <ModusPagination>

## Prompt 1
**User Question:** Create a large pagination component for a blog website with a maximum of 50 pages, starting from page 1. The previous and next buttons should be labeled "Previous" and "Next".

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a pagination component with a maximum of 50 pages, starting from page 1. The size of the pagination should be large, and the previous and next buttons should have the text "Previous" and "Next" respectively. The design ensures easy navigation through the blog pages.

```tsx
import React from 'react';
import { ModusPagination } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="pagination-container" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', overflow: 'auto' }}>
      <ModusPagination
        active-page={1}
        max-page={50}
        minPage={1}
        prev-page-button-text="Previous"
        next-page-button-text="Next"
        size="large" />
    </div>
  );
};

export default MyComponent;
```

# <ModusProgressBar>

## Prompt 1
**User Question:** Create a webpage with 3 progress bars. The first progress bar should have a value of 50, a maximum value of 100, a minimum value of 0, and display the text "50%". The second progress bar should be small-sized with a value of 30, a maximum value of 50, a minimum value of 0, and have a background color of red. The third progress bar should be compact-sized, indeterminate mode, and have a color of green.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three progress bars with different sizes, colors, values, and modes. The first progress bar is a default-sized progress bar with a value of 50, a maximum value of 100, a minimum value of 0, and displays the text "50%". The second progress bar is a small-sized progress bar with a value of 30, a maximum value of 50, a minimum value of 0, and has a background color of red. The third progress bar is a compact-sized progress bar in indeterminate mode and has a color of green.

```tsx
import React from 'react';
import { ModusProgressBar } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="progress-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusProgressBar value={50} maxValue={100} minValue={0} text="50%" />
      <ModusProgressBar value={30} maxValue={50} minValue={0} size="small" background-color="red" />
      <ModusProgressBar mode="indeterminate" size="compact" color="green" />
    </div>
  );
};

export default MyComponent;
```

# <ModusSentimentScale>

## Prompt 1
**User Question:** Create a disabled sentiment scale with smiley icons and log the selected sentiment to the console.
**Agent Answer:**
References:
To create a sentiment scale with smiley icons and ensure it is disabled, we use the `<ModusSentimentScale>` component with the `type` attribute set to "smileys" and the `disabled` attribute set to `true`. Additionally, we add an event listener to log the selected sentiment to the console when a sentiment is selected.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusSentimentScale } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const sentimentScaleRef = useRef<ModusSentimentScale>(null);

  useEffect(() => {
    const sentimentScale = sentimentScaleRef.current;
    if (sentimentScale) {
      sentimentScale.addEventListener('sentimentSelection', (event: any) => {
        console.log('Sentiment selected:', event.detail);
      });
    }
  }, []);

  return <ModusSentimentScale ref={sentimentScaleRef} type="smileys" disabled={true} />;
};

export default MyComponent;
```
## Prompt 2
**User Question:** Create a sentiment scale with thumb icons, set an aria label "Sentiment Scale", ensure it is enabled, and log the selected sentiment to the console?

**Agent Answer:**
References:
To create a sentiment scale with thumb icons, set an aria label "Sentiment Scale", ensure it is enabled, and log the selected sentiment to the console, we can use the `<ModusSentimentScale>` component. The component will be configured with the `type` attribute set to "thumbs" for thumb icons, `ariaLabel` set to "Sentiment Scale" for accessibility, and `disabled` set to `false` to ensure it is enabled. We will add an event listener to log the selected sentiment to the console.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusSentimentScale } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const sentimentScaleRef = useRef<ModusSentimentScale>(null);

  useEffect(() => {
    const sentimentScale = sentimentScaleRef.current;
    if (sentimentScale) {
      sentimentScale.addEventListener('sentimentSelection', (event: any) => {
        console.log('Sentiment selected:', event.detail);
      });
    }
  }, []);

  return <ModusSentimentScale ref={sentimentScaleRef} type="thumbs" ariaLabel="Sentiment Scale" disabled={false} />;
};

export default MyComponent;
```

# <ModusSideNavigation>
## Prompt 1
**User Question:** Create a webpage with a side navigation that has three items: "Dashboard", "Reports", and "Settings". The "Dashboard" item should have a submenu with "Overview" and "Analytics". The side navigation should be in push mode and should collapse when clicked outside.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a side navigation with three main items: "Dashboard", "Reports", and "Settings". The "Dashboard" item should have a submenu with "Overview" and "Analytics". We have a Navbar and we used it's DOM event `mainMenuClick` The side navigation should be in push mode and should collapse when clicked outside. The approach involves setting up the side navigation items and handling the submenu for "Dashboard". The side navigation will be configured to collapse when clicked outside.

```tsx
import React, { useEffect, useRef, useState } from 'react';
import { ModusNavbar, ModusSideNavigation, ModusSideNavigationItem } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const sideNavRef = useRef<any>(null);
  const navbarRef = useRef<any>(null);
  const [sideNavExpanded, setSideNavExpanded] = useState(false);

  useEffect(() => {
    if (sideNavRef.current) {
      sideNavRef.current.data = [
        {
          id: 'dashboard',
          menuIcon: 'dashboard',
          label: 'Dashboard',
          isHeader: {
            enabled: true,
            items: [
              { id: 'overview', label: 'Overview', icon: 'overview' },
              { id: 'analytics', label: 'Analytics', icon: 'analytics' },
            ],
          },
          onSideNavItemHeaderClicked: selectionHeaderHandler,
        },
        {
          id: 'reports',
          menuIcon: 'reports',
          label: 'Reports',
          onSideNavItemClicked: selectionHandler,
        },
        {
          id: 'settings',
          menuIcon: 'settings',
          label: 'Settings',
          onSideNavItemClicked: selectionHandler,
        },
      ];
    }

    if (navbarRef.current) {
      const element = navbarRef.current;
      element.apps = [
        {
          description: 'The One Trimble Design System',
          logoUrl: 'https://modus.trimble.com/favicon.svg',
          name: 'Trimble Modus',
          url: 'https://modus.trimble.com/',
        },
      ];
      element.logoOptions = {
        primary: {
          url: 'https://modus.trimble.com/img/trimble-logo.svg',
          height: 24,
        },
        secondary: {
          url: 'https://modus.trimble.com/favicon.svg',
          height: 24,
        },
      };
      element.profileMenuOptions = {
        avatarUrl: 'https://avatar.example.com/broken-image-link.png',
        email: 'modus_user@trimble.com',
        initials: 'MU',
        signOutText: 'Sign out',
        username: 'Modus User',
      };

      element.addEventListener('mainMenuClick', () => {
        setSideNavExpanded((prev) => !prev);
      });
    }
  }, []);

  const selectionHandler = (e: any) => {
    if (e.detail.selected) {
      const panel = document.querySelector('#panelcontent');
      document.querySelector('#sidenav-content-title')?.remove();
      const el = document.createElement('h3');
      el.id = 'sidenav-content-title';
      const selectedItem = e.target.data?.find((item: any) => item.id === e.detail.id);
      if (selectedItem) {
        el.innerHTML = selectedItem.label || 'Home Page';
      }
      panel?.insertBefore(el, document.querySelector('#overview'));
    }
  };

  const selectionHeaderHandler = (e: any) => {
    const headerLabel = e.detail.id;
    let newItems = [];

    if (headerLabel === 'overview') {
      newItems = [
        { label: 'Overview', icon: 'overview' },
        { label: 'Analytics', icon: 'analytics' },
      ];
      getLabel(newItems);

      const simulatedEvent = {
        detail: { selected: true, id: 'overview' },
        target: { data: [{ id: 'overview', label: 'Overview' }] },
      };
      selectionHandler(simulatedEvent);
    }
  };

  const getLabel = (newItems: any) => {
    if (sideNavRef.current) {
      sideNavRef.current.data = [
        {
          id: 'dashboard',
          menuIcon: 'dashboard',
          label: 'Dashboard',
          isHeader: {
            enabled: true,
            items: [
              { id: 'overview', label: 'Overview', icon: 'overview' },
              { id: 'analytics', label: 'Analytics', icon: 'analytics' },
            ],
          },
          onSideNavItemHeaderClicked: selectionHeaderHandler,
        },
        {
          id: 'reports',
          menuIcon: newItems[0].menuIcon,
          label: newItems[0].label,
          onSideNavItemClicked: selectionHandler,
        },
        {
          id: 'settings',
          menuIcon: newItems[1].icon,
          label: newItems[1].label,
          onSideNavItemClicked: selectionHandler,
        },
      ];
    }
  };

  return (
    <div id="dataTemplate" style={{ height: '100vh', overflow: 'auto' }}>
      <div style={{ width: '100%', alignItems: 'center', height: '56px', boxShadow: '0 0 2px var(--modus-secondary) !important', marginTop: '50px' }}>
        <ModusNavbar id="navbar6" ref={navbarRef} showAppsMenu showHelp showMainMenu showNotifications />
      </div>
      <div id="container" style={{ display: 'flex', minHeight: '500px', overflowY: 'auto', position: 'relative', boxShadow: '0 0 2px var(--modus-secondary)!important' }}>
        <ModusSideNavigation ref={sideNavRef} maxWidth="300px" targetContent="#dataTemplate #panelcontent" mode="push" collapseOnClickOutside={true} expanded={sideNavExpanded} />

        <div id="panelcontent" style={{ padding: '10px', transition: 'all 0.25s linear 0s' }}>
          <div id="overview">
            <p>
              The side navigation of an application provides context through accessible menu options and positions a consistent
              component to connect to various pages in the application.
            </p>
            <p>
              The side navigation is a collapsible side content of the site’s pages. It is located alongside the page’s primary
              content. The component is designed to add side content to a fullscreen application. It is activated through the
              “hamburger” menu in the Navbar.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyComponent;
```
## Prompt 2
**User Question:** Create a webpage with a side navigation that has nested menu items, including Home, Usage, Styles, and Accessibility pages. Include a navbar with main menu integration, and add switches to toggle between blue and default themes and between overlay and push modes.

**Agent Answer:**
References:
Analyzing the requirements, we need to create a complex side navigation with nested menu structure and theme customization. The solution uses ModusNavbar, ModusSideNavigation, and ModusSwitch components working together. The side navigation includes multi-level nesting (up to 3 levels deep) with Home, Usage, Styles, and Accessibility sections. The navbar is configured with a logo and profile details. Two switches provide user control: one toggles between default and blue themes by applying CSS variables for colors and icons, while the other switches between "push" and "overlay" modes affecting how the content panel behaves when the navigation opens. The side navigation is toggled via the navbar's hamburger menu, and selection events update the main content area with the selected menu item's title.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusNavbar, ModusSideNavigation, ModusSwitch } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const navbarRef = useRef<any>(null);
  const sideNavRef = useRef<any>(null);

  useEffect(() => {
    if (navbarRef.current) {
      const element = navbarRef.current;
      element.logoOptions = {
        primary: {
          url: 'https://modus.trimble.com/img/trimble-logo.svg',
        },
      };
      element.profileMenuOptions = {
        avatarUrl: 'https://avatar.example.com/broken-image-link.png',
        email: 'modus_user@trimble.com',
        initials: 'MU',
        username: 'Modus User',
      };
    }

    if (sideNavRef.current) {
      const sidenav = sideNavRef.current;
      sidenav.data = [
        {
          id: 'home-menu',
          menuIcon: 'home',
          label: 'Home page 1',
          children: [
            {
              id: 'home-menu-2',
              menuIcon: 'home',
              label: 'Home page 2',
              onSideNavItemClicked: selectionHandler,
            },
            {
              id: 'usage-menu-2',
              children: [
                {
                  id: 'home-menu-3',
                  menuIcon: 'home',
                  label: 'Home page 3',
                  onSideNavItemClicked: selectionHandler,
                },
              ],
              menuIcon: 'flowchart',
              label: 'Usage page 2',
            },
          ],
        },
        {
          id: 'usage-menu',
          menuIcon: 'flowchart',
          label: 'Usage page 1',
          onSideNavItemClicked: selectionHandler,
        },
        {
          id: 'styles-menu',
          menuIcon: 'bar_graph_line',
          label: 'Styles page 1',
          onSideNavItemClicked: selectionHandler,
        },
        {
          id: 'accessibility-menu',
          menuIcon: 'screen',
          label: 'Accessibility page 1',
          onSideNavItemClicked: selectionHandler,
        },
      ];
    }

    const blueTheme = `--modus-side-navigation-link-color:#ffffff;--modus-side-navigation-bg:#0e416c;--modus-side-navigation-item-color:#ffffff;--modus-side-navigation-item-active-bg:#217cbb;--modus-side-navigation-item-hover-bg:#0063a3;--modus-side-navigation-item-icon-color:#ffffff;--modus-side-navigation-item-chevron-color:#ffffff;--modus-side-navigation-item-icon-filter:invert(100%) sepia(0%) saturate(24%) hue-rotate(114deg) brightness(108%) contrast(108%);`;

    const switchTheme = document.querySelector('#switch-theme') as HTMLElement;
    const switchMode = document.querySelector('#switch-mode') as HTMLElement;

    switchTheme.addEventListener('switchClick', (e: any) => {
      const sidenav = sideNavRef.current;
      if (e.detail) {
        sidenav.style = blueTheme;
      } else sidenav.style = '';
    });

    switchMode.addEventListener('switchClick', (e: any) => {
      const sidenav = sideNavRef.current;
      sidenav.mode = sidenav.mode === 'push' ? 'overlay' : 'push';
    });

    document.addEventListener('mainMenuClick', (e: any) => {
      const panel = sideNavRef.current;
      panel.expanded = !panel.expanded;
    });
  }, []);

  const selectionHandler = (e: any) => {
    if (e.detail) {
      const panel = document.querySelector('#panelcontent');
      document.querySelector('#sidenav-content-title')?.remove();
      const el = document.createElement('h3');
      el.id = 'sidenav-content-title';
      el.innerHTML = e.target?.label || 'Home page';
      panel?.insertBefore(el, document.querySelector('#overview'));
    }
  };

  return (
    <div id="dataTemplate" style={{ height: '100vh', overflow: 'auto' }}>
      <ModusSwitch id="switch-theme" label="Enable blue theme" />
      <br />
      <ModusSwitch id="switch-mode" label="Enable Push Side Navigation" />
      <div style={{ width: '100%', alignItems: 'center', height: '56px', boxShadow: '0 0 2px var(--modus-secondary)!important', marginTop: '10px' }}>
        <ModusNavbar id="navbar7" ref={navbarRef} showAppsMenu showHelp showMainMenu showNotifications />
      </div>

      <div id="container" style={{ display: 'flex', minHeight: '500px', overflowY: 'auto', position: 'relative', boxShadow: '0 0 2px var(--modus-secondary)!important' }}>
        <ModusSideNavigation ref={sideNavRef} maxWidth="300px" id="sideNav" targetContent="#dataTemplate #panelcontent" mode="overlay" />

        <div id="panelcontent" style={{ padding: '10px', transition: 'all 0.25s linear 0s' }}>
          <div id="overview">
            <p>
              The side navigation of an application provides context through accessible menu options and positions a consistent
              component to connect to various pages in the application.
            </p>
            <p>
              The side navigation is a collapsible side content of the site’s pages. It is located alongside the page’s primary
              content. The component is designed to add side content to a fullscreen application. It is activated through the
              “hamburger” menu in the Navbar.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyComponent;
```

# <ModusSlider>

## Prompt 1
**User Question:** Create a webpage with a slider labeled "Volume" that has a minimum value of 0, a maximum value of 100, and starts at 50. The slider should also have an ariaLabel "volume-slider".

**Agent Answer:**
References:
To create the slider, I broke down the requirements into the following components: the label, minimum value, maximum value, initial value, and ariaLabel. I used the `<ModusSlider>` component from the Modus design system to implement these features. The slider is placed inside a container with flex styling to ensure proper alignment and spacing.

```tsx
import React from 'react';
import { ModusSlider } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="slider-container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusSlider 
        label="Volume" 
        minValue={0} 
        maxValue={100} 
        value={50} 
        ariaLabel="volume-slider" 
      />
    </div>
  );
};

export default MyComponent;
```

# <ModusSwitch>

## Prompt 1
**User Question:** Create a webpage with three switches: a small checked switch labeled "Small Switch", a disabled medium switch labeled "Medium Switch", and an interactive medium switch labeled "Interactive Switch" that logs its checked status to the console when clicked?

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three switches with different sizes, labels, and functionalities. The first switch is a small switch with the label "Small Switch" and should be checked by default. The second switch is a medium switch with the label "Medium Switch" and should be disabled. The third switch is a medium switch with the label "Interactive Switch" and should log its checked status to the console when clicked.

```tsx
import React, { useEffect } from 'react';
import { ModusSwitch } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const interactiveSwitch = document.querySelector('#interactiveSwitch') as HTMLElement | null;
    if (interactiveSwitch) {
      interactiveSwitch.addEventListener('switchClick', (event: Event) => {
        const target = event.target as HTMLInputElement;
        console.log(`Switch is now ${target.checked ? 'checked' : 'unchecked'}`);
      });
    }
    return () => {
      if (interactiveSwitch) {
        interactiveSwitch.removeEventListener('switchClick', () => {});
      }
    };
  }, []);

  return (
    <div id="switch-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusSwitch label="Small Switch" size="small" checked />
      <ModusSwitch label="Medium Switch" disabled />
      <ModusSwitch id="interactiveSwitch" label="Interactive Switch" />
    </div>
  );
};

export default MyComponent;
```

# <ModusTable>
Based on your request, I'll create a UserQuestion and AgentAnswer entry for the ModusTable component example, following the format in the UI_KB.md file.

# <ModusTable>

## Prompt 1
**User Question:** Create a detailed data table with columns for personal information including name, age, status, priority, and email. Include features like column resizing, sorting, pagination, row selection, and a toolbar with column visibility options. The table should also display summary rows with totals.

**Agent Answer:** 
References:
To create a comprehensive data table with the specified features, I'll use the `ModusTable` component with various configuration options. The implementation includes:

1. **Column Configuration**: I'm defining multiple columns with different data types (text, integer, badge, link, date) and setting specific properties for each:
   - Setting width constraints with `size`, `minSize`, and `maxSize` properties for optimal display
   - Enabling column totals with `showTotal` for numerical columns (age, visits, progress)
   - Configuring editable cells with `cellEditable` and providing options through `cellEditorType` and `cellEditorArgs`

2. **Data Structure**: The table data includes multiple rows with structured information, including badge-type data for priorities and link-type data for emails.

3. **Interactive Features**:
   - `hover={true}` enables row highlighting on hover for better user experience

```jsx
import React, { useEffect, useState } from 'react';
import { ModusTable } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const [tableColumns, setTableColumns] = useState<any[]>([]);
  const [tableData, setTableData] = useState<any[]>([]);

  useEffect(() => {
    setTableColumns([
      { header: 'First Name', accessorKey: 'firstName', id: 'first-name', dataType: 'text', size: 150, minSize: 80 },
      { header: 'Last Name', accessorKey: 'lastName', id: 'last-name', dataType: 'text', size: 150, minSize: 80 },
      { header: 'Age', accessorKey: 'age', id: 'age', dataType: 'integer', size: 60, minSize: 60, showTotal: true },
      { header: 'Visits', accessorKey: 'visits', id: 'visits', dataType: 'integer', maxSize: 80, minSize: 80, enableResizing: false, showTotal: true },
      { header: 'Status', accessorKey: 'status', id: 'status', dataType: 'text', minSize: 80, cellEditable: true, cellEditorType: 'select', cellEditorArgs: { options: [{ display: 'Verified' }, { display: 'Pending' }, { display: 'Rejected' }] } },
      { header: 'Priority', accessorKey: 'priority', id: 'priority', dataType: 'badge', cellEditable: true, cellEditorType: 'select', cellEditorArgs: { options: [{ size: 'medium', type: 'counter', display: 'High', color: 'success' }, { size: 'medium', type: 'counter', display: 'Low', color: 'danger' }, { size: 'medium', type: 'counter', display: 'Medium', color: 'warning' }] } },
      { header: 'Email', accessorKey: 'email', id: 'email', dataType: 'link', size: 230, minSize: 80, cellEditable: true, cellEditorType: 'select', cellEditorArgs: { options: [{ display: 'Google', url: 'https://www.google.com' }, { display: 'Yahoo', url: 'https://www.yahoo.com' }, { display: 'Bing', url: 'https://www.bing.com' }] } },
      { header: 'Profile Progress', accessorKey: 'progress', id: 'progress', dataType: 'integer', minSize: 100, showTotal: true },
      { header: 'Created At', accessorKey: 'createdAt', id: 'createdAt', dataType: 'date', size: 210, minSize: 100 },
    ]);

    setTableData([
      {
        firstName: 'Alice',
        lastName: 'Johnson',
        age: 30,
        visits: 120,
        progress: 80,
        status: 'Verified',
        priority: { size: 'medium', type: 'counter', text: 'Medium', color: 'warning' },
        email: { display: 'Google', url: 'https://www.google.com' },
        createdAt: '2021-01-15T10:00:00.000Z',
      },
      {
        firstName: 'Bob',
        lastName: 'Smith',
        age: 45,
        visits: 200,
        progress: 90,
        status: 'Pending',
        priority: { size: 'medium', type: 'counter', text: 'High', color: 'success' },
        email: { display: 'Yahoo', url: 'https://www.yahoo.com' },
        createdAt: '2020-05-20T14:30:00.000Z',
      },
      {
        firstName: 'Charlie',
        lastName: 'Brown',
        age: 28,
        visits: 150,
        progress: 70,
        status: 'Rejected',
        priority: { size: 'medium', type: 'counter', text: 'Low', color: 'danger' },
        email: { display: 'Bing', url: 'https://www.bing.com' },
        createdAt: '2019-11-11T08:45:00.000Z',
      },
      {
        firstName: 'Diana',
        lastName: 'Prince',
        age: 35,
        visits: 180,
        progress: 85,
        status: 'Verified',
        priority: { size: 'medium', type: 'counter', text: 'Critical', color: 'danger' },
        email: { display: 'Google', url: 'https://www.google.com' },
        createdAt: '2022-03-25T16:20:00.000Z',
      },
    ]);
  }, []);

  return (
    <div style={{ width: '950px', overflowX: 'auto' }}>
      <ModusTable
        id="table4"
        columns={tableColumns}
        data={tableData}
        hover={true}
        sort={true}
        columnResize={true}
        pagination={true}
        showSortIconOnHover={true}
        toolbar={true}
        toolbarOptions={{ columnsVisibility: { title: 'Column Visibility', requiredColumns: ['first-name'], hiddenColumns: ['last-name'] } }}
        summaryRow={true}
        rowSelectionOptions={{ multiple: true, subRowSelection: true }}
        rowSelectionDisabled={(row) => row.original.status === 'Rejected'}
        fullWidth={true}
      />
    </div>
  );
};

export default MyComponent;
```


# <ModusToolbar>

## Prompt 1
**User Question:** Create a toolbar with three buttons labeled "Save", "Edit", and "Delete". The toolbar should have an aria label "Main Toolbar" and should not be disabled.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a toolbar with three buttons labeled "Save", "Edit", and "Delete". The toolbar should have an aria label "Main Toolbar" and should not be disabled. The `ModusToolbar` component is used to create the toolbar, and the `ModusButton` component is used for the buttons. The `ariaLabel` attribute is set to "Main Toolbar" for accessibility, and the `disabled` attribute is set to `false` to ensure the toolbar is active.

```tsx
import React from 'react';
import { ModusToolbar, ModusButton } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <ModusToolbar ariaLabel="Main Toolbar" disabled={false}>
      <ModusButton>Save</ModusButton>
      <ModusButton>Edit</ModusButton>
      <ModusButton>Delete</ModusButton>
    </ModusToolbar>
  );
};

export default MyComponent;
```

# <ModusTooltip>

## Prompt 1
**User Question:** Create a webpage with a tooltip that displays "Hover over me!" at the bottom, initially disabled, wrapping around a button labeled "Click Me".
**Agent Answer:** 
References:
Analyzing the requirements, we need to create a tooltip with the text "Hover over me!" positioned at the bottom. The tooltip should be disabled initially and should wrap around a button with the text "Click Me".

```tsx
import React from 'react';
import { ModusTooltip, ModusButton } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="tooltip-container" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <ModusTooltip text="Hover over me!" position="bottom" disabled={true}>
        <ModusButton>Click Me</ModusButton>
      </ModusTooltip>
    </div>
  );
};

export default MyComponent;
```

# <ModusUtilityPanel>

## Prompt 1
**User Question:** Create a webpage with a utility panel that overlays the main content. The utility panel should have a header "Utility Panel Header", a body with the text "This is the body of the utility panel", and a footer "Utility Panel Footer". The panel should be initially collapsed and should expand when a button in the navbar is clicked.

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a utility panel that overlays the main content. The panel should have a header, body, and footer with specified texts. The panel should be initially collapsed and should expand when a button in the navbar is clicked. We will use the `expanded` property to control the visibility of the panel and the `pushContent` property to ensure the panel overlays the main content.

```tsx
import React, { useEffect, useState } from 'react';
import { ModusNavbar, ModusUtilityPanel } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const [expanded, setExpanded] = useState<boolean>(false);

  useEffect(() => {
    const handleButtonClick = () => {
      setExpanded((prev) => !prev);
    };

    document.addEventListener('buttonClick', handleButtonClick);

    return () => {
      document.removeEventListener('buttonClick', handleButtonClick);
    };
  }, []);

  return (
    <div id="defaultTemplate">
      <div
        style={{
          width: '100%',
          alignItems: 'center',
          height: '56px',
          boxShadow: '0 0 2px var(--modus-secondary)!important',
          marginTop: '50px',
        }}
      >
        <ModusNavbar
          id="navbar"
          showMainMenu={true}
          buttons={[
            {
              id: 'addMenu',
              icon: 'add',
              tooltip: {
                text: 'Add',
              },
            },
          ]}
        />
      </div>
      <div
        id="container"
        style={{
          display: 'flex',
          minHeight: '500px',
          overflow: 'hidden',
          position: 'relative',
          boxShadow: '0 0 2px var(--modus-secondary)!important',
        }}
      >
        <ModusUtilityPanel
          targetContent="#panelcontent"
          expanded={expanded}
          pushContent={false}
        >
          <span slot="header">Utility Panel Header</span>
          <div slot="body">This is the body of the utility panel</div>
          <span slot="footer">Utility Panel Footer</span>
        </ModusUtilityPanel>

        <div id="panelcontent" style={{ padding: '10px' }}>
          <div id="overview">
            <p>
              The side navigation of an application provides context through accessible menu options and positions a consistent
              component to connect to various pages in the application. The side navigation is a collapsible side content of the
              site’s pages. It is located alongside the page’s primary content. The component is designed to add side content to
              a fullscreen application. It is activated through the “hamburger” menu in the Navbar.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyComponent;
```

# <ModusTabs>

## Prompt 1

**User Question:** Create a tabs component that displays 5 tabs with some having icons, and show the active tab index when a user clicks on a different tab. Make sure to properly handle the tab change events.

**Agent Answer:**
References:
To create a tabs component that displays 5 tabs with some having icons and shows the active tab index when a user clicks on a different tab, I'll use the `ModusTabs` component from the Modus React library. The solution involves using React's `useState` to track the active tab and `useRef` to access the tabs DOM element. The component will include proper event handling through an event listener for the `tabChange` event, which updates the active tab state whenever a user selects a different tab.

```tsx
import React, { useEffect, useRef, useState } from 'react';
import { ModusTabs } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const tabsRef = useRef<any>(null);
  const [activeTab, setActiveTab] = useState(0);
  const tabData = [
    { id: 0, label: 'Tab 1', icon: 'sun' },
    { id: 1, label: 'Tab 2' },
    { id: 2, label: 'Tab 3', icon: 'moon' },
    { id: 3, label: 'Tab 4' },
    { id: 4, label: 'Tab 5', icon: 'sun' },
  ];

  useEffect(() => {
    const modusTabs = tabsRef.current?.querySelector('modus-tabs');
    if (modusTabs) {
      modusTabs.tabs = tabData.map(tab => ({
        id: tab.id,
        label: tab.label,
        leftIcon: tab.icon,
      }));
      modusTabs.addEventListener('tabChange', (e: any) => {
        setActiveTab(e.detail);
      });
    }
  }, []);

  return (
    <div id="tabs-container2" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px', padding: '16px', overflow: 'auto' }} ref={tabsRef}>
      <ModusTabs></ModusTabs>
      <div id="tab-content3" style={{ width: '80%', textAlign: 'center' }}>
        <h1 id="tab-heading3">Tab Index: {activeTab}</h1>
      </div>
    </div>
  );
};

export default MyComponent;
```
