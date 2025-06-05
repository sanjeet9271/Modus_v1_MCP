# <ModusAccordion>

## Prompt 1
**User Question:** How do I create an accordion with expandable and collapsible items?

**Agent Answer:**
References:
I've analyzed the ModusAccordion component and its child component ModusAccordionItem. The key properties to focus on are:
- `header-text`: Sets the visible header text for each accordion item
- `disabled`: Makes an accordion item non-interactive
- `expanded`: Sets the initial state of an accordion item to be expanded
- `size`: Sets the size of accordion items ("standard" or "condensed")
- `expand-button-type`: Changes the appearance of the expand/collapse button

The component emits `opened` and `closed` events when the accordion items are expanded or collapsed, which should be handled to respond to user interactions.

```html
<div id="accordion-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-accordion id="basic-accordion">
    <modus-accordion-item header-text="Product Information" expanded>
      <div style="padding: 8px;">This section contains product details and specifications.</div>
    </modus-accordion-item>
    <modus-accordion-item header-text="Pricing" icon="payment">
      <div style="padding: 8px;">View pricing information and available discounts.</div>
    </modus-accordion-item>
    <modus-accordion-item header-text="Support" disabled>
      <div style="padding: 8px;">Contact customer support for assistance.</div>
    </modus-accordion-item>
  </modus-accordion>
</div>
```

```typescript
const accordion = document.querySelector('#basic-accordion');
const accordionItems = accordion.querySelectorAll('modus-accordion-item');

// Add event listeners to all accordion items
accordionItems.forEach((item, index) => {
  item.addEventListener('opened', (event) => {
    console.log(`Accordion item ${index + 1} expanded`);
  });
  
  item.addEventListener('closed', (event) => {
    console.log(`Accordion item ${index + 1} collapsed`);
  });
});
```

## Prompt 2
**User Question:** How can I create a condensed accordion with custom expand button styles?

**Agent Answer:**
References:
For this implementation, I'll demonstrate two key features of the ModusAccordion:
1. The `size="condensed"` property which creates a more compact accordion style
2. The `expand-button-type="circleArrow"` property which changes the default expand button appearance

This approach provides a different visual style while maintaining the same functionality. The condensed size is useful for interfaces where space is limited but structured navigation is still required.

```html
<div id="condensed-accordion-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-accordion id="custom-accordion">
    <modus-accordion-item 
      header-text="Configuration Options" 
      size="condensed" 
      expand-button-type="circleArrow"
      expanded>
      <div style="padding: 8px;">Manage application settings and preferences.</div>
    </modus-accordion-item>
    <modus-accordion-item 
      header-text="User Profiles" 
      size="condensed"
      expand-button-type="circleArrow"
      icon="person">
      <div style="padding: 8px;">View and edit user profile information.</div>
    </modus-accordion-item>
    <modus-accordion-item 
      header-text="System Status" 
      size="condensed"
      expand-button-type="circleArrow"
      supporting-label="(New)">
      <div style="padding: 8px;">Check the current system status and health metrics.</div>
    </modus-accordion-item>
  </modus-accordion>
</div>
```

```typescript
const customAccordion = document.querySelector('#custom-accordion');

// Track which items are currently expanded
let expandedItems = new Set([0]); // First item is expanded by default

customAccordion.querySelectorAll('modus-accordion-item').forEach((item, index) => {
  item.addEventListener('opened', (event) => {
    expandedItems.add(index);
    console.log('Currently expanded items:', Array.from(expandedItems));
  });
  
  item.addEventListener('closed', (event) => {
    expandedItems.delete(index);
    console.log('Currently expanded items:', Array.from(expandedItems));
  });
});
```



# <ModusAlert>

## Prompt 1
**User Question:** How do I create different types of alerts in my application?

**Agent Answer:**
References:
I've analyzed the ModusAlert component properties and determined that the most important properties to demonstrate are:
- `type`: Defines the alert style (info, error, success, warning)
- `message`: The content displayed in the alert
- `dismissible`: Makes the alert closable by the user
- `buttonText`: Adds an action button to the alert

The component emits `dismissClick` and `actionClick` events which should be handled to respond to user interactions. This implementation shows how to create different alert types and handle their events appropriately.

```html
<div id="alerts-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <!-- Info alert (default) -->
  <modus-alert 
    id="info-alert"
    message="This is an informational message.">
  </modus-alert>
  
  <!-- Success alert with action button -->
  <modus-alert 
    id="success-alert"
    message="Operation completed successfully!" 
    type="success"
    button-text="View Details">
  </modus-alert>
  
  <!-- Warning alert with dismiss option -->
  <modus-alert 
    id="warning-alert"
    message="Your session will expire in 5 minutes." 
    type="warning"
    dismissible>
  </modus-alert>
  
  <!-- Error alert with both action and dismiss -->
  <modus-alert 
    id="error-alert"
    message="Unable to save changes. Please try again." 
    type="error"
    button-text="Retry"
    dismissible>
  </modus-alert>
</div>
```

```typescript
// Get references to all alerts
const infoAlert = document.querySelector('#info-alert');
const successAlert = document.querySelector('#success-alert');
const warningAlert = document.querySelector('#warning-alert');
const errorAlert = document.querySelector('#error-alert');

// Add event listeners to success alert
successAlert.addEventListener('actionClick', (event) => {
  console.log('Success alert action clicked - Showing details');
  // Logic to show operation details
});

// Add event listeners to warning alert
warningAlert.addEventListener('dismissClick', (event) => {
  console.log('Warning alert dismissed');
  // The alert will automatically be removed from DOM when dismissed
});

// Add event listeners to error alert
errorAlert.addEventListener('actionClick', (event) => {
  console.log('Error alert action clicked - Retrying operation');
  // Logic to retry the failed operation
});

errorAlert.addEventListener('dismissClick', (event) => {
  console.log('Error alert dismissed');
  // The alert will automatically be removed from DOM when dismissed
});
```

## Prompt 2
**User Question:** How can I create an alert with custom HTML content inside?

**Agent Answer:**
References:
While the `message` property allows for simple text content in alerts, using slot content instead enables the inclusion of rich HTML content. This is useful for alerts that need to contain links, formatted text, or other HTML elements.

I'm demonstrating how to create alerts with custom HTML content including links, formatting, and even more complex elements. This approach gives more flexibility while maintaining the alert's semantic purpose and styling.

```html
<div id="custom-alerts-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <!-- Alert with HTML content including a link -->
  <modus-alert 
    id="html-alert" 
    type="info">
    <div>
      This alert contains <strong>formatted text</strong> and 
      <a href="https://example.com" style="color: inherit; text-decoration: underline;">a hyperlink</a>.
    </div>
  </modus-alert>
  
  <!-- Success alert with HTML content -->
  <modus-alert 
    id="success-html-alert" 
    type="success"
    dismissible>
    <div>
      <strong>Installation Complete!</strong>
      <ul style="margin: 8px 0 0 20px; padding: 0;">
        <li>Core components installed</li>
        <li>Configuration updated</li>
        <li>Services restarted</li>
      </ul>
    </div>
  </modus-alert>
</div>
```

```typescript
// Get references to the alerts
const htmlAlert = document.querySelector('#html-alert');
const successHtmlAlert = document.querySelector('#success-html-alert');

// Track alert visibility
let alertsVisible = {
  htmlAlert: true,
  successHtmlAlert: true
};

// Add dismiss handler to the success alert with HTML content
successHtmlAlert.addEventListener('dismissClick', (event) => {
  console.log('Success alert with HTML content dismissed');
  alertsVisible.successHtmlAlert = false;
  
  // You might want to show another alert after this one is dismissed
  if (!alertsVisible.htmlAlert && !alertsVisible.successHtmlAlert) {
    console.log('All alerts have been dismissed');
    // Logic to handle when all alerts are dismissed
  }
});
```



# <ModusAutocomplete>

## Prompt 1
**User Question:** How do I create a basic autocomplete component with string options?

**Agent Answer:**
References:
I've analyzed the ModusAutocomplete component and identified that it supports different ways to provide options. For a basic implementation, I'm demonstrating:
- How to create an autocomplete with string array options
- Setting a label and placeholder to improve usability
- Including search icon for visual clarity
- Adding event handling for when values change or options are selected

This basic implementation shows the most common use case while keeping the code concise and focused on core functionality.

```html
<div id="autocomplete-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 400px;">
  <modus-autocomplete 
    id="fruit-autocomplete"
    label="Select a Fruit"
    placeholder="Start typing..."
    include-search-icon>
  </modus-autocomplete>
</div>
```

```typescript
const fruitAutocomplete = document.querySelector('#fruit-autocomplete');
if (fruitAutocomplete) {
  // Set the options as a simple string array
  fruitAutocomplete.options = [
    'Apple',
    'Banana',
    'Orange',
    'Mango',
    'Pineapple',
    'Grapes',
    'Watermelon',
    'Strawberry',
    'Blueberry',
    'Raspberry'
  ];
  
  // Listen for value changes (as user types)
  fruitAutocomplete.addEventListener('valueChange', (event) => {
    console.log('Search input value:', event.detail);
  });
  
  // Listen for option selection
  fruitAutocomplete.addEventListener('optionSelected', (event) => {
    console.log('Selected fruit:', event.detail);
  });
}
```

## Prompt 2
**User Question:** How can I create an autocomplete component with multiple selection and object options?

**Agent Answer:**
References:
For this more advanced implementation, I'm demonstrating several important features:
- Using the `multiple` property to allow selecting multiple options
- Using ModusAutocompleteOption objects with id/value pairs instead of simple strings
- Making the component clearable for better user experience
- Handling the specialized `selectionsChanged` event for multiple selections
- Using error text to provide feedback when needed

This approach is especially useful for forms where users need to select multiple items from a structured data set.

```html
<div id="multi-select-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 400px;">
  <modus-autocomplete 
    id="country-selector"
    label="Select Countries" 
    placeholder="Search countries..."
    multiple
    clearable>
  </modus-autocomplete>
  
  <div id="selection-display" style="margin-top: 8px; font-size: 14px;">
    Selected countries: None
  </div>
</div>
```

```typescript
const countrySelector = document.querySelector('#country-selector');
const selectionDisplay = document.querySelector('#selection-display');
let selectedCountries = [];

if (countrySelector) {
  // Set structured options with id/value pairs
  countrySelector.options = [
    { id: 'us', value: 'United States' },
    { id: 'ca', value: 'Canada' },
    { id: 'mx', value: 'Mexico' },
    { id: 'br', value: 'Brazil' },
    { id: 'uk', value: 'United Kingdom' },
    { id: 'fr', value: 'France' },
    { id: 'de', value: 'Germany' },
    { id: 'jp', value: 'Japan' },
    { id: 'cn', value: 'China' },
    { id: 'in', value: 'India' },
    { id: 'au', value: 'Australia' }
  ];
  
  // Listen for selections changed event (specific to multiple selection mode)
  countrySelector.addEventListener('selectionsChanged', (event) => {
    // Get array of selected country IDs
    selectedCountries = event.detail;
    
    // Update the display
    if (selectionDisplay) {
      if (selectedCountries.length > 0) {
        // Map selected IDs to country names for display
        const countryNames = selectedCountries.map(id => {
          const option = countrySelector.options.find(opt => opt.id === id);
          return option ? option.value : id;
        });
        selectionDisplay.textContent = `Selected countries: ${countryNames.join(', ')}`;
      } else {
        selectionDisplay.textContent = 'Selected countries: None';
      }
    }
    
    // Validate selection (example: require at least 2 selections)
    if (selectedCountries.length < 2) {
      countrySelector.errorText = "Please select at least 2 countries";
    } else {
      countrySelector.errorText = undefined;
    }
  });
}
```



# <ModusBadge>

## Prompt 1
**User Question:** How do I create different types of badges with various colors and sizes?

**Agent Answer:**
References:
I've analyzed the ModusBadge component and identified the key properties for customization:
- `type`: Determines the badge style (default, counter, or text)
- `color`: Sets the color scheme (primary, secondary, tertiary, dark, warning, danger, success)
- `size`: Controls the badge size (small, medium, large)

Badges are simple but versatile components that can be used to highlight information, indicate statuses, or show counters. The example below demonstrates the three main badge types with different colors and sizes to provide a comprehensive overview of available options.

```html
<div id="badges-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%; margin-bottom: 8px;">Default Badges:</h4>
    <modus-badge>Primary</modus-badge>
    <modus-badge color="secondary">Secondary</modus-badge>
    <modus-badge color="tertiary">Tertiary</modus-badge>
    <modus-badge color="dark">Dark</modus-badge>
    <modus-badge color="warning">Warning</modus-badge>
    <modus-badge color="danger">Danger</modus-badge>
    <modus-badge color="success">Success</modus-badge>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%; margin-bottom: 8px;">Counter Badges:</h4>
    <modus-badge type="counter">8</modus-badge>
    <modus-badge type="counter" color="danger">15</modus-badge>
    <modus-badge type="counter" color="warning" size="small">3</modus-badge>
    <modus-badge type="counter" color="success" size="large">42</modus-badge>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%; margin-bottom: 8px;">Text Badges:</h4>
    <modus-badge type="text">New</modus-badge>
    <modus-badge type="text" color="secondary">Updated</modus-badge>
    <modus-badge type="text" color="success">Active</modus-badge>
    <modus-badge type="text" color="danger">Critical</modus-badge>
    <modus-badge type="text" color="dark" size="large">Premium</modus-badge>
  </div>
</div>
```

```typescript
// For a dynamic badge example - updating a counter badge
const updateBadgeCounter = () => {
  const counterBadge = document.querySelector('modus-badge[type="counter"]');
  if (counterBadge) {
    // Get the current count and increment it
    let count = parseInt(counterBadge.textContent || '0');
    count++;
    
    // Update the badge text content
    counterBadge.textContent = count.toString();
    
    // Optionally change color based on threshold
    if (count > 10) {
      counterBadge.setAttribute('color', 'danger');
    } else if (count > 5) {
      counterBadge.setAttribute('color', 'warning');
    }
  }
};

// Example: Set up a button that updates the counter
const setupCounterButton = () => {
  const container = document.getElementById('badges-container');
  if (container) {
    const button = document.createElement('button');
    button.textContent = 'Increment Counter';
    button.style.marginTop = '16px';
    button.addEventListener('click', updateBadgeCounter);
    container.appendChild(button);
  }
};

// Call this to set up the demo
setupCounterButton();
```

## Prompt 2
**User Question:** How can I use badges in a notification or status context?

**Agent Answer:**
References:
Badges are particularly useful when representing statuses or indicating notifications. For this implementation, I'll focus on:
- Using badges within other UI elements (like buttons or list items)
- Combining different badge types to represent status and counts
- Creating a realistic notification panel scenario

This approach demonstrates practical application of badges in common UI patterns for status indication and notification counts.

```html
<div id="status-badges-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; max-width: 400px;">
  <!-- Notification Button with Counter Badge -->
  <div style="position: relative; width: fit-content;">
    <button style="padding: 8px 16px; background: #f5f5f5; border: 1px solid #ddd; border-radius: 4px;">
      Notifications
    </button>
    <div style="position: absolute; top: -8px; right: -8px;">
      <modus-badge id="notification-count" type="counter" color="danger" size="small">5</modus-badge>
    </div>
  </div>
  
  <!-- Status List with Various Badge Types -->
  <div style="border: 1px solid #ddd; border-radius: 4px; overflow: hidden;">
    <div style="padding: 10px; background: #f5f5f5; font-weight: bold;">System Status</div>
    <ul style="list-style: none; margin: 0; padding: 0;">
      <li style="padding: 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
        Database <modus-badge type="text" color="success">Online</modus-badge>
      </li>
      <li style="padding: 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
        API Server <modus-badge type="text" color="warning">Degraded</modus-badge>
      </li>
      <li style="padding: 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
        Storage <modus-badge type="text" color="danger">Offline</modus-badge>
      </li>
      <li style="padding: 12px; display: flex; justify-content: space-between; align-items: center;">
        Web Frontend <modus-badge type="text" color="success">Online</modus-badge>
      </li>
    </ul>
  </div>
  
  <!-- Task List with Priority Badges -->
  <div style="border: 1px solid #ddd; border-radius: 4px; overflow: hidden;">
    <div style="padding: 10px; background: #f5f5f5; font-weight: bold;">Tasks</div>
    <ul style="list-style: none; margin: 0; padding: 0;">
      <li style="padding: 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
        <span>Update user documentation</span>
        <modus-badge color="dark">Low</modus-badge>
      </li>
      <li style="padding: 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
        <span>Fix authentication bug</span>
        <modus-badge color="warning">Medium</modus-badge>
      </li>
      <li style="padding: 12px; display: flex; justify-content: space-between; align-items: center;">
        <span>Resolve security vulnerability</span>
        <modus-badge color="danger">Urgent</modus-badge>
      </li>
    </ul>
  </div>
</div>
```

```typescript
// Simulate receiving new notifications
const simulateNewNotification = () => {
  const notificationBadge = document.getElementById('notification-count');
  if (notificationBadge) {
    // Get current count
    let count = parseInt(notificationBadge.textContent || '0');
    count++;
    
    // Update badge
    notificationBadge.textContent = count.toString();
    
    // Flash animation
    notificationBadge.style.transform = 'scale(1.3)';
    setTimeout(() => {
      notificationBadge.style.transform = 'scale(1)';
    }, 200);
    
    // Update system status randomly for demo
    updateRandomSystemStatus();
  }
};

// Update a random system status for demonstration
const updateRandomSystemStatus = () => {
  const statusItems = document.querySelectorAll('#status-badges-container li');
  if (statusItems.length > 0) {
    // Pick a random status item
    const randomIndex = Math.floor(Math.random() * statusItems.length);
    const statusItem = statusItems[randomIndex];
    const badge = statusItem.querySelector('modus-badge');
    
    if (badge) {
      // Rotate through statuses
      const currentStatus = badge.textContent;
      const statuses = {
        'Online': { text: 'Degraded', color: 'warning' },
        'Degraded': { text: 'Offline', color: 'danger' },
        'Offline': { text: 'Online', color: 'success' }
      };
      
      if (statuses[currentStatus]) {
        badge.textContent = statuses[currentStatus].text;
        badge.setAttribute('color', statuses[currentStatus].color);
      }
    }
  }
};

// Set an interval to simulate notifications (for demo purposes)
const notificationInterval = setInterval(simulateNewNotification, 5000);

// Clean up interval when page is closed
window.addEventListener('beforeunload', () => {
  clearInterval(notificationInterval);
});
```



# <ModusBreadcrumb>

## Prompt 1
**User Question:** How do I create a breadcrumb navigation component for my application?

**Agent Answer:**
References:
I've analyzed the ModusBreadcrumb component and its usage pattern. The key aspects to understand are:
- The component requires a `crumbs` array with each item having `id` and `display` properties
- You can set `underlineLinks` to true if you want the breadcrumb links to be underlined
- The component emits a `crumbClick` event when a user clicks on a breadcrumb

This implementation demonstrates a basic breadcrumb navigation with event handling to respond to user navigation.

```html
<div id="breadcrumb-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-breadcrumb 
    id="main-breadcrumb" 
    aria-label="Site Navigation">
  </modus-breadcrumb>
</div>
```

```typescript
// Get a reference to the breadcrumb component
const breadcrumb = document.querySelector('#main-breadcrumb');

if (breadcrumb) {
  // Define the navigation path
  const crumbs = [
    { id: 'home', display: 'Home' },
    { id: 'products', display: 'Products' },
    { id: 'electronics', display: 'Electronics' },
    { id: 'computers', display: 'Computers' }
  ];
  
  // Set the crumbs property
  breadcrumb.crumbs = crumbs;
  
  // Handle breadcrumb navigation
  breadcrumb.addEventListener('crumbClick', (event) => {
    const clickedCrumb = event.detail;
    console.log(`Navigating to: ${clickedCrumb.display} (${clickedCrumb.id})`);
    
    // Here you would typically navigate to the corresponding page
    // For example in a single-page application:
    // router.navigate([clickedCrumb.id]);
    
    // For demo purposes, let's update the breadcrumb based on the click
    // This simulates navigation by removing crumbs after the clicked one
    const clickedIndex = crumbs.findIndex(crumb => crumb.id === clickedCrumb.id);
    if (clickedIndex >= 0) {
      const newCrumbs = crumbs.slice(0, clickedIndex + 1);
      breadcrumb.crumbs = newCrumbs;
    }
  });
}
```

## Prompt 2
**User Question:** How can I create a dynamic breadcrumb that updates as users navigate through the application?

**Agent Answer:**
References:
For dynamic breadcrumbs that update with user navigation, I'm implementing:
- A function to update breadcrumbs based on the current page path
- An approach that manages breadcrumb history as users navigate
- Underlined breadcrumb links for better visibility
- Custom styling to match application design

This pattern is commonly used in applications where the navigation structure is deep or complex, providing users with context about their location in the app.

```html
<div id="dynamic-breadcrumb-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; align-items: center; gap: 16px;">
    <modus-breadcrumb 
      id="dynamic-breadcrumb" 
      underline-links
      aria-label="Application Navigation">
    </modus-breadcrumb>
  </div>
  
  <!-- Simulated navigation buttons for demo -->
  <div style="display: flex; gap: 8px; margin-top: 16px;">
    <button id="nav-home" style="padding: 6px 12px;">Home</button>
    <button id="nav-dashboard" style="padding: 6px 12px;">Dashboard</button>
    <button id="nav-settings" style="padding: 6px 12px;">Settings</button>
    <button id="nav-profile" style="padding: 6px 12px;">User Profile</button>
    <button id="nav-security" style="padding: 6px 12px;">Security Settings</button>
  </div>
</div>
```

```typescript
// Navigation state and history management
let currentPath = '';
const pathHistory = {};

// Get a reference to the breadcrumb component
const dynamicBreadcrumb = document.querySelector('#dynamic-breadcrumb');

// Function to update breadcrumbs based on current path
const updateBreadcrumbs = (path) => {
  if (!dynamicBreadcrumb) return;
  
  currentPath = path;
  let segments = path.split('/').filter(segment => segment);
  
  // Define breadcrumb structure
  const navigationMap = {
    '': { id: 'home', display: 'Home' },
    'dashboard': { id: 'dashboard', display: 'Dashboard' },
    'settings': { id: 'settings', display: 'Settings' },
    'profile': { id: 'profile', display: 'User Profile' },
    'security': { id: 'security', display: 'Security Settings' }
  };
  
  // Build breadcrumb trail
  const crumbs = [navigationMap['']]; // Always include home
  
  let currentPathSegment = '';
  segments.forEach(segment => {
    currentPathSegment += segment;
    
    if (navigationMap[segment]) {
      crumbs.push(navigationMap[segment]);
    }
    
    currentPathSegment += '/';
  });
  
  // Update the breadcrumb component
  dynamicBreadcrumb.crumbs = crumbs;
  
  // Store this path in history
  pathHistory[path] = crumbs;
};

// Set up navigation button event listeners
document.querySelector('#nav-home')?.addEventListener('click', () => {
  updateBreadcrumbs('');
});

document.querySelector('#nav-dashboard')?.addEventListener('click', () => {
  updateBreadcrumbs('dashboard');
});

document.querySelector('#nav-settings')?.addEventListener('click', () => {
  updateBreadcrumbs('settings');
});

document.querySelector('#nav-profile')?.addEventListener('click', () => {
  updateBreadcrumbs('settings/profile');
});

document.querySelector('#nav-security')?.addEventListener('click', () => {
  updateBreadcrumbs('settings/security');
});

// Set initial breadcrumb
updateBreadcrumbs('');

// Handle breadcrumb navigation
dynamicBreadcrumb?.addEventListener('crumbClick', (event) => {
  const clickedCrumb = event.detail;
  
  // Navigate based on the clicked crumb
  switch (clickedCrumb.id) {
    case 'home':
      updateBreadcrumbs('');
      break;
    case 'dashboard':
      updateBreadcrumbs('dashboard');
      break;
    case 'settings':
      updateBreadcrumbs('settings');
      break;
    case 'profile':
      updateBreadcrumbs('settings/profile');
      break;
    case 'security':
      updateBreadcrumbs('settings/security');
      break;
  }
});
```



# <ModusButton>

## Prompt 1
**User Question:** How do I create different button styles and handle button click events?

**Agent Answer:**
References:
I've analyzed the ModusButton component and identified its key properties for creating various styles:
- `color`: Controls the button's color scheme (primary, secondary, tertiary, danger, special)
- `buttonStyle`: Defines the button appearance (fill, outline, borderless)
- `size`: Adjusts the button dimensions (small, medium, large)
- `disabled`: Makes the button non-interactive
- Icon options: `leftIcon`, `rightIcon`, and `iconOnly` for different icon placements

The implementation below demonstrates common button variants and proper event handling through the `buttonClick` event.

```html
<div id="button-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">Basic Buttons:</h4>
    <modus-button id="primary-btn" color="primary">Primary</modus-button>
    <modus-button id="secondary-btn" color="secondary">Secondary</modus-button>
    <modus-button id="tertiary-btn" color="tertiary">Tertiary</modus-button>
    <modus-button id="danger-btn" color="danger">Danger</modus-button>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">Button Styles:</h4>
    <modus-button button-style="fill" color="primary">Fill</modus-button>
    <modus-button button-style="outline" color="primary">Outline</modus-button>
    <modus-button button-style="borderless" color="primary">Borderless</modus-button>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">Button Sizes:</h4>
    <modus-button size="small" color="primary">Small</modus-button>
    <modus-button size="medium" color="primary">Medium</modus-button>
    <modus-button size="large" color="primary">Large</modus-button>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">States:</h4>
    <modus-button color="primary">Enabled</modus-button>
    <modus-button color="primary" disabled>Disabled</modus-button>
  </div>
  
  <div id="event-display" style="margin-top: 16px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px; min-height: 40px;">
    Click a button to see events
  </div>
</div>
```

```typescript
// Get references to specific buttons and display area
const primaryBtn = document.querySelector('#primary-btn');
const secondaryBtn = document.querySelector('#secondary-btn');
const tertiaryBtn = document.querySelector('#tertiary-btn');
const dangerBtn = document.querySelector('#danger-btn');
const eventDisplay = document.querySelector('#event-display');

// Function to handle button clicks
const handleButtonClick = (event, buttonName) => {
  console.log(`${buttonName} button clicked`, event);
  
  if (eventDisplay) {
    eventDisplay.textContent = `${buttonName} button was clicked at ${new Date().toLocaleTimeString()}`;
  }
  
  // You would typically perform an action based on which button was clicked
  switch (buttonName) {
    case 'Primary':
      // Handle primary action
      break;
    case 'Secondary':
      // Handle secondary action
      break;
    case 'Tertiary':
      // Handle tertiary action
      break;
    case 'Danger':
      // Handle dangerous action
      break;
  }
};

// Add click event listeners to buttons
if (primaryBtn) {
  primaryBtn.addEventListener('buttonClick', (event) => handleButtonClick(event, 'Primary'));
}

if (secondaryBtn) {
  secondaryBtn.addEventListener('buttonClick', (event) => handleButtonClick(event, 'Secondary'));
}

if (tertiaryBtn) {
  tertiaryBtn.addEventListener('buttonClick', (event) => handleButtonClick(event, 'Tertiary'));
}

if (dangerBtn) {
  dangerBtn.addEventListener('buttonClick', (event) => handleButtonClick(event, 'Danger'));
}

// Add global event listener to catch all button clicks in container
const buttonContainer = document.querySelector('#button-container');
if (buttonContainer) {
  buttonContainer.addEventListener('buttonClick', (event) => {
    // You can use event delegation here to handle all buttons with one listener
    const button = event.target;
    console.log('Button clicked via delegation:', button);
  });
}
```

## Prompt 2
**User Question:** How do I create buttons with icons and special behaviors like loading states?

**Agent Answer:**
References:
For this implementation, I'm focusing on more advanced button features:
- Using icons in different positions: left, right, and icon-only buttons
- Creating a loading state using a spinner component inside the button
- Demonstrating the critical action animation for dangerous operations
- Showing the caret option for dropdown-style buttons

These features make buttons more informative and provide visual feedback for different states and actions.

```html
<div id="advanced-buttons-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">Icon Buttons:</h4>
    <modus-button id="left-icon-btn" left-icon="add">Add Item</modus-button>
    <modus-button id="right-icon-btn" color="secondary" right-icon="arrow_right">Continue</modus-button>
    <modus-button id="both-icons-btn" color="tertiary" left-icon="check" right-icon="arrow_right">Validate & Continue</modus-button>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">Icon-Only Buttons:</h4>
    <modus-button icon-only="edit" aria-label="Edit"></modus-button>
    <modus-button icon-only="delete" color="danger" aria-label="Delete"></modus-button>
    <modus-button icon-only="settings" button-style="outline" aria-label="Settings"></modus-button>
    <modus-button icon-only="info" color="tertiary" button-style="borderless" aria-label="Information"></modus-button>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
    <h4 style="width: 100%;">Special Behaviors:</h4>
    <modus-button id="loading-btn" color="primary">
      Click to Load
    </modus-button>
    
    <modus-button id="critical-btn" color="danger" critical-action>
      Delete Account
    </modus-button>
    
    <modus-button color="secondary" show-caret="true">
      Dropdown
    </modus-button>
  </div>
</div>
```

```typescript
// Get references to buttons with special behaviors
const loadingBtn = document.querySelector('#loading-btn');
const criticalBtn = document.querySelector('#critical-btn');

// Handle loading button clicks - toggle loading state
if (loadingBtn) {
  let isLoading = false;
  
  loadingBtn.addEventListener('buttonClick', () => {
    if (!isLoading) {
      // Set loading state
      isLoading = true;
      
      // Store original text
      const originalText = loadingBtn.textContent;
      
      // Replace with spinner and text
      loadingBtn.innerHTML = `
        <modus-spinner color="white" size=".5rem"></modus-spinner>
        &nbsp;Loading...
      `;
      
      // Disable button during loading
      loadingBtn.disabled = true;
      
      // Simulate loading process
      setTimeout(() => {
        // Reset button state
        loadingBtn.textContent = originalText;
        loadingBtn.disabled = false;
        isLoading = false;
      }, 2000);
    }
  });
}

// Handle critical action button clicks
if (criticalBtn) {
  criticalBtn.addEventListener('buttonClick', () => {
    // Confirm with user before proceeding with critical action
    const confirmAction = window.confirm('Are you sure you want to delete this account? This action cannot be undone.');
    
    if (confirmAction) {
      // Perform the critical action
      console.log('Critical action confirmed, proceeding...');
      
      // Disable the button to prevent multiple clicks
      criticalBtn.disabled = true;
      
      // Simulate processing
      setTimeout(() => {
        alert('Account deleted successfully');
        
        // Re-enable the button
        criticalBtn.disabled = false;
      }, 1500);
    } else {
      console.log('Critical action cancelled');
    }
  });
}

// Add event listeners to icon buttons for demo
document.querySelector('#left-icon-btn')?.addEventListener('buttonClick', () => {
  console.log('Add item button clicked');
});

document.querySelector('#right-icon-btn')?.addEventListener('buttonClick', () => {
  console.log('Continue button clicked');
});

document.querySelector('#both-icons-btn')?.addEventListener('buttonClick', () => {
  console.log('Validate & Continue button clicked');
});
```



# <ModusButtonGroup>

## Prompt 1
**User Question:** How do I create a button group with single selection capability?

**Agent Answer:**
References:
I've analyzed the ModusButtonGroup component and focused on implementing a single-selection button group, which is particularly useful for mutually exclusive options. Key properties to understand include:
- `selection-type`: Setting this to "single" ensures only one button can be selected at a time
- `color`: Defines the color scheme for all buttons in the group
- `buttonStyle`: Controls the visual style of buttons (outline, fill, borderless)
- `selectionChange` event: Fires when a button selection changes, providing the currently selected button

This implementation includes proper event handling to track selection changes and update related content accordingly.

```html
<div id="button-group-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h4>View Mode</h4>
  <modus-button-group 
    id="view-mode-group"
    selection-type="single" 
    color="primary"
    button-style="outline"
    aria-label="Select View Mode">
    <modus-button id="list-view-btn" selected>List</modus-button>
    <modus-button id="grid-view-btn">Grid</modus-button>
    <modus-button id="table-view-btn">Table</modus-button>
  </modus-button-group>
  
  <div id="view-mode-display" style="margin-top: 16px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px;">
    Current view mode: List
  </div>
</div>
```

