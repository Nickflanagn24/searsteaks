# Sear Steaks

![Django](https://img.shields.io/badge/Framework-Django-green?logo=django&logoColor=white)  
![Deployed on Heroku](https://img.shields.io/badge/Deployed-Heroku-purple?logo=heroku&logoColor=white)  
![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-blue)

---

A restaurant table booking system that allows customers to select a table from a visual floor plan and manage their reservations.

[🔗 View the Live Site Here](#) <!-- Replace # with your actual live site URL -->

---

---

## 📋 Table Of Contents
- [Sear Steaks](#sear-steaks)
- [Planning Phase](#planning-phase)
- [Structure & User Flow](#structure--user-flow)
- [Database Schema](#database-schema)
- [Surface: Branding & UI Design](#surface-branding--ui-design)
- [Features](#features)
- [Future Development](#future-development)
- [Testing Phase](#testing-phase)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Credits](#credits)

---

## Planning Phase

### Strategy

#### Site Aims

Managing restaurant reservations efficiently is crucial for both customers and restaurant owners. Traditionally, customers call or visit restaurants to book tables, which can lead to overbookings, miscommunication, and scheduling conflicts.

This web application aims to simplify and streamline the booking process by allowing:
- Customers to register, select a table from a floor plan, and manage their reservations.
- Admins (Restaurant Owners) to manage availability, prevent double bookings, and oversee reservations from a dashboard.

By implementing a visual floor plan, user authentication, and real-time table booking, this application ensures a smoother reservation process while preventing conflicts in scheduling.

### Opportunities

During the planning phase, various features were brainstormed. Using a feasibility chart, we prioritized the most important and viable functionalities.

| Opportunity                        | Importance | Viability/Feasibility |
|------------------------------------|------------|-----------------------|
| Customer login & registration      | 5          | 5                     |
| Select a table from a floor plan   | 5          | 5                     |
| Make & modify bookings             | 5          | 5                     |
| Admin dashboard for restaurant owners | 5      | 5                     |
| Prevent double bookings            | 5          | 5                     |
| Booking confirmation email         | 4          | 4                     |
| User profile for tracking bookings | 3          | 4                     |
| Mobile responsiveness              | 5          | 5                     |
| Display available tables in real-time | 4        | 4                     |
| Payment integration for reservations | 2        | 2                     |
| Customer reviews for restaurants   | 1          | 2                     |

### Scope

To ensure the project remains feasible within the given timeframe, we categorized features into three priority levels:

#### ✅ Must-Have (MVP) Features

These are essential to launch the Minimum Viable Product (MVP) and meet the core requirements:
- User Registration & Login (Customers & Admins).
- Table Selection from a Floor Plan (Real-time availability).
- Book, Modify, and Cancel Reservations.
- Admin Dashboard to Manage Bookings & Table Availability.
- No Double Booking Prevention.

#### 🟡 Should-Have Features

Features that improve usability and enhance the experience but are not essential for MVP:
- Booking Confirmation via Email.
- User Profile to View Booking History.
- Mobile-Friendly UI with Accessibility Considerations.

#### 🔴 Could-Have (Future Enhancements)

Features that are not a priority for the initial release but could be implemented later:
- Payment Integration for Table Reservations.
- Customer Reviews & Ratings.
- Loyalty System or Discounts for Returning Customers.

### Structure & User Flow

To map out the user journey, I created a flowchart that visualizes how users interact with the system.

![User Journey Diagram](bookings/static/images/readme-images/full_restaurant_user_journey.png)

#### User Flow Overview

- Landing Page → Customers & admins log in or register.
- Customer Dashboard → View available tables in a floor plan.
- Select a Table → Choose date, time, and number of guests.
- Confirm Booking → Receive confirmation via email.
- Modify or Cancel Booking → Customers can adjust reservations.
- Admin Dashboard → Manage reservations & prevent double bookings.

### User Stories

#### As an Admin, I Can...
- ✅ Log in to an Admin Dashboard to manage restaurant reservations.
- ✅ View all upcoming bookings in an organized manner.
- ✅ Update table availability and prevent double bookings.
- ✅ Modify or cancel bookings on behalf of customers.
- ✅ Ensure only valid users can make reservations through authentication.

#### As an Unregistered User, I Can...
- ✅ View restaurant details without needing an account.
- ✅ Register for an account to access booking features.

#### As a Registered Customer, I Can...
- ✅ Log in securely and manage my profile.
- ✅ Browse available tables in a floor plan and pick my preferred seat.
- ✅ Select a date & time and make a table reservation.
- ✅ Modify or cancel my booking before the scheduled time.
- ✅ Receive an email confirmation of my reservation.

#### As a System, It Will...
- ✅ Prevent double bookings by checking table availability in real-time.
- ✅ Send email notifications for booking confirmations.
- ✅ Display an intuitive UI for customers to navigate smoothly.

### Skeleton: Wireframes & UX Design

To create an intuitive User Experience (UX), wireframes were designed to ensure:
- A clean interface for customers to book tables easily.
- An efficient dashboard for admins to manage reservations.
- Accessibility considerations for all screen sizes.

📥 [Wireframes Links] (Include final link once uploaded)
home page wireframe 
booking wireframe 
menu wireframe
contact wire

### Database Schema

To ensure data is well-structured and easily retrievable, the following database schema was planned:

| Table Name | Fields |
|------------|--------|
| User       | id (PK), username, email, password, phone_number, role (customer/admin) |
| Table      | id (PK), table_number, capacity, is_available |
| Booking    | id (PK), user_id (FK), table_id (FK), date, time, guests |

### Surface: Branding & UI Design

#### Color Scheme

This is the colour scheme I will use. I used coolors.co to create the colour scheme
![Sear Steaks Color Palette](bookings/static/images/readme-images/colour_scheme.png)

A modern, restaurant-friendly color palette was chosen using Coolors.co, ensuring:
- ✅ High contrast for readability.
- ✅ Warm & inviting tones to reflect a comfortable dining experience.
- ✅ Consistent branding across all pages.

#### Typography

- Primary Font: Lato – Clean & readable.
- Secondary Font: Playfair Display – Elegant touch for headings.

### Final Notes

This planning phase ensures that the restaurant booking web application aligns with Agile methodology, MVC structure, and the project assessment criteria.

---

# ✨ Features

## Site Navigation
### Navbar
- **Brand Identity**: The Sear Steaks logo prominently displayed in the top-left corner serves as a home button across all pages.
- **Responsive Design**: The navigation automatically transforms from a horizontal menu to a hamburger dropdown on mobile and tablet devices.
- **Authentication-Based Navigation**:
  - Logged-out users: Home, Menu, About, Contact, Login, and Register.
  - Logged-in customers: Home, Menu, About, Contact, My Bookings, and Logout.
  - Admin users: Additional Admin Dashboard link.
- **Hover Effects**: Subtle animation on hover for tactile feedback.

## Hero Section
- **Dynamic Hero Images**: Unique hero image per page.
- **Call-to-Action Buttons**: "Reserve Your Table" button leading to booking page.
- **Overlay Text**: Highlighting restaurant’s identity: "Authentic BBQ flavors, grilled to perfection."

## User Authentication
### Registration System
- Clean, straightforward registration form.
- Form validation and error handling.
- Redirection to login on successful registration.

### Login System
- Secure authentication (Django built-in).
- Remember Me functionality.
- Login verification and protected routes.

### Profile Management
- Display and manage user details.
- View booking history.
- Update contact information.

## Main Page Content
### Homepage
- Welcome Section with intro text.
- About Section: Restaurant story and quality commitment.
- Menu Preview with call-to-action button.
- Contact Preview with basic info.
- Visual Appeal: High-quality images.

## Floor Plan & Table Selection
- Interactive layout of restaurant seating.
- Color-coded tables (availability shown visually).
- Table details like capacity and location.
- Easy click-to-select process.
- Availability filters by date/time.

## Booking Form
- Calendar date selection.
- Time slot selection.
- Party size input.
- Special requests field.
- Real-time validation.
- Booking summary confirmation.

## Booking Management
- Reservation list view.
- Modify or cancel reservations.
- Booking details page.
- Visual status indicators (confirmed, pending, past).

## Menu Page
- Categorized sections (Appetizers, Mains, Sides, Desserts).
- Descriptive food items.
- Pricing info.
- Featured dishes highlighted.
- Visual food images.

## Contact Page
- Address info with Google Map embed.
- Business hours displayed clearly.
- Phone, email, and contact form.
- Social media links.

## Admin Features
### Admin Dashboard
- Overview statistics.
- Quick access to booking and table management.
- Today's bookings focus.
- Notifications for pending actions.

### Bookings Management
- Full booking list with filters.
- Booking details view.
- Status management (confirm, seat, cancel, complete).
- Customer search functionality.
- Customer booking history view.

### Table Management
- Table status overview.
- Availability control.
- Capacity management.
- Reassign bookings to different tables.

## Responsive Design
- Mobile-first layout strategy.
- Flexible grids adapting to screen sizes.
- Touch-friendly interactive elements.
- Responsive images.
- Accessible, readable typography.
- Simplified navigation for smaller devices.

---

# 🔮 Future Development
- Payment Integration
- Customer Reviews
- Loyalty Program
- Menu Pre-ordering
- Staff Scheduling
- Google Calendar API Sync

---

# 🧪 Testing Phase

For detailed information about testing methodologies, validation results, and bug reports, please see the [comprehensive testing documentation](TESTING.md).

## Code Validation
- HTML5: W3C Validator
- CSS3: W3C Validator
- JavaScript: JSHint
- Python: PEP8 Standards

## Browser Testing
- Chrome, Firefox, Safari, Edge
- Mobile device testing

## User Story Testing
- Functional testing against user stories
- Edge case testing

## Lighthouse Testing
- Performance
- Accessibility
- Best Practices
- SEO scores

## Known Bugs
- [List any known issues here]

---

# 🚀 Deployment

## Local Deployment

```bash
git clone https://github.com/Nickflanagn24/searsteaks.git
python -m venv venv
# Activate environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
```
