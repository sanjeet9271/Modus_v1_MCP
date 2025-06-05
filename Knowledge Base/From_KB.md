# <ModusAutocomplete>

## Prompt 1
**User Question:** Create a webpage with an autocomplete component to search for fruits and display the selected fruit's name below the component?

**Agent Answer:**
References:
To create an autocomplete component that allows users to search for fruits and display the selected fruit's name below the component, we will use the `ModusAutocomplete` component with an `optionSelected` event to handle the selection. The approach involves defining a list of fruit options, setting up the autocomplete component, and handling the selection event to update the displayed fruit name.

```tsx
import React, { useState } from 'react';
import { ModusAutocomplete } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const [selectedFruit, setSelectedFruit] = useState<string | null>(null);
  const options = [
    { id: '0', value: 'Apple' },
    { id: '1', value: 'Banana' },
    { id: '2', value: 'Orange' },
    { id: '3', value: 'Mango' },
    { id: '4', value: 'Pineapple' },
    { id: '5', value: 'Grapes' },
    { id: '6', value: 'Watermelon' },
    { id: '7', value: 'Strawberry' },
    { id: '8', value: 'Blueberry' },
    { id: '9', value: 'Raspberry' },
    { id: '10', value: 'Blackberry' },
    { id: '11', value: 'Cherry' },
    { id: '12', value: 'Peach' },
    { id: '13', value: 'Pear' },
    { id: '14', value: 'Plum' },
    { id: '15', value: 'Kiwi' },
    { id: '16', value: 'Lemon' },
    { id: '17', value: 'Lime' },
    { id: '18', value: 'Papaya' },
    { id: '19', value: 'Passion Fruit' }
  ];

  const handleOptionSelected = (event: CustomEvent<string>) => {
    const selectedOption = options.find(option => option.id === event.detail);
    if (selectedOption) {
      setSelectedFruit(selectedOption.value);
    }
  };

  return (
    <div style={{ width: '500px', padding: '16px', overflow: 'auto' }}>
      <ModusAutocomplete
        id="fruit-search"
        label="Fruit Search"
        placeholder="Search for a fruit..."
        options={options}
        onOptionSelected={handleOptionSelected}
      />
      <div id="selected-fruit" style={{ marginTop: '16px', fontWeight: 'bold' }}>
        {selectedFruit ? `Selected Fruit: ${selectedFruit}` : ''}
      </div>
    </div>
  );
};

export default MyComponent;
```

## Prompt 2
**User Question:** Create a webpage with an autocomplete component that allows users to search and select multiple programming languages. Display the list of selected languages below the autocomplete component.

**Agent Answer:** 
References:
To create an autocomplete component that allows users to search and select multiple programming languages and display the list of selected languages below the component, we will use the `ModusAutocomplete` component with the `multiple` attribute and the `selectionsChanged` event to handle the selections.

The approach involves breaking down the problem into simpler components:
1. Define the options for the autocomplete component.
2. Implement the state management for selected languages using React's `useState` hook.
3. Set up the event listener to handle changes in selections.
4. Render the autocomplete component and the selected languages list.

The choice of colors and attributes:
- The `multiple` attribute is used to allow multiple selections.
- The `label` attribute is set to "Programming Languages" to clearly indicate the purpose of the autocomplete component.
- The `placeholder` attribute is set to "Search for languages..." to guide the user.

```tsx
import React, { useState, useEffect } from 'react';
import { ModusAutocomplete } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const [selectedLanguages, setSelectedLanguages] = useState<string[]>([]);
  const options = [
    { id: '0', value: 'JavaScript' },
    { id: '1', value: 'Python' },
    { id: '2', value: 'Java' },
    { id: '3', value: 'C#' },
    { id: '4', value: 'C++' },
    { id: '5', value: 'Ruby' },
    { id: '6', value: 'Go' },
    { id: '7', value: 'Swift' },
    { id: '8', value: 'Kotlin' },
    { id: '9', value: 'PHP' }
  ];

  const handleSelectionsChanged = (event: CustomEvent<string[]>) => {
    const selectedIds = event.detail;
    const selectedValues = selectedIds.map((id) => {
      const language = options.find((option) => option.id === id);
      return language ? language.value : '';
    });
    setSelectedLanguages(selectedValues);
  };

  useEffect(() => {
    const languagesSearch = document.querySelector('#languages-search') as any;
    if (languagesSearch) {
      languagesSearch.options = options;
      languagesSearch.addEventListener('selectionsChanged', handleSelectionsChanged);
    }
    return () => {
      if (languagesSearch) {
        languagesSearch.removeEventListener('selectionsChanged', handleSelectionsChanged);
      }
    };
  }, [options]);

  return (
    <div style={{ width: '500px', padding: '16px', overflow: 'auto' }}>
      <ModusAutocomplete
        id="languages-search"
        label="Programming Languages"
        multiple
        placeholder="Search for languages..."
      />
      <div id="selected-languages" style={{ marginTop: '16px' }}>
        Selected Languages: {selectedLanguages.join(', ')}
      </div>
    </div>
  );
};

export default MyComponent;
```