```typescript
// Get references to the button group and display element
const viewModeGroup = document.querySelector('#view-mode-group');
const viewModeDisplay = document.querySelector('#view-mode-display');

if (viewModeGroup) {
  // Listen for selection changes
  viewModeGroup.addEventListener('selectionChange', (event) => {
    // The event detail contains an array of selected buttons (in this case, only one)
    const selectedButtons = event.detail;
    
    if (selectedButtons.length > 0) {
      const selectedButton = selectedButtons[0];
      const viewMode = selectedButton.textContent.trim();
      
      // Update the display to show current selection
      if (viewModeDisplay) {
        viewModeDisplay.textContent = `Current view mode: ${viewMode}`;
      }
      
      // You would typically update your UI based on the selection here
      console.log(`View mode changed to: ${viewMode}`);
    }
  });
  
  // You can also listen for individual button clicks for more detailed control
  viewModeGroup.addEventListener('buttonClick', (event) => {
    const buttonInfo = event.detail;
    console.log(`Button clicked: ${buttonInfo.button.textContent.trim()}`);
    console.log(`Is selected: ${buttonInfo.isSelected}`);
  });
}
```

## Prompt 2
**User Question:** How can I create a multi-select button group for filtering options?

**Agent Answer:**
References:
For this implementation, I'm focusing on creating a button group with multiple selection capability, which is ideal for filters or options where multiple choices are allowed. Key features demonstrated:
- `selection-type="multiple"`: Enables selecting multiple buttons simultaneously
- Setting initial selections with the `selected` attribute on buttons 
- Handling `selectionChange` events to get the array of all currently selected buttons
- Combining this component with other UI elements to create a functional filter system

The multiple selection mode is particularly useful for filters, tags, or any interface where users can select several options at once.

```html
<div id="filter-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h4>Filter by Category</h4>
  <modus-button-group 
    id="category-filter-group"
    selection-type="multiple" 
    color="secondary"
    button-style="fill"
    size="small"
    aria-label="Filter by Category">
    <modus-button id="electronics-btn" selected>Electronics</modus-button>
    <modus-button id="clothing-btn">Clothing</modus-button>
    <modus-button id="books-btn" selected>Books</modus-button>
    <modus-button id="home-btn">Home</modus-button>
  </modus-button-group>
  
  <h4 style="margin-top: 16px;">Price Range</h4>
  <modus-button-group 
    id="price-filter-group"
    selection-type="multiple" 
    color="tertiary"
    button-style="borderless"
    size="small"
    aria-label="Filter by Price">
    <modus-button id="price-low-btn">$0-$25</modus-button>
    <modus-button id="price-med-btn" selected>$25-$100</modus-button>
    <modus-button id="price-high-btn">$100+</modus-button>
  </modus-button-group>
  
  <div id="active-filters" style="margin-top: 24px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px;">
    <h5 style="margin-top: 0;">Active Filters:</h5>
    <div id="filter-tags" style="display: flex; flex-wrap: wrap; gap: 8px;"></div>
  </div>
  
  <button id="apply-filters-btn" style="margin-top: 16px; padding: 8px 16px;">Apply Filters</button>
</div>
```

```typescript
// Keep track of all active filters
let activeFilters = {
  categories: ['Electronics', 'Books'],
  priceRanges: ['$25-$100']
};

// Get references to the button groups
const categoryFilterGroup = document.querySelector('#category-filter-group');
const priceFilterGroup = document.querySelector('#price-filter-group');
const filterTagsContainer = document.querySelector('#filter-tags');
const applyFiltersBtn = document.querySelector('#apply-filters-btn');

// Function to update the filter tags display
const updateFilterTags = () => {
  if (filterTagsContainer) {
    // Clear existing tags
    filterTagsContainer.innerHTML = '';
    
    // Add category filter tags
    activeFilters.categories.forEach(category => {
      const tag = document.createElement('div');
      tag.style.backgroundColor = '#f0f0f0';
      tag.style.padding = '4px 10px';
      tag.style.borderRadius = '16px';
      tag.style.fontSize = '14px';
      tag.textContent = category;
      filterTagsContainer.appendChild(tag);
    });
    
    // Add price range filter tags
    activeFilters.priceRanges.forEach(priceRange => {
      const tag = document.createElement('div');
      tag.style.backgroundColor = '#e0f0ff';
      tag.style.padding = '4px 10px';
      tag.style.borderRadius = '16px';
      tag.style.fontSize = '14px';
      tag.textContent = priceRange;
      filterTagsContainer.appendChild(tag);
    });
    
    // Add message if no filters
    if (activeFilters.categories.length === 0 && activeFilters.priceRanges.length === 0) {
      filterTagsContainer.textContent = 'No filters selected';
    }
  }
};

// Initialize the display
updateFilterTags();

// Handle category filter changes
if (categoryFilterGroup) {
  categoryFilterGroup.addEventListener('selectionChange', (event) => {
    const selectedButtons = event.detail;
    activeFilters.categories = selectedButtons.map(button => button.textContent.trim());
    updateFilterTags();
  });
}

// Handle price range filter changes
if (priceFilterGroup) {
  priceFilterGroup.addEventListener('selectionChange', (event) => {
    const selectedButtons = event.detail;
    activeFilters.priceRanges = selectedButtons.map(button => button.textContent.trim());
    updateFilterTags();
  });
}

// Handle apply filters button
if (applyFiltersBtn) {
  applyFiltersBtn.addEventListener('click', () => {
    console.log('Applying filters:', activeFilters);
    // Here you would typically trigger a data fetch or filter operation
    alert(`Filters applied: ${JSON.stringify(activeFilters)}`);
  });
}
```



# <ModusCard>

## Prompt 1
**User Question:** How do I create a basic card component with content and styling?

**Agent Answer:**
References:
I've analyzed the ModusCard component and identified its key properties:
- `height` and `width`: Control the dimensions of the card
- `showCardBorder`: Toggles the visibility of the card's border
- `showShadowOnHover`: Controls the hover effect with a shadow
- `borderRadius`: Adjusts the corner rounding of the card

The ModusCard is primarily a container component that provides styling and structure for content. It doesn't have built-in content sections like some card components in other frameworks, so you need to structure your own content inside it.

```html
<div id="card-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-card 
    id="basic-card"
    height="300px" 
    width="280px" 
    show-card-border="true" 
    show-shadow-on-hover="true">
    <div style="padding: 16px; display: flex; flex-direction: column; height: 100%;">
      <!-- Card Header -->
      <div style="margin-bottom: 12px;">
        <h3 style="margin: 0 0 4px 0; font-size: 18px;">Product Overview</h3>
        <p style="margin: 0; color: #666; font-size: 14px;">Premium Software Solution</p>
      </div>
      
      <!-- Card Content -->
      <div style="flex-grow: 1;">
        <p style="margin-top: 0;">
          This comprehensive solution provides robust features for enterprise needs.
          Streamline workflows and improve productivity with our intuitive interface.
        </p>
        <ul style="padding-left: 20px; margin-bottom: 24px;">
          <li>Advanced analytics dashboard</li>
          <li>Multi-user collaboration</li>
          <li>Secure cloud storage</li>
        </ul>
      </div>
      
      <!-- Card Footer with Actions -->
      <div style="margin-top: auto;">
        <modus-button color="primary">Learn More</modus-button>
        <modus-button button-style="borderless" style="margin-left: 8px;">Contact Sales</modus-button>
      </div>
    </div>
  </modus-card>
</div>
```

```typescript
// Get a reference to the card
const basicCard = document.querySelector('#basic-card');

// Example: Add interaction to the card
if (basicCard) {
  // You can add event listeners to elements inside the card
  const learnMoreButton = basicCard.querySelector('modus-button[color="primary"]');
  const contactButton = basicCard.querySelector('modus-button[button-style="borderless"]');
  
  learnMoreButton?.addEventListener('buttonClick', () => {
    console.log('Learn More button clicked');
    // Navigate to product details page or show more information
    // window.location.href = '/product-details';
  });
  
  contactButton?.addEventListener('buttonClick', () => {
    console.log('Contact Sales button clicked');
    // Open contact form or navigate to contact page
    // openContactForm();
  });
  
  // Optionally make the entire card clickable (common pattern)
  basicCard.style.cursor = 'pointer';
  basicCard.addEventListener('click', (event) => {
    // Prevent click when clicking on buttons
    if (event.target.closest('modus-button')) {
      return;
    }
    
    console.log('Card clicked');
    // Navigate to detailed view or perform primary action
    // window.location.href = '/product-details';
  });
}
```

## Prompt 2
**User Question:** How can I create a grid of different card styles for a product catalog?

**Agent Answer:**
References:
For this implementation, I'll demonstrate:
- Creating a responsive grid of cards with different styles and configurations
- Customizing each card's appearance using the component's properties
- Structuring different content layouts within the cards
- Implementing interactive elements and handling events

This pattern is useful for dashboards, catalogs, or any interface where multiple content cards need to be displayed in a grid layout.

```html
<div id="card-grid-container" style="padding: 16px;">
  <h3>Product Catalog</h3>
  
  <!-- Card Grid with different card styles -->
  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin-top: 16px;">
    
    <!-- Standard Card with Border -->
    <modus-card 
      id="product-card-1" 
      height="320px" 
      width="100%" 
      show-card-border="true" 
      show-shadow-on-hover="true">
      <div style="padding: 16px; height: 100%; display: flex; flex-direction: column;">
        <img src="https://via.placeholder.com/100x80" alt="Product image" style="align-self: center; margin-bottom: 12px;">
        <h4 style="margin: 0 0 8px 0;">Premium Desktop</h4>
        <p style="margin: 0 0 16px 0; color: #707070; font-size: 14px;">High-performance workstation</p>
        <p>Powerful desktop computer with the latest processor, ample memory, and fast storage.</p>
        <div style="margin-top: auto;">
          <p style="font-weight: bold; font-size: 18px;">$1,299.99</p>
          <modus-button color="primary" style="width: 100%;">Add to Cart</modus-button>
        </div>
      </div>
    </modus-card>
    
    <!-- Card without Border -->
    <modus-card 
      id="product-card-2" 
      height="320px" 
      width="100%" 
      show-card-border="false" 
      border-radius="8px"
      show-shadow-on-hover="true">
      <div style="padding: 16px; height: 100%; display: flex; flex-direction: column; background-color: #f8f9fa;">
        <div style="background-color: #e9ecef; padding: 12px; border-radius: 4px; margin-bottom: 12px; text-align: center;">
          <img src="https://via.placeholder.com/100x80" alt="Product image">
        </div>
        <h4 style="margin: 0 0 8px 0;">Wireless Headphones</h4>
        <p style="margin: 0 0 16px 0; color: #707070; font-size: 14px;">Noise-cancelling</p>
        <p>Premium audio experience with long battery life and comfortable design.</p>
        <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center;">
          <p style="font-weight: bold; font-size: 18px;">$249.99</p>
          <modus-button color="secondary" button-style="outline">View Details</modus-button>
        </div>
      </div>
    </modus-card>
    
    <!-- Special Feature Card -->
    <modus-card 
      id="product-card-3" 
      height="320px" 
      width="100%" 
      show-card-border="true"
      border-radius="0px">
      <div style="height: 100%; display: flex; flex-direction: column;">
        <div style="background-color: #0063a3; color: white; padding: 16px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <h4 style="margin: 0;">Limited Offer</h4>
            <span style="background-color: #e63946; padding: 4px 8px; border-radius: 4px; font-size: 12px;">SALE</span>
          </div>
          <p style="margin: 8px 0 0 0; font-size: 14px;">Ends in 48 hours</p>
        </div>
        <div style="padding: 16px; flex-grow: 1;">
          <h4 style="margin: 0 0 8px 0;">Smart Watch Pro</h4>
          <p>Advanced fitness tracking, notifications, and health monitoring in an elegant design.</p>
          <div style="display: flex; align-items: center; margin: 16px 0;">
            <p style="text-decoration: line-through; color: #707070; margin: 0 8px 0 0;">$399.99</p>
            <p style="font-weight: bold; font-size: 18px; margin: 0; color: #e63946;">$299.99</p>
          </div>
          <modus-button color="primary" style="width: 100%;">Add to Cart</modus-button>
        </div>
      </div>
    </modus-card>
    
    <!-- Minimalist Card -->
    <modus-card 
      id="product-card-4" 
      height="320px" 
      width="100%" 
      show-card-border="true"
      border-radius="16px">
      <div style="padding: 0; height: 100%; display: flex; flex-direction: column;">
        <div style="height: 50%; overflow: hidden;">
          <img src="https://via.placeholder.com/300x150" alt="Product image" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div style="padding: 16px; flex-grow: 1; display: flex; flex-direction: column;">
          <h4 style="margin: 0 0 8px 0;">Ultra-Thin Tablet</h4>
          <p style="margin: 0 0 auto 0;">Sleek design with powerful performance for work and entertainment.</p>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px;">
            <p style="font-weight: bold; font-size: 18px; margin: 0;">$649.99</p>
            <modus-button color="tertiary" button-style="borderless" right-icon="arrow_right">Details</modus-button>
          </div>
        </div>
      </div>
    </modus-card>
  </div>
</div>
```

```typescript
// Function to set up card interactions
const setupCardInteractions = () => {
  // Get references to all product cards
  const productCards = document.querySelectorAll('[id^="product-card-"]');
  
  productCards.forEach((card, index) => {
    // Make cards interactive with hover effect
    card.style.cursor = 'pointer';
    
    // Get buttons inside each card
    const primaryButton = card.querySelector('modus-button[color="primary"]');
    const detailsButton = card.querySelector('modus-button:not([color="primary"])');
    
    // Handle primary button clicks (Add to Cart)
    primaryButton?.addEventListener('buttonClick', (event) => {
      event.stopPropagation(); // Prevent card click
      console.log(`Adding product ${index + 1} to cart`);
      
      // Animation feedback for button click
      primaryButton.innerHTML = 'Added to Cart ✓';
      setTimeout(() => {
        primaryButton.innerHTML = 'Add to Cart';
      }, 2000);
    });
    
    // Handle secondary button clicks (View Details)
    detailsButton?.addEventListener('buttonClick', (event) => {
      event.stopPropagation(); // Prevent card click
      console.log(`Viewing details for product ${index + 1}`);
      // Navigate to product details page
      // window.location.href = `/products/${index + 1}`;
    });
    
    // Handle card clicks (open product details)
    card.addEventListener('click', (event) => {
      // Don't trigger card click when clicking buttons
      if (event.target.closest('modus-button')) {
        return;
      }
      
      console.log(`Card ${index + 1} clicked - opening product details`);
      // Navigate to product details page
      // window.location.href = `/products/${index + 1}`;
    });
  });
};

// Initialize card interactions
setupCardInteractions();
```



# <ModusCheckbox>

## Prompt 1
**User Question:** How do I create and use checkboxes with different states and sizes?

**Agent Answer:**
References:
I've analyzed the ModusCheckbox component and identified its key properties:
- `checked`: Controls whether the checkbox is selected
- `indeterminate`: Creates a third "partially selected" state
- `disabled`: Makes the checkbox non-interactive
- `label`: Adds descriptive text next to the checkbox
- `size`: Controls the checkbox size (small or medium)

The component emits a `checkboxClick` event when the user toggles the checkbox state. This implementation demonstrates creating different checkbox states and handling their events properly.

```html
<div id="checkbox-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h4>Basic Checkboxes</h4>
  <div style="display: flex; flex-direction: column; gap: 8px;">
    <modus-checkbox 
      id="terms-checkbox" 
      label="I agree to the terms and conditions">
    </modus-checkbox>
    
    <modus-checkbox 
      id="newsletter-checkbox" 
      label="Subscribe to newsletter"
      checked>
    </modus-checkbox>
    
    <modus-checkbox 
      id="disabled-checkbox" 
      label="Premium features (unavailable)"
      disabled>
    </modus-checkbox>
    
    <modus-checkbox 
      id="disabled-checked-checkbox" 
      label="Required setting (cannot change)"
      checked
      disabled>
    </modus-checkbox>
  </div>
  
  <h4>Indeterminate Checkbox</h4>
  <div style="display: flex; flex-direction: column; gap: 8px;">
    <modus-checkbox 
      id="parent-checkbox" 
      label="Select all items">
    </modus-checkbox>
    
    <div style="margin-left: 24px; display: flex; flex-direction: column; gap: 4px;">
      <modus-checkbox id="child-checkbox-1" label="Item 1"></modus-checkbox>
      <modus-checkbox id="child-checkbox-2" label="Item 2"></modus-checkbox>
      <modus-checkbox id="child-checkbox-3" label="Item 3"></modus-checkbox>
    </div>
  </div>
  
  <h4>Small Checkboxes</h4>
  <div style="display: flex; flex-direction: column; gap: 4px;">
    <modus-checkbox 
      id="small-checkbox-1" 
      label="Small checkbox"
      size="small">
    </modus-checkbox>
    
    <modus-checkbox 
      id="small-checkbox-2" 
      label="Small checked checkbox"
      size="small"
      checked>
    </modus-checkbox>
  </div>
</div>
```

```typescript
// Get references to various checkbox elements
const termsCheckbox = document.querySelector('#terms-checkbox');
const newsletterCheckbox = document.querySelector('#newsletter-checkbox');
const parentCheckbox = document.querySelector('#parent-checkbox');
const childCheckboxes = [
  document.querySelector('#child-checkbox-1'),
  document.querySelector('#child-checkbox-2'),
  document.querySelector('#child-checkbox-3')
];

// Handle individual checkbox changes
termsCheckbox?.addEventListener('checkboxClick', (event) => {
  const isChecked = event.detail;
  console.log(`Terms and conditions ${isChecked ? 'accepted' : 'declined'}`);
  
  // Enable/disable a submit button based on terms acceptance
  // submitButton.disabled = !isChecked;
});

newsletterCheckbox?.addEventListener('checkboxClick', (event) => {
  const isChecked = event.detail;
  console.log(`Newsletter subscription ${isChecked ? 'enabled' : 'disabled'}`);
  
  // Update user preferences
  // updateUserPreferences({ newsletter: isChecked });
});

// Set up parent-child checkbox relationship (common pattern for "Select All" functionality)
// First, set initial parent state based on children
const updateParentCheckboxState = () => {
  if (!parentCheckbox) return;
  
  const selectedCount = childCheckboxes.filter(checkbox => checkbox?.checked).length;
  
  if (selectedCount === 0) {
    // None selected
    parentCheckbox.checked = false;
    parentCheckbox.indeterminate = false;
  } else if (selectedCount === childCheckboxes.length) {
    // All selected
    parentCheckbox.checked = true;
    parentCheckbox.indeterminate = false;
  } else {
    // Some selected
    parentCheckbox.checked = false;
    parentCheckbox.indeterminate = true;
  }
};

// Initialize parent state
updateParentCheckboxState();

// Handle child checkbox clicks
childCheckboxes.forEach(checkbox => {
  checkbox?.addEventListener('checkboxClick', () => {
    updateParentCheckboxState();
  });
});

// Handle parent checkbox click
parentCheckbox?.addEventListener('checkboxClick', (event) => {
  const isChecked = event.detail;
  
  // Update all child checkboxes to match parent
  childCheckboxes.forEach(checkbox => {
    if (checkbox) checkbox.checked = isChecked;
  });
});
```

## Prompt 2
**User Question:** How can I create a form with validation using checkboxes?

**Agent Answer:**
References:
For this implementation, I'll demonstrate how to use checkboxes within a form context with validation. Key aspects include:
- Setting up required checkboxes for form validation
- Managing checkbox state and validating selections
- Providing feedback for validation errors
- Handling form submission with checkbox values

This pattern is common for terms agreement, feature selection, or any scenario requiring multiple option selection within forms.

```html
<div id="checkbox-form-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; max-width: 500px;">
  <h3>Registration Preferences</h3>
  
  <form id="preferences-form" style="display: flex; flex-direction: column; gap: 16px; border: 1px solid #e0e0e0; border-radius: 4px; padding: 16px;">
    <div>
      <h4 style="margin-top: 0;">Required Selections</h4>
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <modus-checkbox 
          id="terms-required" 
          label="I agree to the Terms of Service">
        </modus-checkbox>
        <div id="terms-error" style="color: #d32f2f; font-size: 12px; margin-left: 24px; display: none;">
          You must accept the Terms of Service
        </div>
        
        <modus-checkbox 
          id="privacy-required" 
          label="I agree to the Privacy Policy">
        </modus-checkbox>
        <div id="privacy-error" style="color: #d32f2f; font-size: 12px; margin-left: 24px; display: none;">
          You must accept the Privacy Policy
        </div>
      </div>
    </div>
    
    <div>
      <h4 style="margin-top: 0;">Communication Preferences</h4>
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <modus-checkbox 
          id="email-updates" 
          label="Receive email updates">
        </modus-checkbox>
        
        <modus-checkbox 
          id="product-news" 
          label="Product news and announcements">
        </modus-checkbox>
        
        <modus-checkbox 
          id="partner-offers" 
          label="Special offers from partners">
        </modus-checkbox>
      </div>
      <div id="comm-error" style="color: #d32f2f; font-size: 12px; margin-top: 8px; display: none;">
        Please select at least one communication preference
      </div>
    </div>
    
    <div>
      <h4 style="margin-top: 0;">Account Type</h4>
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <modus-checkbox 
          id="personal-account" 
          label="Personal">
        </modus-checkbox>
        
        <modus-checkbox 
          id="business-account" 
          label="Business">
        </modus-checkbox>
        
        <modus-checkbox 
          id="enterprise-account" 
          label="Enterprise"
          disabled>
        </modus-checkbox>
        <div style="color: #757575; font-size: 12px; margin-left: 24px;">
          Enterprise account requires approval
        </div>
      </div>
      <div id="account-error" style="color: #d32f2f; font-size: 12px; margin-top: 8px; display: none;">
        Please select an account type
      </div>
    </div>
    
    <button 
      id="submit-button" 
      type="submit"
      style="background-color: #0063a3; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; margin-top: 8px;">
      Submit Preferences
    </button>
    
    <div id="form-success" style="color: #388e3c; font-size: 14px; text-align: center; padding: 8px; display: none;">
      Preferences submitted successfully!
    </div>
  </form>
</div>
```

```typescript
// Get form elements
const preferencesForm = document.querySelector('#preferences-form');
const submitButton = document.querySelector('#submit-button');

// Required checkboxes
const termsCheckbox = document.querySelector('#terms-required');
const privacyCheckbox = document.querySelector('#privacy-required');
const termsError = document.querySelector('#terms-error');
const privacyError = document.querySelector('#privacy-error');

// Communication preferences
const emailUpdates = document.querySelector('#email-updates');
const productNews = document.querySelector('#product-news');
const partnerOffers = document.querySelector('#partner-offers');
const commError = document.querySelector('#comm-error');

// Account type
const personalAccount = document.querySelector('#personal-account');
const businessAccount = document.querySelector('#business-account');
const accountError = document.querySelector('#account-error');

// Success message
const formSuccess = document.querySelector('#form-success');

// Validate form on submission
preferencesForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  
  let isValid = true;
  
  // Validate required terms checkboxes
  if (!termsCheckbox?.checked) {
    termsError.style.display = 'block';
    isValid = false;
  } else {
    termsError.style.display = 'none';
  }
  
  if (!privacyCheckbox?.checked) {
    privacyError.style.display = 'block';
    isValid = false;
  } else {
    privacyError.style.display = 'none';
  }
  
  // Validate at least one communication preference is selected
  if (!emailUpdates?.checked && !productNews?.checked && !partnerOffers?.checked) {
    commError.style.display = 'block';
    isValid = false;
  } else {
    commError.style.display = 'none';
  }
  
  // Validate account type selection
  if (!personalAccount?.checked && !businessAccount?.checked) {
    accountError.style.display = 'block';
    isValid = false;
  } else {
    accountError.style.display = 'none';
  }
  
  // Submit form if valid
  if (isValid) {
    // Collect form data
    const formData = {
      terms: termsCheckbox?.checked,
      privacy: privacyCheckbox?.checked,
      communication: {
        email: emailUpdates?.checked,
        productNews: productNews?.checked,
        partnerOffers: partnerOffers?.checked
      },
      accountType: personalAccount?.checked ? 'personal' : 'business'
    };
    
    // Submit data to server (simulated)
    console.log('Form submitted with data:', formData);
    
    // Show success message
    formSuccess.style.display = 'block';
    submitButton.disabled = true;
    
    // Reset form after delay
    setTimeout(() => {
      formSuccess.style.display = 'none';
      submitButton.disabled = false;
    }, 3000);
  } else {
    console.log('Form validation failed');
  }
});

// Clear errors when checkboxes are clicked
[termsCheckbox, privacyCheckbox].forEach(checkbox => {
  checkbox?.addEventListener('checkboxClick', (event) => {
    if (event.detail === true) {
      // Hide error when checked
      if (checkbox === termsCheckbox) termsError.style.display = 'none';
      if (checkbox === privacyCheckbox) privacyError.style.display = 'none';
    }
  });
});

// Clear communication error when any preference is selected
[emailUpdates, productNews, partnerOffers].forEach(checkbox => {
  checkbox?.addEventListener('checkboxClick', () => {
    if (emailUpdates?.checked || productNews?.checked || partnerOffers?.checked) {
      commError.style.display = 'none';
    }
  });
});

// Clear account type error when an option is selected
[personalAccount, businessAccount].forEach(checkbox => {
  checkbox?.addEventListener('checkboxClick', () => {
    if (personalAccount?.checked || businessAccount?.checked) {
      accountError.style.display = 'none';
    }
  });
});
```



# <ModusChip>

## Prompt 1
**User Question:** How do I create different types of chips for filtering and selections?

**Agent Answer:**
References:
I've analyzed the ModusChip component and identified its key properties for creating various chip styles:
- `value`: Sets the text content displayed on the chip
- `chip-style`: Controls visual appearance (solid or outline)
- `size`: Adjusts the chip size (medium or small)
- `active`: Visually indicates selection state
- `show-close`: Adds a close/remove button to the chip
- `image-url`: Displays an image alongside the text
- `disabled` and `has-error`: Control special states

These properties allow for versatile chips that can be used for filtering, tag selection, or contact representation.

```html
<div id="chip-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h4>Basic Chips</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center;">
    <modus-chip 
      id="basic-chip" 
      value="Basic Chip">
    </modus-chip>
    
    <modus-chip 
      id="active-chip"
      value="Selected" 
      active>
    </modus-chip>
    
    <modus-chip 
      id="outline-chip"
      value="Outline Style" 
      chip-style="outline">
    </modus-chip>
    
    <modus-chip 
      id="small-chip"
      value="Small Size" 
      size="small">
    </modus-chip>
  </div>
  
  <h4>Interactive Chips</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center;">
    <modus-chip 
      id="close-chip"
      value="Removable" 
      show-close>
    </modus-chip>
    
    <modus-chip 
      id="image-chip"
      value="John Doe" 
      image-url="https://randomuser.me/api/portraits/thumb/men/1.jpg"
      show-close>
    </modus-chip>
    
    <modus-chip 
      id="disabled-chip"
      value="Disabled" 
      disabled>
    </modus-chip>
    
    <modus-chip 
      id="error-chip"
      value="Invalid Selection" 
      has-error
      show-close>
    </modus-chip>
  </div>
  
  <div id="chip-interaction-display" style="margin-top: 16px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px; min-height: 24px; font-size: 14px;">
    Click on a chip to see interactions
  </div>
</div>
```

```typescript
// Get reference to the interaction display area
const interactionDisplay = document.querySelector('#chip-interaction-display');

// Function to handle chip clicks
const handleChipClick = (chipId, chipValue) => {
  if (interactionDisplay) {
    interactionDisplay.textContent = `Clicked on ${chipValue} (${chipId})`;
  }
  console.log(`Chip clicked: ${chipId} - ${chipValue}`);
};

// Function to handle close button clicks
const handleCloseClick = (chipId, chipValue) => {
  if (interactionDisplay) {
    interactionDisplay.textContent = `Removed ${chipValue} (${chipId})`;
  }
  console.log(`Chip removed: ${chipId} - ${chipValue}`);
  
  // Hide the chip when close is clicked (common pattern)
  const chip = document.querySelector(`#${chipId}`);
  if (chip && chip.parentElement) {
    chip.style.display = 'none';
  }
};

// Add event listeners to all chips
const chips = document.querySelectorAll('modus-chip');
chips.forEach(chip => {
  const chipId = chip.id;
  const chipValue = chip.getAttribute('value');
  
  // Handle chip clicks
  chip.addEventListener('chipClick', () => {
    // Skip for disabled chips
    if (chip.disabled) return;
    
    // Toggle active state (common pattern for selectable chips)
    if (!chip.hasAttribute('active') && !chip.hasAttribute('has-error')) {
      chip.setAttribute('active', '');
    } else {
      chip.removeAttribute('active');
    }
    
    handleChipClick(chipId, chipValue);
  });
  
  // Handle close button clicks
  chip.addEventListener('closeClick', (event) => {
    event.stopPropagation(); // Prevent chip click
    handleCloseClick(chipId, chipValue);
  });
});
```

## Prompt 2
**User Question:** How can I implement a tag input system with chips?

**Agent Answer:**
References:
For this implementation, I'll demonstrate creating a tag input system where users can enter text to create new chips. This pattern is commonly used for:
- Adding multiple tags or categories to items
- Creating a list of recipients/contacts
- Implementing a filtering interface with multiple selections

The implementation combines text input with chip creation and management, allowing for dynamic addition and removal of chips.

```html
<div id="tag-input-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; max-width: 600px;">
  <h3>Tag Input with Chips</h3>
  
  <div style="border: 1px solid #ccc; border-radius: 4px; padding: 8px 12px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center;">
    <!-- Container for dynamically added chips -->
    <div id="chips-container" style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center;"></div>
    
    <!-- Input for new tags -->
    <input 
      id="tag-input" 
      type="text" 
      placeholder="Add tag..." 
      style="border: none; outline: none; padding: 4px 0; flex: 1; min-width: 120px;">
  </div>
  
  <div style="display: flex; gap: 8px;">
    <button id="clear-all-btn" style="padding: 6px 12px;">Clear All</button>
    <button id="add-sample-btn" style="padding: 6px 12px;">Add Sample Tags</button>
  </div>
  
  <div>
    <h4>Suggestions:</h4>
    <div id="suggestions-container" style="display: flex; flex-wrap: wrap; gap: 8px;">
      <modus-chip 
        id="suggestion-1" 
        value="JavaScript" 
        chip-style="outline" 
        size="small">
      </modus-chip>
      <modus-chip 
        id="suggestion-2" 
        value="TypeScript" 
        chip-style="outline" 
        size="small">
      </modus-chip>
      <modus-chip 
        id="suggestion-3" 
        value="Angular" 
        chip-style="outline" 
        size="small">
      </modus-chip>
      <modus-chip 
        id="suggestion-4" 
        value="React" 
        chip-style="outline" 
        size="small">
      </modus-chip>
      <modus-chip 
        id="suggestion-5" 
        value="Vue" 
        chip-style="outline" 
        size="small">
      </modus-chip>
    </div>
  </div>
  
  <div style="margin-top: 16px;">
    <h4>Selected Tags:</h4>
    <div id="selected-tags-display" style="border: 1px solid #e0e0e0; border-radius: 4px; padding: 12px; min-height: 24px;">
      No tags selected
    </div>
  </div>
</div>
```

```typescript
// Keep track of added tags
let tags = [];

// Get references to DOM elements
const tagsContainer = document.querySelector('#chips-container');
const tagInput = document.querySelector('#tag-input');
const clearAllBtn = document.querySelector('#clear-all-btn');
const addSampleBtn = document.querySelector('#add-sample-btn');
const suggestionsContainer = document.querySelector('#suggestions-container');
const selectedTagsDisplay = document.querySelector('#selected-tags-display');

// Function to update the selected tags display
const updateSelectedTagsDisplay = () => {
  if (selectedTagsDisplay) {
    if (tags.length > 0) {
      selectedTagsDisplay.textContent = tags.join(', ');
    } else {
      selectedTagsDisplay.textContent = 'No tags selected';
    }
  }
};

