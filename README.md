# calculator
https://calculator-9135.onrender.com/

<img width="1911" height="875" alt="image" src="https://github.com/user-attachments/assets/293c80dd-3b81-412f-a6c0-2be19c6af8d3" />

# Step-by-Step Process: Django Calculator Project
---

## Step 1: Problem Identification

The objective of this project was to develop a **simple web-based calculator** that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The project aims to demonstrate the use of **Python Django framework**, server-side processing, and a clean user interface.

---

## Step 2: Requirement Analysis

The following requirements were identified:

* Python 3.10 or above
* Django web framework
* Web browser
* Basic knowledge of HTML and CSS

Functional Requirements:

* Accept two numerical inputs from the user
* Allow selection of arithmetic operation
* Display the calculated result

Non-Functional Requirements:

* Simple and user-friendly interface
* Responsive and visually appealing design
* Error handling for invalid inputs

---

## Step 3: Environment Setup

1. Python was installed and verified using the command:

   ```
   python --version
   ```
2. A virtual environment was created to isolate project dependencies:

   ```
   python -m venv env
   ```
3. The virtual environment was activated.
4. Django was installed using:

   ```
   pip install django
   ```

---

## Step 4: Creating the Django Project

A new Django project was created using the following command:

```
django-admin startproject server
```

This generated the core project structure including `settings.py`, `urls.py`, and `manage.py`.

---

## Step 5: Creating the Calculator App

A dedicated Django app named `calculator` was created to handle calculator logic:

```
python manage.py startapp calculator
```

The app was then registered in the project’s `INSTALLED_APPS` section.

---

## Step 6: URL Configuration

URL routing was configured so that the calculator page loads at the home URL:

* Project-level URLs forward requests to the calculator app
* App-level URLs map requests to the appropriate view function

This ensures proper navigation and request handling.

---

## Step 7: Implementing Business Logic (Views)

The calculator logic was implemented inside a Django view function. This view:

* Accepts user input through an HTML form
* Performs arithmetic operations based on user selection
* Handles invalid input using exception handling
* Sends the calculated result back to the template

---

## Step 8: Designing the User Interface (Templates)

HTML templates were created to display the calculator interface. The interface includes:

* Input fields for numbers
* Dropdown menu for operator selection
* Submit button to perform calculation
* Result display section

Templates were placed inside the app’s `templates` directory following Django standards.

---

## Step 9: Enhancing UI with CSS, Icons, and Animations

To make the project visually appealing:

* Gradient background and glassmorphism effects were applied
* Font Awesome icons were added for calculator symbols
* CSS animations such as floating icons, hover effects, and smooth transitions were implemented

This improves user experience and makes the project presentation-ready.

---

## Step 10: Error Handling and Testing

The application was tested for:

* Valid numeric inputs
* Division by zero
* Invalid or empty inputs

Errors were handled gracefully to prevent application crashes.

---

## Step 11: Creating `requirements.txt`

A `requirements.txt` file was added to specify project dependencies, making deployment and installation easier.

---

## Step 12: Running and Final Testing

The application was executed using:

```
python manage.py runserver
```

The calculator was accessed through the browser and tested thoroughly to ensure correct functionality and UI responsiveness.

---

## Step 13: Final Review

The project was reviewed to ensure:

* Clean code structure
* Proper folder organization
* Aesthetic user interface
* Compatibility with college project standards