## Prompt 3

**User Question:** Create a webpage with an autocomplete component that allows users to search for countries, includes a clear button, and displays an error message if no results are found?

**Agent Answer:**
References:
To create an autocomplete component that allows users to search for countries, includes a clear button, and displays an error message if no results are found, we will use the `ModusAutocomplete` component with the `clearable`, `showNoResultsFoundMessage`, `noResultsFoundText`, and `errorText` properties. The `clearable` property adds a clear button to the input field. The `showNoResultsFoundMessage` property ensures that a message is displayed when no results are found, and the `noResultsFoundText` property specifies the text for this message. The `errorText` property is used to display an error message if the user does not select a valid country.

```tsx
import React, { useState } from 'react';
import { ModusAutocomplete } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const options = [
    { id: '0', value: 'United States' },
    { id: '1', value: 'Canada' },
    { id: '2', value: 'Mexico' },
    { id: '3', value: 'United Kingdom' },
    { id: '4', value: 'Germany' },
    { id: '5', value: 'France' },
    { id: '6', value: 'Italy' },
    { id: '7', value: 'Spain' },
    { id: '8', value: 'Australia' },
    { id: '9', value: 'Japan' }
  ];

  return (
    <div style={{ width: '500px', padding: '16px', overflow: 'auto' }}>
      <ModusAutocomplete
        id="country-search"
        label="Country Search"
        placeholder="Search for a country..."
        options={options}
        clearable
        showNoResultsFoundMessage
        noResultsFoundText="No countries found"
        errorText="Please select a valid country"
      />
    </div>
  );
};

export default MyComponent;
```


# <ModusCheckbox>

## Prompt 1

**User Question:** Create a webpage with a checkbox labeled "Accept Terms" that logs the checked status to the console when clicked?
**Agent Answer:**
References:
To create a checkbox with the label "Accept Terms" and log its checked status to the console when clicked, we will use the `ModusCheckbox` component. We will add an event listener for the `checkboxClick` event to handle the logging.

```tsx
import React, { useEffect } from 'react';
import { ModusCheckbox } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const acceptTermsCheckbox = document.querySelector('#accept-terms') as HTMLElement | null;
    if (acceptTermsCheckbox) {
      acceptTermsCheckbox.addEventListener('checkboxClick', (event: CustomEvent<boolean>) => {
        console.log(`Checkbox is now ${event.detail ? 'checked' : 'unchecked'}`);
      });
    }
    return () => {
      if (acceptTermsCheckbox) {
        acceptTermsCheckbox.removeEventListener('checkboxClick', () => {});
      }
    };
  }, []);

  return (
    <div id="checkbox-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusCheckbox id="accept-terms" label="Accept Terms" />
    </div>
  );
};

export default MyComponent;
```

## Prompt 2
**User Question:** Create a webpage with three checkboxes. The first checkbox should be labeled "Option 1" and be checked by default. The second checkbox should be labeled "Option 2" and be disabled. The third checkbox should be labeled "Option 3" and be in an indeterminate state.
**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three checkboxes with different properties. The first checkbox should be labeled "Option 1" and be checked by default. The second checkbox should be labeled "Option 2" and be disabled. The third checkbox should be labeled "Option 3" and be in an indeterminate state. The approach involves using the `<ModusCheckbox>` component and setting the appropriate properties for each checkbox.

```tsx
import React from 'react';
import { ModusCheckbox } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="checkbox-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusCheckbox label="Option 1" checked />
      <ModusCheckbox label="Option 2" disabled />
      <ModusCheckbox label="Option 3" indeterminate />
    </div>
  );
};

export default MyComponent;
```

# <ModusDateInput>

## Prompt 1
**User Question:** Create a date range picker with the label "Travel Dates", where the start date input is labeled "Start Date" and the end date input is labeled "End Date"? Both inputs should use the format "dd-mm-yyyy" and display a calendar icon.