// Function to create a new chip element
const createChip = (value, withClose = true) => {
  // Create unique ID for the chip
  const chipId = `chip-${Date.now()}-${Math.floor(Math.random() * 1000)}`;
  
  // Create chip element
  const chip = document.createElement('modus-chip');
  chip.id = chipId;
  chip.setAttribute('value', value);
  
  if (withClose) {
    chip.setAttribute('show-close', '');
  }
  
  // Add event listeners
  chip.addEventListener('closeClick', () => {
    // Remove from tags array
    const index = tags.indexOf(value);
    if (index > -1) {
      tags.splice(index, 1);
    }
    
    // Remove chip from DOM
    chip.remove();
    
    // Update display
    updateSelectedTagsDisplay();
  });
  
  return chip;
};

// Function to add a new tag
const addTag = (value) => {
  if (!value || value.trim() === '') return;
  
  // Clean up the value
  value = value.trim();
  
  // Check for duplicates
  if (tags.includes(value)) {
    highlightExistingTag(value);
    return;
  }
  
  // Add to tags array
  tags.push(value);
  
  // Create and add chip to container
  const chip = createChip(value);
  tagsContainer?.appendChild(chip);
  
  // Update display
  updateSelectedTagsDisplay();
};

// Function to highlight existing tag (flash animation)
const highlightExistingTag = (value) => {
  const chips = tagsContainer?.querySelectorAll('modus-chip');
  
  chips?.forEach(chip => {
    if (chip.getAttribute('value') === value) {
      // Add and remove a class to create flash effect
      chip.style.transform = 'scale(1.1)';
      chip.style.transition = 'transform 0.2s';
      
      setTimeout(() => {
        chip.style.transform = 'scale(1)';
      }, 200);
    }
  });
};

// Handle input events
tagInput?.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' || event.key === ',') {
    event.preventDefault();
    
    const value = tagInput.value.replace(',', '');
    addTag(value);
    
    // Clear input
    tagInput.value = '';
  }
});

// Handle input blur event (add tag when focus is lost)
tagInput?.addEventListener('blur', () => {
  if (tagInput.value.trim()) {
    addTag(tagInput.value);
    tagInput.value = '';
  }
});

// Handle clear all button
clearAllBtn?.addEventListener('click', () => {
  // Clear tags array
  tags = [];
  
  // Remove all chips
  if (tagsContainer) {
    tagsContainer.innerHTML = '';
  }
  
  // Update display
  updateSelectedTagsDisplay();
});

// Handle add sample tags button
addSampleBtn?.addEventListener('click', () => {
  const sampleTags = ['HTML', 'CSS', 'JavaScript', 'Web Development'];
  
  sampleTags.forEach(tag => {
    addTag(tag);
  });
});

// Handle suggestion chips
const suggestionChips = suggestionsContainer?.querySelectorAll('modus-chip');
suggestionChips?.forEach(chip => {
  chip.addEventListener('chipClick', () => {
    const value = chip.getAttribute('value');
    addTag(value);
  });
});

// Initialize with empty state
updateSelectedTagsDisplay();
```

# <ModusDataTable>

## Prompt 1
**User Question:** How do I create a basic data table with columns and data?

**Agent Answer:**
References:
I've analyzed the ModusDataTable component and identified the key properties required for implementation:
- `columns`: Defines the table structure (can be simple string[] or TColumn[] for more control)
- `data`: The actual table data (array of arrays or object array)
- `displayOptions`: Controls visual appearance like borders and sizing
- Event handling for user interactions with the table

This implementation shows how to create a basic data table with both the simple approach and a more customized approach.

```html
<div id="data-table-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 100%;">
  <h3>Basic Data Table</h3>
  
  <!-- Simple data table with string columns -->
  <modus-data-table id="simple-data-table"></modus-data-table>
  
  <!-- Advanced data table with column customization -->
  <h3>Advanced Data Table</h3>
  <modus-data-table id="advanced-data-table"></modus-data-table>
</div>
```

```typescript
// Get references to the data table elements
const simpleDataTable = document.getElementById('simple-data-table');
const advancedDataTable = document.getElementById('advanced-data-table');

// Simple data table setup
if (simpleDataTable) {
  // Define columns as string array
  simpleDataTable.columns = ['Name', 'Age', 'Email', 'Status'];
  
  // Define data as array of arrays (rows and cells)
  simpleDataTable.data = [
    ['John Smith', 32, 'john.smith@example.com', true],
    ['Jane Doe', 28, 'jane.doe@example.com', true],
    ['Bob Johnson', 45, 'bob.johnson@example.com', false],
    ['Alice Williams', 36, 'alice.williams@example.com', true]
  ];
}

// Advanced data table setup
if (advancedDataTable) {
  // Define columns with more control over appearance
  advancedDataTable.columns = [
    { display: 'Employee Name', id: 'name', width: '25%' },
    { display: 'Department', id: 'department' },
    { display: 'Salary', id: 'salary', align: 'right' },
    { display: 'Active', id: 'active' }
  ];
  
  // Define data as array of objects
  advancedDataTable.data = [
    { 
      name: 'John Smith', 
      department: 'Engineering', 
      salary: '$95,000',
      active: true 
    },
    { 
      name: 'Jane Doe', 
      department: 'Marketing', 
      salary: '$82,000', 
      active: true 
    },
    { 
      name: 'Bob Johnson', 
      department: 'Finance', 
      salary: '$110,000', 
      active: false 
    },
    { 
      name: 'Alice Williams', 
      department: 'Engineering', 
      salary: '$98,000', 
      active: true 
    }
  ];
  
  // Customize display options
  advancedDataTable.displayOptions = {
    borderless: false,
    cellBorderless: false,
    rowStripe: true,
    size: 'small'
  };
}
```

## Prompt 2
**User Question:** How do I implement row actions, sorting, and row selection in a data table?

**Agent Answer:**
References:
For this implementation, I'll demonstrate advanced ModusDataTable features:
- Row actions: Adding clickable actions to each row
- Sorting: Enabling and configuring column sorting
- Row selection: Implementing both single and checkbox selection modes
- Event handlers: Responding to user interactions with the table

These features are essential for interactive data tables that allow users to manipulate and extract information from tabular data.

```html
<div id="interactive-table-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 100%;">
  <h3>Interactive Data Table</h3>
  
  <!-- Data table with interactive features -->
  <modus-data-table id="interactive-data-table"></modus-data-table>
  
  <!-- Status display area -->
  <div id="table-status" style="margin-top: 16px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px;">
    Interact with the table to see events
  </div>
</div>
```

```typescript
// Get references to the elements
const dataTable = document.getElementById('interactive-data-table');
const statusDisplay = document.getElementById('table-status');

// Configure the interactive data table
if (dataTable) {
  // Define columns
  dataTable.columns = [
    { display: 'ID', id: 'id', width: '10%' },
    { display: 'Customer Name', id: 'name', width: '25%' },
    { display: 'Order Date', id: 'date' },
    { display: 'Order Total', id: 'total', align: 'right' },
    { display: 'Status', id: 'status' }
  ];
  
  // Define data with different cell types
  dataTable.data = [
    { 
      _id: 'order-1',  // Unique ID for row selection
      id: '1001', 
      name: 'John Smith', 
      date: '2023-01-15', 
      total: '$245.99',
      status: { _type: 'badge', color: 'success', text: 'Completed', type: 'text' }
    },
    { 
      _id: 'order-2', 
      id: '1002', 
      name: 'Jane Doe', 
      date: '2023-01-28', 
      total: '$124.50',
      status: { _type: 'badge', color: 'warning', text: 'Processing', type: 'text' }
    },
    { 
      _id: 'order-3', 
      id: '1003', 
      name: 'Bob Johnson', 
      date: '2023-02-03', 
      total: '$532.75',
      status: { _type: 'badge', color: 'success', text: 'Completed', type: 'text' }
    },
    { 
      _id: 'order-4', 
      id: '1004', 
      name: 'Alice Williams', 
      date: '2023-02-10', 
      total: '$87.25',
      status: { _type: 'badge', color: 'danger', text: 'Cancelled', type: 'text' }
    },
    { 
      _id: 'order-5', 
      id: '1005', 
      name: { 
        _type: 'link', 
        display: 'Michael Brown', 
        url: '#customer-michael' 
      }, 
      date: '2023-02-15', 
      total: '$198.65',
      status: { _type: 'badge', color: 'warning', text: 'Processing', type: 'text' }
    }
  ];
  
  // Enable row selection with checkbox
  dataTable.selectionOptions = {
    canSelect: true,
    checkboxSelection: true
  };
  
  // Enable sorting
  dataTable.sortOptions = {
    canSort: true,
    serverSide: false
  };
  
  // Add row actions
  dataTable.rowActions = [
    { 
      _id: 'view', 
      display: { 
        icon: 'visibility', 
        text: 'View Order' 
      } 
    },
    { 
      _id: 'edit', 
      display: { 
        icon: 'edit', 
        text: 'Edit Order' 
      } 
    },
    { 
      _id: 'delete', 
      display: { 
        icon: 'delete', 
        text: 'Delete Order' 
      } 
    }
  ];
  
  // Set display options
  dataTable.displayOptions = {
    borderless: false,
    cellBorderless: false,
    rowStripe: true,
    animateRowActionsDropdown: true,
    size: 'small'
  };
  
  // Event Handlers
  
  // Handle row action clicks
  dataTable.addEventListener('rowActionClick', (event) => {
    const { actionId, rowId } = event.detail;
    updateStatus(`Action: ${actionId} clicked for row: ${rowId}`);
    
    // Handle specific actions
    if (actionId === 'delete') {
      if (confirm(`Are you sure you want to delete order ${rowId}?`)) {
        // In a real application, you would delete the data from your database
        // For demo purposes, we'll just log it
        updateStatus(`Order ${rowId} would be deleted`);
      }
    } else if (actionId === 'view') {
      updateStatus(`Viewing details for order ${rowId}`);
      // In a real app, you might navigate to a detail page or show a modal
    } else if (actionId === 'edit') {
      updateStatus(`Editing order ${rowId}`);
      // In a real app, you might navigate to an edit form or show a modal
    }
  });
  
  // Handle selection changes
  dataTable.addEventListener('selection', (event) => {
    const selectedIds = event.detail;
    updateStatus(`Selected rows: ${selectedIds.join(', ')}`);
  });
  
  // Handle sorting
  dataTable.addEventListener('sort', (event) => {
    const { columnId, direction } = event.detail;
    updateStatus(`Sorted by ${columnId} in ${direction} order`);
  });
  
  // Handle link clicks
  dataTable.addEventListener('cellLinkClick', (event) => {
    const link = event.detail;
    updateStatus(`Link clicked: ${link.display} (${link.url})`);
    // In a real app, you might navigate to the URL or handle the click differently
  });
  
  // Handle row double-clicks
  dataTable.addEventListener('rowDoubleClick', (event) => {
    const rowId = event.detail;
    updateStatus(`Row double-clicked: ${rowId}`);
    // In a real app, you might show detailed information
  });
  
  // Helper function to update status display
  function updateStatus(message) {
    if (statusDisplay) {
      // Add timestamp
      const timestamp = new Date().toLocaleTimeString();
      statusDisplay.innerHTML = `<strong>${timestamp}</strong>: ${message}`;
    }
    console.log(message);
  }
}
```

## Prompt 3
**User Question:** How can I create a data table with dynamic data loading and customized cell formatting?

**Agent Answer:**
References:
In this implementation, I'll show more advanced usage patterns of the ModusDataTable:
- Dynamic data loading with a simulated API call
- Customized cell formatting for different data types
- Using badges and links within cells
- State management for user interactions

This approach is particularly useful for enterprise applications where data tables need to display complex information in a user-friendly format.

```html
<div id="advanced-table-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 100%;">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <h3>Product Inventory</h3>
    <div>
      <modus-button id="refresh-btn" color="primary" size="small">Refresh Data</modus-button>
      <modus-button id="download-btn" color="secondary" size="small" left-icon="download">Export</modus-button>
    </div>
  </div>
  
  <!-- Loading indicator -->
  <div id="loading-indicator" style="display: none; text-align: center; padding: 20px;">
    Loading data...
  </div>
  
  <!-- Data table with advanced formatting -->
  <modus-data-table id="product-table"></modus-data-table>
  
  <!-- Selected items summary -->
  <div id="selected-items-summary" style="margin-top: 16px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px; display: none;">
    <h4 style="margin-top: 0;">Selected Items</h4>
    <div id="selected-items-content"></div>
  </div>
</div>
```

```typescript
// Get references to all elements
const productTable = document.getElementById('product-table');
const refreshBtn = document.getElementById('refresh-btn');
const downloadBtn = document.getElementById('download-btn');
const loadingIndicator = document.getElementById('loading-indicator');
const selectedItemsSummary = document.getElementById('selected-items-summary');
const selectedItemsContent = document.getElementById('selected-items-content');

// Define the table structure
if (productTable) {
  // Set up columns
  productTable.columns = [
    { display: 'Product ID', id: 'id', width: '10%' },
    { display: 'Product Name', id: 'name', width: '25%' },
    { display: 'Category', id: 'category' },
    { display: 'Stock', id: 'stock', align: 'right' },
    { display: 'Price', id: 'price', align: 'right' },
    { display: 'Status', id: 'status' }
  ];
  
  // Enable features
  productTable.selectionOptions = {
    canSelect: true,
    checkboxSelection: true
  };
  
  productTable.sortOptions = {
    canSort: true,
    serverSide: false
  };
  
  productTable.rowActions = [
    { _id: 'view', display: { icon: 'visibility', text: 'View' } },
    { _id: 'edit', display: { icon: 'edit', text: 'Edit' } },
    { _id: 'archive', display: { icon: 'archive', text: 'Archive' } }
  ];
  
  // Styling
  productTable.displayOptions = {
    borderless: false,
    cellBorderless: true,
    rowStripe: true,
    size: 'small'
  };
  
  // Event handlers
  productTable.addEventListener('selection', handleSelection);
  productTable.addEventListener('rowActionClick', handleRowAction);
  productTable.addEventListener('sort', handleSort);
  
  // Initial data load
  loadTableData();
}

// Add event listeners to buttons
if (refreshBtn) {
  refreshBtn.addEventListener('buttonClick', () => {
    loadTableData();
  });
}

if (downloadBtn) {
  downloadBtn.addEventListener('buttonClick', () => {
    exportTableData();
  });
}

// Function to load data into the table
function loadTableData() {
  // Show loading indicator
  if (loadingIndicator) loadingIndicator.style.display = 'block';
  
  // Hide selected items summary during reload
  if (selectedItemsSummary) selectedItemsSummary.style.display = 'none';
  
  // Simulate API call with setTimeout
  setTimeout(() => {
    // Generate mock data (in a real app, this would come from an API)
    const mockData = generateMockProductData(25);
    
    // Populate the table with the data
    if (productTable) {
      productTable.data = mockData;
    }
    
    // Hide loading indicator
    if (loadingIndicator) loadingIndicator.style.display = 'none';
  }, 1000); // Simulate 1 second API delay
}

// Function to handle selection changes
function handleSelection(event) {
  const selectedIds = event.detail;
  
  if (selectedIds.length > 0) {
    // Find the selected items from the data
    const selectedItems = [];
    const tableData = productTable.data;
    
    // Loop through the data to find selected items
    selectedIds.forEach(id => {
      const item = tableData.find(row => row._id === id);
      if (item) {
        selectedItems.push(item);
      }
    });
    
    // Build a summary of the selected items
    if (selectedItemsContent) {
      let summary = '';
      
      if (selectedItems.length === 1) {
        // Single item selected - show details
        const item = selectedItems[0];
        summary = `
          <div>
            <p><strong>Product:</strong> ${item.name}</p>
            <p><strong>Category:</strong> ${item.category}</p>
            <p><strong>Stock:</strong> ${item.stock} units</p>
            <p><strong>Price:</strong> ${item.price}</p>
          </div>
        `;
      } else {
        // Multiple items selected - show summary
        const totalItems = selectedItems.length;
        const totalStock = selectedItems.reduce((sum, item) => sum + parseInt(item.stock), 0);
        
        // Calculate average price
        const totalPrice = selectedItems.reduce((sum, item) => {
          // Extract numeric value from price string (remove $ and commas)
          const priceValue = parseFloat(item.price.replace(/[$,]/g, ''));
          return sum + priceValue;
        }, 0);
        const avgPrice = (totalPrice / totalItems).toFixed(2);
        
        summary = `
          <div>
            <p><strong>Selected:</strong> ${totalItems} items</p>
            <p><strong>Total Stock:</strong> ${totalStock} units</p>
            <p><strong>Average Price:</strong> $${avgPrice}</p>
            <modus-button id="bulk-edit-btn" size="small" color="primary">Bulk Edit</modus-button>
          </div>
        `;
        
        // Add event listener to bulk edit button after it's created
        setTimeout(() => {
          const bulkEditBtn = document.getElementById('bulk-edit-btn');
          if (bulkEditBtn) {
            bulkEditBtn.addEventListener('buttonClick', () => {
              alert(`Bulk editing ${totalItems} items`);
            });
          }
        }, 0);
      }
      
      selectedItemsContent.innerHTML = summary;
    }
    
    // Show the summary panel
    if (selectedItemsSummary) {
      selectedItemsSummary.style.display = 'block';
    }
  } else {
    // Hide the summary panel when no items are selected
    if (selectedItemsSummary) {
      selectedItemsSummary.style.display = 'none';
    }
  }
}

// Function to handle row actions
function handleRowAction(event) {
  const { actionId, rowId } = event.detail;
  console.log(`Action ${actionId} for row ${rowId}`);
  
  // In a real app, you would handle each action type
  switch (actionId) {
    case 'view':
      // Navigate to product details view
      console.log(`Viewing product ${rowId}`);
      break;
      
    case 'edit':
      // Open edit form/modal
      console.log(`Editing product ${rowId}`);
      break;
      
    case 'archive':
      // Archive the product (with confirmation)
      if (confirm('Are you sure you want to archive this product?')) {
        console.log(`Archiving product ${rowId}`);
        // In a real app, you would call an API and refresh the data
      }
      break;
  }
}

// Function to handle sorting
function handleSort(event) {
  const { columnId, direction } = event.detail;
  console.log(`Sorting by ${columnId} in ${direction} direction`);
  
  // In a real app with server-side sorting, you would:
  // 1. Update your API query parameters
  // 2. Call your API again with the new sort parameters
  // 3. Update the table with the newly sorted data
}

// Function to export table data (simple demo)
function exportTableData() {
  const tableData = productTable?.data;
  
  if (!tableData) {
    alert('No data to export');
    return;
  }
  
  // In a real app, you would format the data appropriately for export
  // Here we'll just show a message
  alert(`Exporting ${tableData.length} records to CSV`);
  console.log('Data to export:', tableData);
}

// Helper function to generate mock product data
function generateMockProductData(count = 10) {
  const categories = ['Electronics', 'Furniture', 'Clothing', 'Office Supplies', 'Kitchen'];
  const statuses = [
    { text: 'In Stock', color: 'success' },
    { text: 'Low Stock', color: 'warning' },
    { text: 'Out of Stock', color: 'danger' }
  ];
  const products = [
    'Laptop', 'Monitor', 'Keyboard', 'Chair', 'Desk', 'Bookshelf',
    'T-Shirt', 'Jeans', 'Shoes', 'Stapler', 'Notepad', 'Pen Set',
    'Coffee Maker', 'Blender', 'Toaster', 'Headphones', 'Smartphone'
  ];
  
  return Array.from({ length: count }, (_, i) => {
    // Generate a random stock quantity
    const stockQty = Math.floor(Math.random() * 200);
    
    // Determine status based on stock
    let status;
    if (stockQty === 0) {
      status = statuses[2]; // Out of Stock
    } else if (stockQty < 10) {
      status = statuses[1]; // Low Stock
    } else {
      status = statuses[0]; // In Stock
    }
    
    // Generate a random price between $10 and $2000
    const price = (Math.random() * 1990 + 10).toFixed(2);
    const formattedPrice = `$${parseFloat(price).toLocaleString('en-US', { minimumFractionDigits: 2 })}`;
    
    // Randomize if this will be a link type for the product name
    const useLink = Math.random() > 0.7;
    
    const productName = `${products[Math.floor(Math.random() * products.length)]} ${String.fromCharCode(65 + Math.floor(Math.random() * 26))}-${Math.floor(Math.random() * 1000)}`;
    
    // Create the data row
    return {
      _id: `product-${i + 1}`,
      id: `PRD-${100 + i}`,
      name: useLink ? { 
        _type: 'link',
        display: productName,
        url: `#product/${i + 1}`
      } : productName,
      category: categories[Math.floor(Math.random() * categories.length)],
      stock: stockQty.toString(),
      price: formattedPrice,
      status: {
        _type: 'badge',
        text: status.text,
        color: status.color,
        type: 'text'
      }
    };
  });
}
```


# <ModusDateInput>

## Prompt 1
**User Question:** How do I create a basic date input field with a specific format and validation?

**Agent Answer:**
References:
The ModusDateInput component is a versatile date input field that supports various formats and validations. For this implementation, I'll focus on key properties:
- `format`: Defines the display format for the date (e.g., "mmm dd, yyyy")
- `allowed-chars-regex`: Restricts the characters that can be typed into the input
- `helper-text`: Provides guidance about the expected format
- `value`: Sets the initial date value (in ISO format "yyyy-mm-dd")
- `min` and `max`: Optionally restrict the date range
- `valueChange` event: Captures when the user changes the date

```html
<div id="date-input-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-date-input
    id="date-input"
    label="Event Date"
    format="mmm dd, yyyy" 
    allowed-chars-regex="[\d\/]"
    helper-text="mmm dd, yyyy"
    placeholder="Jan 01, 2023"
    value="2023-01-01"
    min="2023-01-01"
    max="2023-12-31">
  </modus-date-input>
</div>
```

```typescript
const dateInput = document.querySelector('#date-input');
if (dateInput) {
  dateInput.addEventListener('valueChange', (event: any) => {
    const selectedDate = event.detail.value;
    console.log('Selected date:', selectedDate);
    
    // You can access various date details from the event
    console.log('Date details:', event.detail);
  });
}
```

## Prompt 2
**User Question:** How can I implement a date range picker with start and end dates?

**Agent Answer:**
References:
To implement a date range selection, we need to use the ModusDatePicker component along with two ModusDateInput components. The ModusDatePicker acts as a container, while the ModusDateInput components need to have their `type` property set to "start" and "end" respectively.

Key considerations:
- Use `modus-date-picker` as the container
- Add two `modus-date-input` components with `type="start"` and `type="end"`
- Set consistent `format` for both inputs
- Use `show-calendar-icon="true"` to display calendar icons
- Add event listeners to track both dates for processing the range

```html
<div id="date-range-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-date-picker id="date-picker" label="Select date range">
    <modus-date-input
      id="start-date"
      type="start"
      label="Start Date"
      format="dd-mm-yyyy"
      helper-text="dd-mm-yyyy"
      allowed-chars-regex="[\d-]"
      show-calendar-icon="true"
      value="2023-01-01">
    </modus-date-input>

    <modus-date-input
      id="end-date"
      type="end"
      label="End Date"
      format="dd-mm-yyyy"
      helper-text="dd-mm-yyyy"
      allowed-chars-regex="[\d-]"
      show-calendar-icon="true"
      value="2023-01-15">
    </modus-date-input>
  </modus-date-picker>
</div>
```

```typescript
const startDateInput = document.querySelector('#start-date');
const endDateInput = document.querySelector('#end-date');
let dateRange = { start: '2023-01-01', end: '2023-01-15' };

if (startDateInput && endDateInput) {
  startDateInput.addEventListener('valueChange', (event: any) => {
    dateRange.start = event.detail.value;
    console.log('Date range updated:', dateRange);
    
    // You can implement validation here
    validateDateRange();
  });
  
  endDateInput.addEventListener('valueChange', (event: any) => {
    dateRange.end = event.detail.value;
    console.log('Date range updated:', dateRange);
    
    // You can implement validation here
    validateDateRange();
  });
  
  // Example validation function
  function validateDateRange() {
    if (new Date(dateRange.start) > new Date(dateRange.end)) {
      console.error('Start date cannot be after end date');
      // You can set error state here
    }
  }
}
```

## Prompt 3
**User Question:** How can I handle custom date format validation and respond to calendar icon clicks?

**Agent Answer:**
References:
For custom date format validation and handling calendar icon interactions, we need to:
1. Set up a custom format with `format` property
2. Use `disableValidation` to handle custom validation logic
3. Implement a listener for the `calendarIconClicked` event
4. Add validation with the available `validate()` method

This example demonstrates how to create a date input with a custom format, implement custom validation, and respond to calendar icon clicks - three common requirements when working with date inputs.

```html
<div id="custom-date-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-date-input
    id="custom-date-input"
    label="Custom Formatted Date"
    format="yyyy-mm"
    helper-text="yyyy-mm (Year-Month)"
    allowed-chars-regex="[\d-]"
    show-calendar-icon="true"
    value="2023-06-01">
  </modus-date-input>
  
  <div id="validation-message" style="color: #666; font-size: 14px;"></div>
</div>
```

```typescript
const dateInput: any = document.querySelector('#custom-date-input');
const validationMessage = document.querySelector('#validation-message');

if (dateInput && validationMessage) {
  // Handle value changes
  dateInput.addEventListener('valueChange', async (event: any) => {
    const dateValue = event.detail.value;
    console.log('Date changed:', dateValue);
    
    // Custom validation logic
    const isValid = await validateCustomDate(dateValue);
    if (!isValid) {
      validationMessage.textContent = 'Please enter a date within the current year';
      validationMessage.style.color = '#d9363e';
    } else {
      validationMessage.textContent = 'Valid date selected';
      validationMessage.style.color = '#008744';
    }
  });
  
  // Handle calendar icon clicks
  dateInput.addEventListener('calendarIconClicked', (event: any) => {
    console.log('Calendar icon clicked!', event.detail);
    
    // Here you could open a custom calendar or perform other actions
    validationMessage.textContent = 'Calendar icon clicked - you could open a custom calendar here';
    validationMessage.style.color = '#0063a3';
  });
  
  // Example custom validation function
  async function validateCustomDate(dateValue: string): Promise<boolean> {
    if (!dateValue) return false;
    
    const currentYear = new Date().getFullYear();
    const selectedYear = parseInt(dateValue.split('-')[0], 10);
    
    // Only allow dates from current year
    return selectedYear === currentYear;
  }
}
```


# <ModusDropdown>

## Prompt 1
**User Question:** How do I create a basic dropdown menu with a button trigger?

**Agent Answer:**
References:
The ModusDropdown component requires a toggle element and a dropdown list. The key properties are:
- `toggle-element-id`: References the ID of the element that triggers the dropdown
- `slot="dropdownToggle"`: Applied to the trigger element (typically a button)
- `slot="dropdownList"`: Applied to the content that should appear in the dropdown
- The dropdown content can be any element, but `modus-list` with `modus-list-item` components work well for navigation menus

For this implementation, I'll create a standard dropdown with a button trigger and a list of options. The dropdown will appear below the button by default.

```html
<div id="dropdown-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-dropdown id="basic-dropdown" toggle-element-id="dropdown-trigger">
    <modus-button id="dropdown-trigger" slot="dropdownToggle" show-caret="true">
      Select an Option
    </modus-button>
    
    <modus-list slot="dropdownList">
      <modus-list-item id="option-1" size="condensed" borderless>Option 1</modus-list-item>
      <modus-list-item id="option-2" size="condensed" borderless>Option 2</modus-list-item>
      <modus-list-item id="option-3" size="condensed" borderless>Option 3</modus-list-item>
    </modus-list>
  </modus-dropdown>
</div>
```

```typescript
const dropdown = document.querySelector('#basic-dropdown');
const options = document.querySelectorAll('modus-list-item');
const triggerBtn = document.querySelector('#dropdown-trigger');

// Handle dropdown close event
if (dropdown) {
  dropdown.addEventListener('dropdownClose', () => {
    console.log('Dropdown closed');
  });
}

// Handle option selection
if (options) {
  options.forEach(option => {
    option.addEventListener('click', (event) => {
      const selectedOption = event.target as HTMLElement;
      console.log('Selected:', selectedOption.textContent);
      
      if (triggerBtn) {
        // Update button text with selection (optional)
        triggerBtn.textContent = selectedOption.textContent;
      }
    });
  });
}
```

## Prompt 2
**User Question:** How can I create a dropdown with custom placement and prevent it from closing when an option is selected?

**Agent Answer:**
References:
For more advanced dropdown usage, we can leverage several properties:
- `placement`: Controls where the dropdown opens relative to the toggle element
- `disable-close-on-select`: Keeps the dropdown open after a selection
- `animate-list`: Adds an animation effect when the dropdown opens
- `custom-placement`: Allows fine-tuning the dropdown position
- `border-radius`: Controls the rounded corners of the dropdown

This implementation demonstrates a dropdown that opens to the right of the toggle button, has rounded corners, and stays open when items are selected. This pattern is useful for multi-select scenarios or when users need to make multiple consecutive selections.

```html
<div id="custom-dropdown-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-dropdown 
    id="custom-dropdown"
    toggle-element-id="custom-dropdown-trigger"
    placement="right"
    disable-close-on-select="true"
    animate-list="true"
    border-radius="8px"
    show-dropdown-list-border="true">
    
    <modus-button 
      id="custom-dropdown-trigger" 
      slot="dropdownToggle"
      button-style="borderless"
      color="primary">
      Filter Options
    </modus-button>
    
    <div slot="dropdownList" style="padding: 8px;">
      <div style="font-weight: bold; margin-bottom: 8px;">Select multiple options:</div>
      <modus-list>
        <modus-list-item id="filter-1" size="condensed">
          <label style="display: flex; align-items: center; width: 100%;">
            <modus-checkbox id="cb-1"></modus-checkbox>
            <span style="margin-left: 8px;">Category 1</span>
          </label>
        </modus-list-item>
        
        <modus-list-item id="filter-2" size="condensed">
          <label style="display: flex; align-items: center; width: 100%;">
            <modus-checkbox id="cb-2"></modus-checkbox>
            <span style="margin-left: 8px;">Category 2</span>
          </label>
        </modus-list-item>
        
        <modus-list-item id="filter-3" size="condensed">
          <label style="display: flex; align-items: center; width: 100%;">
            <modus-checkbox id="cb-3"></modus-checkbox>
            <span style="margin-left: 8px;">Category 3</span>
          </label>
        </modus-list-item>
      </modus-list>
      
      <div style="display: flex; justify-content: flex-end; margin-top: 8px;">
        <modus-button id="apply-filters" color="primary" size="small">Apply</modus-button>
      </div>
    </div>
  </modus-dropdown>
</div>
```

```typescript
const customDropdown = document.querySelector('#custom-dropdown');
const checkboxes = document.querySelectorAll('modus-checkbox');
const applyButton = document.querySelector('#apply-filters');

// Track selected filters
const selectedFilters: string[] = [];

// Handle checkbox changes
checkboxes.forEach((checkbox: any, index) => {
  checkbox.addEventListener('valueChange', (event: any) => {
    const categoryId = `Category ${index + 1}`;
    
    if (event.detail) {
      // Add to selected filters if checked
      if (!selectedFilters.includes(categoryId)) {
        selectedFilters.push(categoryId);
      }
    } else {
      // Remove from selected filters if unchecked
      const filterIndex = selectedFilters.indexOf(categoryId);
      if (filterIndex !== -1) {
        selectedFilters.splice(filterIndex, 1);
      }
    }
    
    console.log('Selected filters:', selectedFilters);
  });
});

// Apply button closes the dropdown manually
if (applyButton) {
  applyButton.addEventListener('click', () => {
    console.log('Applying filters:', selectedFilters);
    
    // To close the dropdown programmatically, you can toggle the trigger button
    const triggerBtn = document.querySelector('#custom-dropdown-trigger') as any;
    if (triggerBtn && triggerBtn.click) {
      triggerBtn.click();
    }
  });
}

