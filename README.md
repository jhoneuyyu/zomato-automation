# Zomato Automation Testing Framework

A comprehensive Selenium-based automation testing framework for the Zomato web application, covering authentication, restaurant search, filtering, and table booking functionalities.

## 📋 Features

- **Authentication Testing**: Login and Sign-up flows
- **Restaurant Search**: Location-based restaurant search with filters
- **Filtering & Sorting**: Multi-criteria filtering (cuisine, rating, etc.)
- **Table Booking**: End-to-end table reservation flow
- **Restaurant Details**: Contact information and alert handling
- **HTML Reports**: Comprehensive test execution reports with pytest-html

## 🛠️ Tech Stack

- **Python 3.x**
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **Webdriver Manager** - Automatic driver management
- **Pytest-HTML** - HTML test reports

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/zomato-automation.git
   cd zomato-automation
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Run All Tests
```bash
pytest --html=report.html --self-contained-html
```

### Run Specific Test File
```bash
pytest tests/test_login.py --html=report.html --self-contained-html
pytest tests/test_filter.py --html=report.html --self-contained-html
pytest tests/test_spot.py --html=report.html --self-contained-html
```

### Run Using Batch File (Windows)
```bash
run_tests.bat
```

## 📂 Project Structure

```
zomato-automation/
├── pages/                          # Page Object Model classes
│   ├── empireRestaurant_page.py   # Empire Restaurant page actions
│   ├── filter_page.py             # Filter and sort functionality
│   ├── login_page.py              # Login page actions
│   ├── resto_page.py              # Restaurant search actions
│   ├── sign_page.py               # Sign-up page actions
│   └── spot_page.py               # Table booking actions
├── tests/                          # Test files
│   ├── test_empireresto.py        # Empire Restaurant tests
│   ├── test_filter.py             # Filtering tests
│   ├── test_login.py              # Login tests
│   ├── test_resto.py              # Restaurant search tests
│   ├── test_sign.py               # Sign-up tests
│   └── test_spot.py               # Table booking tests
├── utils/                          # Utility modules
│   └── driver_setup.py            # WebDriver configuration
├── conftest.py                     # Pytest configuration
├── requirements.txt                # Project dependencies
├── TEST_CASES.md                   # Detailed test case documentation
└── README.md                       # This file
```

## 📝 Test Cases

Detailed test cases are documented in [TEST_CASES.md](TEST_CASES.md)

### Test Coverage:
- ✅ **TC_AUTH_001**: Login with phone number
- ✅ **TC_AUTH_002**: New user sign-up
- ✅ **TC_SEARCH_001**: Search restaurant by location and name
- ✅ **TC_FILTER_001**: Apply multiple filters (rating & cuisine)
- ✅ **TC_BOOK_001**: Book a table at specific restaurant
- ✅ **TC_RESTO_001**: View restaurant details and contact

## 📊 Test Reports

After running tests, an HTML report (`report.html`) is generated in the root directory with:
- Test execution summary
- Pass/Fail status for each test
- Execution time
- Error details (if any)

## 🔧 Configuration

### WebDriver Setup
The framework uses `webdriver-manager` to automatically manage ChromeDriver. Configuration is in `utils/driver_setup.py`.

### Test Data
Test data (phone numbers, locations, restaurant names) can be found in individual test files or in [TEST_CASES.md](TEST_CASES.md).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is for educational and testing purposes.

## 👤 Author

**Venkateshwar Shavi**

## 🙏 Acknowledgments

- Zomato for the web application
- Selenium WebDriver community
- Pytest community