**Agent Answer:**
References:
Analyzing the requirements, we need to create a date range picker with specific labels for the picker and the start and end date inputs. Both inputs should use a specific format and display a calendar icon. The approach involves using the `<ModusDatePicker>` component to encapsulate two `<ModusDateInput>` components, one for the start date and one for the end date. The `label`, `format`, `helperText`, `allowedCharsRegex`, and `showCalendarIcon` properties are set to meet the specified requirements.

```tsx
import React, { useEffect } from 'react';
import { ModusDatePicker, ModusDateInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const datePicker = document.querySelector('modus-date-picker') as HTMLElement;
    if (datePicker) {
      const handleValueChange = (event: Event) => {
        const customEvent = event as CustomEvent<{ value: string }>;
        console.log('Date range changed:', customEvent.detail.value);
      };
      datePicker.addEventListener('valueChange', handleValueChange);
      return () => {
        datePicker.removeEventListener('valueChange', handleValueChange);
      };
    }
  }, []);

  return (
    <div style={{ padding: '16px', overflow: 'auto' }}>
      <ModusDatePicker label="Travel Dates">
        <ModusDateInput
          type="start"
          label="Start Date"
          format="dd-mm-yyyy"
          helperText="(dd-mm-yyyy)"
          allowedCharsRegex="[d-]"
          showCalendarIcon={true}
          value="2022-12-22"
        />
        <ModusDateInput
          type="end"
          label="End Date"
          format="dd-mm-yyyy"
          helperText="(dd-mm-yyyy)"
          allowedCharsRegex="[d-]"
          showCalendarIcon={true}
          value="2022-12-22"
        />
      </ModusDatePicker>
    </div>
  );
};

export default MyComponent;
```

# <ModusSelect>

## Prompt 1
**User Question:** Create a webpage with a select input labeled "Choose Option", a placeholder "Select an option", and marked as required. The options should be "Option A", "Option B", and "Option C". Log the selected option to the console when the value changes.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a select input with a label "Choose Option", a placeholder "Select an option", and it should be required. The options should be "Option A", "Option B", and "Option C". Additionally, we need to log the selected option to the console when the value changes.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusSelect } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const options = [{ display: 'Option A' }, { display: 'Option B' }, { display: 'Option C' }];
  const selectRef = useRef<any>(null);

  useEffect(() => {
    if (selectRef.current) {
      selectRef.current.options = options;
      selectRef.current.addEventListener('valueChange', handleValueChange);
    }

    return () => {
      if (selectRef.current) {
        selectRef.current.removeEventListener('valueChange', handleValueChange);
      }
    };
  }, []);

  const handleValueChange = (e: any) => {
    const selectedOption = e.detail;
    console.log(`Selected option: ${selectedOption.display}`);
  };

  return (
    <div>
      <ModusSelect
        ref={selectRef}
        label="Choose Option"
        placeholder="Select an option"
        required
        optionsDisplayProp="display"
      />
    </div>
  );
};

export default MyComponent;
```
## Prompt 2
**User Question:** Create a webpage with two select inputs. The first select input should have a label "Select Demo 1" and be disabled with helper text "Helper demo". The second select input should have a label "Select Demo 2" and display an error text "Error demo". Both should have options "Option 1", "Option 2", and "Option 3".

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create two select inputs. The first select input should have a label "Select Demo 1", be disabled, and have helper text "Helper demo". The second select input should have a label "Select Demo 2" and display an error text "Error demo". Both should have options "Option 1", "Option 2", and "Option 3". The approach involves using the `ModusSelect` component for rendering the select inputs and setting their properties accordingly.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusSelect } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const options = [{ display: 'Option 1' }, { display: 'Option 2' }, { display: 'Option 3' }];
  const select1Ref = useRef<any>(null);
  const select2Ref = useRef<any>(null);

  useEffect(() => {
    if (select1Ref.current) {
      select1Ref.current.options = options;
    }
    if (select2Ref.current) {
      select2Ref.current.options = options;
    }
  }, []);

  return (
    <div>
      <ModusSelect
        ref={select1Ref}
        label="Select Demo 1"
        disabled
        helperText="Helper demo"
        optionsDisplayProp="display"
      /><br />
      <ModusSelect
        ref={select2Ref}
        label="Select Demo 2"
        errorText="Error demo"
        optionsDisplayProp="display"
      />
    </div>
  );
};

export default MyComponent;
```
## Prompt 3
**User Question:** Create a webpage with a select input labeled "Select Size", with a size of "large", and valid text "Valid selection"? The options should be "Small", "Medium", and "Large". When the value changes, the selected value should be updated in the select input.