// Handle dropdown close
if (customDropdown) {
  customDropdown.addEventListener('dropdownClose', () => {
    console.log('Dropdown closed');
  });
}
```

# <ModusFileDropzone>

## Prompt 1
**User Question:** How do I implement a basic file upload dropzone that accepts specific file types?

**Agent Answer:**
References:
The ModusFileDropzone component provides a user-friendly interface for uploading files through drag and drop or file browser. Key properties to consider:
- `accept-file-types`: Restricts the types of files that can be uploaded (e.g., "image/*" or ".pdf,.docx")
- `multiple`: Controls whether multiple files can be uploaded at once
- `dropzone-width` and `dropzone-height`: Define the size of the dropzone
- `label` and `description`: Provide context to users
- `files` event: Captures when files are added or removed, returning both the files and any validation errors

This implementation creates a simple file dropzone for accepting only image files with size constraints:

```html
<div id="file-upload-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-file-dropzone
    id="image-dropzone"
    accept-file-types="image/*"
    label="Image Upload"
    description="Upload product images in JPG, PNG or GIF format"
    dropzone-height="200px"
    dropzone-width="400px"
    max-file-count="5"
    max-total-file-size-bytes="5242880">
  </modus-file-dropzone>
  
  <div id="upload-status" style="margin-top: 10px; font-size: 14px;"></div>
</div>
```

```typescript
const imageDropzone = document.querySelector('#image-dropzone');
const uploadStatus = document.querySelector('#upload-status');
let currentFiles: File[] = [];

if (imageDropzone && uploadStatus) {
  imageDropzone.addEventListener('files', (event: any) => {
    const [files, error] = event.detail;
    currentFiles = files;
    
    if (error) {
      uploadStatus.textContent = `Error: ${error}`;
      uploadStatus.setAttribute('style', 'color: #d9363e; margin-top: 10px; font-size: 14px;');
    } else {
      // Display file information
      if (files.length > 0) {
        uploadStatus.innerHTML = `
          <div style="color: #008744;">
            ${files.length} file(s) ready to upload:
            <ul style="margin-top: 5px;">
              ${Array.from(files).map(file => 
                `<li>${file.name} (${(file.size / 1024).toFixed(1)} KB)</li>`
              ).join('')}
            </ul>
          </div>
        `;
      } else {
        uploadStatus.textContent = 'No files selected';
        uploadStatus.setAttribute('style', 'color: #666; margin-top: 10px; font-size: 14px;');
      }
    }
  });
  
  // Example of how to handle an upload button
  const uploadButton = document.createElement('modus-button');
  uploadButton.color = 'primary';
  uploadButton.textContent = 'Upload Files';
  uploadButton.style.marginTop = '10px';
  
  uploadButton.addEventListener('click', async () => {
    if (currentFiles.length === 0) {
      uploadStatus.textContent = 'Please select files first';
      uploadStatus.setAttribute('style', 'color: #d9363e; margin-top: 10px; font-size: 14px;');
      return;
    }
    
    uploadStatus.textContent = 'Uploading files...';
    
    // Simulate file upload
    setTimeout(() => {
      uploadStatus.textContent = `Successfully uploaded ${currentFiles.length} file(s)`;
      uploadStatus.setAttribute('style', 'color: #008744; margin-top: 10px; font-size: 14px;');
    }, 1500);
  });
  
  document.querySelector('#file-upload-container').appendChild(uploadButton);
}
```

## Prompt 2
**User Question:** How can I programmatically add and remove files from the dropzone and handle file validation?

**Agent Answer:**
References:
For more advanced usage of the ModusFileDropzone, we can leverage its methods to programmatically manage files and implement custom validation. The key methods are:
- `addFile()`: Programmatically add a file to the dropzone
- `removeFile()`: Remove a file by name
- `getFiles()`: Retrieve the current files in the dropzone
- `getError()`: Check if there are any validation errors

This implementation demonstrates how to:
1. Programmatically add files to the dropzone
2. Create custom validation for file types and sizes
3. Display a list of added files with remove buttons
4. Handle various error states

```html
<div id="advanced-dropzone-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-file-dropzone
    id="document-dropzone"
    accept-file-types=".pdf,.docx,.xlsx"
    label="Document Upload"
    description="Upload documents (PDF, Word, Excel)"
    dropzone-height="180px"
    dropzone-width="100%"
    max-file-count="10"
    max-total-file-size-bytes="10485760">
  </modus-file-dropzone>
  
  <div id="file-list-container" style="margin-top: 10px;">
    <h4 style="margin: 0 0 8px 0; font-size: 16px;">Selected Files</h4>
    <div id="file-list" style="border: 1px solid #eee; padding: 8px; min-height: 50px; border-radius: 4px;"></div>
  </div>
  
  <div style="display: flex; gap: 8px; margin-top: 8px;">
    <modus-button id="add-sample-file" color="secondary" size="small">Add Sample File</modus-button>
    <modus-button id="clear-files" button-style="borderless" size="small">Clear All</modus-button>
  </div>
</div>
```

```typescript
const documentDropzone: any = document.querySelector('#document-dropzone');
const fileListEl = document.querySelector('#file-list');
const addSampleBtn = document.querySelector('#add-sample-file');
const clearBtn = document.querySelector('#clear-files');

let uploadedFiles: File[] = [];

// Helper function to update the file list display
async function updateFileList() {
  if (!fileListEl) return;
  
  if (uploadedFiles.length === 0) {
    fileListEl.innerHTML = '<div style="color: #666; font-style: italic;">No files selected</div>';
    return;
  }
  
  let listHtml = '';
  for (const file of uploadedFiles) {
    // Format file size
    const sizeInKB = file.size / 1024;
    let sizeText = sizeInKB < 1024 
      ? `${sizeInKB.toFixed(1)} KB` 
      : `${(sizeInKB / 1024).toFixed(2)} MB`;
      
    // Color code by file type
    let typeColor = '#666';
    if (file.name.endsWith('.pdf')) typeColor = '#d9363e';
    else if (file.name.endsWith('.docx')) typeColor = '#0063a3'; 
    else if (file.name.endsWith('.xlsx')) typeColor = '#2e7d32';
    
    listHtml += `
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 4px 0; border-bottom: 1px solid #f0f0f0;">
        <div>
          <span style="color: ${typeColor}; font-weight: bold;">${file.name}</span>
          <span style="color: #666; font-size: 12px; margin-left: 8px;">${sizeText}</span>
        </div>
        <modus-button 
          data-filename="${file.name}"
          class="remove-file-btn" 
          button-style="borderless" 
          icon="delete" 
          size="small"
          aria-label="Remove file">
        </modus-button>
      </div>
    `;
  }
  
  fileListEl.innerHTML = listHtml;
  
  // Add event listeners to remove buttons
  document.querySelectorAll('.remove-file-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      const target = e.currentTarget as HTMLElement;
      const fileName = target.getAttribute('data-filename');
      
      if (fileName && documentDropzone) {
        await documentDropzone.removeFile(fileName);
        
        // Update local file array
        const files = await documentDropzone.getFiles();
        uploadedFiles = files;
        
        updateFileList();
      }
    });
  });
}

if (documentDropzone && fileListEl) {
  // Handle files event
  documentDropzone.addEventListener('files', async (event: any) => {
    const [files, error] = event.detail;
    uploadedFiles = files;
    
    await updateFileList();
    
    if (error) {
      // Display error notification
      const errorMsg = document.createElement('div');
      errorMsg.textContent = `Error: ${error}`;
      errorMsg.setAttribute('style', 'color: #d9363e; margin-top: 5px; font-size: 14px;');
      fileListEl.appendChild(errorMsg);
      
      // Auto-remove error after 5 seconds
      setTimeout(() => {
        errorMsg.remove();
      }, 5000);
    }
  });
  
  // Initial empty state
  updateFileList();
}

// Add a sample file button
if (addSampleBtn && documentDropzone) {
  addSampleBtn.addEventListener('click', async () => {
    // Create a sample file (in real app, this would be from user input)
    const sampleContent = new Blob(['Sample document content'], { type: 'application/pdf' });
    const timestamp = new Date().getTime();
    const sampleFile = new File([sampleContent], `sample-${timestamp}.pdf`, { type: 'application/pdf' });
    
    // Add the file to the dropzone
    await documentDropzone.addFile(sampleFile);
    
    // Update the local file array
    const files = await documentDropzone.getFiles();
    uploadedFiles = files;
    
    updateFileList();
  });
}

// Clear all files button
if (clearBtn && documentDropzone) {
  clearBtn.addEventListener('click', async () => {
    // Remove all files one by one
    for (const file of uploadedFiles) {
      await documentDropzone.removeFile(file.name);
    }
    
    uploadedFiles = [];
    updateFileList();
  });
}
```


# <ModusIcon>

## Prompt 1
**User Question:** How do I use the basic icon component with different sizes and colors?

**Agent Answer:**
References:
The ModusIcon component is a simple yet flexible way to display icons in your application. The key properties are:
- `name`: Required property specifying which icon to display
- `size`: Controls the icon size (default is 16px)
- `color`: Determines the icon color, supporting standard color names or hex values
- `iconClick` event: Fires when the user clicks on the icon

Here's an implementation showing how to use ModusIcon with various sizes and colors:

```html
<div id="icons-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-icon id="icon-small" name="calendar" size="16" color="#0063a3"></modus-icon>
    <span>Small calendar icon (16px)</span>
  </div>
  
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-icon id="icon-medium" name="notifications" size="24" color="#d9363e"></modus-icon>
    <span>Medium notification icon (24px)</span>
  </div>
  
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-icon id="icon-large" name="check_circle" size="32" color="#008744"></modus-icon>
    <span>Large check circle icon (32px)</span>
  </div>
  
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-icon id="icon-xlarge" name="menu" size="48" color="black"></modus-icon>
    <span>Extra large menu icon (48px)</span>
  </div>
</div>
```

```typescript
// Add click handlers to each icon
const icons = document.querySelectorAll('modus-icon');

icons.forEach(icon => {
  icon.addEventListener('iconClick', (event) => {
    const clickedIcon = event.target as HTMLElement;
    console.log(`Icon clicked: ${clickedIcon.getAttribute('name')}`);
    
    // You can perform actions based on which icon was clicked
    switch (clickedIcon.getAttribute('name')) {
      case 'calendar':
        console.log('Calendar action triggered');
        break;
      case 'notifications':
        console.log('Notification action triggered');
        break;
      case 'check_circle':
        console.log('Check action triggered');
        break;
      case 'menu':
        console.log('Menu action triggered');
        break;
    }
  });
});
```

## Prompt 2
**User Question:** How can I create a custom button with an icon and handle click events?

**Agent Answer:**
References:
You can combine the ModusIcon component with other elements to create custom UI components like icon buttons. This pattern is useful when you need controls that aren't covered by the standard components.

In this implementation, I'll create custom icon buttons that:
1. Display different icons with appropriate colors
2. Include proper accessibility attributes
3. Handle click events for user interaction
4. Show hover effects for better user experience

```html
<div id="icon-buttons-container" style="display: flex; flex-direction: column; gap: 24px; padding: 16px;">
  <h4 style="margin: 0;">Icon Button Examples</h4>
  
  <div style="display: flex; gap: 16px;">
    <!-- Edit button -->
    <div id="edit-button" class="icon-button" role="button" tabindex="0" aria-label="Edit item">
      <modus-icon name="edit" size="20" color="#0063a3"></modus-icon>
    </div>
    
    <!-- Delete button -->
    <div id="delete-button" class="icon-button" role="button" tabindex="0" aria-label="Delete item">
      <modus-icon name="delete" size="20" color="#d9363e"></modus-icon>
    </div>
    
    <!-- Share button -->
    <div id="share-button" class="icon-button" role="button" tabindex="0" aria-label="Share item">
      <modus-icon name="share" size="20" color="#0063a3"></modus-icon>
    </div>
    
    <!-- Settings button -->
    <div id="settings-button" class="icon-button" role="button" tabindex="0" aria-label="Settings">
      <modus-icon name="settings" size="20" color="#666666"></modus-icon>
    </div>
  </div>
  
  <div id="action-result" style="font-size: 14px; color: #666;">Click an icon button to see the action</div>
  
  <style>
    .icon-button {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.2s ease;
    }
    
    .icon-button:hover {
      background-color: #f0f0f0;
    }
    
    .icon-button:active {
      background-color: #e0e0e0;
    }
    
    .icon-button:focus {
      outline: 2px solid #0063a3;
      outline-offset: 2px;
    }
  </style>
</div>
```

```typescript
// Get references to all elements
const editButton = document.querySelector('#edit-button');
const deleteButton = document.querySelector('#delete-button');
const shareButton = document.querySelector('#share-button');
const settingsButton = document.querySelector('#settings-button');
const actionResult = document.querySelector('#action-result');

// Helper function to handle button clicks
function handleButtonClick(action: string): void {
  if (actionResult) {
    actionResult.textContent = `Action performed: ${action}`;
    
    // Reset the message after a delay
    setTimeout(() => {
      actionResult.textContent = 'Click an icon button to see the action';
    }, 2000);
  }
}

// Add click and keyboard event listeners to each button
if (editButton) {
  editButton.addEventListener('click', () => handleButtonClick('Edit'));
  editButton.addEventListener('keydown', (event: KeyboardEvent) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleButtonClick('Edit');
    }
  });
}

if (deleteButton) {
  deleteButton.addEventListener('click', () => handleButtonClick('Delete'));
  deleteButton.addEventListener('keydown', (event: KeyboardEvent) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleButtonClick('Delete');
    }
  });
}

if (shareButton) {
  shareButton.addEventListener('click', () => handleButtonClick('Share'));
  shareButton.addEventListener('keydown', (event: KeyboardEvent) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleButtonClick('Share');
    }
  });
}

if (settingsButton) {
  settingsButton.addEventListener('click', () => handleButtonClick('Settings'));
  settingsButton.addEventListener('keydown', (event: KeyboardEvent) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleButtonClick('Settings');
    }
  });
}
```

# <ModusList>

## Prompt 1
**User Question:** How do I create a basic list with items of different sizes and states?

**Agent Answer:**
References:
The ModusList component is a container that works with ModusListItem components to create structured lists. Key features include:
- Different item sizes: `condensed`, `standard` (default), and `large`
- Item states: selected, disabled
- Optional subtext for additional information
- Borderless option for clean layout
- Click event handling for interactive lists

This implementation demonstrates a list with various item configurations:

```html
<div id="list-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; max-width: 400px;">
  <h4>User List Example</h4>
  
  <modus-list id="user-list">
    <!-- Condensed size item -->
    <modus-list-item id="item-1" size="condensed" left-icon="person">
      John Smith
    </modus-list-item>
    
    <!-- Standard size with subtext -->
    <modus-list-item id="item-2" wrap-sub-text="true" sub-text="Available">
      Sarah Johnson
    </modus-list-item>
    
    <!-- Selected item -->
    <modus-list-item id="item-3" selected>
      Michael Brown
    </modus-list-item>
    
    <!-- Disabled item -->
    <modus-list-item id="item-4" disabled>
      David Wilson
    </modus-list-item>
    
    <!-- Large size item -->
    <modus-list-item id="item-5" size="large" left-icon="star">
      Emily Davis
    </modus-list-item>
    
    <!-- Borderless item -->
    <modus-list-item id="item-6" borderless sub-text="Away - Back in 30 minutes">
      Robert Taylor
    </modus-list-item>
  </modus-list>
  
  <div id="selection-result" style="margin-top: 8px; font-size: 14px; color: #666;">
    Click on a user to select them
  </div>
</div>
```

```typescript
const userList = document.querySelector('#user-list');
const selectionResult = document.querySelector('#selection-result');
let selectedItemId: string | null = null;

// Function to handle item selection
function handleItemSelection(itemId: string, userName: string): void {
  // Reset previous selection (visual only, doesn't affect component's selected property)
  const previouslySelectedItem = document.querySelector(`#${selectedItemId}`);
  if (previouslySelectedItem && previouslySelectedItem.id !== itemId) {
    previouslySelectedItem.removeAttribute('selected');
  }
  
  // Mark new item as selected
  const currentItem = document.querySelector(`#${itemId}`);
  if (currentItem) {
    currentItem.setAttribute('selected', 'true');
    selectedItemId = itemId;
  }
  
  // Update the selection display
  if (selectionResult) {
    selectionResult.textContent = `Selected user: ${userName}`;
    selectionResult.style.color = '#0063a3';
    selectionResult.style.fontWeight = 'bold';
  }
}

// Add click event listeners to all list items
if (userList) {
  const items = userList.querySelectorAll('modus-list-item');
  
  items.forEach(item => {
    // Skip disabled items
    if (item.hasAttribute('disabled')) return;
    
    item.addEventListener('itemClick', (event) => {
      const clickedItem = event.target as HTMLElement;
      const itemId = clickedItem.id;
      const userName = clickedItem.textContent?.trim() || 'Unknown User';
      
      handleItemSelection(itemId, userName);
    });
  });
  
  // Initialize with the selected item if any
  const initiallySelectedItem = userList.querySelector('modus-list-item[selected]') as HTMLElement;
  if (initiallySelectedItem) {
    selectedItemId = initiallySelectedItem.id;
    const userName = initiallySelectedItem.textContent?.trim() || 'Unknown User';
    
    if (selectionResult) {
      selectionResult.textContent = `Selected user: ${userName}`;
      selectionResult.style.color = '#0063a3';
      selectionResult.style.fontWeight = 'bold';
    }
  }
}
```

## Prompt 2
**User Question:** How do I create a navigation menu with list items and icons that responds to user interactions?

**Agent Answer:**
References:
The ModusList component is well-suited for creating navigation menus. Key features for this use case:
- `leftIcon` property to add visual cues for each navigation option
- `iconColor` property to customize icon appearance
- `selected` property to indicate the current active page
- `itemClick` event to handle navigation
- Different sizes to accommodate various layout needs

This implementation creates a sidebar navigation using the ModusList component:

```html
<div style="display: flex; height: 400px;">
  <!-- Navigation Sidebar -->
  <div style="width: 240px; background-color: #f5f5f5; border-right: 1px solid #e0e0e0; padding: 16px 0;">
    <div style="padding: 0 16px 16px;">
      <h3 style="margin: 0; font-size: 18px;">Application Menu</h3>
    </div>
    
    <modus-list id="nav-menu">
      <!-- Dashboard -->
      <modus-list-item 
        id="nav-dashboard" 
        left-icon="dashboard" 
        icon-color="#0063a3" 
        selected>
        Dashboard
      </modus-list-item>
      
      <!-- Projects -->
      <modus-list-item 
        id="nav-projects" 
        left-icon="folder"
        icon-color="#0063a3">
        Projects
      </modus-list-item>
      
      <!-- Tasks -->
      <modus-list-item 
        id="nav-tasks" 
        left-icon="assignment"
        icon-color="#0063a3">
        Tasks
      </modus-list-item>
      
      <!-- Calendar -->
      <modus-list-item 
        id="nav-calendar" 
        left-icon="calendar_today"
        icon-color="#0063a3">
        Calendar
      </modus-list-item>
      
      <!-- Reports -->
      <modus-list-item 
        id="nav-reports" 
        left-icon="bar_chart"
        icon-color="#0063a3">
        Reports
      </modus-list-item>
      
      <!-- Settings (with separator) -->
      <div style="height: 1px; background-color: #e0e0e0; margin: 8px 0;"></div>
      
      <modus-list-item 
        id="nav-settings" 
        left-icon="settings"
        icon-color="#666666">
        Settings
      </modus-list-item>
      
      <!-- Help -->
      <modus-list-item 
        id="nav-help" 
        left-icon="help"
        icon-color="#666666">
        Help & Support
      </modus-list-item>
    </modus-list>
  </div>
  
  <!-- Main Content Area -->
  <div id="content-area" style="flex: 1; padding: 24px;">
    <h2 id="page-title">Dashboard</h2>
    <p id="page-description">Welcome to the dashboard. Select a navigation item to change pages.</p>
  </div>
</div>
```

```typescript
const navMenu = document.querySelector('#nav-menu');
const pageTitle = document.querySelector('#page-title');
const pageDescription = document.querySelector('#page-description');

// Page content mapping
const pageContent = {
  'nav-dashboard': {
    title: 'Dashboard',
    description: 'Welcome to the dashboard. View your key metrics and recent activity.'
  },
  'nav-projects': {
    title: 'Projects',
    description: 'Manage your projects, create new ones, and track progress.'
  },
  'nav-tasks': {
    title: 'Tasks',
    description: 'View and manage your tasks and assignments.'
  },
  'nav-calendar': {
    title: 'Calendar',
    description: 'Schedule meetings and view upcoming events.'
  },
  'nav-reports': {
    title: 'Reports',
    description: 'Generate and view reports for your projects and tasks.'
  },
  'nav-settings': {
    title: 'Settings',
    description: 'Configure application settings and preferences.'
  },
  'nav-help': {
    title: 'Help & Support',
    description: 'Get help and support for using the application.'
  }
};

// Function to handle navigation
function navigateTo(navItemId: string): void {
  // Update content
  if (pageTitle && pageDescription && pageContent[navItemId]) {
    pageTitle.textContent = pageContent[navItemId].title;
    pageDescription.textContent = pageContent[navItemId].description;
  }
  
  // Update selected state in navigation
  if (navMenu) {
    const navItems = navMenu.querySelectorAll('modus-list-item');
    
    navItems.forEach(item => {
      if (item.id === navItemId) {
        item.setAttribute('selected', 'true');
      } else {
        item.removeAttribute('selected');
      }
    });
  }
}

// Add click handlers to navigation items
if (navMenu) {
  const navItems = navMenu.querySelectorAll('modus-list-item');
  
  navItems.forEach(item => {
    item.addEventListener('itemClick', () => {
      navigateTo(item.id);
    });
  });
  
  // Optionally, you can also handle keyboard navigation
  navItems.forEach((item, index) => {
    item.addEventListener('keydown', (event: KeyboardEvent) => {
      // Handle arrow key navigation
      if (event.key === 'ArrowDown' && index < navItems.length - 1) {
        event.preventDefault();
        (navItems[index + 1] as any).focusItem();
      } else if (event.key === 'ArrowUp' && index > 0) {
        event.preventDefault();
        (navItems[index - 1] as any).focusItem();
      }
    });
  });
}
```


# <ModusMessage>

## Prompt 1
**User Question:** How do I create basic info and question messages with the ModusMessage component?

**Agent Answer:**
References:
The ModusMessage component is used to display informational or question-style messages to users. Key properties to consider:
- `type`: Sets the message style, can be either "info" (default) or "question"
- `icon`: Optionally override the default icon that appears with the message
- `aria-label`: Improves accessibility by providing a label for screen readers

This implementation demonstrates both info and question message types with default styling:

```html
<div id="messages-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h4>Message Examples</h4>
  
  <!-- Info message (default) -->
  <modus-message id="info-message" type="info">
    This is an informational message providing details to the user.
  </modus-message>
  
  <!-- Question message -->
  <modus-message id="question-message" type="question">
    Have you reviewed the documentation before submitting your request?
  </modus-message>
  
  <!-- Info message with link -->
  <modus-message id="info-link-message" type="info">
    Please review our <a href="#" style="color: #0063a3;">privacy policy</a> for more information.
  </modus-message>
</div>
```

```typescript
// No TypeScript is required for basic message display
// The component is primarily static with no event handling
// However, you could add code to dynamically toggle messages:

const infoMessage = document.querySelector('#info-message');
const questionMessage = document.querySelector('#question-message');

// Example of how you might programmatically toggle message visibility
function toggleMessageVisibility(messageId: string): void {
  const message = document.querySelector(`#${messageId}`);
  if (message) {
    message.style.display = message.style.display === 'none' ? 'block' : 'none';
  }
}

// Example usage (not executed by default):
// setTimeout(() => toggleMessageVisibility('info-message'), 3000);
```

## Prompt 2
**User Question:** How can I create messages with custom icons and dynamically show/hide them based on user actions?

**Agent Answer:**
References:
For more advanced usage of the ModusMessage component, we can:
1. Override the default icons using the `icon` property
2. Create functions to dynamically show and hide messages
3. Integrate messages with form validation or user actions
4. Style messages for different contexts

This implementation demonstrates a form with validation that dynamically shows appropriate messages:

```html
<div id="form-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; max-width: 500px;">
  <h4>Contact Form</h4>
  
  <!-- Form fields -->
  <div style="display: flex; flex-direction: column; gap: 8px;">
    <modus-text-input 
      id="name-input" 
      label="Name" 
      placeholder="Enter your full name">
    </modus-text-input>
    
    <modus-text-input 
      id="email-input" 
      label="Email" 
      placeholder="Enter your email address">
    </modus-text-input>
    
    <modus-textarea-input
      id="message-input"
      label="Message"
      placeholder="Enter your message"
      rows="4">
    </modus-textarea-input>
  </div>
  
  <!-- Messages - initially hidden -->
  <div style="display: flex; flex-direction: column; gap: 8px;">
    <modus-message id="form-info-message" type="info" icon="info" style="display: none;">
      All fields are required. We'll respond within 2 business days.
    </modus-message>
    
    <modus-message id="form-question-message" type="question" icon="help" style="display: none;">
      Do you want us to contact you by phone instead? Add your number in the message.
    </modus-message>
    
    <modus-message id="form-error-message" type="info" icon="error" style="display: none; color: #d9363e;">
      Please correct the errors in the form before submitting.
    </modus-message>
    
    <modus-message id="form-success-message" type="info" icon="check_circle" style="display: none; color: #008744;">
      Your message has been sent successfully!
    </modus-message>
  </div>
  
  <!-- Form buttons -->
  <div style="display: flex; gap: 8px; margin-top: 8px;">
    <modus-button id="info-toggle-btn" button-style="borderless" color="secondary">
      Show Info
    </modus-button>
    
    <modus-button id="question-toggle-btn" button-style="borderless" color="secondary">
      Show Question
    </modus-button>
    
    <div style="flex-grow: 1;"></div>
    
    <modus-button id="submit-btn" color="primary">
      Submit
    </modus-button>
  </div>
</div>
```

```typescript
// Get references to form elements
const nameInput = document.querySelector('#name-input') as HTMLInputElement;
const emailInput = document.querySelector('#email-input') as HTMLInputElement;
const messageInput = document.querySelector('#message-input') as HTMLTextAreaElement;

// Get references to message elements
const infoMessage = document.querySelector('#form-info-message') as HTMLElement;
const questionMessage = document.querySelector('#form-question-message') as HTMLElement;
const errorMessage = document.querySelector('#form-error-message') as HTMLElement;
const successMessage = document.querySelector('#form-success-message') as HTMLElement;

// Get references to buttons
const infoToggleBtn = document.querySelector('#info-toggle-btn');
const questionToggleBtn = document.querySelector('#question-toggle-btn');
const submitBtn = document.querySelector('#submit-btn');

// Function to toggle message visibility
function toggleMessage(message: HTMLElement): void {
  if (!message) return;
  
  // Hide all messages first
  [infoMessage, questionMessage, errorMessage, successMessage].forEach(msg => {
    if (msg && msg !== message) {
      msg.style.display = 'none';
    }
  });
  
  // Toggle the target message
  message.style.display = message.style.display === 'none' ? 'block' : 'none';
}

// Function to validate form
function validateForm(): boolean {
  let isValid = true;
  
  // Simple validation
  if (!nameInput || !nameInput.value.trim()) {
    nameInput.setAttribute('error-text', 'Name is required');
    isValid = false;
  } else {
    nameInput.removeAttribute('error-text');
  }
  
  if (!emailInput || !emailInput.value.trim()) {
    emailInput.setAttribute('error-text', 'Email is required');
    isValid = false;
  } else if (!emailInput.value.includes('@')) {
    emailInput.setAttribute('error-text', 'Please enter a valid email');
    isValid = false;
  } else {
    emailInput.removeAttribute('error-text');
  }
  
  if (!messageInput || !messageInput.value.trim()) {
    messageInput.setAttribute('error-text', 'Message is required');
    isValid = false;
  } else {
    messageInput.removeAttribute('error-text');
  }
  
  return isValid;
}

// Set up event listeners
if (infoToggleBtn) {
  infoToggleBtn.addEventListener('click', () => toggleMessage(infoMessage));
}

if (questionToggleBtn) {
  questionToggleBtn.addEventListener('click', () => toggleMessage(questionMessage));
}

if (submitBtn) {
  submitBtn.addEventListener('click', () => {
    // Hide all messages before validation
    [infoMessage, questionMessage, errorMessage, successMessage].forEach(msg => {
      if (msg) msg.style.display = 'none';
    });
    
    const isValid = validateForm();
    
    if (isValid) {
      // Show success message
      if (successMessage) {
        successMessage.style.display = 'block';
      }
      
      // Simulate form submission
      console.log('Form submitted:', {
        name: nameInput?.value,
        email: emailInput?.value,
        message: messageInput?.value
      });
      
      // Reset form after successful submission
      setTimeout(() => {
        if (nameInput) nameInput.value = '';
        if (emailInput) emailInput.value = '';
        if (messageInput) messageInput.value = '';
      }, 1500);
    } else {
      // Show error message
      if (errorMessage) {
        errorMessage.style.display = 'block';
      }
    }
  });
}
```



# <ModusModal>

## Prompt 1
**User Question:** How do I create a basic modal dialog with a header and action buttons?

**Agent Answer:**
References:
The ModusModal component creates an overlay dialog that requires user interaction before returning to the main application. Key properties to consider:
- `header-text`: Sets the title of the modal
- `primary-button-text` and `secondary-button-text`: Define action buttons
- Opening/closing is controlled via the `open()` and `close()` methods
- Events like `primaryButtonClick`, `secondaryButtonClick`, and `closed` let you respond to user actions

This implementation demonstrates a standard modal with a header and two buttons:

```html
<div id="modal-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-button id="open-modal-btn" color="primary">Open Modal</modus-button>
  
  <modus-modal 
    id="demo-modal"
    header-text="Confirm Action" 
    primary-button-text="Confirm" 
    secondary-button-text="Cancel"
    primary-button-aria-label="Confirm action"
    secondary-button-aria-label="Cancel action">
    
    <p>Are you sure you want to proceed with this action? This cannot be undone.</p>
    <p>Please confirm your choice by clicking one of the buttons below.</p>
  </modus-modal>
</div>
```

```typescript
const modalButton = document.querySelector('#open-modal-btn');
const modal = document.querySelector('#demo-modal') as any;

if (modalButton && modal) {
  // Open modal when button is clicked
  modalButton.addEventListener('buttonClick', () => {
    modal.open();
  });
  
  // Handle primary button click (Confirm)
  modal.addEventListener('primaryButtonClick', () => {
    console.log('Action confirmed!');
    
    // You can perform actions here before closing the modal
    // For example, saving data, making API calls, etc.
    
    // Close the modal
    modal.close();
  });
  
  // Handle secondary button click (Cancel)
  modal.addEventListener('secondaryButtonClick', () => {
    console.log('Action cancelled');
    modal.close();
  });
  
  // Handle modal close event (triggered by any close action)
  modal.addEventListener('closed', () => {
    console.log('Modal closed');
    
    // Return focus to the button that opened the modal
    setTimeout(() => {
      (modalButton as any).focusButton();
    }, 100);
  });
}
```

## Prompt 2
**User Question:** How can I create a modal with a custom footer and prevent it from closing when clicking outside?

**Agent Answer:**
References:
For more advanced modal usage, we can leverage:
- The `footerContent` slot to create custom footer layouts
- The `backdrop="static"` property to prevent closing when clicking outside
- The `fullscreen` and `showFullscreenToggle` properties for expanded views
- Custom event handlers for complex interaction patterns

This implementation demonstrates a form modal with custom buttons and behavior:

```html
<div id="advanced-modal-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-button id="open-form-modal-btn" color="primary">Open Form Modal</modus-button>
  
  <modus-modal 
    id="form-modal"
    header-text="User Registration" 
    backdrop="static"
    show-fullscreen-toggle="true"
    z-index="1050">
    
    <!-- Modal content -->
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <p>Please fill out the registration form below. All fields are required.</p>
      
      <modus-text-input 
        id="name-input"
        label="Full Name" 
        placeholder="Enter your full name"
        required>
      </modus-text-input>
      
      <modus-text-input 
        id="email-input"
        label="Email" 
        placeholder="Enter your email address"
        required>
      </modus-text-input>
      
      <modus-select 
        id="role-select"
        label="Role"
        placeholder="Select your role">
      </modus-select>
      
      <modus-checkbox 
        id="terms-checkbox"
        label="I agree to the Terms and Conditions">
      </modus-checkbox>
    </div>
    
    <!-- Custom footer with multiple buttons -->
    <div 
      slot="footerContent"
      style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
      
      <div>
        <modus-button 
          id="cancel-btn"
          button-style="borderless"
          color="danger">
          Cancel
        </modus-button>
      </div>
      
      <div style="display: flex; gap: 8px;">
        <modus-button 
          id="save-draft-btn"
          color="secondary">
          Save Draft
        </modus-button>
        
        <modus-button 
          id="submit-btn"
          color="primary">
          Submit
        </modus-button>
      </div>
    </div>
  </modus-modal>
