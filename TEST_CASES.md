# Zomato Automation Test Cases

This document outlines the test cases implemented in the `tests/` directory. These tests cover the core functionalities of the Zomato web application including Authentication, Restaurant Search, Filtering, Table Booking, and Restaurant Details.

---

## 1. Authentication

### 1.1 Login
**Test Case ID**: TC_AUTH_001  
**Test File**: `tests/test_login.py`  
**Description**: Verify that a user can initiate the login process using a phone number.  
**Pre-conditions**: User is on the Zomato home page.  
**Steps**:
1. Open the Zomato delivery page (`https://www.zomato.com/bangalore/delivery`).
2. Click on the "Log in" button.
3. Switch to the Login iframe.
4. Enter a valid phone number (`7019035690`).
5. Click on "Send One Time Password".

**Expected Result**: The OTP is sent to the phone number, and the user is prompted to enter the OTP.

---

### 1.2 Sign Up
**Test Case ID**: TC_AUTH_002  
**Test File**: `tests/test_sign.py`  
**Description**: Verify that a new user can sign up by providing necessary details.  
**Pre-conditions**: User is on the Zomato home page.  
**Steps**:
1. Open the Zomato delivery page (`https://www.zomato.com/bangalore/delivery`).
2. Click on the "Sign up" button.
3. Enter a valid Full Name (`Venkateshwar Shavi`).
4. Enter a valid Email address (`vshavi060@gmail.com`).
5. Select the Terms and Conditions checkbox.
6. Click on "Create Account".

**Expected Result**: The account creation process is initiated (or OTP is requested).

---

## 2. Restaurant Search

### 2.1 Search Restaurant by Location and Name
**Test Case ID**: TC_SEARCH_001  
**Test File**: `tests/test_resto.py`  
**Description**: Verify that a user can search for a specific restaurant in a specific location.  
**Pre-conditions**: User is on the Zomato restaurants page.  
**Steps**:
1. Open the Zomato restaurants page (`https://www.zomato.com/bangalore/restaurants`).
2. Enter location (`Kengeri Upanagara, Bengaluru, India`) in the location search bar and press Enter.
3. Enter restaurant name (`Hotel Gowdru Mane`) in the search bar and press Enter.
4. Wait 2 seconds for search results to load.
5. Select the restaurant from the search results.

**Expected Result**: The user is navigated to the details page of the selected restaurant.

---

## 3. Filtering and Sorting

### 3.1 Apply Multiple Filters (Rating & Cuisine)
**Test Case ID**: TC_FILTER_001  
**Test File**: `tests/test_filter.py`  
**Description**: Verify that a user can apply multiple filters including rating sort and cuisine filter.  
**Pre-conditions**: User is on the Zomato restaurants page.  
**Steps**:
1. Open the Zomato restaurants page.
2. Click on the "Filters" button.
3. Click on "Sort by".
4. Select "Rating: High to Low".
5. Click "Apply".
6. Switch to "Dining Out" tab.
7. Click on "Filters" again.
8. Click on "Cuisines".
9. Search for "Indian" cuisine.
10. Select the "North Indian" checkbox.
11. Apply the cuisines filter.
12. Click on rating filter to verify filtering options.

**Expected Result**: The restaurant list is filtered and sorted according to the selected criteria (high rated North Indian restaurants displayed).

---

## 4. Table Booking (Dining Out)

### 4.1 Book a Table at Specific Restaurant
**Test Case ID**: TC_BOOK_001  
**Test File**: `tests/test_spot.py`  
**Description**: Verify that a user can complete the flow to book a table at RCB Bar & Cafe.  
**Pre-conditions**: User is on the Zomato main website.  
**Steps**:
1. Open the Zomato main site.
2. Click on "Dining Out" or "Book a Spot".
3. Enter location (`Brigade Road, Bangalore`).
4. Enter restaurant name (`RCB Bar & Cafe`).
5. Click the search button.
6. Navigate to "Book a Table" button and click it.
7. Select a Date from the dropdown.
8. Select the Number of Guests.
9. Select "Dinner" time slot.
10. Select a specific time slot.
11. Choose an offer (if available).
12. Click "Cart" to proceed.
13. Wait 9 seconds for confirmation.

**Expected Result**: The booking details are added to the cart/summary, and the user can view the booking confirmation.

---

## 5. Restaurant Details & Contact

### 5.1 View Empire Restaurant Details and Contact
**Test Case ID**: TC_RESTO_001  
**Test File**: `tests/test_empireresto.py`  
**Description**: Verify that a user can navigate to a specific restaurant, view contact details, and handle alert dialogs.  
**Pre-conditions**: User is on the Zomato website.  
**Steps**:
1. Open the Zomato restaurants page with delivery category filter (`https://www.zomato.com/bangalore/restaurants?category=1`).
2. Click on "Delivery" button to ensure correct category.
3. Scroll down 500 pixels.
4. Wait 3 seconds for content to load.
5. Click on "Empire Restaurant - Since 1966".
6. Click on the phone number link (`+917026610096`).
7. Wait 5 seconds for the alert to appear.
8. Accept/dismiss the browser alert box.

**Expected Result**: 
- User successfully navigates to Empire Restaurant details page.
- Phone number is clickable and triggers an alert.
- Alert is successfully handled (accepted).

---

## Test Execution Notes

### Prerequisites
- Selenium WebDriver
- Chrome browser with ChromeDriver
- pytest and pytest-html
- Internet connection

### How to Run Tests

**Run all tests:**
```bash
pytest --html=report.html --self-contained-html
```

**Run specific test:**
```bash
pytest tests/test_empireresto.py --html=report.html --self-contained-html
```

**Run using batch file:**
```bash
run_tests.bat
```

### Test Data
- **Login Phone**: 7019035690
- **Sign Up Name**: Venkateshwar Shavi
- **Sign Up Email**: vshavi060@gmail.com
- **Search Location**: Kengeri Upanagara, Bengaluru, India
- **Search Restaurant**: Hotel Gowdru Mane
- **Booking Location**: Brigade Road, Bangalore
- **Booking Restaurant**: RCB Bar & Cafe
- **Empire Restaurant Phone**: +917026610096