**Agent Answer:**
References:
To create a select input with the specified label, size, and valid text, we use the `<ModusSelect>` component. The options "Small", "Medium", and "Large" are provided as an array. We add an event listener to update the selected value when the value changes.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusSelect } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const options = [{ display: 'Small' }, { display: 'Medium' }, { display: 'Large' }];
  const selectRef = useRef<any>(null);

  useEffect(() => {
    if (selectRef.current) {
      selectRef.current.options = options;
      selectRef.current.addEventListener('valueChange', handleValueChange);
    }

    return () => {
      if (selectRef.current) {
        selectRef.current.removeEventListener('valueChange', handleValueChange);
      }
    };
  }, []);

  const handleValueChange = (e: any) => {
    const selectedOption = e.detail;
    if (selectRef.current) {
      selectRef.current.value = selectedOption.display;
    }
  };

  return (
    <div>
      <ModusSelect
        ref={selectRef}
        label="Select Size"
        size="large"
        validText="Valid selection"
        optionsDisplayProp="display"
      />
    </div>
  );
};

export default MyComponent;
```

# <ModusTextInput>

## Prompt 1
**User Question:** Create a form with three text input fields: a required "Username" field with a placeholder "Enter your username", an "Email" field with a placeholder "Enter your email" and an error state "Invalid email", and a "Password" field with a placeholder "Enter your password" and a password text toggle icon.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three text input fields with different labels, placeholders, and additional properties. The first field is a required field with a label "Username" and a placeholder "Enter your username". The second field is an email field with an error state and the text "Invalid email". The third field is a password field with a password text toggle icon.

```tsx
import React from 'react';
import { ModusTextInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="input-container1" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusTextInput label="Username" placeholder="Enter your username" required />
      <ModusTextInput label="Email" placeholder="Enter your email" errorText="Invalid email" />
      <ModusTextInput label="Password" placeholder="Enter your password" type="password" includePasswordTextToggle />
    </div>
  );
};

export default MyComponent;
```

## Prompt 2
**User Question:** Create a webpage with two text input fields. The first field should have a label "Search", a placeholder "Search here...", and should include a search icon. The second field should have a label "Description", a placeholder "Enter description", and should have helper text "Provide a brief description".

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create two text input fields with different labels, placeholders, and additional properties. The first field is a search field with a search icon and a placeholder "Search here...". The second field is a description field with helper text "Provide a brief description".

```tsx
import React from 'react';
import { ModusTextInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="input-container2" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusTextInput label="Search" placeholder="Search here..." includeSearchIcon />
      <ModusTextInput label="Description" placeholder="Enter description" helperText="Provide a brief description" />
    </div>
  );
};

export default MyComponent;
```

# ModusRadioGroup

## Prompt 1
**User Question:** Create a webpage with a radio group named "Favorite Fruit" containing three radio buttons labeled "Apple", "Banana", and "Cherry", with "Banana" selected by default, an ariaLabel "Fruit Selection", and size "small"?

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a radio group named "Favorite Fruit" with three radio buttons labeled "Apple", "Banana", and "Cherry". The "Banana" option should be selected by default. The radio group should have an ariaLabel "Fruit Selection" and size "small".

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusRadioGroup } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const radioGroupRef = useRef<any>(null);

  useEffect(() => {
    if (radioGroupRef.current) {
      radioGroupRef.current.radioButtons = [
        {
          id: '0',
          label: 'Apple',
        },
        {
          id: '1',
          checked: true,
          label: 'Banana',
        },
        {
          id: '2',
          label: 'Cherry',
        },
      ];
    }
  }, []);

  return (
    <ModusRadioGroup
      checkedId="1"
      name="favorite-fruit"
      ariaLabel="Fruit Selection"
      size="small"
      ref={radioGroupRef}
    ></ModusRadioGroup>
  );
};

export default MyComponent;
```


## Prompt 2
**User Question:** Create a webpage with a radio group named "Payment Method" containing three radio buttons labeled "Credit Card", "PayPal", and "Bank Transfer", with "Credit Card" selected by default, and log the selected payment method to the console whenever a radio button is clicked?