</div>
```

```typescript
const openButton = document.querySelector('#open-form-modal-btn');
const formModal = document.querySelector('#form-modal') as any;
const cancelBtn = document.querySelector('#cancel-btn');
const saveDraftBtn = document.querySelector('#save-draft-btn');
const submitBtn = document.querySelector('#submit-btn');

// Form elements
const nameInput = document.querySelector('#name-input');
const emailInput = document.querySelector('#email-input');
const roleSelect = document.querySelector('#role-select');
const termsCheckbox = document.querySelector('#terms-checkbox');

// Initialize the select component with options
if (roleSelect) {
  const roleOptions = [
    { text: 'Administrator', value: 'admin' },
    { text: 'Developer', value: 'dev' },
    { text: 'Designer', value: 'design' },
    { text: 'Manager', value: 'manager' }
  ];
  
  (roleSelect as any).options = roleOptions;
}

if (openButton && formModal) {
  // Open modal when button is clicked
  openButton.addEventListener('buttonClick', () => {
    formModal.open();
  });
  
  // Form validation function
  function validateForm(): boolean {
    let isValid = true;
    
    // Validate name
    if (!(nameInput as any).value) {
      (nameInput as any).errorText = 'Name is required';
      isValid = false;
    } else {
      (nameInput as any).errorText = '';
    }
    
    // Validate email
    if (!(emailInput as any).value) {
      (emailInput as any).errorText = 'Email is required';
      isValid = false;
    } else if (!(emailInput as any).value.includes('@')) {
      (emailInput as any).errorText = 'Please enter a valid email address';
      isValid = false;
    } else {
      (emailInput as any).errorText = '';
    }
    
    // Validate role selection
    if (!(roleSelect as any).value) {
      (roleSelect as any).errorText = 'Please select a role';
      isValid = false;
    } else {
      (roleSelect as any).errorText = '';
    }
    
    // Validate terms agreement
    if (!(termsCheckbox as any).checked) {
      // Display error near checkbox
      const errorMsg = document.createElement('div');
      errorMsg.textContent = 'You must agree to the terms';
      errorMsg.style.color = '#d9363e';
      errorMsg.style.fontSize = '12px';
      errorMsg.id = 'terms-error';
      
      // Remove existing error if any
      const existingError = document.querySelector('#terms-error');
      if (existingError) {
        existingError.remove();
      }
      
      termsCheckbox.insertAdjacentElement('afterend', errorMsg);
      isValid = false;
    } else {
      // Remove error if exists
      const existingError = document.querySelector('#terms-error');
      if (existingError) {
        existingError.remove();
      }
    }
    
    return isValid;
  }
  
  // Handle cancel button
  if (cancelBtn) {
    cancelBtn.addEventListener('buttonClick', () => {
      // Show confirmation before closing if form has data
      const hasData = (nameInput as any)?.value || 
                      (emailInput as any)?.value || 
                      (roleSelect as any)?.value;
      
      if (hasData) {
        if (confirm('Are you sure you want to cancel? All entered data will be lost.')) {
          formModal.close();
        }
      } else {
        formModal.close();
      }
    });
  }
  
  // Handle save draft button
  if (saveDraftBtn) {
    saveDraftBtn.addEventListener('buttonClick', () => {
      // Save current form data (example implementation)
      const formData = {
        name: (nameInput as any)?.value || '',
        email: (emailInput as any)?.value || '',
        role: (roleSelect as any)?.value || '',
        termsAccepted: (termsCheckbox as any)?.checked || false
      };
      
      console.log('Saving draft:', formData);
      localStorage.setItem('formDraft', JSON.stringify(formData));
      
      // Show confirmation
      alert('Draft saved successfully!');
    });
  }
  
  // Handle submit button
  if (submitBtn) {
    submitBtn.addEventListener('buttonClick', () => {
      const isValid = validateForm();
      
      if (isValid) {
        // Collect form data
        const formData = {
          name: (nameInput as any).value,
          email: (emailInput as any).value,
          role: (roleSelect as any).value,
          termsAccepted: (termsCheckbox as any).checked
        };
        
        console.log('Form submitted:', formData);
        
        // Simulate submission success
        alert('Registration successful!');
        formModal.close();
      } else {
        console.log('Form validation failed');
      }
    });
  }
  
  // Handle modal opened event
  formModal.addEventListener('opened', () => {
    console.log('Modal opened');
    
    // Check for saved draft
    const savedDraft = localStorage.getItem('formDraft');
    if (savedDraft) {
      const formData = JSON.parse(savedDraft);
      
      // Ask if user wants to restore the draft
      const restoreDraft = confirm('You have a saved draft. Would you like to restore it?');
      
      if (restoreDraft) {
        // Restore form data
        if (nameInput) (nameInput as any).value = formData.name || '';
        if (emailInput) (emailInput as any).value = formData.email || '';
        if (roleSelect) (roleSelect as any).value = formData.role || '';
        if (termsCheckbox) (termsCheckbox as any).checked = formData.termsAccepted || false;
      }
    }
  });
}
```



# <ModusNavbar>

## Prompt 1
**User Question:** How do I create a basic navigation bar with a logo, dropdown menu, and profile?

**Agent Answer:**
References:
The ModusNavbar component provides a comprehensive application header with numerous customization options. For a basic implementation, we need to focus on:
- `logoOptions`: For primary and secondary logos
- `dropdownOptions`: For creating a project/context selector
- `profileMenuOptions`: For user information and sign out functionality
- Event handlers for various interactions

Here's a basic implementation of the ModusNavbar with essential features:

```html
<div id="app-container">
  <modus-navbar 
    id="main-navbar"
    show-shadow="true"
    show-profile="true">
  </modus-navbar>
  
  <div style="padding: 24px;">
    <h2>Application Content</h2>
    <p>Main content goes here. The navbar is fixed at the top of the page.</p>
  </div>
</div>
```

```typescript
// Get reference to navbar
const navbar = document.querySelector('#main-navbar');

if (navbar) {
  // Configure logo options
  navbar.logoOptions = {
    primary: {
      url: 'https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg',
      height: '24',
      alt: 'Company Logo'
    },
    secondary: {
      url: 'https://modus.trimble.com/favicon.svg',
      height: '24'
    },
    clickable: true
  };
  
  // Configure dropdown options (project selector)
  const dropdownItems = [
    { text: 'Project Alpha', value: '1' },
    { text: 'Project Beta', value: '2' },
    { text: 'Project Gamma', value: '3' }
  ];
  
  navbar.dropdownOptions = {
    ariaLabel: 'Project selector',
    items: dropdownItems
  };
  
  // Set initial selected item
  navbar.selectedDropdownItem = dropdownItems[0];
  
  // Configure profile menu
  navbar.profileMenuOptions = {
    username: 'John Doe',
    email: 'john.doe@example.com',
    initials: 'JD',
    signOutText: 'Sign Out',
    links: [
      {
        id: 'profile',
        display: 'My Profile',
        icon: 'person'
      },
      {
        id: 'settings',
        display: 'Settings',
        icon: 'settings'
      }
    ]
  };
  
  // Add event listeners
  navbar.addEventListener('productLogoClick', (event) => {
    console.log('Logo clicked, navigating to home');
    // Navigate to home page
  });
  
  navbar.addEventListener('dropdownItemSelect', (event: any) => {
    console.log('Selected project:', event.detail.text);
    // Handle project change
  });
  
  navbar.addEventListener('profileMenuSignOutClick', () => {
    console.log('Sign out clicked');
    // Handle sign out process
  });
  
  navbar.addEventListener('profileMenuLinkClick', (event: any) => {
    const linkId = event.detail;
    console.log(`Profile menu link clicked: ${linkId}`);
    
    // Handle different profile menu links
    switch (linkId) {
      case 'profile':
        console.log('Navigate to profile page');
        break;
      case 'settings':
        console.log('Navigate to settings page');
        break;
    }
  });
}
```

## Prompt 2
**User Question:** How can I implement a full-featured navbar with notifications, search, and custom menus?

**Agent Answer:**
References:
For a more advanced implementation of ModusNavbar, we can utilize:
- Slots for custom content in menus
- Notification counters and custom content
- Search functionality
- Custom app menu entries
- Different color variants

This implementation provides a comprehensive navbar with all major features enabled:

```html
<div id="advanced-app-container">
  <!-- Advanced Navbar with all features enabled -->
  <modus-navbar 
    id="advanced-navbar"
    show-shadow="true"
    show-profile="true"
    show-apps-menu="true" 
    show-help="true"
    show-main-menu="true"
    show-notifications="true"
    show-search="true"
    enable-search-overlay="true"
    variant="blue">
    
    <!-- Main Menu Content -->
    <div slot="main" style="width: 250px; padding: 16px;">
      <h3 style="margin-top: 0;">Main Menu</h3>
      <modus-list>
        <modus-list-item id="menu-dashboard" left-icon="dashboard">Dashboard</modus-list-item>
        <modus-list-item id="menu-projects" left-icon="folder">Projects</modus-list-item>
        <modus-list-item id="menu-calendar" left-icon="calendar_today">Calendar</modus-list-item>
        <modus-list-item id="menu-reports" left-icon="bar_chart">Reports</modus-list-item>
      </modus-list>
    </div>
    
    <!-- Notification Menu Content -->
    <div slot="notifications" style="width: 300px; padding: 16px;">
      <h3 style="margin-top: 0;">Notifications</h3>
      <div style="max-height: 300px; overflow-y: auto;">
        <div style="padding: 8px; border-bottom: 1px solid #eee;">
          <div style="font-weight: bold;">Project update</div>
          <div>Project Alpha has been updated</div>
          <div style="font-size: 12px; color: #666;">2 minutes ago</div>
        </div>
        <div style="padding: 8px; border-bottom: 1px solid #eee;">
          <div style="font-weight: bold;">New comment</div>
          <div>John added a comment to your task</div>
          <div style="font-size: 12px; color: #666;">1 hour ago</div>
        </div>
        <div style="padding: 8px;">
          <div style="font-weight: bold;">Meeting reminder</div>
          <div>Team meeting in 15 minutes</div>
          <div style="font-size: 12px; color: #666;">Just now</div>
        </div>
      </div>
    </div>
    
    <!-- Profile Menu Content (using default implementation) -->
  </modus-navbar>
  
  <div style="padding: 24px;">
    <h2>Application Content</h2>
    <p>Main content goes here. The navbar is fixed at the top of the page.</p>
  </div>
</div>
```

```typescript
// Get reference to the advanced navbar
const advancedNavbar = document.querySelector('#advanced-navbar');

if (advancedNavbar) {
  // Configure logo options
  advancedNavbar.logoOptions = {
    primary: {
      url: 'https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg',
      height: '24',
      alt: 'Company Logo'
    },
    secondary: {
      url: 'https://modus.trimble.com/favicon.svg',
      height: '24'
    },
    clickable: true
  };
  
  // Configure apps menu
  advancedNavbar.apps = [
    {
      name: 'Dashboard',
      description: 'Main dashboard application',
      logoUrl: 'https://modus.trimble.com/favicon.svg',
      url: '#dashboard',
      category: 'Primary'
    },
    {
      name: 'Analytics',
      description: 'Data analytics platform',
      logoUrl: 'https://modus.trimble.com/favicon.svg',
      url: '#analytics',
      category: 'Primary'
    },
    {
      name: 'Calendar',
      description: 'Schedule and appointments',
      logoUrl: 'https://modus.trimble.com/favicon.svg',
      url: '#calendar',
      category: 'Tools'
    },
    {
      name: 'Settings',
      description: 'Application configuration',
      logoUrl: 'https://modus.trimble.com/favicon.svg',
      url: '#settings',
      category: 'Tools'
    }
  ];
  
  // Configure dropdown options
  const dropdownItems = [
    { text: 'Project Alpha', value: '1' },
    { text: 'Project Beta', value: '2' },
    { text: 'Project Gamma', value: '3' }
  ];
  
  advancedNavbar.dropdownOptions = {
    ariaLabel: 'Project selector',
    items: dropdownItems
  };
  
  // Set initial selected item
  advancedNavbar.selectedDropdownItem = dropdownItems[1];
  
  // Configure profile menu
  advancedNavbar.profileMenuOptions = {
    username: 'Alex Johnson',
    email: 'alex.johnson@example.com',
    initials: 'AJ',
    signOutText: 'Sign Out',
    links: [
      {
        id: 'profile',
        display: 'My Profile',
        icon: 'person'
      },
      {
        id: 'settings',
        display: 'Account Settings',
        icon: 'settings'
      },
      {
        id: 'help',
        display: 'Help & Support',
        icon: 'help'
      },
      {
        id: 'feedback',
        display: 'Send Feedback',
        icon: 'feedback'
      }
    ]
  };
  
  // Set notification count
  advancedNavbar.notificationCount = 3;
  
  // Configure tooltips
  advancedNavbar.helpTooltip = {
    text: 'Get Help',
    ariaLabel: 'Access help resources'
  };
  
  advancedNavbar.searchTooltip = {
    text: 'Search',
    ariaLabel: 'Search the application'
  };
  
  // Add custom buttons
  advancedNavbar.buttons = [
    {
      id: 'add',
      icon: 'add',
      orderIndex: 0,
      tooltip: {
        text: 'Create New',
        ariaLabel: 'Create a new item'
      }
    },
    {
      id: 'favorite',
      icon: 'star',
      orderIndex: 1,
      tooltip: {
        text: 'Favorites',
        ariaLabel: 'View favorites'
      }
    }
  ];
  
  // Add help URL
  advancedNavbar.helpUrl = 'https://support.example.com';
  
  // Event Handlers
  
  // Main menu events
  advancedNavbar.addEventListener('mainMenuClick', () => {
    console.log('Main menu clicked');
  });
  
  // Search events
  advancedNavbar.addEventListener('searchChange', (event: any) => {
    console.log('Search query:', event.detail);
  });
  
  advancedNavbar.addEventListener('searchMenuClick', () => {
    console.log('Search clicked');
  });
  
  // Notification events
  advancedNavbar.addEventListener('notificationsMenuOpen', () => {
    console.log('Notifications menu opened');
    // You could fetch latest notifications here
  });
  
  // Apps menu events
  advancedNavbar.addEventListener('appsMenuOpen', () => {
    console.log('Apps menu opened');
  });
  
  advancedNavbar.addEventListener('appsMenuAppOpen', (event: any) => {
    console.log('App selected:', event.detail.name);
    // Navigate to the selected app
  });
  
  // Custom button events
  advancedNavbar.addEventListener('buttonClick', (event: any) => {
    const buttonId = event.detail;
    console.log(`Button clicked: ${buttonId}`);
    
    switch (buttonId) {
      case 'add':
        console.log('Opening create new item dialog');
        // Open a create dialog
        break;
      case 'favorite':
        console.log('Opening favorites list');
        // Show favorites
        break;
    }
  });
  
  // Main menu item click handlers
  const menuItems = document.querySelectorAll('modus-list-item[id^="menu-"]');
  menuItems.forEach(item => {
    item.addEventListener('itemClick', (event) => {
      const menuId = (event.target as HTMLElement).id;
      console.log(`Menu item clicked: ${menuId}`);
      
      // Close main menu after selection (optional)
      const mainMenuButton = advancedNavbar.shadowRoot.querySelector('.main-menu-button');
      if (mainMenuButton) {
        (mainMenuButton as HTMLElement).click();
      }
    });
  });
}
```


# <ModusNumberInput>

## Prompt 1
**User Question:** How do I create a basic number input field with validation for min and max values?

**Agent Answer:**
References:
The ModusNumberInput component provides a specialized input field for numeric values. Key properties to consider:
- `minValue` and `maxValue`: Define the acceptable range of values
- `step`: Controls increment/decrement precision
- `valueChange` event: Captures when the user changes the value
- Validation states: Use `errorText` and `validText` to provide feedback

Here's an implementation of a number input with validation for a value between 0 and 100:

```html
<div id="number-input-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-number-input
    id="quantity-input"
    label="Quantity"
    min-value="0"
    max-value="100"
    step="1"
    placeholder="Enter quantity"
    helper-text="Enter a number between 0 and 100"
    required>
  </modus-number-input>
  
  <div id="validation-message" style="font-size: 14px;"></div>
</div>
```

```typescript
const numberInput = document.querySelector('#quantity-input');
const validationMessage = document.querySelector('#validation-message');

if (numberInput && validationMessage) {
  // Handle value changes
  numberInput.addEventListener('valueChange', (event: any) => {
    const value = parseFloat(event.detail);
    const minValue = 0;
    const maxValue = 100;
    
    // Clear previous validation state
    numberInput.removeAttribute('error-text');
    numberInput.removeAttribute('valid-text');
    
    // Validate value
    if (isNaN(value)) {
      numberInput.setAttribute('error-text', 'Please enter a valid number');
      validationMessage.textContent = 'Error: Please enter a valid number';
      validationMessage.style.color = '#d9363e';
    } else if (value < minValue) {
      numberInput.setAttribute('error-text', 'Value cannot be less than 0');
      validationMessage.textContent = 'Error: Value cannot be less than 0';
      validationMessage.style.color = '#d9363e';
    } else if (value > maxValue) {
      numberInput.setAttribute('error-text', 'Value cannot exceed 100');
      validationMessage.textContent = 'Error: Value cannot exceed 100';
      validationMessage.style.color = '#d9363e';
    } else {
      numberInput.setAttribute('valid-text', 'Valid value');
      validationMessage.textContent = `Value accepted: ${value}`;
      validationMessage.style.color = '#008744';
    }
  });
}
```

## Prompt 2
**User Question:** How can I create a number input with currency formatting and custom step controls?

**Agent Answer:**
References:
For more advanced usage of ModusNumberInput, we can leverage:
- `currency` property to display monetary values
- `locale` property to format according to regional standards
- `text-align="right"` for better readability of numbers
- Custom validation for specific business rules

This example demonstrates a price input with currency formatting that restricts to increment or decrements of 0.25:

```html
<div id="price-input-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; max-width: 400px;">
  <h4>Product Price Configuration</h4>
  
  <modus-number-input
    id="price-input"
    label="Product Price"
    currency="USD"
    locale="en-US"
    min-value="0.00"
    step="0.25"
    text-align="right"
    value="24.99"
    helper-text="Price will be adjusted in $0.25 increments">
  </modus-number-input>
  
  <div style="display: flex; gap: 8px; margin-top: 8px;">
    <modus-button id="decrease-btn" size="small">
      -$0.25
    </modus-button>
    
    <modus-button id="increase-btn" color="primary" size="small">
      +$0.25
    </modus-button>
  </div>
  
  <div id="total-display" style="margin-top: 16px; padding: 12px; border: 1px solid #eee; border-radius: 4px;">
    <div style="display: flex; justify-content: space-between;">
      <span>Base Price:</span>
      <span id="base-price">$24.99</span>
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: 8px;">
      <span>Tax (8%):</span>
      <span id="tax-amount">$2.00</span>
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: 8px; font-weight: bold; border-top: 1px solid #eee; padding-top: 8px;">
      <span>Total Price:</span>
      <span id="total-price">$26.99</span>
    </div>
  </div>
</div>
```

```typescript
const priceInput: any = document.querySelector('#price-input');
const decreaseBtn = document.querySelector('#decrease-btn');
const increaseBtn = document.querySelector('#increase-btn');
const basePrice = document.querySelector('#base-price');
const taxAmount = document.querySelector('#tax-amount');
const totalPrice = document.querySelector('#total-price');

// Tax rate (8%)
const TAX_RATE = 0.08;
// Increment/decrement step
const STEP = 0.25;

// Helper function to format currency
function formatCurrency(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(value);
}

// Helper function to update the displayed totals
function updateTotals(price: number): void {
  if (isNaN(price) || price < 0) price = 0;
  
  const tax = price * TAX_RATE;
  const total = price + tax;
  
  if (basePrice) basePrice.textContent = formatCurrency(price);
  if (taxAmount) taxAmount.textContent = formatCurrency(tax);
  if (totalPrice) totalPrice.textContent = formatCurrency(total);
}

// Initialize with default value
if (priceInput) {
  // Get initial value and update totals
  const initialValue = parseFloat(priceInput.value || '0');
  updateTotals(initialValue);
  
  // Handle value change
  priceInput.addEventListener('valueChange', (event: any) => {
    const newValue = parseFloat(event.detail);
    
    // Ensure value is valid
    if (!isNaN(newValue)) {
      // Round to nearest step (0.25)
      const roundedValue = Math.round(newValue / STEP) * STEP;
      
      // Update totals
      updateTotals(roundedValue);
      
      // Update input if rounding changed the value
      if (roundedValue !== newValue) {
        priceInput.value = roundedValue.toString();
      }
    }
  });
}

// Handle manual increment/decrement buttons
if (decreaseBtn) {
  decreaseBtn.addEventListener('buttonClick', () => {
    if (!priceInput) return;
    
    // Get current value
    const currentValue = parseFloat(priceInput.value || '0');
    if (isNaN(currentValue)) return;
    
    // Calculate new value (minimum 0)
    const newValue = Math.max(0, currentValue - STEP);
    
    // Update input and totals
    priceInput.value = newValue.toString();
    updateTotals(newValue);
  });
}

if (increaseBtn) {
  increaseBtn.addEventListener('buttonClick', () => {
    if (!priceInput) return;
    
    // Get current value
    const currentValue = parseFloat(priceInput.value || '0');
    if (isNaN(currentValue)) return;
    
    // Calculate new value 
    const newValue = currentValue + STEP;
    
    // Update input and totals
    priceInput.value = newValue.toString();
    updateTotals(newValue);
  });
}
```

## Prompt 3
**User Question:** How can I implement a quantity selector with increment/decrement buttons and stock validation?

**Agent Answer:**
References:
This implementation combines ModusNumberInput with custom buttons to create a quantity selector often seen in e-commerce applications. Key features:
- Custom increment/decrement buttons for intuitive interaction
- Real-time validation against available stock
- Disabled state when stock is unavailable
- Visual feedback for valid/invalid selections

```html
<div id="product-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; gap: 16px;">
    <div style="width: 80px; height: 80px; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center;">
      <span>Product</span>
    </div>
    
    <div style="flex-grow: 1;">
      <h4 style="margin: 0 0 8px 0;">Premium Widget</h4>
      <div style="color: #666; font-size: 14px;">SKU: WDG-123</div>
      <div id="stock-status" style="color: #008744; font-size: 14px; margin-top: 4px;">
        In Stock: 10 units
      </div>
    </div>
  </div>
  
  <div style="display: flex; align-items: flex-end; gap: 8px;">
    <div style="display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px;">
      <modus-button 
        id="decrement-btn" 
        button-style="borderless"
        size="small"
        icon="remove"
        aria-label="Decrease quantity">
      </modus-button>
      
      <modus-number-input
        id="quantity-input"
        value="1"
        min-value="1"
        max-value="10"
        step="1"
        style="width: 80px; margin: 0 4px;"
        text-align="center">
      </modus-number-input>
      
      <modus-button 
        id="increment-btn" 
        button-style="borderless"
        size="small"
        icon="add"
        aria-label="Increase quantity">
      </modus-button>
    </div>
    
    <modus-button 
      id="add-to-cart-btn" 
      color="primary">
      Add to Cart
    </modus-button>
  </div>
  
  <div id="feedback-message" style="font-size: 14px;"></div>
</div>
```

```typescript
// Configuration
const AVAILABLE_STOCK = 10;

// Get references to components
const quantityInput: any = document.querySelector('#quantity-input');
const decrementBtn = document.querySelector('#decrement-btn');
const incrementBtn = document.querySelector('#increment-btn');
const addToCartBtn = document.querySelector('#add-to-cart-btn');
const stockStatus = document.querySelector('#stock-status');
const feedbackMessage = document.querySelector('#feedback-message');

// Helper function to update UI based on selected quantity
function updateQuantityUI(quantity: number): void {
  if (isNaN(quantity) || quantity < 1) quantity = 1;
  
  // Update buttons state
  if (decrementBtn) {
    if (quantity <= 1) {
      decrementBtn.setAttribute('disabled', 'true');
    } else {
      decrementBtn.removeAttribute('disabled');
    }
  }
  
  if (incrementBtn) {
    if (quantity >= AVAILABLE_STOCK) {
      incrementBtn.setAttribute('disabled', 'true');
    } else {
      incrementBtn.removeAttribute('disabled');
    }
  }
  
  // Update feedback message
  if (feedbackMessage) {
    if (quantity === 1) {
      feedbackMessage.textContent = 'Minimum quantity: 1';
      feedbackMessage.style.color = '#666';
    } else if (quantity === AVAILABLE_STOCK) {
      feedbackMessage.textContent = 'Maximum quantity reached';
      feedbackMessage.style.color = '#d9363e';
    } else {
      feedbackMessage.textContent = '';
    }
  }
  
  // Format stock status display
  if (stockStatus) {
    if (AVAILABLE_STOCK > 5) {
      stockStatus.textContent = `In Stock: ${AVAILABLE_STOCK} units`;
      stockStatus.style.color = '#008744';
    } else if (AVAILABLE_STOCK > 0) {
      stockStatus.textContent = `Low Stock: ${AVAILABLE_STOCK} units`;
      stockStatus.style.color = '#ff9e00';
    } else {
      stockStatus.textContent = 'Out of Stock';
      stockStatus.style.color = '#d9363e';
    }
  }
}

// Initialize UI
if (quantityInput) {
  const initialQuantity = parseInt(quantityInput.value || '1');
  updateQuantityUI(initialQuantity);
  
  // Handle value change
  quantityInput.addEventListener('valueChange', (event: any) => {
    const newQuantity = parseInt(event.detail);
    
    // Validate quantity
    if (isNaN(newQuantity) || newQuantity < 1) {
      quantityInput.value = '1';
      updateQuantityUI(1);
    } else if (newQuantity > AVAILABLE_STOCK) {
      quantityInput.value = AVAILABLE_STOCK.toString();
      updateQuantityUI(AVAILABLE_STOCK);
    } else {
      updateQuantityUI(newQuantity);
    }
  });
}

// Handle decrement button click
if (decrementBtn) {
  decrementBtn.addEventListener('buttonClick', () => {
    if (!quantityInput) return;
    
    const currentQuantity = parseInt(quantityInput.value || '1');
    if (isNaN(currentQuantity) || currentQuantity <= 1) return;
    
    const newQuantity = currentQuantity - 1;
    quantityInput.value = newQuantity.toString();
    updateQuantityUI(newQuantity);
  });
}

// Handle increment button click
if (incrementBtn) {
  incrementBtn.addEventListener('buttonClick', () => {
    if (!quantityInput) return;
    
    const currentQuantity = parseInt(quantityInput.value || '1');
    if (isNaN(currentQuantity) || currentQuantity >= AVAILABLE_STOCK) return;
    
    const newQuantity = currentQuantity + 1;
    quantityInput.value = newQuantity.toString();
    updateQuantityUI(newQuantity);
  });
}

// Handle add to cart button click
if (addToCartBtn) {
  addToCartBtn.addEventListener('buttonClick', () => {
    if (!quantityInput) return;
    
    const quantity = parseInt(quantityInput.value || '1');
    if (isNaN(quantity) || quantity < 1 || quantity > AVAILABLE_STOCK) {
      if (feedbackMessage) {
        feedbackMessage.textContent = 'Invalid quantity selected';
        feedbackMessage.style.color = '#d9363e';
      }
      return;
    }
    
    // Simulate adding to cart
    if (feedbackMessage) {
      feedbackMessage.textContent = `Added ${quantity} item(s) to cart`;
      feedbackMessage.style.color = '#008744';
    }
    
    // In a real application, you would call your cart service here
    console.log(`Adding ${quantity} items to cart`);
  });
}
```

# <ModusPagination>

## Prompt 1
**User Question:** How do I implement basic pagination in my application?

**Agent Answer:**
References:
I've analyzed the ModusPagination component and its key properties. The most essential properties are `activePage`, `maxPage`, and `minPage` which control the pagination behavior. The `size` property allows you to adjust the visual appearance based on your UI requirements.

For this implementation, I'm setting up a standard medium-sized pagination element with basic navigation functionality. The component displays page numbers and provides navigation controls to move between pages.

```html
<div id="pagination-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-pagination 
    id="basic-pagination"
    active-page="3" 
    min-page="1" 
    max-page="10" 
    size="medium">
  </modus-pagination>
</div>
```

```typescript
const paginationElement = document.querySelector('#basic-pagination');
if (paginationElement) {
  paginationElement.addEventListener('pageChange', (event: CustomEvent) => {
    const newPageNumber = event.detail;
    console.log(`Page changed to: ${newPageNumber}`);
    
    // Here you would typically load data for the new page
    // loadPageData(newPageNumber);
  });
}
```

## Prompt 2
**User Question:** How do I customize the pagination controls with text buttons instead of icons?

**Agent Answer:**
References:
The ModusPagination component allows you to replace the default icon navigation controls with text buttons using the `prev-page-button-text` and `next-page-button-text` properties. This is useful when you want more explicit navigation labels or need to provide localized text for better accessibility.

In this implementation, I'm configuring the pagination component to use custom text labels "Previous" and "Next" instead of the default icons, while maintaining all the core pagination functionality.

```html
<div id="custom-pagination-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-pagination 
    id="custom-pagination"
    active-page="5" 
    min-page="1" 
    max-page="20" 
    prev-page-button-text="Previous" 
    next-page-button-text="Next"
    size="large">
  </modus-pagination>
</div>
```

```typescript
const customPagination = document.querySelector('#custom-pagination');
if (customPagination) {
  // Track the current page for application state management
  let currentPage = 5;
  
  customPagination.addEventListener('pageChange', (event: CustomEvent) => {
    currentPage = event.detail;
    console.log(`Navigated to page ${currentPage}`);
    
    // Update your view with the content for the new page
    updatePageContent(currentPage);
  });
}

function updatePageContent(page: number) {
  // Example function that would update your page content
  // fetchDataForPage(page).then(data => renderContent(data));
}
```


# <ModusProgressBar>

## Prompt 1
**User Question:** How do I implement a basic progress bar with percentage display?

**Agent Answer:**
References:
I've analyzed the ModusProgressBar component properties to create a standard determinate progress bar. The key properties being used are `value`, `min-value`, and `max-value` to control the progress state, along with the `text` property to display the percentage completion.

This implementation demonstrates a standard progress bar that visually represents completion progress with a percentage indicator. The progress bar will calculate the percentage based on the current value relative to the min and max values.

```html
<div id="progress-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 100%; max-width: 500px;">
  <modus-progress-bar
    id="percent-progress-bar"
    value="75"
    min-value="0"
    max-value="100"
    text="75%">
  </modus-progress-bar>
</div>
```

```typescript
const progressBar = document.querySelector('#percent-progress-bar');

// Example of how you might update the progress programmatically
function updateProgress(newValue) {
  if (progressBar) {
    const maxValue = parseInt(progressBar.getAttribute('max-value') || '100');
    const percentage = Math.round((newValue / maxValue) * 100);
    
    progressBar.setAttribute('value', newValue.toString());
    progressBar.setAttribute('text', `${percentage}%`);
  }
}

// Example usage:
// setTimeout(() => updateProgress(90), 2000);
```

## Prompt 2
**User Question:** How do I create an indeterminate progress bar for processes with unknown completion times?

**Agent Answer:**
References:
When dealing with processes where the completion time or progress percentage can't be determined, the indeterminate mode of ModusProgressBar is most appropriate. This creates an animated progress indicator that shows activity without showing specific progress.

The implementation below shows how to create an indeterminate progress bar using the `mode` property set to "indeterminate". This removes the need to manage progress values manually and provides visual feedback that a process is ongoing.

```html
<div id="indeterminate-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 100%; max-width: 500px;">
  <h3>Loading Data...</h3>
  <modus-progress-bar
    id="indeterminate-progress"
    mode="indeterminate"
    aria-label="Loading data">
  </modus-progress-bar>
</div>
```

```typescript
const indeterminateProgress = document.querySelector('#indeterminate-progress');

// Example of how you might toggle the visibility based on loading state
function toggleLoading(isLoading) {
  const container = document.querySelector('#indeterminate-container');
  if (container) {
    container.style.display = isLoading ? 'flex' : 'none';
  }
}

