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
**User Question:** Create a webpage with a dismissible error alert that logs a message to the console when dismissed.

**Agent Answer:** 
References:
The alert is created using the `<ModusAlert>` component with the `dismissible` and `type="error"` properties. An event listener is added to the dismiss button to log a message to the console when the alert is dismissed.

**code**:
```tsx
import React, { useEffect, useRef } from 'react';
import { ModusAlert } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const alertRef = useRef<HTMLModusAlertElement>(null);

  useEffect(() => {
    const alertElement = alertRef.current;
    if (alertElement) {
      const handleDismiss = () => {
        console.log('Alert dismissed');
      };
      alertElement.addEventListener('dismiss', handleDismiss);
      return () => {
        alertElement.removeEventListener('dismiss', handleDismiss);
      };
    }
  }, []);

  return (
    <div id="alert-container" style={{ padding: '16px' }}>
      <ModusAlert ref={alertRef} message="An error occurred" type="error" dismissible></ModusAlert>
    </div>
  );
};

export default MyComponent;
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

## Prompt 3
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

**User Question:** Create a webpage with a tree view that has a search input to filter the tree items. The tree should have the following structure: "Inbox" with sub-items "Personal" and "More ...", and "Archived" with sub-items "Folder1" containing "File1" and "File2". The search input should filter the tree items based on the text entered.

**Agent Answer:**
References:
To create a tree view with a search input to filter the tree items, we need to use the `<ModusTreeView>` and `<ModusTextInput>` components. The tree structure includes "Inbox" with sub-items "Personal" and "More ...", and "Archived" with sub-items "Folder1" containing "File1" and "File2". The search input will filter the tree items based on the text entered. The approach involves setting up the tree structure, managing the filter text state, and updating the display of tree items based on the filter text.

```tsx
import React, { useEffect, useRef, useState } from 'react';
import { ModusTreeView, ModusTreeViewItem, ModusTextInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const [filterText, setFilterText] = useState<string>('');
  const [items, setItems] = useState<Map<string, string>>(new Map());
  const treeViewRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const container = treeViewRef.current;
    const root = container?.querySelector('modus-tree-view');

    const itemMap = new Map();
    container?.querySelectorAll('modus-tree-view-item').forEach((element) => {
      const nodeId = element.getAttribute('node-id') || '';
      const label = element.querySelector("div[slot='label']")?.innerHTML || '';
      itemMap.set(nodeId, label);
    });
    setItems(itemMap);
    if (root) {
      root.expandedItems = Array.from(itemMap.keys());
    }
  }, []);

  useEffect(() => {
    const container = treeViewRef.current;

    if (filterText) {
      const searchResult = [...items]
        .filter(([key, value]) => value.toLowerCase().includes(filterText.toLowerCase()))
        .map(([key]) => key);

      const getParents = (element: HTMLElement): HTMLElement[] => {
        const parent = element.parentElement?.closest('modus-tree-view-item');
        return parent ? [parent, ...getParents(parent)] : [];
      };

      items.forEach((value, key) => {
        const element = container?.querySelector(`modus-tree-view-item[node-id='${key}']`);
        if (element) {
          if (searchResult.includes(key)) {
            element.querySelector("div[slot='label']")!.style.color = '#0063a3';
            element.style.display = 'block';
            getParents(element).forEach((parent) => {
              parent.style.display = 'block';
            });
          } else {
            element.querySelector("div[slot='label']")!.style.color = '';
            element.style.display = 'none';
          }
        }
      });
    } else {
      items.forEach((value, key) => {
        const element = container?.querySelector(`modus-tree-view-item[node-id='${key}']`);
        if (element) {
          element.querySelector("div[slot='label']")!.style.color = '';
          element.style.display = 'block';
        }
      });
    }
  }, [filterText, items]);

  return (
    <div id="tree-with-filter" style={{ display: 'flex', flexDirection: 'column', width: '400px' }} ref={treeViewRef}>
      <ModusTextInput
        id="filter"
        size="large"
        placeholder="Search"
        disabled={false}
        includeSearchIcon
        onValueChange={(e) => setFilterText(e.detail)}
      />
      <ModusTreeView>
        <ModusTreeViewItem nodeId="1">
          <div slot="label">Inbox</div>
          <ModusTreeViewItem nodeId="2">
            <div slot="label">Personal</div>
          </ModusTreeViewItem>
          <ModusTreeViewItem nodeId="5">
            <div slot="label">More ...</div>
          </ModusTreeViewItem>
        </ModusTreeViewItem>
        <ModusTreeViewItem nodeId="6">
          <div slot="label">Archived</div>
          <ModusTreeViewItem nodeId="7" isLastChild>
            <div slot="label">Folder1</div>
            <ModusTreeViewItem nodeId="8">
              <div slot="label">File1</div>
            </ModusTreeViewItem>
            <ModusTreeViewItem nodeId="11" isLastChild>
              <div slot="label">File2</div>
            </ModusTreeViewItem>
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

## Prompt 1
**User Question:** Create a webpage with a table that has 5 columns: "First Name", "Last Name", "Age", "Visits", and "Status", with row hover effect, sorting enabled, and a custom button in each row under a "Custom" column? The table should also be borderless.

**Agent Answer:**
References:
To create the table as per the requirements, we need to use the `<ModusTable>` component with the specified columns and properties. The table will have row hover effect, sorting enabled, and a custom button in each row under a "Custom" column. The table will also be borderless. The columns and data are defined in the `useEffect` hook to ensure they are set after the component mounts. The fullWidth should always be true so that it takes all the space properly


```tsx
import React, { useEffect, useRef } from 'react';
import { ModusTable, ModusButton } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const tableRef = useRef<HTMLModusTableElement>(null);

  useEffect(() => {
    if (tableRef.current) {
      tableRef.current.columns = [
        {
          header: 'First Name',
          accessorKey: 'firstName',
          id: 'first-name',
          dataType: 'text',
        },
        {
          header: 'Last Name',
          accessorKey: 'lastName',
          id: 'last-name',
          dataType: 'text',
        },
        { header: 'Age', accessorKey: 'age', id: 'age', dataType: 'integer' },
        {
          header: 'Visits',
          accessorKey: 'visits',
          id: 'visits',
          dataType: 'integer',
        },
        { header: 'Status', accessorKey: 'status', id: 'status', dataType: 'text' },
        {
          header: 'Custom',
          accessorKey: 'custom',
          id: 'custom',
          dataType: 'custom',
        }
      ];

      tableRef.current.data = [
        {
          firstName: 'Gordon',
          lastName: 'Lemke',
          age: 40,
          visits: 434,
          status: 'single',
          custom: <ModusButton color='primary'>Custom1</ModusButton>
        },
        {
          firstName: 'Elliott',
          lastName: 'Bosco',
          age: 21,
          visits: 348,
          status: 'complicated',
          custom: <ModusButton color='secondary'>Custom2</ModusButton>
        },
        {
          firstName: 'Agnes',
          lastName: 'Breitenberg',
          age: 34,
          visits: 639,
          status: 'single',
          custom: <ModusButton color='tertiary'>Custom3</ModusButton>
        },
        {
          firstName: 'Nicolette',
          lastName: 'Stamm',
          age: 13,
          visits: 518,
          status: 'relationship',
          custom: <ModusButton color='danger'>Custom4</ModusButton>
        },
      ];
    }
  }, []);

  return (
    <div style={{ width: '950px' }}>
      <ModusTable ref={tableRef} hover={true} sort={true} displayOptions={{ borderless: true }} fullWidth={true} />
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
**User Question:** Create a webpage with a ModusTabs component that has 4 tabs: "Home" with a left icon "home", "Profile" with a right icon "user", "Settings" as the active tab, and an icon-only tab with the icon "gear". The tabs should be full-width and have an aria-label "Main Navigation".

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a ModusTabs component with 4 tabs. The first tab should have a label "Home" and a left icon "home". The second tab should have a label "Profile" and a right icon "user". The third tab should be labeled "Settings" and be the active tab. The fourth tab should be icon-only with the icon "gear". Additionally, the tabs should be full-width and have an aria-label "Main Navigation".

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusTabs } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const modusTabsRef = useRef<any>(null);

  useEffect(() => {
    if (modusTabsRef.current) {
      modusTabsRef.current.tabs = [
        {
          id: 0,
          label: 'Home',
          leftIcon: 'home',
        },
        {
          id: 1,
          label: 'Profile',
          rightIcon: 'user',
        },
        {
          id: 2,
          label: 'Settings',
          active: true,
        },
        {
          id: 3,
          iconOnly: 'gear',
        },
      ];
    }
  }, []);

  return (
    <ModusTabs ref={modusTabsRef} fullWidth={true} ariaLabel="Main Navigation"></ModusTabs>
  );
};

export default MyComponent;
```