**Agent Answer:**
References:
To achieve the desired functionality, we need to create a radio group named "Payment Method" with three radio buttons labeled "Credit Card", "PayPal", and "Bank Transfer". The "Credit Card" option should be selected by default. Additionally, we need to log the selected payment method to the console whenever a radio button is clicked. The approach involves using the `ModusRadioGroup` component and setting up event listeners to handle the button click events.

```tsx
import React, { useEffect, useRef } from 'react';
import { ModusRadioGroup } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  const radioGroupRef = useRef<any>(null);

  useEffect(() => {
    if (radioGroupRef.current) {
      radioGroupRef.current.radioButtons = [
        {
          id: '0',
          checked: true,
          label: 'Credit Card',
        },
        {
          id: '1',
          label: 'PayPal',
        },
        {
          id: '2',
          label: 'Bank Transfer',
        },
      ];

      radioGroupRef.current.addEventListener('buttonClick', (event: any) => {
        const selectedButton = radioGroupRef.current.radioButtons.find(
          (button: any) => button.id === event.detail
        );
        console.log(`Selected payment method: ${selectedButton?.label}`);
      });
    }
  }, []);

  return (
    <ModusRadioGroup
      checkedId="0"
      name="payment-method"
      ref={radioGroupRef}
    ></ModusRadioGroup>
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

# <ModusTextareaInput>

## Prompt 1
**User Question:** Create a webpage with a textarea input field that has the following properties: 
- Label: "User Feedback"
- Placeholder: "Enter your feedback here..."
- Required: true
- Helper Text: "Please provide detailed feedback."
- Error Text: "Feedback is required."
- Valid Text: "Thank you for your feedback."
- Size: large
- Rows: 5
- Max Length: 500
- Min Length: 10
- Clearable: true
- Auto Focus: true
- Auto Correct: on
- Enter Key Hint: send
- Spell Check: true
- Text Align: left
- Value: "Initial feedback text"

**Agent Answer:** 
References:
Analyzing the requirements from the prompt, we need to create a textarea input field with various properties such as label, placeholder, required, helper text, error text, valid text, size, rows, max length, min length, clearable, auto focus, auto correct, enter key hint, spell check, text align, and value. 

The approach involves breaking down the properties and setting them accordingly in the <ModusTextareaInput> component. The choice of properties ensures that the textarea input field meets the user's requirements for feedback collection.

```tsx
import React from 'react';
import { ModusTextareaInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="textarea-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusTextareaInput
        label="User Feedback"
        placeholder="Enter your feedback here..."
        required
        helperText="Please provide detailed feedback."
        errorText="Feedback is required."
        validText="Thank you for your feedback."
        size="large"
        rows={5}
        maxLength={500}
        minLength={10}
        clearable
        autoFocusInput
        autocorrect="on"
        enterkeyhint="send"
        spellcheck
        textAlign="left"
        value="Initial feedback text"
      />
    </div>
  );
};

export default MyComponent;
```
## Prompt 2
**User Question:** Create a webpage with a textarea input field that has the following properties: 
- Label: "Comments"
- Placeholder: "Enter your comments..."
- Disabled
- Read Only
- Value: "This field is read-only and disabled."

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create a textarea input field with properties such as label, placeholder, disabled, read only, and value. The <ModusTextareaInput> component is used to achieve this. The label attribute sets the label of the textarea, the placeholder attribute sets the placeholder text, the disabled attribute makes the textarea non-interactive, the readOnly attribute ensures the content cannot be modified, and the value attribute sets the initial content of the textarea.

```tsx
import React from 'react';
import { ModusTextareaInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="textarea-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusTextareaInput
        label="Comments"
        placeholder="Enter your comments..."
        disabled
        readOnly
        value="This field is read-only and disabled."
      />
    </div>
  );
};