// Example usage:
// toggleLoading(true);  // Show when starting a process
// setTimeout(() => toggleLoading(false), 3000);  // Hide when complete
```


# <ModusRadioGroup>

## Prompt 1
**User Question:** How do I create a simple radio button group with multiple options?

**Agent Answer:**
References:
I've analyzed the ModusRadioGroup component and determined that the essential properties are `name`, `checked-id`, and `radioButtons`. The radio buttons are provided as an array of objects with each button having properties like `id`, `label`, and optional `checked` and `disabled` states.

This implementation demonstrates a basic radio group with three options where one option is pre-selected. The `buttonClick` event is used to handle selection changes.

```html
<div id="radio-group-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Select an option:</h3>
  <modus-radio-group 
    id="simple-radio-group"
    name="options-group" 
    checked-id="option2">
  </modus-radio-group>
</div>
```

```typescript
const radioGroup = document.querySelector('#simple-radio-group');
if (radioGroup) {
  // Configure the radio buttons
  radioGroup.radioButtons = [
    {
      id: 'option1',
      label: 'Option 1'
    },
    {
      id: 'option2',
      label: 'Option 2',
      checked: true
    },
    {
      id: 'option3',
      label: 'Option 3'
    }
  ];

  // Handle selection changes
  radioGroup.addEventListener('buttonClick', (event: CustomEvent) => {
    const selectedButton = event.detail;
    console.log('Selected option:', selectedButton);
    
    // Here you would typically handle the selected option
    // handleOptionSelection(selectedButton.id);
  });
}
```

## Prompt 2
**User Question:** How do I create a radio group with some disabled options and handle selection changes?

**Agent Answer:**
References:
For more complex radio group implementations, we can include disabled options and different sizes. In this example, I'm using the `disabled` property on individual radio buttons to prevent selection of specific options, and the `size` property on the group to create a more compact appearance.

The implementation also demonstrates proper handling of the selection event to update your application state based on user choices.

```html
<div id="advanced-radio-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Service Tier Selection:</h3>
  <modus-radio-group 
    id="service-tier-group"
    name="service-tiers" 
    checked-id="standard"
    size="small">
  </modus-radio-group>
  <div id="selected-tier-info" style="margin-top: 12px; padding: 8px; border: 1px solid #ccc; border-radius: 4px;"></div>
</div>
```

```typescript
// Configure the radio group for service tier selection
const serviceTierGroup = document.querySelector('#service-tier-group');
const tierInfoElement = document.querySelector('#selected-tier-info');

if (serviceTierGroup) {
  // Set up the radio buttons with some disabled options
  serviceTierGroup.radioButtons = [
    {
      id: 'basic',
      label: 'Basic Tier'
    },
    {
      id: 'standard',
      label: 'Standard Tier',
      checked: true
    },
    {
      id: 'premium',
      label: 'Premium Tier'
    },
    {
      id: 'enterprise',
      label: 'Enterprise Tier',
      disabled: true // Option not available for selection
    }
  ];

  // Handle selection changes and update the UI
  serviceTierGroup.addEventListener('buttonClick', (event: CustomEvent) => {
    const selectedTier = event.detail;
    
    if (tierInfoElement) {
      // Update the display with information about the selected tier
      switch(selectedTier.id) {
        case 'basic':
          tierInfoElement.textContent = 'Basic Tier: Includes essential features for individuals.';
          break;
        case 'standard':
          tierInfoElement.textContent = 'Standard Tier: Recommended for small teams with additional collaboration tools.';
          break;
        case 'premium':
          tierInfoElement.textContent = 'Premium Tier: Full feature set with advanced analytics and priority support.';
          break;
        default:
          tierInfoElement.textContent = 'Please select a service tier.';
      }
    }
  });
  
  // Trigger initial display
  if (tierInfoElement) {
    tierInfoElement.textContent = 'Standard Tier: Recommended for small teams with additional collaboration tools.';
  }
}
```





# <ModusSelect>

## Prompt 1
**User Question:** How do I create a basic select dropdown with a list of options?

**Agent Answer:**
References:
I've analyzed the ModusSelect component and found that the most important properties are `options`, `optionsDisplayProp`, and handling the `valueChange` event. The component needs to be provided with an array of option objects and needs to know which property to display.

The implementation below demonstrates a simple select dropdown with a list of options. When a user selects an option, the `valueChange` event fires and we update the component's value accordingly.

```html
<div id="select-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 300px;">
  <modus-select 
    id="basic-select" 
    label="Select Country" 
    options-display-prop="name">
  </modus-select>
  <div id="selection-result" style="margin-top: 8px;"></div>
</div>
```

```typescript
const selectElement = document.querySelector('#basic-select');
const resultElement = document.querySelector('#selection-result');

if (selectElement) {
  // Define the options for the select dropdown
  const countries = [
    { id: 1, name: 'United States' },
    { id: 2, name: 'Canada' },
    { id: 3, name: 'United Kingdom' },
    { id: 4, name: 'Australia' },
    { id: 5, name: 'Germany' }
  ];
  
  // Set the options to the select component
  selectElement.options = countries;
  
  // Handle selection changes
  selectElement.addEventListener('valueChange', (event: CustomEvent) => {
    const selectedOption = event.detail;
    selectElement.value = selectedOption;
    
    if (resultElement) {
      resultElement.textContent = `Selected: ${selectedOption.name} (ID: ${selectedOption.id})`;
    }
  });
}
```

## Prompt 2
**User Question:** How do I implement a select dropdown with validation and helper text?

**Agent Answer:**
References:
For more advanced usage, ModusSelect supports validation states with error and helper text. This implementation demonstrates how to create a select dropdown with form validation features including required field validation, helper text for guidance, and error messages when validation fails.

I'm using the `required`, `helperText`, and `errorText` properties to enhance the user experience and provide clear feedback during form interaction.

```html
<div id="validation-select-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 300px;">
  <modus-select 
    id="product-category-select" 
    label="Product Category" 
    options-display-prop="categoryName"
    helper-text="Select the category for your product"
    required
    size="large">
  </modus-select>
  
  <button id="submit-button" style="margin-top: 16px; padding: 8px 16px;">Submit</button>
</div>
```

```typescript
const categorySelect = document.querySelector('#product-category-select');
const submitButton = document.querySelector('#submit-button');

if (categorySelect && submitButton) {
  // Define the product categories
  const productCategories = [
    { id: 'electronics', categoryName: 'Electronics' },
    { id: 'clothing', categoryName: 'Clothing' },
    { id: 'home', categoryName: 'Home & Kitchen' },
    { id: 'books', categoryName: 'Books' },
    { id: 'sports', categoryName: 'Sports & Outdoors' }
  ];
  
  // Set the options to the select component
  categorySelect.options = productCategories;
  
  // Handle selection changes
  categorySelect.addEventListener('valueChange', (event: CustomEvent) => {
    const selectedCategory = event.detail;
    categorySelect.value = selectedCategory;
    
    // Clear any error messages when user selects a value
    categorySelect.setAttribute('error-text', '');
  });
  
  // Handle form submission with validation
  submitButton.addEventListener('click', () => {
    if (!categorySelect.value) {
      // Show error if no category is selected
      categorySelect.setAttribute('error-text', 'Please select a category');
    } else {
      // Process the form with the selected category
      console.log('Form submitted with category:', categorySelect.value);
      
      // Show success message
      categorySelect.setAttribute('error-text', '');
      categorySelect.setAttribute('valid-text', 'Category selected successfully!');
      
      // Reset validation state after a delay
      setTimeout(() => {
        categorySelect.setAttribute('valid-text', '');
      }, 3000);
    }
  });
}
```





# <ModusSentimentScale>

## Prompt 1
**User Question:** How do I implement a thumbs up/down feedback component?

**Agent Answer:**
References:
The ModusSentimentScale component provides an easy way to collect binary feedback using thumbs up/down icons. For this implementation, I'm using the `type="thumbs"` property to specify the thumbs up/down icons and handling the `sentimentSelection` event to capture the user's feedback choice.

This implementation demonstrates how to add a simple thumbs up/down feedback mechanism to your application and handle the user's selection.

```html
<div id="feedback-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Was this article helpful?</h3>
  <modus-sentiment-scale 
    id="thumbs-feedback" 
    type="thumbs">
  </modus-sentiment-scale>
  <div id="feedback-response" style="margin-top: 12px; min-height: 20px;"></div>
</div>
```

```typescript
const thumbsFeedback = document.querySelector('#thumbs-feedback');
const feedbackResponse = document.querySelector('#feedback-response');

if (thumbsFeedback) {
  thumbsFeedback.addEventListener('sentimentSelection', (event: CustomEvent) => {
    const selectedSentiment = event.detail;
    console.log('User feedback:', selectedSentiment);
    
    if (feedbackResponse) {
      if (selectedSentiment === 'thumbs-up') {
        feedbackResponse.textContent = 'Thank you for your positive feedback!';
      } else if (selectedSentiment === 'thumbs-down') {
        feedbackResponse.textContent = 'We're sorry to hear that. How can we improve?';
      }
    }
    
    // Here you might also want to send the feedback to your backend
    // sendFeedbackToServer(selectedSentiment);
  });
}
```

## Prompt 2
**User Question:** How do I create a more detailed sentiment scale with smiley icons?

**Agent Answer:**
References:
For more nuanced feedback collection, the ModusSentimentScale component offers a `type="smileys"` option that provides five different sentiment levels using smiley icons. This implementation demonstrates how to use the smiley-based sentiment scale to gather detailed user satisfaction feedback.

The example below shows how to implement the smiley sentiment scale and process the more nuanced feedback options it provides.

```html
<div id="satisfaction-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Rate your experience:</h3>
  <modus-sentiment-scale 
    id="satisfaction-scale" 
    type="smileys">
  </modus-sentiment-scale>
  <div id="satisfaction-level" style="margin-top: 12px;"></div>
  <div id="follow-up-question" style="margin-top: 12px; display: none;">
    <textarea id="feedback-text" placeholder="Please tell us more about your experience..." 
      style="width: 100%; min-height: 80px; padding: 8px;"></textarea>
    <button id="submit-feedback" style="margin-top: 8px; padding: 6px 12px;">Submit Feedback</button>
  </div>
</div>
```

```typescript
const satisfactionScale = document.querySelector('#satisfaction-scale');
const satisfactionLevel = document.querySelector('#satisfaction-level');
const followUpQuestion = document.querySelector('#follow-up-question');
const submitFeedback = document.querySelector('#submit-feedback');
const feedbackText = document.querySelector('#feedback-text') as HTMLTextAreaElement;

let currentSentiment = '';

if (satisfactionScale && satisfactionLevel && followUpQuestion) {
  satisfactionScale.addEventListener('sentimentSelection', (event: CustomEvent) => {
    const selectedSentiment = event.detail;
    currentSentiment = selectedSentiment;
    
    // Display appropriate message based on the sentiment level
    let message = '';
    switch(selectedSentiment) {
      case 'smiley-satisfied':
        message = 'Excellent! We\'re glad you\'re very satisfied.';
        break;
      case 'smiley-somewhat-satisfied':
        message = 'Good! You seem mostly satisfied.';
        break;
      case 'smiley-neutral':
        message = 'Thanks for your feedback. Your experience was neutral.';
        break;
      case 'smiley-somewhat-dissatisfied':
        message = 'We apologize that your experience wasn\'t better.';
        break;
      case 'smiley-dissatisfied':
        message = 'We\'re sorry you had a negative experience.';
        break;
    }
    
    if (satisfactionLevel) {
      satisfactionLevel.textContent = message;
    }
    
    // Show follow-up question for more detailed feedback
    followUpQuestion.style.display = 'block';
  });
  
  if (submitFeedback) {
    submitFeedback.addEventListener('click', () => {
      if (feedbackText && feedbackText.value) {
        console.log('Sentiment:', currentSentiment);
        console.log('Detailed feedback:', feedbackText.value);
        
        // Here you would typically send the feedback to your server
        // sendDetailedFeedback(currentSentiment, feedbackText.value);
        
        // Show confirmation and reset
        satisfactionLevel.textContent = 'Thank you for your detailed feedback!';
        followUpQuestion.style.display = 'none';
        feedbackText.value = '';
      }
    });
  }
}
```





# <ModusSideNavigation>

## Prompt 1
**User Question:** How do I create a basic side navigation menu with icons and expandable items?

**Agent Answer:**
References:
The ModusSideNavigation component provides a collapsible side panel for navigation. Key features include:
- Expandable/collapsible panel using the `expanded` property
- Icon support for menu items through the `menuIcon` property
- Support for nested items using child elements
- Ability to handle click events and track selected items

Here's an implementation of a basic side navigation with icons and expandable sections:

```html
<div id="app-container" style="display: flex; height: 100vh;">
  <modus-side-navigation 
    id="main-sidenav" 
    max-width="300px" 
    target-content="#main-content">
    
    <!-- Home Menu Item -->
    <modus-side-navigation-item 
      id="home-menu" 
      label="Home">
      <modus-icon name="home" size="24" slot="menu-icon"></modus-icon>
    </modus-side-navigation-item>
    
    <!-- Projects Menu Item (Expandable) -->
    <modus-side-navigation-item 
      id="projects-menu" 
      label="Projects"
      show-expand-icon>
      <modus-icon name="folder" size="24" slot="menu-icon"></modus-icon>
      
      <!-- Nested Items -->
      <modus-side-navigation-item 
        id="active-projects" 
        label="Active Projects">
      </modus-side-navigation-item>
      <modus-side-navigation-item 
        id="archived-projects" 
        label="Archived Projects">
      </modus-side-navigation-item>
    </modus-side-navigation-item>
    
    <!-- Reports Menu Item -->
    <modus-side-navigation-item 
      id="reports-menu" 
      label="Reports">
      <modus-icon name="bar_chart" size="24" slot="menu-icon"></modus-icon>
    </modus-side-navigation-item>
    
    <!-- Settings Menu Item -->
    <modus-side-navigation-item 
      id="settings-menu" 
      label="Settings">
      <modus-icon name="settings" size="24" slot="menu-icon"></modus-icon>
    </modus-side-navigation-item>
  </modus-side-navigation>

  <div id="main-content" style="flex: 1; padding: 20px;">
    <h1 id="page-title">Welcome to the Dashboard</h1>
    <div id="page-content">Select a menu item to navigate</div>
  </div>
</div>
```

```typescript
const sideNav = document.querySelector('#main-sidenav');
const pageTitle = document.querySelector('#page-title');
const pageContent = document.querySelector('#page-content');

if (sideNav) {
  // Handle item selection
  sideNav.addEventListener('sideNavItemClicked', (event: CustomEvent) => {
    const { id, selected } = event.detail;
    
    if (selected && pageTitle && pageContent) {
      // Update page content based on selection
      switch (id) {
        case 'home-menu':
          pageTitle.textContent = 'Home';
          pageContent.textContent = 'Welcome to the home page';
          break;
        case 'projects-menu':
          pageTitle.textContent = 'Projects';
          pageContent.textContent = 'View and manage your projects';
          break;
        case 'active-projects':
          pageTitle.textContent = 'Active Projects';
          pageContent.textContent = 'Currently active projects';
          break;
        case 'archived-projects':
          pageTitle.textContent = 'Archived Projects';
          pageContent.textContent = 'Previously completed projects';
          break;
        case 'reports-menu':
          pageTitle.textContent = 'Reports';
          pageContent.textContent = 'View analytics and reports';
          break;
        case 'settings-menu':
          pageTitle.textContent = 'Settings';
          pageContent.textContent = 'Configure application settings';
          break;
      }
    }
  });
  
  // Track expansion state
  sideNav.addEventListener('sideNavExpand', (event: CustomEvent) => {
    const isExpanded = event.detail;
    console.log(`Side navigation is now ${isExpanded ? 'expanded' : 'collapsed'}`);
  });
}
```

## Prompt 2
**User Question:** How do I implement a side navigation with dynamic data and header dropdown features?

**Agent Answer:**
References:
For more advanced usage of ModusSideNavigation, we can use the `data` property to dynamically populate items and leverage the header dropdown feature. This implementation demonstrates:
- Using the `data` property for dynamic menu items
- Header dropdown functionality with `isHeader`
- Different navigation modes (overlay/push)
- Theme customization

```html
<div style="width: 100%; min-height: 500px;">
  <!-- Theme and Mode Controls -->
  <div style="margin-bottom: 16px;">
    <modus-switch id="theme-switch" label="Enable Blue Theme"></modus-switch>
    <modus-switch id="mode-switch" label="Toggle Push Mode" style="margin-left: 16px;"></modus-switch>
  </div>
  
  <!-- Main Container -->
  <div id="app-layout" style="display: flex; min-height: 500px; position: relative;">
    <modus-side-navigation 
      id="dynamic-sidenav"
      max-width="300px"
      target-content="#dynamic-content"
      mode="overlay">
    </modus-side-navigation>

    <div id="dynamic-content" style="flex: 1; padding: 20px;">
      <h2 id="section-title">Welcome</h2>
      <p id="section-description">Select a menu item to begin</p>
    </div>
  </div>
</div>
```

```typescript
const dynamicSidenav = document.querySelector('#dynamic-sidenav');
const sectionTitle = document.querySelector('#section-title');
const sectionDescription = document.querySelector('#section-description');
const themeSwitch = document.querySelector('#theme-switch');
const modeSwitch = document.querySelector('#mode-switch');

// Define navigation data structure
const navigationData = [
  {
    id: 'dashboard',
    label: 'Dashboard',
    menuIcon: 'dashboard',
    isHeader: {
      enabled: true,
      items: [
        {
          id: 'overview',
          label: 'Overview',
          icon: 'bar_chart'
        },
        {
          id: 'analytics',
          label: 'Analytics',
          icon: 'analytics'
        }
      ]
    }
  },
  {
    id: 'projects',
    label: 'Projects',
    menuIcon: 'folder',
    children: [
      {
        id: 'current',
        label: 'Current Projects',
        menuIcon: 'folder_open'
      },
      {
        id: 'archived',
        label: 'Archived Projects',
        menuIcon: 'folder_closed'
      }
    ]
  },
  {
    id: 'resources',
    label: 'Resources',
    menuIcon: 'library_books'
  },
  {
    id: 'settings',
    label: 'Settings',
    menuIcon: 'settings',
    disabled: false
  }
];

// Custom theme styles
const blueTheme = `
  --modus-side-navigation-link-color: #ffffff;
  --modus-side-navigation-bg: #0e416c;
  --modus-side-navigation-item-color: #ffffff;
  --modus-side-navigation-item-active-bg: #217cbb;
  --modus-side-navigation-item-hover-bg: #0063a3;
  --modus-side-navigation-item-icon-color: #ffffff;
  --modus-side-navigation-item-chevron-color: #ffffff;
  --modus-side-navigation-item-icon-filter: invert(100%) sepia(0%) saturate(24%) hue-rotate(114deg) brightness(108%) contrast(108%);
`;

if (dynamicSidenav) {
  // Initialize with data
  dynamicSidenav.data = navigationData;
  
  // Handle item selection
  dynamicSidenav.addEventListener('sideNavItemClicked', (event: CustomEvent) => {
    const { id, selected } = event.detail;
    
    if (selected && sectionTitle && sectionDescription) {
      updateContent(id);
    }
  });
  
  // Handle header dropdown selection
  dynamicSidenav.addEventListener('sideNavItemHeaderClicked', (event: CustomEvent) => {
    const { id, selected } = event.detail;
    
    if (selected && sectionTitle && sectionDescription) {
      updateContent(id, true);
    }
  });
}

// Handle theme switching
if (themeSwitch) {
  themeSwitch.addEventListener('switchClick', (event: CustomEvent) => {
    if (dynamicSidenav) {
      dynamicSidenav.style = event.detail ? blueTheme : '';
    }
  });
}

// Handle mode switching
if (modeSwitch) {
  modeSwitch.addEventListener('switchClick', (event: CustomEvent) => {
    if (dynamicSidenav) {
      dynamicSidenav.mode = event.detail ? 'push' : 'overlay';
    }
  });
}

function updateContent(id: string, isHeaderItem: boolean = false) {
  if (!sectionTitle || !sectionDescription) return;
  
  const contentMap: { [key: string]: { title: string, description: string } } = {
    dashboard: {
      title: 'Dashboard',
      description: 'Main dashboard overview'
    },
    overview: {
      title: 'Dashboard Overview',
      description: 'High-level metrics and KPIs'
    },
    analytics: {
      title: 'Analytics Dashboard',
      description: 'Detailed analytics and insights'
    },
    projects: {
      title: 'Projects',
      description: 'View and manage all projects'
    },
    current: {
      title: 'Current Projects',
      description: 'Active and ongoing projects'
    },
    archived: {
      title: 'Archived Projects',
      description: 'Completed and archived projects'
    },
    resources: {
      title: 'Resources',
      description: 'Access documentation and resources'
    },
    settings: {
      title: 'Settings',
      description: 'Configure application settings'
    }
  };
  
  const content = contentMap[id] || { 
    title: 'Not Found', 
    description: 'The requested section was not found' 
  };
  
  sectionTitle.textContent = content.title;
  sectionDescription.textContent = content.description;
}
```




# <ModusSlider>

## Prompt 1
**User Question:** How do I create a basic slider control with a label and value range?

**Agent Answer:**
References:
I'll demonstrate how to implement a ModusSlider component with a label and defined value range. The component supports key features like:
- Custom minimum and maximum values
- Current value binding
- Label for accessibility
- Value change events for real-time updates

Here's an implementation of a basic slider with event handling:

```html
<div id="slider-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 300px;">
  <modus-slider 
    id="range-slider"
    label="Volume Control"
    min-value="0"
    max-value="100"
    value="50"
    aria-label="Adjust volume level">
  </modus-slider>
  
  <div id="value-display" style="text-align: center; font-size: 14px;">
    Current Value: 50
  </div>
</div>
```

```typescript
const slider = document.querySelector('#range-slider');
const valueDisplay = document.querySelector('#value-display');

if (slider) {
  // Handle value changes
  slider.addEventListener('valueChange', (event: CustomEvent) => {
    const newValue = event.detail;
    console.log(`Value changed to: ${newValue}`);
    
    if (valueDisplay) {
      valueDisplay.textContent = `Current Value: ${newValue}`;
    }
  });
  
  // Handle continuous value input (optional)
  slider.addEventListener('valueInput', (event: CustomEvent) => {
    const inputValue = event.detail;
    
    if (valueDisplay) {
      valueDisplay.textContent = `Current Value: ${inputValue}`;
    }
  });
}
```

## Prompt 2
**User Question:** How do I create an interactive slider with custom styling and disabled states?

**Agent Answer:**
References:
This implementation demonstrates more advanced usage of the ModusSlider component, including:
- Multiple sliders for different controls
- Disabled state handling
- Interaction between sliders
- Real-time value synchronization

```html
<div id="advanced-slider-container" style="display: flex; flex-direction: column; gap: 24px; padding: 16px; width: 300px;">
  <!-- Main Volume Control -->
  <div class="slider-group">
    <modus-slider 
      id="master-volume"
      label="Master Volume"
      min-value="0"
      max-value="100"
      value="75"
      aria-label="Adjust master volume">
    </modus-slider>
    <div class="value-label">75%</div>
  </div>
  
  <!-- Channel Controls -->
  <div class="slider-group">
    <modus-slider 
      id="left-channel"
      label="Left Channel"
      min-value="0"
      max-value="100"
      value="75"
      aria-label="Adjust left channel volume">
    </modus-slider>
    <div class="value-label">75%</div>
  </div>
  
  <div class="slider-group">
    <modus-slider 
      id="right-channel"
      label="Right Channel"
      min-value="0"
      max-value="100"
      value="75"
      aria-label="Adjust right channel volume">
    </modus-slider>
    <div class="value-label">75%</div>
  </div>
  
  <!-- Mute Control -->
  <modus-switch 
    id="mute-toggle"
    label="Mute Audio">
  </modus-switch>
</div>

<style>
.slider-group {
  display: flex;
  align-items: center;
  gap: 16px;
}

.value-label {
  min-width: 48px;
  text-align: right;
  font-size: 14px;
}
</style>
```

```typescript
interface SliderControl {
  slider: HTMLElement;
  label: HTMLElement;
  lastValue: number;
}

// Get references to all controls
const masterVolume = document.querySelector('#master-volume');
const leftChannel = document.querySelector('#left-channel');
const rightChannel = document.querySelector('#right-channel');
const muteToggle = document.querySelector('#mute-toggle');

// Store slider references and their associated labels
const sliders: { [key: string]: SliderControl } = {
  master: {
    slider: masterVolume,
    label: masterVolume?.parentElement?.querySelector('.value-label'),
    lastValue: 75
  },
  left: {
    slider: leftChannel,
    label: leftChannel?.parentElement?.querySelector('.value-label'),
    lastValue: 75
  },
  right: {
    slider: rightChannel,
    label: rightChannel?.parentElement?.querySelector('.value-label'),
    lastValue: 75
  }
};

// Update value display for a slider
function updateSliderDisplay(control: SliderControl, value: number) {
  if (control.label) {
    control.label.textContent = `${value}%`;
  }
}

// Handle slider value changes
Object.entries(sliders).forEach(([key, control]) => {
  if (control.slider) {
    control.slider.addEventListener('valueChange', (event: CustomEvent) => {
      const newValue = event.detail;
      control.lastValue = newValue;
      updateSliderDisplay(control, newValue);
      
      // If master volume changes, update channel volumes proportionally
      if (key === 'master') {
        const ratio = newValue / 100;
        Object.entries(sliders).forEach(([channelKey, channelControl]) => {
          if (channelKey !== 'master' && channelControl.slider) {
            const adjustedValue = Math.round(channelControl.lastValue * ratio);
            (channelControl.slider as any).value = adjustedValue;
            updateSliderDisplay(channelControl, adjustedValue);
          }
        });
      }
    });
  }
});

// Handle mute toggle
if (muteToggle) {
  muteToggle.addEventListener('switchClick', (event: CustomEvent) => {
    const isMuted = event.detail;
    
    Object.values(sliders).forEach(control => {
      if (control.slider) {
        if (isMuted) {
          control.lastValue = parseInt((control.slider as any).value);
          (control.slider as any).value = 0;
          (control.slider as any).disabled = true;
          updateSliderDisplay(control, 0);
        } else {
          (control.slider as any).disabled = false;
          (control.slider as any).value = control.lastValue;
          updateSliderDisplay(control, control.lastValue);
        }
      }
    });
  });
}
```


# <ModusSpinner>

## Prompt 1
**User Question:** How do I implement loading spinners with different colors and sizes?

**Agent Answer:**
References:
The ModusSpinner component is used to indicate loading or processing states in your application. Key properties to note:
- `color`: Supports predefined variants (primary, secondary, tertiary) or custom colors
- `size`: Controls the spinner dimensions using CSS size units

This implementation demonstrates different spinner variants and how to integrate them into loading states:

```html
<div id="spinner-container" style="display: flex; flex-direction: column; gap: 24px; padding: 16px;">
  <!-- Basic primary spinner -->
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-spinner id="primary-spinner"></modus-spinner>
    <span>Loading...</span>
  </div>
  
  <!-- Secondary spinner with custom size -->
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-spinner 
      id="secondary-spinner"
      color="secondary"
      size="1.5rem">
    </modus-spinner>
    <span>Processing...</span>
  </div>
  
  <!-- Tertiary spinner -->
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-spinner 
      id="tertiary-spinner"
      color="tertiary"
      size="2.5rem">
    </modus-spinner>
    <span>Please wait...</span>
  </div>
</div>
```

```typescript
const primarySpinner = document.querySelector('#primary-spinner');
const secondarySpinner = document.querySelector('#secondary-spinner');
const tertiarySpinner = document.querySelector('#tertiary-spinner');

// Example of dynamically showing/hiding spinners
function simulateAsyncOperation() {
  // Show spinners
  if (primarySpinner) {
    primarySpinner.style.display = 'inline-block';
  }
  if (secondarySpinner) {
    secondarySpinner.style.display = 'inline-block';
  }
  if (tertiarySpinner) {
    tertiarySpinner.style.display = 'inline-block';
  }
  
  // Simulate async operation and hide spinners after completion
  setTimeout(() => {
    if (primarySpinner) {
      primarySpinner.style.display = 'none';
    }
    if (secondarySpinner) {
      secondarySpinner.style.display = 'none';
    }
    if (tertiarySpinner) {
      tertiarySpinner.style.display = 'none';
    }
  }, 3000);
}
```

## Prompt 2
**User Question:** How can I use the spinner with a custom color and integrate it into a loading button?

**Agent Answer:**
References:
For custom spinner integration, we'll:
1. Use a custom color value
2. Show how to integrate the spinner with a button
3. Demonstrate proper loading state management

This example shows a more practical use case of the spinner within an interactive component:

```html
<div id="custom-spinner-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <!-- Custom colored spinner -->
  <div style="display: flex; align-items: center; gap: 12px;">
    <modus-spinner 
      id="custom-spinner"
      color="#6c47ff"
      size="2rem"
      style="display: none;">
    </modus-spinner>
    <span id="custom-status">Ready</span>
  </div>
  
  <!-- Loading button with integrated spinner -->
  <div style="position: relative; display: inline-block;">
    <modus-button 
      id="action-button"
      color="primary">
      Submit Data
    </modus-button>
    <modus-spinner
      id="button-spinner"
      size="1rem"
      style="display: none; position: absolute; right: 8px; top: 50%; transform: translateY(-50%);">
    </modus-spinner>
  </div>
</div>
```

```typescript
const customSpinner = document.querySelector('#custom-spinner');
const customStatus = document.querySelector('#custom-status');
const actionButton = document.querySelector('#action-button');
const buttonSpinner = document.querySelector('#button-spinner');

// Handle button click and loading state
if (actionButton && buttonSpinner && customSpinner && customStatus) {
  let isLoading = false;
  
  actionButton.addEventListener('buttonClick', async () => {
    if (isLoading) return;
    
    isLoading = true;
    customStatus.textContent = 'Processing...';
    customSpinner.style.display = 'inline-block';
    buttonSpinner.style.display = 'inline-block';
    (actionButton as any).disabled = true;
    
    try {
      // Simulate async operation
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      customStatus.textContent = 'Completed!';
      customStatus.style.color = '#2db67c';
    } catch (error) {
      customStatus.textContent = 'Error occurred';
      customStatus.style.color = '#d9363e';
    } finally {
      isLoading = false;
      customSpinner.style.display = 'none';
      buttonSpinner.style.display = 'none';
      (actionButton as any).disabled = false;
    }
  });
}
```



# <ModusSwitch>

## Prompt 1
**User Question:** How do I create a basic toggle switch with a label and handle state changes?

**Agent Answer:**
References:
I've analyzed the ModusSwitch component and found that the key properties are:
- `checked`: Controls the switch state (on/off)
- `label`: Displays text beside the switch
- `labelPosition`: Places the label on either side of the switch
- `disabled`: Makes the switch non-interactive
The component emits a `switchClick` event when toggled, providing the new state as a boolean.

The implementation below demonstrates a basic switch with a label and state management:

```html
<div id="switch-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <!-- Basic switch with label -->
  <modus-switch 
    id="theme-switch"
    label="Dark Theme"
    label-position="right">
  </modus-switch>
  
  <div id="status-display" style="padding: 8px; border: 1px solid #e0e0e0; border-radius: 4px;">
    Theme: Light
  </div>
</div>
```

```typescript
const themeSwitch = document.querySelector('#theme-switch');
const statusDisplay = document.querySelector('#status-display');

