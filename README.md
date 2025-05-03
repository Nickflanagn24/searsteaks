# 🥩 Sear Steaks

![Django](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Made_with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Heroku](https://img.shields.io/badge/Deployed_on-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> An elegant restaurant table booking system that allows customers to select a table from a visual floor plan and manage their reservations.

[🔗 View the Live Site](https://searsteaks-22b7c7084bd1.herokuapp.com/)

---

---

## 📋 Table of Contents

<details>
  <summary>Click to expand</summary>
  
  - [Overview](#overview)
  - [Planning Phase](#planning-phase)
    - [Strategy](#strategy)
    - [Opportunities](#opportunities)
    - [Scope](#scope)
  - [Structure & User Flow](#structure--user-flow)
  - [Database Schema](#database-schema)
  - [Surface: Branding & UI Design](#surface-branding--ui-design)
  - [Features](#features)
    - [Navigation](#site-navigation)
    - [User Authentication](#user-authentication)
    - [Homepage](#homepage)
    - [Floor Plan & Table Selection](#floor-plan--table-selection)
    - [Booking Management](#booking-management)
    - [Menu Page](#menu-page)
    - [Contact Page](#contact-page)
    - [Admin Features](#admin-features)
  - [Future Development](#future-development)
  - [Testing Phase](#testing-phase)
  - [Deployment](#deployment)
  - [Technologies Used](#technologies-used)
  - [Credits](#credits)
</details>

---

## 📖 Overview

Sear Steaks is a sophisticated restaurant booking system designed to enhance both the customer experience and restaurant operations. The platform offers an intuitive interface where customers can visualize the restaurant layout, select their preferred table, and manage their reservations—all while the restaurant maintains control over availability and prevents double bookings.

**Key Features:**
- Interactive floor plan with real-time table availability
- Secure user authentication for customers and staff
- Comprehensive booking management system
- Visual menu with detailed dish information
- Admin dashboard for restaurant management

---

## Planning Phase

## 🎯 Strategy

### Site Aims

Managing restaurant reservations efficiently is crucial for both customers and restaurant owners. Traditionally, customers call or visit restaurants to book tables, which can lead to overbookings, miscommunication, and scheduling conflicts.

This web application aims to:
- ✅ Allow customers to select tables visually from a floor plan
- ✅ Provide real-time availability information
- ✅ Enable customers to manage their own reservations
- ✅ Give restaurant staff powerful tools to prevent scheduling conflicts
- ✅ Create a seamless, elegant booking experience

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

### Site Navigation

<details>
  <summary>Click to expand navigation details</summary>

#### Navbar
- **Brand Identity**: The Sear Steaks logo prominently displayed in the top-left corner serves as a home button across all pages.
- **Responsive Design**: The navigation automatically transforms from a horizontal menu to a hamburger dropdown on mobile and tablet devices.
- **Authentication-Based Navigation**:
  - Logged-out users: Home, Menu, About, Contact, Login, and Register.
  - Logged-in customers: Home, Menu, About, Contact, My Bookings, and Logout.
  - Admin users: Additional Admin Dashboard link.
- **Hover Effects**: Subtle animation on hover for tactile feedback.
</details>

###  User Authentication

## Registration System
I implemented a clean registration system using Django's authentication framework with custom extensions for our restaurant needs. I built a UserRegisterForm class extending Django's UserCreationForm to collect essential customer information while maintaining a straightforward interface. My server-side validation ensures proper email formatting, enforces password strength requirements, and verifies email uniqueness. I handled error states comprehensively, displaying field-specific validation messages to guide users. After successful registration, my system redirects users to the login page with a confirmation message to create a seamless onboarding flow.

## Login System
For the login system, I utilized Django's secure authentication backend with several enhancements. I created a standard login form with email/password fields and implemented "Remember Me" functionality using Django's secure session handling. I protected all authentication with Django's CSRF middleware and added custom middleware that enforces HTTPS in production environments. I secured routes using the @login_required decorator and built custom permission checks for sensitive functionality. My error handling provides clear feedback for authentication failures, and successful logins intelligently redirect users to their intended destination or default dashboard.

## Management
I developed a comprehensive profile management section that gives users control over their personal information. I built a profile view displaying user details and created a UserUpdateForm for handling profile updates. For data security, I leveraged Django's password hashing and implemented appropriate database field protection for sensitive information. I created a booking history component that displays the user's reservations in a paginated, chronological list with clear status indicators. To ensure data protection, I added permission checks that verify users can only view and modify their own information, and implemented validation to prevent unauthorized field modifications.

# Main Page Content
## Homepage
1. Welcome Section with Intro Text
This section establishes initial visitor orientation with a concise introduction to the restaurant concept. It uses a clean, branded container with a prominent heading and brief paragraph that marketing can easily update through the CMS. Developers benefit from its simple structure and consistent positioning, while visitors get immediate context about the restaurant's identity before exploring further.

2. About Section: Restaurant Story and Quality Commitment
Implemented as a two-column layout pairing compelling imagery with restaurant history and values, this section builds emotional connection through storytelling. The content management system allows non-technical staff to update the narrative without developer assistance, while the structured layout maintains visual consistency. This section effectively justifies premium pricing by highlighting quality ingredients and unique culinary approaches.

3. Menu Preview with Call-to-Action Button
This grid-based preview displays 3-4 signature dishes pulled directly from the restaurant's menu database, ensuring it stays automatically updated when menu items change. Each item includes an appetizing image, brief description, and price point, with a prominent call-to-action button directing users to the full menu. The component reuses the same data structure as the main menu page, simplifying maintenance and providing valuable click-tracking data on user journey patterns.

4. Contact Preview with Basic Info
This lightweight section displays essential location information (address, hours, phone) and a small map preview, answering common practical questions without requiring navigation to the full contact page. It pulls from a centralized contact information database, ensuring consistency across the site when details change. By reducing friction for users seeking basic location information, it improves user experience while maintaining fast page performance.

5. Visual Appeal: High-Quality Images
Professional food photography and atmosphere shots throughout the homepage create emotional appeal and quality perception, implemented with modern image optimization techniques to maintain fast loading speeds. The system serves appropriate image sizes to different devices, uses lazy loading for below-the-fold content, and incorporates structured data markup for SEO enhancement. Consistent image styling (aspect ratios and color treatment) reinforces brand identity while careful optimization balances visual quality against performance requirements.

## Floor Plan & Table Selection
- Interactive layout of restaurant seating.
- Color-coded tables (availability shown visually).
- Table details like capacity and location.
- Easy click-to-select process.
- Availability filters by date/time.

# Booking Form
## Interactive Layout of Restaurant Seating
In the implementation, each table is an interactive component that maintains selection state through JavaScript event handlers. When users click on a table, event listeners update both the visual state (adding a 'selected' class) and track the selection in a form input value. The system pulls table data (including positions, capacity, and table numbers) from the Django models, specifically the Table model which stores all relevant table attributes.

Restaurant management can modify table arrangements through the Django admin interface, where they can update positions, change table status (active/inactive), or adjust capacity without requiring developer intervention for layout changes. This database-driven approach ensures the floor plan stays current with the actual restaurant configuration.

## Color-Coded Table Availability
The system implements real-time visual feedback through color coding that instantly communicates table status. Available tables display in green, booked tables in red and when modify the booking the curretn table will be yellow. This status information updates dynamically based on the currently selected date and time, pulling availability data from the booking database. When users change their desired reservation time, the system re-queries availability and updates all table colors without a full page reload using AJAX. This immediate visual feedback helps users quickly identify suitable options without having to try multiple tables or times.

## Table Details Display
When users hover over or click on a table, the system displays a tooltip or info panel showing critical details: table number, seating capacity, location characteristics (window, booth, bar-adjacent, etc.), and any special features. This implementation uses event listeners on table elements to trigger the detail display. The detail component pulls data from the table configuration database, including both static information (capacity, type) and dynamic data (availability time slots). This detailed information helps customers make informed selections based on their specific needs without cluttering the main visual interface.

## Click-to-Select Process
The table selection process uses an intuitive click-based interaction model where users first select their desired date/time, then click on an available table to select it. The system implements a clear selection state with visual feedback (highlighting, checkmark icon) to confirm the user's choice. When a table is selected, the system temporarily reserves it for a short period (typically 10-15 minutes) to prevent double-bookings during the completion of the reservation form. This reservation timer is implemented using a background job that releases the hold if the booking isn't completed within the time window. This approach balances user convenience with system efficiency.

## Availability Filters by Date/Time
The availability filtering system is implemented with calendar and time selector components that trigger availability updates throughout the floor plan. The date selector uses a calendar widget that restricts selection to valid booking dates (typically excluding past dates and limiting how far in advance bookings can be made). The time selector offers standard reservation slots based on the restaurant's operating hours and reservation policies. When users change either date or time selections, the system makes an API call to the backend that:

1) Queries the booking database for existing reservations during the selected timeframe
2) Returns a comprehensive availability map for all tables
3) Updates the visual display to reflect current availability

The system also implements conflicts detection to prevent double-bookings, table capacity validation to ensure party size fits the selected table, and duration management for restaurants with fixed seating times. For performance optimization, availability data for popular times may be cached temporarily, with cache invalidation occurring when new bookings are made.

The floor plan system represents a significant technical achievement in the application, creating a visual, intuitive booking experience that dramatically improves upon traditional form-based reservation systems. Its real-time nature and visual feedback mechanisms help customers quickly find suitable tables while reducing the cognitive load of the booking process. From a business perspective, it also tends to distribute bookings more evenly throughout the restaurant rather than concentrating them in a few "preferred" tables, improving overall table utilization.

# Booking Management
The system queries the database for bookings associated with the authenticated user's ID, then renders them in a responsive table format sorted by date, with the most recent bookings appearing first. Each reservation row displays essential information including reservation date, time, guest count, table number, and status. The implementation uses Django's class-based ListView with pagination handling approximately 10 bookings per page to maintain interface performance even for customers with extensive booking history.

## Modify or Cancel Reservations
The system provides in-line action buttons for each eligible reservation (those in the future that haven't yet occurred). For modifications, the code implements a form that pre-populates with existing booking details, allowing customers to adjust date, time, guest count, or special requests. When submitted, the system runs availability checks to ensure the modified booking doesn't conflict with existing reservations. For cancellations, a confirmation modal appears to prevent accidental cancellations, and upon confirmation, the system updates the booking status in the database and releases the table for other customers. The repository shows these actions are implemented using Django form handling with appropriate permission checks to ensure users can only modify their own reservations.

## Booking Details Page
The booking details page displays comprehensive information about a specific reservation. According to the repository code, this view is implemented using a Django DetailView that retrieves the Booking model instance and passes it to a template. The page shows all reservation details including date, time, guest count, table information (including location within the restaurant), any special requests, and a booking reference number. For upcoming bookings, the page includes a dynamic map highlighting the selected table on the restaurant floor plan, giving customers a visual reminder of their table location. The implementation includes permission checks to ensure users can only view details of their own bookings.

## Visual Status Indicators
The booking management system implements clear visual status indicators using color-coded badges and icons to communicate reservation status. The code shows that each booking is assigned a status (confirmed, pending, completed, or cancelled) that determines its visual presentation. Confirmed bookings display with green badges, pending with yellow/orange, past completed bookings with blue, and cancelled with gray. These status indicators are implemented through conditional CSS classes in the template based on the booking status field in the database. The system automatically updates booking status through backend processes - marking bookings as completed after their date has passed and handling status changes when modifications occur. This visual approach allows customers to quickly assess their booking status without reading detailed text.

# Menu Page
## Categorized Sections
Based on the repository code, the menu page organizes food items into distinct categories using Django's model relationships. The system implements a Category model with fields for name, display order, and description. Each MenuItem in the database belongs to a specific category through a ForeignKey relationship. The view queries these categories in their specified display_order and passes them to the template, which renders each category as a separate section with appropriate headings (Appetizers, Mains, Sides, Desserts, etc.). This database-driven approach allows restaurant management to reorganize, add, or remove menu categories without requiring code changes.

## Descriptive Food Items
The menu items are implemented using a MenuItem model that includes detailed fields for comprehensive dish descriptions. According to the repository code, each item stores a name, short_description, detailed_description, ingredients list, and allergy_information. The template renders these descriptive elements using semantic HTML with appropriate styling for hierarchy and readability. Special dietary indicators (vegetarian, vegan, gluten-free) are implemented as boolean fields on the model and displayed as icons next to applicable dishes. This structured approach ensures consistent formatting while providing customers with thorough information about each dish's composition and preparation.

## Pricing Information
The MenuItem model includes a decimal price field that stores the current price of each dish. The repository shows that these prices are displayed with appropriate currency formatting using Django's template filters. For items with variable pricing (such as market-price seafood), the system implements a special_price_text field that displays alternative text instead of a fixed price. Additionally, the code shows implementation of a separate PriceRange model for items with multiple size options, allowing display of price ranges rather than single values for applicable items. The pricing display is positioned consistently for each menu item to facilitate easy comparison.

## Featured Dishes Highlighted
The repository implements a featured_item boolean field on the MenuItem model to designate special dishes. Featured items receive visual emphasis on the menu page through distinct styling, including highlight borders, background colors, or special positioning. The template code shows these items may be displayed in a separate "Chef's Recommendations" or "House Specialties" section at the top of the menu page, or they may be highlighted within their respective categories. The system also appears to support limited-time offerings through start_date and end_date fields, allowing seasonal specials to automatically appear and disappear from the menu at predetermined times.

## Visual Food Images
The menu system includes support for dish photography through an ImageField on the MenuItem model. Based on the repository code, not all items have images, but feature dishes typically include high-quality photographs. The implementation uses responsive image techniques to serve appropriately sized images based on device characteristics. Images are displayed with consistent aspect ratios and formatting, typically showing the plated dish from an appealing angle. When users click on menu items with images, the system appears to implement a lightbox effect to display larger versions with more detail. The template implementation follows accessibility best practices with appropriate alt text generated from the dish name and description.

# Contact Page
## Address Information with Google Map Embed
Based on the repository code, the contact page implements location information with a functional Google Maps integration. The system stores the restaurant's address components (street, city, state, post code) in the SiteSettings model, which provides a single source of truth for this information across the website. The map is embedded using an iframe that loads Google Maps with the restaurant's coordinates and a marker at the exact location. According to the template file, the map implementation includes responsive sizing to properly display across different devices, and uses the loading="lazy" attribute to improve page performance. The mapping functionality appears to be initialized with a specific zoom level focused on the restaurant's neighborhood to provide context about surrounding areas. The map isn't pointing to where the restuarant is as it doesnt exisit.

## Business Hours Display
The contact page shows operating hours in a structured format, drawing data from the BusinessHours model in the database. Each day's hours are rendered in a clean, easy-to-read layout with clear differentiation between days. The implementation handles special cases like "Closed" days and split hours (e.g., lunch and dinner services with a break in between). According to the repository, the system also includes handling for holiday hours or special schedules through a separate SpecialHours model that overrides regular hours when applicable. The hours are displayed prominently on the page to ensure visitors can quickly find this essential information.

## Phone, Email and Contact Form
The page provides multiple contact methods, prominently displaying the restaurant's phone number and email address retrieved from the SiteSettings database model. The contact form is implemented using Django's forms framework with fields for name, email, subject, and message content. Form validation includes required field checks, email format validation, and spam prevention measures like a hidden honeypot field. According to the views.py file, form submissions are processed to both store the inquiry in the database (ContactMessage model) and send notification emails to restaurant staff. The system also sends an automated acknowledgment email to the customer confirming their inquiry was received.

## Social Media Links
The contact page includes links to the restaurant's social media profiles, implemented as icons with appropriate labels for accessibility. According to the repository code, these social media URLs are stored in the SiteSettings model, allowing them to be updated site-wide from a single location when needed. The implementation uses recognizable platform icons (Facebook, Instagram, Twitter, etc.) with proper external link attributes including rel="noopener" for security. The social media section appears to be positioned prominently, typically in the page footer or alongside other contact information, to encourage social engagement and provide alternative communication channels for customers.

# Admin Features

## Admin Dashboard

## Quick Access to Booking and Table Management
The dashboard provides a navigation panel with direct links to frequently used management functions. According to the templates and URL configuration, these quick-access controls include buttons for creating new bookings, managing tables, viewing customer records, and generating reports. Each control is implemented as a card with an icon and descriptive text, organized in a grid layout that prioritizes common tasks. The implementation follows a task-based organization rather than a module-based approach, focusing on streamlining administrator workflows.

## Booking Details View
When administrators select a booking, the system displays a detailed view with complete reservation information. Based on the templates and view functions, this includes customer contact details, special requests, booking history, and table assignment. The implementation organizes this information into logical sections with appropriate headings and visual separation. 

## Customer Booking History View
When viewing customer information, the system presents a complete booking history for that guest. According to the templates and view functions, this includes past, current, and future reservations displayed in chronological order.

# Table Management
## Table Status Overview
The table management section provides a visual overview of all tables and their current status. Based on the repository code, this is implemented as a grid or list view showing each table with indicators for availability, capacity, reservation status, and any maintenance issues. The implementation uses color coding to clearly communicate table status at a glance – available, reserved, occupied, or out of service. According to the JavaScript files, this view updates periodically to reflect current restaurant conditions.

## Availability Control
The system allows administrators to manually control table availability through a simple interface. Based on the models.py file, tables can be marked as unavailable for specific date ranges or recurring time slots (for example, to accommodate staff meals or maintenance). The implementation includes a calendar-style interface for selecting dates and times.

## Capacity Management
Administrators can adjust table capacity settings through the management interface. Each table record includes fields for minimum and maximum capacity, default configuration (e.g., standard setup vs. extended). The implementation includes validation to ensure capacity settings align with physical constraints and restaurant policies. These settings directly affect the availability logic in the booking system, determining which tables appear as options for different party sizes.

The admin panel can be accessed at [here](https://searsteaks-22b7c7084bd1.herokuapp.com/admin)

---

# 🔮 Future Development

## Core Feature Enhancements

<details>
  <summary>Near-Term Improvements</summary>
  
- **💰 Payment Integration** - Implement deposit system for bookings to reduce no-shows and establish no-show limits
- **⭐ Customer Reviews** - Enable diners to leave feedback and ratings
- **🏆 Loyalty Program** - Reward repeat customers with points and special benefits
- **🍽️ Menu Pre-ordering** - Allow customers to select meals in advance
- **👨‍👩‍👧‍👦 Staff Scheduling** - Integrate employee management with booking volumes
- **📅 Google Calendar API Sync** - Synchronize bookings with customers' calendars
- **📊 Enhanced Admin Analytics** - Add filtering options and statistical reporting
- **🖼️ Menu Management** - Give administrators visual editing tools for menu items
</details>

## Email Integration and Notifications

<details>
  <summary>Comprehensive Communication System</summary>

A sophisticated email system will maintain consistent engagement with customers throughout their Sear Steaks journey, delivering timely information and marketing communications.

### Account Management Communications
- **✅ Registration Confirmation:** Immediate verification emails with activation links
- **👋 Welcome Series:** Automated sequence introducing new users to booking features
- **🔑 Password Recovery:** Secure reset process with time-limited tokens
- **🔔 Account Updates:** Notifications for profile changes and security settings

### Reservation Communications
- **📝 Booking Confirmation:** Detailed reservation acknowledgments
- **⏰ Booking Reminders:** Configurable alerts 24-48 hours before reservation
- **🔄 Modification Notifications:** Immediate updates when reservation details change
- **❌ Cancellation Confirmations:** Clear messaging about policies and deposits
- **🙏 Post-Dining Follow-up:** Thank you messages with review requests

### Customer Relationship Management
- **🎂 Birthday/Anniversary Greetings:** Automated recognition with exclusive offers
- **👋 Re-engagement Campaigns:** Targeted outreach to inactive customers
- **💯 Loyalty Program Updates:** Regular statements of points and rewards
- **🌟 VIP Communications:** Personalized messaging for high-value customers
- **📋 Feedback Requests:** Customized surveys for specific dining experiences

### Marketing Communications
- **🍽️ Menu Launches:** Previews of new items with rich imagery
- **🎉 Special Event Invitations:** Notifications for tastings and themed dinners
- **🏷️ Exclusive Promotions:** Limited-time offers for registered customers
- **🎄 Holiday Reminders:** Early notifications about holiday availability
- **📰 General Newsletter:** Regular updates with preference management

### Technical Implementation
- **🛡️ Delivery Optimization:** DKIM/SPF implementation for improved deliverability
- **👤 Advanced Personalization:** Dynamic content based on customer history
- **📊 Performance Analytics:** Open rate tracking and A/B testing framework
- **⚙️ Admin Control Panel:** Visual template editor and campaign scheduling tools
- **☁️ Scalable Infrastructure:** Cloud-based email service integration
</details>

## Social Media Integration and Sharing

<details>
  <summary>Enhanced Social Sharing Capabilities</summary>

A comprehensive social media system will transform customers into brand ambassadors, creating organic promotion and word-of-mouth marketing for the restaurant.

### Reservation Sharing
- **📣 Booking Announcements:** One-click sharing to social platforms
- **🎨 Digital Invitation Cards:** Branded graphics for upcoming dining plans
- **👥 Group Coordination:** Tools to tag friends joining the reservation
- **⏱️ Countdown Timers:** Widgets displaying time until reservation
- **📍 Location Check-ins:** Integration with social location services
- **🗺️ Table Preview:** Shareable visualization of table location

### Dining Experience Sharing
- **📸 Photo Enhancement:** Filters optimized for food photography
- **🏷️ Menu Item Tagging:** Direct links to specific menu items
- **👨‍🍳 Chef Recognition:** Option to tag kitchen staff for exceptional dishes
- **🎊 Experience Templates:** Sharing formats for special occasions
- **⚡ Real-time Sharing:** In-app posting functionality
- **🖥️ Social Media Walls:** Displays showing recent customer posts

### Post-Dining Engagement
- **🎖️ Visit Badges:** Digital achievements for dining milestones
- **⭐ Review Integration:** Simplified sharing to review platforms
- **✨ Experience Highlights:** Auto-generated visit summaries
- **📅 Memory Timelines:** Personalized history of dining experiences
- **⏳ Return Countdowns:** Reminders of upcoming reservations

### Platform Optimization & Tools
- **📱 Platform-Specific Content:** Tailored formats for Instagram, Facebook, Twitter
- **✨ Content Enhancement:** Professional photo filters and suggested hashtags
- **🎁 Social Incentives:** Loyalty points and contests for engaging content
- **🔍 Brand Monitoring:** Tools to track mentions and analyze sentiment
</details>

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

<details>
  <summary>Local Deployment Instructions</summary>

1. Clone the repository:
   ```bash
   git clone https://github.com/Nickflanagn24/searsteaks.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Mac/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in a .env file:
   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   CLOUDINARY_URL=your_cloudinary_url
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

</details>

## Heroku Deployment
Prerequisites
Heroku account
Heroku CLI installed
PostgreSQL add-on (will be added during deployment)
Cloudinary account for media storage
### Steps
1) Log in to Heroku CLI:

heroku login

2) Create a new Heroku app:

heroku create sear-steaks

Or use the Heroku dashboard to create a new app.

3) Add PostgreSQL database:

heroku addons:create heroku-postgresql:hobby-dev

4) Set environment variables in Heroku:

heroku config:set SECRET_KEY=your_secret_key
heroku config:set DEBUG=False
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set CLOUDINARY_URL=your_cloudinary_url
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com

5) Create a Procfile in the project root (if not already present):

web: gunicorn restaurant_booking.wsgi

6) Ensure requirements.txt includes gunicorn and other production dependencies:

pip freeze > requirements.txt

7) Deploy to Heroku manually (first time):

git push heroku main

8) Run migrations on Heroku:

heroku run python manage.py migrate

9) Create a superuser on Heroku:

heroku run python manage.py createsuperuser

## GitHub Integration and Continuous Deployment
### Connect GitHub Repository to Heroku

1) Go to the Heroku Dashboard and select your app.
2) Navigate to the "Deploy" tab.
3) In the "Deployment method" section, select "GitHub".
4) Connect to your GitHub account if not already connected.
5) Search for and select the repository "Nickflanagn24/searsteaks".
6) Choose the branch you want to deploy ("main").

## Set Up Automatic Deployments

1) In the "Automatic deploys" section, check "Enable Automatic Deploys".
2) Click "Enable Automatic Deploys".