export default MyComponent;
```

# <ModusTimePicker>

## Prompt 1
**User Question:** Create a time picker with a label "Appointment Time", placeholder "12:00 AM", and helper text "hh:mm AM/PM" that uses the 12-hour format with AM/PM and includes a time zone selector with options "PST", "EST", and "CST"?

**Agent Answer:**
References:
To create a time picker with the specified requirements, we use the `<ModusTimePicker>` component for the time input and the `<ModusSelect>` component for the time zone selector. The time picker is configured to use the 12-hour format with AM/PM, and the time zone selector is populated with the options "PST", "EST", and "CST".The `<ModusTimePicker>` component is used to create the time input field with the specified label, placeholder, and helper text. The `ampm` attribute is set to `true` to enable the 12-hour format with AM/PM. The `<ModusSelect>` component is used to create the time zone selector, and its options are populated using the `useEffect` hook. The `optionsDisplayProp` attribute is set to "display" to ensure the options are displayed correctly.

```tsx
import React, { useEffect } from 'react';
import { ModusTimePicker, ModusSelect } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  useEffect(() => {
    const modusSelect = document.querySelector('#timezone') as any;
    modusSelect.options = [
      { display: 'PST' },
      { display: 'EST' },
      { display: 'CST' },
    ];
  }, []);

  return (
    <div id="timepicker-container2" style={{ padding: '16px', overflow: 'auto' }}>
      <ModusTimePicker
        label="Appointment Time"
        placeholder="12:00 AM"
        helperText="hh:mm AM/PM"
        ampm={true}
        autoFormat={true}
      >
        <div style={{ width: '300px', paddingLeft: '0.5rem' }} slot="timeZone">
          <ModusSelect id="timezone" label="Time Zone" ariaLabel="Time Zone" optionsDisplayProp="display" />
        </div>
      </ModusTimePicker>
    </div>
  );
};

export default MyComponent;
```

# <ModusNumberInput>

## Prompt 1
**User Question:** Create a webpage with three number input fields. The first input field should have a label "Salary", a placeholder "Enter your salary", and display the value in USD currency format for the locale "en-US". The second input field should have a label "Phone Number", an error text "Invalid number", and a placeholder "Enter your phone number". The third input field should have a label "Age", a valid text "Valid age", and a placeholder "Enter your age".

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three number input fields with different labels, placeholders, and additional properties. The first input field should display the value in USD currency format for the locale "en-US". The second input field should display an error text when the input is invalid. The third input field should display a valid text when the input is valid.

```tsx
import React from 'react';
import { ModusNumberInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="input-container1" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusNumberInput label="Salary" placeholder="Enter your salary" currency="USD" locale="en-US" value="50000" />
      <ModusNumberInput label="Phone Number" errorText="Invalid number" placeholder="Enter your phone number" />
      <ModusNumberInput label="Age" validText="Valid age" placeholder="Enter your age" />
    </div>
  );
};

export default MyComponent;
```
## Prompt 2

**User Question:** Create a webpage with two number input fields. The first input field should have a label "Quantity", a placeholder "Enter quantity", a helper text "Enter a number between 1 and 100", a minimum value of 1, and a maximum value of 100. The second input field should have a label "Discount", a placeholder "Enter discount", a step value of 0.01, and the text aligned to the right.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create two number input fields with different labels, placeholders, and additional properties. The first input field should have a helper text, a minimum value, and a maximum value. The second input field should have a step value and the text aligned to the right.

```tsx
import React from 'react';
import { ModusNumberInput } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="input-container2" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px', overflow: 'auto' }}>
      <ModusNumberInput 
        label="Quantity" 
        placeholder="Enter quantity" 
        helperText="Enter a number between 1 and 100" 
        minValue={1} 
        maxValue={100} 
      />
      <ModusNumberInput 
        label="Discount" 
        placeholder="Enter discount" 
        step={0.01} 
        textAlign="right" 
      />
    </div>
  );
};

export default MyComponent;
```

# <ModusToast>

## Prompt 1
**User Question:** Create a webpage with 3 toasts: a primary toast with "Welcome" text and dismissible, a success toast with "Operation Successful" text and an icon, and a danger toast with "Error Occurred" text and a 5000ms delay.

**Agent Answer:**
References:
Analyzing the requirements from the prompt, we need to create three toasts with different types, texts, and properties. The first toast is a primary toast with the text "Welcome" and should be dismissible. The second toast is a success toast with the text "Operation Successful" and should show an icon. The third toast is a danger toast with the text "Error Occurred" and should have a delay of 5000ms. The primary toast is used to welcome the user, the success toast indicates a successful operation, and the danger toast alerts the user of an error.

```tsx
import React from 'react';
import { ModusToast } from '@trimble-oss/modus-react-components';

const MyComponent: React.FC = () => {
  return (
    <div id="toast-container" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '16px' }}>
      <ModusToast type="primary" dismissible={true}>Welcome</ModusToast>
      <ModusToast type="success" show-icon={true}>Operation Successful</ModusToast>
      <ModusToast type="danger" delay={5000}>Error Occurred</ModusToast>
    </div>
  );
};

export default MyComponent;
```