if (themeSwitch) {
  themeSwitch.addEventListener('switchClick', (event: CustomEvent) => {
    const isDarkTheme = event.detail;
    
    console.log('Theme switched:', isDarkTheme ? 'Dark' : 'Light');
    if (statusDisplay) {
      statusDisplay.textContent = `Theme: ${isDarkTheme ? 'Dark' : 'Light'}`;
    }
    
    // Here you would typically apply theme changes to your application
    document.body.style.background = isDarkTheme ? '#333333' : '#ffffff';
    document.body.style.color = isDarkTheme ? '#ffffff' : '#333333';
  });
}
```

## Prompt 2
**User Question:** How do I create multiple switches for different settings with various configurations?

**Agent Answer:**
References:
This example demonstrates using multiple ModusSwitch components for a settings panel. It shows how to:
- Position labels on different sides
- Handle disabled state
- Use switches in a form-like layout
- Track and respond to multiple switch states

```html
<div id="settings-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; width: 300px;">
  <h3 style="margin: 0;">Application Settings</h3>
  
  <!-- Notifications switch -->
  <modus-switch 
    id="notifications-switch"
    label="Enable Notifications"
    label-position="right"
    checked>
  </modus-switch>
  
  <!-- Sound switch -->
  <modus-switch 
    id="sound-switch"
    label="Sound Effects"
    label-position="right">
  </modus-switch>
  
  <!-- Auto-update switch (disabled) -->
  <modus-switch 
    id="auto-update-switch"
    label="Auto Updates"
    label-position="right"
    disabled
    checked>
  </modus-switch>
  
  <!-- Custom position switch -->
  <modus-switch 
    id="custom-switch"
    label="Custom Setting"
    label-position="left">
  </modus-switch>
  
  <!-- Settings summary -->
  <div id="settings-summary" style="margin-top: 8px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px; font-size: 14px;">
    Current Settings:
    <ul style="margin: 8px 0;"></ul>
  </div>
</div>
```

```typescript
interface SettingSwitch {
  id: string;
  element: HTMLElement;
  label: string;
  initialState: boolean;
}

// Get references to all switches
const switches: SettingSwitch[] = [
  {
    id: 'notifications-switch',
    element: document.querySelector('#notifications-switch')!,
    label: 'Notifications',
    initialState: true
  },
  {
    id: 'sound-switch',
    element: document.querySelector('#sound-switch')!,
    label: 'Sound Effects',
    initialState: false
  },
  {
    id: 'auto-update-switch',
    element: document.querySelector('#auto-update-switch')!,
    label: 'Auto Updates',
    initialState: true
  },
  {
    id: 'custom-switch',
    element: document.querySelector('#custom-switch')!,
    label: 'Custom Setting',
    initialState: false
  }
];

const summaryList = document.querySelector('#settings-summary ul');

// Function to update settings summary
function updateSettingsSummary() {
  if (!summaryList) return;
  
  summaryList.innerHTML = switches
    .map(({ label, element }) => {
      const isEnabled = (element as any).checked;
      return `<li>${label}: ${isEnabled ? 'Enabled' : 'Disabled'}</li>`;
    })
    .join('');
}

// Initialize switches and add event listeners
switches.forEach(({ element, initialState }) => {
  if (element) {
    (element as any).checked = initialState;
    
    element.addEventListener('switchClick', (event: CustomEvent) => {
      console.log(`Switch changed: ${event.detail ? 'ON' : 'OFF'}`);
      updateSettingsSummary();
    });
  }
});

// Initial summary update
updateSettingsSummary();
```

Note to keep in mind:
- The `switchClick` event provides a boolean value indicating the new state
- Label positioning affects the overall layout and user experience
- Use disabled state for settings that are not currently available
- Always provide visual feedback when switches are toggled



# <ModusTable>

## Prompt 1
**User Question:** How do I create a basic data table with sorting and pagination?

**Agent Answer:**
References:
I'll demonstrate how to create a ModusTable with essential features including:
- Column definitions with data types
- Sortable columns
- Pagination controls
- Hover effects
- Basic styling

This implementation provides a foundation that can be extended with more advanced features.

```html
<div id="table-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Employee Directory</h3>
  
  <modus-table 
    id="employee-table"
    sort="true"
    pagination="true"
    hover="true">
  </modus-table>
</div>
```

```typescript
const table = document.querySelector('#employee-table');

if (table) {
  // Define columns
  table.columns = [
    {
      header: 'Employee ID',
      accessorKey: 'id',
      id: 'employee-id',
      dataType: 'text',
      size: 100
    },
    {
      header: 'Name',
      accessorKey: 'name',
      id: 'employee-name',
      dataType: 'text',
      size: 200
    },
    {
      header: 'Department',
      accessorKey: 'department',
      id: 'department',
      dataType: 'text',
      size: 150
    },
    {
      header: 'Hire Date',
      accessorKey: 'hireDate',
      id: 'hire-date',
      dataType: 'date',
      size: 120
    },
    {
      header: 'Salary',
      accessorKey: 'salary',
      id: 'salary',
      dataType: 'currency',
      size: 120,
      align: 'right'
    },
    {
      header: 'Status',
      accessorKey: 'status',
      id: 'status',
      dataType: 'badge',
      size: 100
    }
  ];

  // Sample data
  table.data = [
    {
      id: 'EMP001',
      name: 'John Smith',
      department: 'Engineering',
      hireDate: '2023-01-15',
      salary: '$85,000',
      status: { text: 'Active', color: 'success', type: 'text' }
    },
    {
      id: 'EMP002',
      name: 'Jane Doe',
      department: 'Marketing',
      hireDate: '2023-03-22',
      salary: '$72,000',
      status: { text: 'Active', color: 'success', type: 'text' }
    },
    {
      id: 'EMP003',
      name: 'Bob Wilson',
      department: 'Finance',
      hireDate: '2023-02-08',
      salary: '$92,000',
      status: { text: 'On Leave', color: 'warning', type: 'text' }
    },
    {
      id: 'EMP004',
      name: 'Alice Brown',
      department: 'Engineering',
      hireDate: '2023-04-05',
      salary: '$88,000',
      status: { text: 'Active', color: 'success', type: 'text' }
    },
    {
      id: 'EMP005',
      name: 'Charlie Davis',
      department: 'Sales',
      hireDate: '2023-01-30',
      salary: '$78,000',
      status: { text: 'Inactive', color: 'danger', type: 'text' }
    }
  ];

  // Configure pagination
  table.pageSizeList = [5, 10, 25, 50];

  // Handle sort changes
  table.addEventListener('sortChange', (event: CustomEvent) => {
    const { columnId, direction } = event.detail;
    console.log(`Table sorted by ${columnId} in ${direction} direction`);
  });
}
```

## Prompt 2
**User Question:** How do I implement row selection, actions, and custom toolbar features?

**Agent Answer:**
References:
This implementation demonstrates advanced ModusTable features:
- Multi-row selection with checkboxes
- Row actions with custom buttons
- Column visibility management
- Toolbar customization
- Row expandability

```html
<div id="advanced-table-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Project Management</h3>
  
  <modus-table 
    id="projects-table"
    sort="true"
    pagination="true"
    hover="true"
    row-selection="true"
    rows-expandable="true"
    toolbar="true"
    column-resize="true"
    show-sort-icon-on-hover="true">
  </modus-table>
  
  <div id="selection-summary" style="display: none; margin-top: 16px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px;">
    Selected projects: <span id="selected-count">0</span>
  </div>
</div>
```

```typescript
const projectTable = document.querySelector('#projects-table');
const selectionSummary = document.querySelector('#selection-summary');
const selectedCount = document.querySelector('#selected-count');

if (projectTable) {
  // Configure multi-selection
  projectTable.rowSelectionOptions = {
    multiple: true,
    subRowSelection: true
  };

  // Define columns with sub-rows
  projectTable.columns = [
    {
      header: 'Project',
      accessorKey: 'name',
      id: 'project-name',
      dataType: 'text',
      size: 200
    },
    {
      header: 'Manager',
      accessorKey: 'manager',
      id: 'manager',
      dataType: 'text',
      size: 150
    },
    {
      header: 'Progress',
      accessorKey: 'progress',
      id: 'progress',
      dataType: 'text',
      size: 100
    },
    {
      header: 'Due Date',
      accessorKey: 'dueDate',
      id: 'due-date',
      dataType: 'date',
      size: 120
    },
    {
      header: 'Status',
      accessorKey: 'status',
      id: 'status',
      dataType: 'badge',
      size: 100
    }
  ];

  // Configure row actions
  projectTable.rowActions = [
    {
      id: 'edit',
      icon: 'edit',
      label: 'Edit Project',
      tooltipText: 'Edit project details',
      buttonStyle: 'borderless',
      color: 'primary'
    },
    {
      id: 'archive',
      icon: 'archive',
      label: 'Archive Project',
      tooltipText: 'Move to archive',
      buttonStyle: 'borderless',
      color: 'secondary'
    },
    {
      id: 'delete',
      icon: 'delete',
      label: 'Delete Project',
      tooltipText: 'Delete permanently',
      buttonStyle: 'borderless',
      color: 'danger',
      isDisabled: (row) => row.status.text === 'In Progress'
    }
  ];

  // Configure toolbar options
  projectTable.toolbarOptions = {
    columnsVisibility: {
      title: 'Customize Columns',
      requiredColumns: ['project-name'], // Project name cannot be hidden
      hiddenColumns: [] // All columns visible by default
    }
  };

  // Sample data with expandable rows
  projectTable.data = [
    {
      name: 'Website Redesign',
      manager: 'John Smith',
      progress: '75%',
      dueDate: '2023-12-31',
      status: { text: 'In Progress', color: 'primary', type: 'text' },
      subRows: [
        {
          name: 'Homepage Design',
          manager: 'Alice Chen',
          progress: '90%',
          dueDate: '2023-11-30',
          status: { text: 'Review', color: 'warning', type: 'text' }
        },
        {
          name: 'Mobile Optimization',
          manager: 'Bob Wilson',
          progress: '60%',
          dueDate: '2023-12-15',
          status: { text: 'In Progress', color: 'primary', type: 'text' }
        }
      ]
    },
    {
      name: 'API Integration',
      manager: 'Jane Doe',
      progress: '45%',
      dueDate: '2024-01-15',
      status: { text: 'In Progress', color: 'primary', type: 'text' },
      subRows: [
        {
          name: 'Authentication Service',
          manager: 'Mike Johnson',
          progress: '80%',
          dueDate: '2023-12-20',
          status: { text: 'Testing', color: 'info', type: 'text' }
        }
      ]
    }
  ];

  // Event Handlers
  projectTable.addEventListener('rowSelect', (event: CustomEvent) => {
    const selectedRows = event.detail;
    if (selectionSummary && selectedCount) {
      selectionSummary.style.display = selectedRows.length > 0 ? 'block' : 'none';
      selectedCount.textContent = selectedRows.length.toString();
    }
  });

  projectTable.addEventListener('rowActionClick', (event: CustomEvent) => {
    const { id: actionId, rowId } = event.detail;
    console.log(`Action ${actionId} triggered for row ${rowId}`);

    switch (actionId) {
      case 'edit':
        // Handle edit action
        console.log('Opening edit modal...');
        break;
      case 'archive':
        // Handle archive action
        if (confirm('Are you sure you want to archive this project?')) {
          console.log('Archiving project...');
        }
        break;
      case 'delete':
        // Handle delete action
        if (confirm('Are you sure you want to delete this project?')) {
          console.log('Deleting project...');
        }
        break;
    }
  });
}
```

## Prompt 3
**User Question:** How do I implement server-side sorting and pagination with the table?

**Agent Answer:**
References:
This example demonstrates how to implement server-side data management with ModusTable:
- Manual sorting configuration
- Manual pagination setup
- Loading states
- API integration pattern

```html
<div id="server-table-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <h3>Sales Orders</h3>
    <modus-button id="refresh-btn" color="primary" size="small" left-icon="refresh">
      Refresh
    </modus-button>
  </div>
  
  <modus-table 
    id="orders-table"
    sort="true"
    pagination="true"
    hover="true"
    row-selection="true"
    toolbar="true">
  </modus-table>
  
  <!-- Loading overlay -->
  <div id="loading-overlay" style="display: none; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(255,255,255,0.8); align-items: center; justify-content: center;">
    <modus-spinner size="3rem" color="primary"></modus-spinner>
  </div>
</div>
```

```typescript
interface OrdersResponse {
  data: any[];
  total: number;
  pageCount: number;
}

// Table configuration and state management
const ordersTable = document.querySelector('#orders-table');
const refreshButton = document.querySelector('#refresh-btn');
const loadingOverlay = document.querySelector('#loading-overlay');

let currentPage = 0;
const defaultPageSize = 10;

if (ordersTable) {
  // Configure columns
  ordersTable.columns = [
    {
      header: 'Order ID',
      accessorKey: 'id',
      id: 'order-id',
      dataType: 'text',
      size: 100
    },
    {
      header: 'Customer',
      accessorKey: 'customer',
      id: 'customer',
      dataType: 'text',
      size: 200
    },
    {
      header: 'Order Date',
      accessorKey: 'orderDate',
      id: 'order-date',
      dataType: 'date',
      size: 120
    },
    {
      header: 'Amount',
      accessorKey: 'amount',
      id: 'amount',
      dataType: 'currency',
      size: 120,
      align: 'right'
    },
    {
      header: 'Status',
      accessorKey: 'status',
      id: 'status',
      dataType: 'badge',
      size: 100
    }
  ];

  // Configure manual sorting
  ordersTable.manualSortingOptions = {
    currentSortingState: {
      columnId: 'order-date',
      direction: 'desc'
    }
  };

  // Configure manual pagination
  ordersTable.manualPaginationOptions = {
    currentPageIndex: currentPage,
    currentPageSize: defaultPageSize,
    pageCount: 0,
    totalRecords: 0
  };

  // Event handlers
  ordersTable.addEventListener('sortChange', async (event: CustomEvent) => {
    const { columnId, direction } = event.detail;
    if (ordersTable.manualSortingOptions) {
      ordersTable.manualSortingOptions.currentSortingState = { columnId, direction };
    }
    await loadTableData();
  });

  ordersTable.addEventListener('pageChange', async (event: CustomEvent) => {
    const { pageIndex, pageSize } = event.detail;
    currentPage = pageIndex;
    
    if (ordersTable.manualPaginationOptions) {
      ordersTable.manualPaginationOptions.currentPageIndex = pageIndex;
      ordersTable.manualPaginationOptions.currentPageSize = pageSize;
    }
    
    await loadTableData();
  });

  // Load data function
  async function loadTableData() {
    try {
      if (loadingOverlay) {
        loadingOverlay.style.display = 'flex';
      }

      // Get current sort state
      const sortState = ordersTable.manualSortingOptions?.currentSortingState;
      
      // Prepare API parameters
      const params = new URLSearchParams({
        page: currentPage.toString(),
        pageSize: defaultPageSize.toString(),
        sortColumn: sortState?.columnId || 'order-date',
        sortDirection: sortState?.direction || 'desc'
      });

      // Simulate API call
      const response: OrdersResponse = await simulateApiCall(params);
      
      // Update table data and pagination info
      ordersTable.data = response.data;
      
      if (ordersTable.manualPaginationOptions) {
        ordersTable.manualPaginationOptions.pageCount = response.pageCount;
        ordersTable.manualPaginationOptions.totalRecords = response.total;
      }

    } catch (error) {
      console.error('Error loading data:', error);
    } finally {
      if (loadingOverlay) {
        loadingOverlay.style.display = 'none';
      }
    }
  }

  // Simulate API call (replace with real API call in production)
  async function simulateApiCall(params: URLSearchParams): Promise<OrdersResponse> {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Generate mock data based on parameters
    const page = parseInt(params.get('page') || '0');
    const pageSize = parseInt(params.get('pageSize') || '10');
    const sortColumn = params.get('sortColumn');
    const sortDirection = params.get('sortDirection');

    // Generate 100 total items
    const totalItems = 100;
    const pageCount = Math.ceil(totalItems / pageSize);
    
    const startIndex = page * pageSize;
    const endIndex = Math.min(startIndex + pageSize, totalItems);
    
    const data = Array.from({ length: endIndex - startIndex }, (_, i) => {
      const index = startIndex + i;
      return {
        id: `ORD-${1000 + index}`,
        customer: `Customer ${index + 1}`,
        orderDate: new Date(2023, 0, 1 + index).toISOString().split('T')[0],
        amount: `$${(Math.random() * 1000 + 100).toFixed(2)}`,
        status: getRandomStatus()
      };
    });

    // Sort data if requested
    if (sortColumn && sortDirection) {
      data.sort((a: any, b: any) => {
        const aValue = a[sortColumn.replace('-', '')];
        const bValue = b[sortColumn.replace('-', '')];
        return sortDirection === 'asc' ? 
          aValue.localeCompare(bValue) : 
          bValue.localeCompare(aValue);
      });
    }

    return {
      data,
      total: totalItems,
      pageCount
    };
  }

  // Helper function for random status
  function getRandomStatus() {
    const statuses = [
      { text: 'Completed', color: 'success' },
      { text: 'Processing', color: 'primary' },
      { text: 'On Hold', color: 'warning' },
      { text: 'Cancelled', color: 'danger' }
    ];
    return { ...statuses[Math.floor(Math.random() * statuses.length)], type: 'text' };
  }

  // Initial data load
  loadTableData();
}

// Refresh button handler
if (refreshButton) {
  refreshButton.addEventListener('buttonClick', () => {
    loadTableData();
  });
}
```


# <ModusTabs>

## Prompt 1
**User Question:** How do I create a basic tab interface with multiple content sections?

**Agent Answer:**
References:
I'll demonstrate how to create a ModusTabs component with multiple content sections. The key features include:
- Setting up multiple tabs with labels
- Handling tab changes
- Basic styling and layout
- Accessibility considerations with aria-label

```html
<div id="tabs-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <h3>Project Overview</h3>
  
  <modus-tabs 
    id="project-tabs"
    aria-label="Project Information Tabs">
  </modus-tabs>
  
  <div id="tab-content" style="padding: 16px; border: 1px solid #e0e0e0; border-radius: 4px;">
    <!-- Content will be updated based on selected tab -->
  </div>
</div>
```

```typescript
const tabsContainer = document.querySelector('#project-tabs');
const tabContent = document.querySelector('#tab-content');

if (tabsContainer && tabContent) {
  // Define tabs
  tabsContainer.tabs = [
    {
      id: 'details',
      label: 'Details',
      icon: 'info'
    },
    {
      id: 'team',
      label: 'Team Members',
      icon: 'group'
    },
    {
      id: 'timeline',
      label: 'Timeline',
      icon: 'calendar'
    },
    {
      id: 'documents',
      label: 'Documents',
      icon: 'file'
    }
  ];

  // Content for each tab
  const tabContents = {
    details: {
      title: 'Project Details',
      content: 'This project aims to improve customer experience through a redesigned user interface.'
    },
    team: {
      title: 'Team Members',
      content: 'Project Lead: John Smith\nDesigner: Alice Chen\nDeveloper: Bob Wilson'
    },
    timeline: {
      title: 'Project Timeline',
      content: 'Start Date: January 1, 2025\nEnd Date: July 31, 2025'
    },
    documents: {
      title: 'Related Documents',
      content: 'Project Charter\nRequirements Document\nDesign Specifications'
    }
  };

  // Handle tab changes
  tabsContainer.addEventListener('tabChange', (event: CustomEvent) => {
    const selectedTab = event.detail;
    const content = tabContents[selectedTab.id];
    
    if (content) {
      tabContent.innerHTML = `
        <h4 style="margin-top: 0;">${content.title}</h4>
        <p style="white-space: pre-line;">${content.content}</p>
      `;
    }
  });

  // Initialize with first tab's content
  const firstTab = tabsContainer.tabs[0];
  const initialContent = tabContents[firstTab.id];
  tabContent.innerHTML = `
    <h4 style="margin-top: 0;">${initialContent.title}</h4>
    <p style="white-space: pre-line;">${initialContent.content}</p>
  `;
}
```

## Prompt 2
**User Question:** How do I create tabs with customized styling and dynamic content loading?

**Agent Answer:**
References:
This example demonstrates advanced ModusTabs features:
- Custom styling with small size variant
- Full-width tabs
- Dynamic content loading
- Active tab indication
- Loading states

```html
<div id="dynamic-tabs-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <h3>Product Dashboard</h3>
    <modus-button id="refresh-btn" color="primary" size="small" left-icon="refresh">
      Refresh
    </modus-button>
  </div>
  
  <modus-tabs 
    id="product-tabs"
    size="small"
    full-width="true"
    aria-label="Product Dashboard Tabs">
  </modus-tabs>
  
  <div id="tab-content-area" style="position: relative;">
    <div id="loading-overlay" style="display: none; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(255,255,255,0.8); align-items: center; justify-content: center;">
      <modus-spinner size="3rem" color="primary"></modus-spinner>
    </div>
    
    <div id="dashboard-content" style="padding: 16px; border: 1px solid #e0e0e0; border-radius: 4px; min-height: 300px;">
      <!-- Content will be dynamically loaded -->
    </div>
  </div>
</div>
```

```typescript
interface DashboardData {
  sales: {
    current: number;
    previous: number;
    trend: 'up' | 'down';
  };
  inventory: {
    total: number;
    lowStock: number;
  };
  reviews: {
    average: number;
    total: number;
    recent: Array<{
      rating: number;
      comment: string;
      date: string;
    }>;
  };
}

const productTabs = document.querySelector('#product-tabs');
const dashboardContent = document.querySelector('#dashboard-content');
const loadingOverlay = document.querySelector('#loading-overlay');
const refreshButton = document.querySelector('#refresh-btn');

let currentData: DashboardData | null = null;

if (productTabs && dashboardContent && loadingOverlay) {
  // Define tabs
  productTabs.tabs = [
    {
      id: 'overview',
      label: 'Overview',
      icon: 'dashboard'
    },
    {
      id: 'sales',
      label: 'Sales',
      icon: 'trending_up'
    },
    {
      id: 'inventory',
      label: 'Inventory',
      icon: 'inventory'
    },
    {
      id: 'reviews',
      label: 'Customer Reviews',
      icon: 'star'
    }
  ];

  // Function to show/hide loading state
  const setLoading = (loading: boolean) => {
    if (loadingOverlay) {
      (loadingOverlay as HTMLElement).style.display = loading ? 'flex' : 'none';
    }
  };

  // Function to load dashboard data
  const loadDashboardData = async (): Promise<DashboardData> => {
    // Simulate API call with timeout
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    return {
      sales: {
        current: 125000,
        previous: 115000,
        trend: 'up'
      },
      inventory: {
        total: 1250,
        lowStock: 15
      },
      reviews: {
        average: 4.5,
        total: 328,
        recent: [
          {
            rating: 5,
            comment: 'Excellent product quality!',
            date: '2025-06-02'
          },
          {
            rating: 4,
            comment: 'Good value for money.',
            date: '2025-06-01'
          }
        ]
      }
    };
  };

  // Function to render content based on selected tab
  const renderTabContent = (tabId: string, data: DashboardData) => {
    if (!dashboardContent) return;

    switch (tabId) {
      case 'overview':
        dashboardContent.innerHTML = `
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px;">
            <div class="stat-card" style="padding: 16px; border: 1px solid #e0e0e0; border-radius: 4px;">
              <h4>Sales Performance</h4>
              <p>Current: $${data.sales.current.toLocaleString()}</p>
              <p style="color: ${data.sales.trend === 'up' ? 'green' : 'red'}">
                Trend: ${data.sales.trend === 'up' ? '↑' : '↓'}
              </p>
            </div>
            
            <div class="stat-card" style="padding: 16px; border: 1px solid #e0e0e0; border-radius: 4px;">
              <h4>Inventory Status</h4>
              <p>Total Items: ${data.inventory.total}</p>
              <p style="color: ${data.inventory.lowStock > 10 ? 'orange' : 'red'}">
                Low Stock Items: ${data.inventory.lowStock}
              </p>
            </div>
            
            <div class="stat-card" style="padding: 16px; border: 1px solid #e0e0e0; border-radius: 4px;">
              <h4>Customer Satisfaction</h4>
              <p>Rating: ${data.reviews.average}/5</p>
              <p>Total Reviews: ${data.reviews.total}</p>
            </div>
          </div>
        `;
        break;

      case 'sales':
        dashboardContent.innerHTML = `
          <div style="padding: 16px;">
            <h4>Sales Report</h4>
            <div style="margin: 16px 0;">
              <strong>Current Period:</strong> $${data.sales.current.toLocaleString()}
              <br>
              <strong>Previous Period:</strong> $${data.sales.previous.toLocaleString()}
              <br>
              <strong>Growth:</strong> 
              <span style="color: ${data.sales.trend === 'up' ? 'green' : 'red'}">
                ${data.sales.trend === 'up' ? '↑' : '↓'}
                ${Math.abs(((data.sales.current - data.sales.previous) / data.sales.previous) * 100).toFixed(1)}%
              </span>
            </div>
          </div>
        `;
        break;

      case 'inventory':
        dashboardContent.innerHTML = `
          <div style="padding: 16px;">
            <h4>Inventory Overview</h4>
            <div style="margin: 16px 0;">
              <strong>Total Items in Stock:</strong> ${data.inventory.total}
              <br>
              <strong>Low Stock Alerts:</strong> 
              <span style="color: ${data.inventory.lowStock > 10 ? 'orange' : 'red'}">
                ${data.inventory.lowStock} items
              </span>
            </div>
          </div>
        `;
        break;

      case 'reviews':
        dashboardContent.innerHTML = `
          <div style="padding: 16px;">
            <h4>Customer Reviews</h4>
            <div style="margin: 16px 0;">
              <strong>Average Rating:</strong> ${data.reviews.average}/5
              <br>
              <strong>Total Reviews:</strong> ${data.reviews.total}
            </div>
            
            <h5>Recent Reviews</h5>
            ${data.reviews.recent.map(review => `
              <div style="margin: 16px 0; padding: 12px; border: 1px solid #e0e0e0; border-radius: 4px;">
                <div style="margin-bottom: 8px;">
                  Rating: ${'★'.repeat(review.rating)}${'☆'.repeat(5-review.rating)}
                </div>
                <div style="margin-bottom: 4px;">${review.comment}</div>
                <div style="font-size: 0.9em; color: #666;">${review.date}</div>
              </div>
            `).join('')}
          </div>
        `;
        break;
    }
  };

  // Handle tab changes
  productTabs.addEventListener('tabChange', async (event: CustomEvent) => {
    const selectedTab = event.detail;
    setLoading(true);
    
    try {
      if (!currentData) {
        currentData = await loadDashboardData();
      }
      renderTabContent(selectedTab.id, currentData);
    } catch (error) {
      console.error('Error loading dashboard data:', error);
      dashboardContent.innerHTML = `
        <div style="padding: 16px; color: red;">
          Error loading data. Please try again.
        </div>
      `;
    } finally {
      setLoading(false);
    }
  });

  // Handle refresh button click
  if (refreshButton) {
    refreshButton.addEventListener('buttonClick', async () => {
      setLoading(true);
      try {
        currentData = await loadDashboardData();
        const currentTab = productTabs.tabs.find(tab => tab.selected);
        if (currentTab) {
          renderTabContent(currentTab.id, currentData);
        }
      } catch (error) {
        console.error('Error refreshing data:', error);
      } finally {
        setLoading(false);
      }
    });
  }

  // Initialize with first tab
  productTabs.dispatchEvent(new CustomEvent('tabChange', { 
    detail: productTabs.tabs[0]
  }));
}
```



# <ModusTextInput>

## Prompt 1
**User Question:** How do I create a basic text input field with validation and handle its value changes?

**Agent Answer:**
References:
I've analyzed the ModusTextInput component and its key features. The implementation below demonstrates:
- Basic text input setup with validation
- Error state handling
- Value change event monitoring
- Helper text display
- Required field validation

```html
<div id="input-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-text-input
    id="email-input"
    type="email"
    label="Email Address"
    placeholder="Enter your email"
    required="true"
    helper-text="Please enter a valid email address"
    error-text="Invalid email format"
    size="medium">
  </modus-text-input>
</div>
```

```typescript
const emailInput = document.querySelector('#email-input');
if (emailInput) {
  emailInput.addEventListener('valueChange', (event: any) => {
    const value = event.detail;
    const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    emailInput.setAttribute('error', (!isValid && value).toString());
  });

  // Example of using the focusInput method
  emailInput.focusInput();
}
```

## Prompt 2
**User Question:** How can I create a password input with visibility toggle and strength validation?

**Agent Answer:**
References:
For this implementation, I'll showcase:
- Password input with toggle functionality
- Password strength validation
- Dynamic helper text updates
- Visual feedback based on password strength

```html
<div id="password-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-text-input
    id="password-input"
    type="password"
    label="Password"
    placeholder="Enter your password"
    required="true"
    show-hide="true"
    helper-text="Use 8+ characters with a mix of letters, numbers & symbols"
    size="medium">
  </modus-text-input>
</div>
```

```typescript
const passwordInput = document.querySelector('#password-input');
if (passwordInput) {
  passwordInput.addEventListener('valueChange', (event: any) => {
    const password = event.detail;
    const strength = checkPasswordStrength(password);
    
    // Update helper text based on password strength
    if (password) {
      if (strength === 'strong') {
        passwordInput.setAttribute('helper-text', '✓ Password strength: Strong');
        passwordInput.setAttribute('valid', 'true');
      } else if (strength === 'medium') {
        passwordInput.setAttribute('helper-text', 'Password strength: Medium - Add special characters');
        passwordInput.setAttribute('valid', 'false');
      } else {
        passwordInput.setAttribute('helper-text', 'Password strength: Weak - Use 8+ characters with mix of types');
        passwordInput.setAttribute('valid', 'false');
      }
    }
  });
}

function checkPasswordStrength(password: string): 'weak' | 'medium' | 'strong' {
  if (!password) return 'weak';
  
  const hasLength = password.length >= 8;
  const hasUpper = /[A-Z]/.test(password);
  const hasLower = /[a-z]/.test(password);
  const hasNumber = /\d/.test(password);
  const hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  
  const score = [hasLength, hasUpper, hasLower, hasNumber, hasSpecial].filter(Boolean).length;
  
  if (score >= 5) return 'strong';
  if (score >= 3) return 'medium';
  return 'weak';
}
```



# <ModusTextareaInput>

## Prompt 1
**User Question:** How do I create a basic textarea input with character count and validation?

**Agent Answer:**
References:
I'll demonstrate how to create a textarea with:
- Character limit and counter
- Required field validation
- Helper text and error states
- Basic event handling
- Auto-focus functionality

This implementation shows the most common use case for collecting multi-line text input with validation.

```html
<div id="textarea-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-textarea-input
    id="feedback-textarea"
    label="Your Feedback"
    placeholder="Please share your thoughts..."
    required="true"
    helper-text="Enter at least 10 characters"
    max-length="500"
    rows="4"
    size="medium">
  </modus-textarea-input>
  
  <div id="char-count" style="font-size: 12px; color: #666; text-align: right;"></div>
</div>
```

```typescript
const textarea = document.querySelector('#feedback-textarea');
const charCount = document.querySelector('#char-count');

if (textarea && charCount) {
  // Set initial focus
  textarea.focusInput();
  
  // Handle value changes
  textarea.addEventListener('valueChange', (event: any) => {
    const value = event.detail;
    const length = value.length;
    
    // Update character counter
    charCount.textContent = `${length}/500 characters`;
    
    // Validate minimum length
    if (length < 10 && length > 0) {
      textarea.setAttribute('error-text', 'Please enter at least 10 characters');
    } else {
      textarea.removeAttribute('error-text');
    }
  });
}
```

## Prompt 2
**User Question:** How can I create a textarea with autosave and character limit validation?

**Agent Answer:**
References:
For this advanced implementation, I'll demonstrate:
- Autosaving content to localStorage
- Real-time character limit validation
- Clear button functionality
- Responsive error and helper text
- Debounced autosave

```html
<div id="notes-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-textarea-input
    id="notes-textarea"
    label="Meeting Notes"
    placeholder="Type your notes here..."
    helper-text="Notes are automatically saved as you type"
    clearable="true"
    max-length="1000"
    rows="6"
    size="large">
  </modus-textarea-input>
  
  <div style="display: flex; justify-content: space-between; font-size: 12px;">
    <div id="save-status" style="color: #666;"></div>
    <div id="notes-char-count" style="color: #666;"></div>
  </div>
</div>
```

```typescript
const notesTextarea = document.querySelector('#notes-textarea');
const saveStatus = document.querySelector('#save-status');
const charCount = document.querySelector('#notes-char-count');

if (notesTextarea && saveStatus && charCount) {
  // Load saved content
  const savedContent = localStorage.getItem('meeting-notes');
  if (savedContent) {
    notesTextarea.setAttribute('value', savedContent);
    updateCharCount(savedContent.length);
  }
  
  let saveTimeout: number | null = null;
  
  // Handle value changes
  notesTextarea.addEventListener('valueChange', (event: any) => {
    const value = event.detail;
    updateCharCount(value.length);
    
    // Debounced autosave
    if (saveTimeout) {
      clearTimeout(saveTimeout);
    }
    
    saveStatus.textContent = 'Saving...';
    saveTimeout = setTimeout(() => {
      localStorage.setItem('meeting-notes', value);
      saveStatus.textContent = 'Changes saved';
      
      // Clear save status after 2 seconds
      setTimeout(() => {
        saveStatus.textContent = '';
      }, 2000);
    }, 1000);
  });
  
  function updateCharCount(length: number) {
    const remaining = 1000 - length;
    charCount.textContent = `${remaining} characters remaining`;
    
    if (remaining < 50) {
      charCount.style.color = '#d9363e';
    } else {
      charCount.style.color = '#666';
    }
  }
}
```


# <ModusTimePicker>

## Prompt 1
**User Question:** How do I create a basic time picker with validation and auto-formatting?

**Agent Answer:**
References:
I'll demonstrate how to create a time picker with:
- Auto-formatting as the user types
- Validation for valid time formats
- Helper text for input guidance
- Error handling for invalid times
- Value change event handling

```html
<div id="time-picker-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-time-picker
    id="meeting-time"
    label="Meeting Time"
    helper-text="hh:mm"
    auto-format="true"
    placeholder="14:30"
    required="true">
  </modus-time-picker>
  
  <div id="time-feedback" style="font-size: 14px; color: #666;"></div>
</div>
```

```typescript
const timePicker = document.querySelector('#meeting-time');
const feedback = document.querySelector('#time-feedback');

if (timePicker && feedback) {
  // Handle value changes
  timePicker.addEventListener('valueChange', (event: any) => {
    const timeValue = event.detail;
    console.log('Time changed:', timeValue);
    
    // Validate time format (HH:mm)
    const isValidFormat = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/.test(timeValue);
    
    if (!timeValue) {
      timePicker.setAttribute('error-text', 'Time is required');
      feedback.textContent = '';
    } else if (!isValidFormat) {
      timePicker.setAttribute('error-text', 'Please enter a valid time (HH:mm)');
      feedback.textContent = '';
    } else {
      timePicker.removeAttribute('error-text');
      feedback.textContent = `Selected time: ${timeValue}`;
      feedback.style.color = '#008744';
    }
  });
  
  // Handle blur events
  timePicker.addEventListener('timeInputBlur', (event: any) => {
    console.log('Time input blurred:', event.detail);
  });
}
```

## Prompt 2
**User Question:** How can I implement a time picker with time zone selection?

**Agent Answer:**
References:
This implementation shows how to:
- Combine time picker with time zone selection
- Use the timeZone slot for the select component
- Handle both time and time zone changes
- Format and validate combined time/zone data
- Provide clear feedback for user selections

```html
<div id="timezone-picker-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <modus-time-picker
    id="schedule-time"
    label="Schedule Time"
    helper-text="hh:mm"
    auto-format="true"
    value="09:00">
    
    <div slot="timeZone" style="padding-left: 8px;">
      <modus-select
        id="timezone-select"
        label="Time Zone"
        options-display-prop="display"
        helper-text="Select your time zone">
      </modus-select>
    </div>
  </modus-time-picker>
  
  <div id="schedule-summary" style="font-size: 14px; margin-top: 8px;"></div>
</div>
```

```typescript
const schedulePicker = document.querySelector('#schedule-time');
const timezoneSelect = document.querySelector('#timezone-select');
const summary = document.querySelector('#schedule-summary');

let selectedTime = '09:00';
let selectedTimezone = '';

if (schedulePicker && timezoneSelect && summary) {
  // Initialize timezone options
  (timezoneSelect as any).options = [
    { display: 'Eastern Time (ET)', value: 'America/New_York' },
    { display: 'Central Time (CT)', value: 'America/Chicago' },
    { display: 'Mountain Time (MT)', value: 'America/Denver' },
    { display: 'Pacific Time (PT)', value: 'America/Los_Angeles' },
    { display: 'UTC', value: 'UTC' }
  ];
  
  // Handle time changes
  schedulePicker.addEventListener('valueChange', (event: any) => {
    selectedTime = event.detail;
    updateSummary();
  });
  
  // Handle timezone selection
  timezoneSelect.addEventListener('valueChange', (event: any) => {
    selectedTimezone = event.detail?.display || '';
    updateSummary();
  });
  
  function updateSummary() {
    if (selectedTime && selectedTimezone) {
      summary.textContent = `Scheduled for ${selectedTime} ${selectedTimezone}`;
      summary.style.color = '#2e2e2e';
    } else {
      summary.textContent = 'Please select both time and time zone';
      summary.style.color = '#666';
    }
  }
  
  // Initial summary
  updateSummary();
}
```




# <ModusToast>

## Prompt 1
**User Question:** How do I create and display basic toast notifications with different types and behaviors?

**Agent Answer:**
References:
The ModusToast component is used to display temporary notifications to users. Key properties to consider:
- `type`: Determines the toast style (primary, secondary, success, danger)
- `delay`: Controls how long the toast is displayed (default 15000ms)
- `dismissible`: Allows user to manually close the toast
- `show-icon`: Displays an icon matching the toast type
- `retain-element`: Keeps the element in DOM after dismissal

Here's an implementation showing different types of toasts with various configurations:

```html
<div id="toast-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; gap: 8px; flex-wrap: wrap;">
    <modus-button id="show-primary-btn" color="primary">Show Primary Toast</modus-button>
    <modus-button id="show-success-btn" color="success">Show Success Toast</modus-button>
    <modus-button id="show-danger-btn" color="danger">Show Danger Toast</modus-button>
  </div>
  
  <!-- Toast elements will be added here dynamically -->
  <div id="toasts-wrapper" style="position: fixed; top: 20px; right: 20px; display: flex; flex-direction: column; gap: 8px; z-index: 1000;"></div>
</div>
```

```typescript
// Get button references
const primaryBtn = document.querySelector('#show-primary-btn');
const successBtn = document.querySelector('#show-success-btn');
const dangerBtn = document.querySelector('#show-danger-btn');
const toastsWrapper = document.querySelector('#toasts-wrapper');

// Function to create and show a toast
function showToast(type: string, message: string) {
  // Create toast element
  const toast = document.createElement('modus-toast');
  toast.setAttribute('type', type);
  toast.setAttribute('dismissible', 'true');
  toast.setAttribute('show-icon', 'true');
  toast.textContent = message;
  
  // Add toast to wrapper
  toastsWrapper.appendChild(toast);
  
  // Listen for dismissal
  toast.addEventListener('toastDismissed', () => {
    if (!toast.hasAttribute('retain-element')) {
      setTimeout(() => {
        toastsWrapper.removeChild(toast);
      }, 300); // Small delay for animation
    }
  });
}

// Add click handlers
if (primaryBtn) {
  primaryBtn.addEventListener('buttonClick', () => {
    showToast('primary', 'This is a primary notification');
  });
}

if (successBtn) {
  successBtn.addEventListener('buttonClick', () => {
    showToast('success', 'Operation completed successfully!');
  });
}

if (dangerBtn) {
  dangerBtn.addEventListener('buttonClick', () => {
    showToast('danger', 'An error occurred. Please try again.');
  });
}
```

## Prompt 2
**User Question:** How do I create a more advanced toast notification system with auto-dismissal and queueing?

**Agent Answer:**
References:
For a more sophisticated toast system, we'll implement:
1. Custom delays for different toast types
2. A queue system to prevent overwhelming the user
3. Auto-dismissal with optional retention
4. Accessibility improvements with ARIA labels and roles

Here's an implementation of an advanced toast notification system:

```html
<div id="advanced-toast-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <div style="display: flex; flex-direction: column; gap: 8px;">
    <h4>Toast Notification System Demo</h4>
    <p>Demonstrates a queue-based notification system with different behaviors.</p>
  </div>
  
  <div style="display: flex; gap: 8px; flex-wrap: wrap;">
    <modus-button id="info-toast-btn" color="primary">Info Update</modus-button>
    <modus-button id="progress-toast-btn" color="secondary">Long Process</modus-button>
    <modus-button id="multi-step-btn" color="primary">Multi-step Process</modus-button>
  </div>
  
  <!-- Toast container with fixed positioning -->
  <div id="advanced-toasts-wrapper" style="position: fixed; top: 20px; right: 20px; display: flex; flex-direction: column; gap: 8px; z-index: 1000;"></div>
</div>
```

```typescript
class ToastManager {
  private queue: Array<{type: string; message: string; delay?: number}> = [];
  private isProcessing = false;
  private wrapper: HTMLElement;
  private maxVisible = 3;
  private activeToasts = 0;

  constructor(wrapperId: string) {
    this.wrapper = document.querySelector(wrapperId);
  }

  addToast(type: string, message: string, delay?: number) {
    this.queue.push({ type, message, delay });
    this.processQueue();
  }

  private processQueue() {
    if (this.isProcessing || this.activeToasts >= this.maxVisible || this.queue.length === 0) {
      return;
    }

    this.isProcessing = true;
    const { type, message, delay } = this.queue.shift();
    
    // Create and configure toast
    const toast = document.createElement('modus-toast');
    toast.setAttribute('type', type);
    toast.setAttribute('dismissible', 'true');
    toast.setAttribute('show-icon', 'true');
    toast.setAttribute('role', type === 'danger' ? 'alert' : 'status');
    toast.setAttribute('aria-label', `${type} notification: ${message}`);
    if (delay) toast.setAttribute('delay', delay.toString());
    toast.textContent = message;

    // Add toast to container
    this.wrapper.appendChild(toast);
    this.activeToasts++;

    // Handle dismissal
    toast.addEventListener('toastDismissed', () => {
      this.activeToasts--;
      setTimeout(() => {
        this.wrapper.removeChild(toast);
        this.isProcessing = false;
        this.processQueue();
      }, 300);
    });
  }

  clearAll() {
    this.queue = [];
    const toasts = this.wrapper.querySelectorAll('modus-toast');
    toasts.forEach(toast => {
      this.wrapper.removeChild(toast);
    });
    this.activeToasts = 0;
    this.isProcessing = false;
  }
}

// Initialize toast manager
const toastManager = new ToastManager('#advanced-toasts-wrapper');

// Add event listeners
document.querySelector('#info-toast-btn')?.addEventListener('buttonClick', () => {
  toastManager.addToast('primary', 'System update: New features available', 5000);
});

document.querySelector('#progress-toast-btn')?.addEventListener('buttonClick', () => {
  toastManager.addToast('secondary', 'Starting background process...', 3000);
  
  setTimeout(() => {
    toastManager.addToast('success', 'Background process completed successfully', 4000);
  }, 4000);
});

document.querySelector('#multi-step-btn')?.addEventListener('buttonClick', () => {
  // Simulate a multi-step process
  toastManager.addToast('primary', 'Step 1: Initializing process...', 2000);
  
  setTimeout(() => {
    toastManager.addToast('secondary', 'Step 2: Processing data...', 2000);
  }, 2500);
  
  setTimeout(() => {
    toastManager.addToast('secondary', 'Step 3: Finalizing...', 2000);
  }, 5000);
  
  setTimeout(() => {
    toastManager.addToast('success', 'Multi-step process completed!', 4000);
  }, 7500);
});
```




# <ModusToolbar>

## Prompt 1
**User Question:** How do I create a basic toolbar with buttons and controls?

**Agent Answer:**
References:
The ModusToolbar component is used to organize buttons and controls in a horizontal layout. Key features include:
- Default slot for adding buttons and other controls
- Support for disabled state
- Proper accessibility with ARIA labels
- Flexible content organization

Here's a basic implementation showing a toolbar with common controls:

```html
<div id="document-toolbar" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; border: 1px solid #e0e0e0;">
  <modus-toolbar 
    id="main-toolbar"
    aria-label="Document editing tools">
    
    <!-- File operations group -->
    <div style="display: flex; gap: 8px; padding-right: 16px; border-right: 1px solid #e0e0e0;">
      <modus-button 
        id="new-btn"
        color="primary"
        left-icon="add">
        New
      </modus-button>
      
      <modus-button 
        id="open-btn"
        color="secondary"
        left-icon="folder_open">
        Open
      </modus-button>
      
      <modus-button 
        id="save-btn"
        color="secondary"
        left-icon="save">
        Save
      </modus-button>
    </div>
    
    <!-- Edit operations group -->
    <div style="display: flex; gap: 8px; padding: 0 16px; border-right: 1px solid #e0e0e0;">
      <modus-button 
        id="cut-btn"
        color="secondary"
        button-style="borderless"
        icon-only="content_cut"
        aria-label="Cut">
      </modus-button>
      
      <modus-button 
        id="copy-btn"
        color="secondary"
        button-style="borderless"
        icon-only="content_copy"
        aria-label="Copy">
      </modus-button>
      
      <modus-button 
        id="paste-btn"
        color="secondary"
        button-style="borderless"
        icon-only="content_paste"
        aria-label="Paste">
      </modus-button>
    </div>
    
    <!-- Format operations group -->
    <div style="display: flex; gap: 8px; padding-left: 16px;">
      <modus-button 
        id="bold-btn"
        color="secondary"
        button-style="borderless"
        icon-only="format_bold"
        aria-label="Bold">
      </modus-button>
      
      <modus-button 
        id="italic-btn"
        color="secondary"
        button-style="borderless"
        icon-only="format_italic"
        aria-label="Italic">
      </modus-button>
      
      <modus-button 
        id="underline-btn"
        color="secondary"
        button-style="borderless"
        icon-only="format_underline"
        aria-label="Underline">
      </modus-button>
    </div>
  </modus-toolbar>
  
  <div id="toolbar-actions" style="font-size: 14px; color: #666;">
    Click any button to see the action
  </div>
</div>
```

```typescript
const toolbar = document.querySelector('#main-toolbar');
const actionsDisplay = document.querySelector('#toolbar-actions');

// Function to handle button clicks
const handleButtonClick = (action: string): void => {
  if (actionsDisplay) {
    actionsDisplay.textContent = `Action performed: ${action}`;
    
    // Reset message after delay
    setTimeout(() => {
      actionsDisplay.textContent = 'Click any button to see the action';
    }, 2000);
  }
};

// Add click handlers for file operations
document.querySelector('#new-btn')?.addEventListener('buttonClick', () => handleButtonClick('New Document'));
document.querySelector('#open-btn')?.addEventListener('buttonClick', () => handleButtonClick('Open Document'));
document.querySelector('#save-btn')?.addEventListener('buttonClick', () => handleButtonClick('Save Document'));

// Add click handlers for edit operations
document.querySelector('#cut-btn')?.addEventListener('buttonClick', () => handleButtonClick('Cut'));
document.querySelector('#copy-btn')?.addEventListener('buttonClick', () => handleButtonClick('Copy'));
document.querySelector('#paste-btn')?.addEventListener('buttonClick', () => handleButtonClick('Paste'));

// Add click handlers for format operations
document.querySelector('#bold-btn')?.addEventListener('buttonClick', () => handleButtonClick('Toggle Bold'));
document.querySelector('#italic-btn')?.addEventListener('buttonClick', () => handleButtonClick('Toggle Italic'));
document.querySelector('#underline-btn')?.addEventListener('buttonClick', () => handleButtonClick('Toggle Underline'));
```

## Prompt 2
**User Question:** How do I create a more complex toolbar with dropdowns and dynamic states?

**Agent Answer:**
References:
This implementation demonstrates advanced toolbar features:
- Integration with dropdowns for complex actions
- Dynamic button state management
- Groups of related controls
- Responsive layout handling

Here's an example of a toolbar with advanced functionality:

```html
<div id="advanced-toolbar-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px; border: 1px solid #e0e0e0;">
  <modus-toolbar 
    id="advanced-toolbar"
    aria-label="Advanced editing tools">
    
    <!-- Main actions with dropdowns -->
    <div style="display: flex; gap: 8px; padding-right: 16px; border-right: 1px solid #e0e0e0;">
      <!-- File menu dropdown -->
      <modus-dropdown id="file-menu" aria-label="File menu">
        <modus-button 
          slot="trigger"
          color="primary"
          right-icon="arrow_drop_down">
          File
        </modus-button>
        
        <modus-list>
          <modus-list-item id="new-doc">New Document</modus-list-item>
          <modus-list-item id="open-doc">Open...</modus-list-item>
          <modus-list-item id="save-doc">Save</modus-list-item>
          <modus-list-item id="export-doc">Export As...</modus-list-item>
        </modus-list>
      </modus-dropdown>
      
      <!-- View options -->
      <modus-button-group
        id="view-options"
        selection-type="single"
        aria-label="View options"
        color="secondary"
        button-style="outline">
        <modus-button id="view-editor" selected>Editor</modus-button>
        <modus-button id="view-preview">Preview</modus-button>
        <modus-button id="view-split">Split</modus-button>
      </modus-button-group>
    </div>
    
    <!-- Format options -->
    <div style="display: flex; gap: 8px; padding: 0 16px; border-right: 1px solid #e0e0e0; align-items: center;">
      <!-- Font family dropdown -->
      <modus-select 
        id="font-select"
        size="small"
        placeholder="Font Family"
        style="width: 120px;">
      </modus-select>
      
      <!-- Font size dropdown -->
      <modus-select 
        id="size-select"
        size="small"
        placeholder="Size"
        style="width: 80px;">
      </modus-select>
      
      <!-- Style toggles -->
      <modus-button-group
        id="style-toggles"
        selection-type="multiple"
        color="secondary"
        button-style="borderless">
        <modus-button icon-only="format_bold" aria-label="Bold"></modus-button>
        <modus-button icon-only="format_italic" aria-label="Italic"></modus-button>
        <modus-button icon-only="format_underline" aria-label="Underline"></modus-button>
      </modus-button-group>
    </div>
    
    <!-- Tools -->
    <div style="display: flex; gap: 8px; padding-left: 16px;">
      <modus-button 
        id="find-btn"
        color="secondary"
        button-style="borderless"
        left-icon="search">
        Find
      </modus-button>
      
      <modus-button 
        id="replace-btn"
        color="secondary"
        button-style="borderless"
        left-icon="find_replace">
        Replace
      </modus-button>
      
      <modus-button 
        id="help-btn"
        color="secondary"
        button-style="borderless"
        icon-only="help"
        aria-label="Help">
      </modus-button>
    </div>
  </modus-toolbar>
  
  <div id="editor-state" style="font-size: 14px; color: #666;">
    Current view: Editor | Font: Default | Size: 12pt
  </div>
</div>
```

```typescript
interface EditorState {
  viewMode: 'editor' | 'preview' | 'split';
  fontFamily: string;
  fontSize: string;
  styles: {
    bold: boolean;
    italic: boolean;
    underline: boolean;
  };
}

// Initialize editor state
let editorState: EditorState = {
  viewMode: 'editor',
  fontFamily: 'Default',
  fontSize: '12pt',
  styles: {
    bold: false,
    italic: false,
    underline: false
  }
};

// Get UI elements
const stateDisplay = document.querySelector('#editor-state');
const toolbar = document.querySelector('#advanced-toolbar');
const fileMenu = document.querySelector('#file-menu');
const viewOptions = document.querySelector('#view-options');
const fontSelect = document.querySelector('#font-select') as any;
const sizeSelect = document.querySelector('#size-select') as any;
const styleToggles = document.querySelector('#style-toggles');

// Configure dropdowns
if (fontSelect) {
  fontSelect.items = [
    { text: 'Default', value: 'default' },
    { text: 'Arial', value: 'arial' },
    { text: 'Times New Roman', value: 'times' },
    { text: 'Courier New', value: 'courier' }
  ];
}

if (sizeSelect) {
  sizeSelect.items = [
    { text: '8pt', value: '8' },
    { text: '10pt', value: '10' },
    { text: '12pt', value: '12' },
    { text: '14pt', value: '14' },
    { text: '16pt', value: '16' },
    { text: '18pt', value: '18' }
  ];
}

// Update state display
const updateStateDisplay = () => {
  if (stateDisplay) {
    const stylesList = Object.entries(editorState.styles)
      .filter(([_, value]) => value)
      .map(([key]) => key.charAt(0).toUpperCase() + key.slice(1))
      .join(', ');
      
    stateDisplay.textContent = 
      `Current view: ${editorState.viewMode.charAt(0).toUpperCase() + editorState.viewMode.slice(1)} | ` +
      `Font: ${editorState.fontFamily} | ` +
      `Size: ${editorState.fontSize}` +
      (stylesList ? ` | Styles: ${stylesList}` : '');
  }
};

// Event handlers
if (fileMenu) {
  document.querySelectorAll('modus-list-item').forEach(item => {
    item.addEventListener('itemClick', () => {
      const action = item.id.replace('-doc', '').charAt(0).toUpperCase() + 
                    item.id.replace('-doc', '').slice(1);
      console.log(`File action: ${action}`);
    });
  });
}

if (viewOptions) {
  viewOptions.addEventListener('selectionChange', (event: any) => {
    const selectedButton = event.detail[0];
    const newMode = selectedButton.id.replace('view-', '') as EditorState['viewMode'];
    editorState.viewMode = newMode;
    updateStateDisplay();
  });
}

if (fontSelect) {
  fontSelect.addEventListener('valueChange', (event: any) => {
    const fontName = event.detail.text;
    editorState.fontFamily = fontName;
    updateStateDisplay();
  });
}

if (sizeSelect) {
  sizeSelect.addEventListener('valueChange', (event: any) => {
    const fontSize = event.detail.text;
    editorState.fontSize = fontSize;
    updateStateDisplay();
  });
}

if (styleToggles) {
  styleToggles.addEventListener('selectionChange', (event: any) => {
    const selectedButtons = event.detail;
    
    editorState.styles.bold = selectedButtons.some((btn: any) => 
      btn.getAttribute('icon-only') === 'format_bold'
    );
    editorState.styles.italic = selectedButtons.some((btn: any) => 
      btn.getAttribute('icon-only') === 'format_italic'
    );
    editorState.styles.underline = selectedButtons.some((btn: any) => 
      btn.getAttribute('icon-only') === 'format_underline'
    );
    
    updateStateDisplay();
  });
}

// Find/Replace handlers
document.querySelector('#find-btn')?.addEventListener('buttonClick', () => {
  console.log('Opening find dialog...');
});

document.querySelector('#replace-btn')?.addEventListener('buttonClick', () => {
  console.log('Opening find and replace dialog...');
});

document.querySelector('#help-btn')?.addEventListener('buttonClick', () => {
  console.log('Opening help documentation...');
});
```


# <ModusTreeView>

## Prompt 1
**User Question:** How do I create a basic tree view with expandable items and handle selection events?

**Agent Answer:**
References:
The ModusTreeView component provides a hierarchical tree structure with expandable and collapsible items. For this basic implementation, I'll focus on creating a simple tree with parent-child relationships and handling selection events.

Key properties I'll use:
- `node-id` (required): Provides a unique identifier for each tree item
- `label`: The text displayed for each item
- `selectedItems`: An array of selected node IDs
- Event handling for `itemSelectionChange` to respond to selections

```html
<div id="tree-container" style="display: flex; flex-direction: column; width: 400px;">
  <modus-tree-view id="basic-tree">
    <modus-tree-view-item node-id="1" label="Documents">
      <modus-tree-view-item node-id="2" label="Work Files">
        <modus-tree-view-item node-id="3" label="Project A"></modus-tree-view-item>
        <modus-tree-view-item node-id="4" label="Project B"></modus-tree-view-item>
      </modus-tree-view-item>
      <modus-tree-view-item node-id="5" label="Personal Files">
        <modus-tree-view-item node-id="6" label="Photos"></modus-tree-view-item>
        <modus-tree-view-item node-id="7" label="Tax Documents"></modus-tree-view-item>
      </modus-tree-view-item>
    </modus-tree-view-item>
    <modus-tree-view-item node-id="8" label="Downloads"></modus-tree-view-item>
  </modus-tree-view>
</div>
```

```typescript
const treeView = document.getElementById('basic-tree');

// Expand initial items if needed
treeView.expandedItems = ['1']; // Expand the Documents node

// Handle selection events
treeView.addEventListener('itemSelectionChange', (event) => {
  const selectedNode = event.detail;
  console.log(`Selected item: ${selectedNode.nodeId}, isSelected: ${selectedNode.isSelected}`);
  
  // Perform actions based on selection
  if (selectedNode.isSelected) {
    // Example: Show details for the selected item
    console.log(`Showing details for item ${selectedNode.nodeId}`);
  }
});
```

## Prompt 2
**User Question:** How can I implement a tree view with checkboxes and handle both checkbox selection and item expansion?

**Agent Answer:**
References:
For this implementation, I'll use the checkbox selection features of the ModusTreeView component. This involves:

1. Setting `checkbox-selection="true"` to enable checkboxes for all items
2. Using `multi-checkbox-selection="true"` to allow multiple checkboxes to be selected
3. Tracking checkbox selections with the `checkedItems` property
4. Handling checkbox clicks with the `checkboxClick` event
5. Managing expanded state with `expandedItems` property

```html
<div id="file-explorer" style="display: flex; flex-direction: column; width: 400px;">
  <modus-tree-view 
    id="checkbox-tree"
    checkbox-selection="true" 
    multi-checkbox-selection="true">
    <modus-tree-view-item node-id="folder-1" label="Project Files">
      <modus-tree-view-item node-id="folder-1-1" label="Source Code">
        <modus-tree-view-item node-id="file-1-1-1" label="main.js"></modus-tree-view-item>
        <modus-tree-view-item node-id="file-1-1-2" label="utils.js"></modus-tree-view-item>
      </modus-tree-view-item>
      <modus-tree-view-item node-id="folder-1-2" label="Documentation">
        <modus-tree-view-item node-id="file-1-2-1" label="README.md"></modus-tree-view-item>
        <modus-tree-view-item node-id="file-1-2-2" label="API.md"></modus-tree-view-item>
      </modus-tree-view-item>
    </modus-tree-view-item>
    <modus-tree-view-item node-id="folder-2" label="Assets">
      <modus-tree-view-item node-id="file-2-1" label="logo.png"></modus-tree-view-item>
      <modus-tree-view-item node-id="file-2-2" label="icon.svg"></modus-tree-view-item>
    </modus-tree-view-item>
  </modus-tree-view>
  <div id="selection-info" style="margin-top: 16px; padding: 8px; border: 1px solid #ccc;">
    Selected items: None
  </div>
</div>
```

```typescript
const checkboxTree = document.getElementById('checkbox-tree');
const selectionInfo = document.getElementById('selection-info');

// Initialize expanded items
checkboxTree.expandedItems = ['folder-1'];

// Handle checkbox selection
checkboxTree.addEventListener('checkboxClick', (event) => {
  // Update the selection information display
  const checked = checkboxTree.checkedItems || [];
  
  if (checked.length === 0) {
    selectionInfo.textContent = 'Selected items: None';
  } else {
    selectionInfo.textContent = `Selected items: ${checked.length} (${checked.join(', ')})`;
  }
});

// Handle item expansion
checkboxTree.addEventListener('itemExpandToggle', (event) => {
  const expanded = checkboxTree.expandedItems || [];
  console.log('Currently expanded folders:', expanded);
});

// Example function to programmatically select items
function selectAllSourceCodeFiles() {
  checkboxTree.checkedItems = ['file-1-1-1', 'file-1-1-2'];
  
  // Make sure the parent folders are expanded to show the selection
  checkboxTree.expandedItems = ['folder-1', 'folder-1-1'];
}
```

## Prompt 3
**User Question:** How do I create a tree view with custom actions (like edit, delete) for each item and handle drag-and-drop reordering?

**Agent Answer:**
References:
This implementation showcases advanced features of the ModusTreeView:

1. Adding custom actions to tree items using the `actions` property
2. Enabling drag-and-drop with `enableReordering="true"`
3. Setting individual items as `draggableItem` and `droppableItem`
4. Handling action clicks with the `itemActionClick` event
5. Responding to drag-and-drop operations with the `itemDrop` event

```html
<div id="advanced-tree-container" style="display: flex; flex-direction: column; width: 400px;">
  <h4>Project Structure</h4>
  <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
    <span>Drag and drop items to reorganize</span>
    <modus-button id="toggle-drag" size="small" color="primary">Toggle Drag Mode</modus-button>
  </div>
  <modus-tree-view id="advanced-tree">
    <modus-tree-view-item node-id="component-1" label="Header Component">
      <modus-tree-view-item node-id="file-1-1" label="header.html"></modus-tree-view-item>
      <modus-tree-view-item node-id="file-1-2" label="header.css"></modus-tree-view-item>
      <modus-tree-view-item node-id="file-1-3" label="header.js"></modus-tree-view-item>
    </modus-tree-view-item>
    <modus-tree-view-item node-id="component-2" label="Footer Component">
      <modus-tree-view-item node-id="file-2-1" label="footer.html"></modus-tree-view-item>
      <modus-tree-view-item node-id="file-2-2" label="footer.css"></modus-tree-view-item>
      <modus-tree-view-item node-id="file-2-3" label="footer.js"></modus-tree-view-item>
    </modus-tree-view-item>
  </modus-tree-view>
  <div id="action-log" style="margin-top: 16px; padding: 8px; border: 1px solid #ccc; height: 80px; overflow-y: auto;">
    Action log:
  </div>
</div>
```

```typescript
// Get references to elements
const advancedTree = document.getElementById('advanced-tree');
const toggleDragBtn = document.getElementById('toggle-drag');
const actionLog = document.getElementById('action-log');

// Initialize the tree
advancedTree.expandedItems = ['component-1', 'component-2'];

// Add custom actions to each tree item
const items = advancedTree.querySelectorAll('modus-tree-view-item');
items.forEach(item => {
  // Only add edit/delete actions to files, not folders
  if (item.nodeId.startsWith('file-')) {
    item.actions = [
      { id: 'edit', icon: 'edit', label: 'Edit' },
      { id: 'delete', icon: 'delete', label: 'Delete' }
    ];
  }
  // Add actions specific to components
  else if (item.nodeId.startsWith('component-')) {
    item.actions = [
      { id: 'add', icon: 'add', label: 'Add File' }
    ];
  }
});

// Handle action clicks
advancedTree.addEventListener('itemActionClick', (event) => {
  const { actionId, nodeId } = event.detail;
  const logEntry = document.createElement('div');
  logEntry.textContent = `Action: ${actionId} on item: ${nodeId}`;
  actionLog.appendChild(logEntry);
  
  // Handle specific actions
  switch(actionId) {
    case 'delete':
      // In a real app, you would confirm deletion first
      const itemToDelete = advancedTree.querySelector(`modus-tree-view-item[node-id="${nodeId}"]`);
      if (itemToDelete && itemToDelete.parentElement) {
        itemToDelete.parentElement.removeChild(itemToDelete);
      }
      break;
      
    case 'edit':
      const itemToEdit = advancedTree.querySelector(`modus-tree-view-item[node-id="${nodeId}"]`);
      if (itemToEdit) {
        itemToEdit.editable = true;
      }
      break;
      
    case 'add':
      const componentItem = advancedTree.querySelector(`modus-tree-view-item[node-id="${nodeId}"]`);
      if (componentItem) {
        const newFileId = `file-new-${Date.now()}`;
        const newItem = document.createElement('modus-tree-view-item');
        newItem.nodeId = newFileId;
        newItem.label = 'New File';
        newItem.editable = true;
        componentItem.appendChild(newItem);
      }
      break;
  }
});

// Toggle drag-and-drop functionality
let dragEnabled = false;
toggleDragBtn.addEventListener('buttonClick', () => {
  dragEnabled = !dragEnabled;
  advancedTree.enableReordering = dragEnabled;
  toggleDragBtn.innerText = dragEnabled ? 'Disable Drag Mode' : 'Enable Drag Mode';
  
  const logEntry = document.createElement('div');
  logEntry.textContent = `Drag mode ${dragEnabled ? 'enabled' : 'disabled'}`;
  actionLog.appendChild(logEntry);
});

// Handle item drops (reordering)
advancedTree.addEventListener('itemDrop', (event) => {
  const updatedItems = event.detail;
  const logEntry = document.createElement('div');
  logEntry.textContent = `Item reordered: ${JSON.stringify(Object.keys(updatedItems))}`;
  actionLog.appendChild(logEntry);
});

// Handle label changes
advancedTree.addEventListener('itemLabelChange', (event) => {
  const newLabel = event.detail;
  const logEntry = document.createElement('div');
  logEntry.textContent = `Label changed to: ${newLabel}`;
  actionLog.appendChild(logEntry);
});
```

