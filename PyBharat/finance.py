# banking_finance.py

def what_is_rbi():
    """Explains what the Reserve Bank of India is and its role."""
    return (
        "The Reserve Bank of India (RBI) is India's central banking institution "
        "that regulates the issue and supply of the Indian rupee and oversees monetary policy. "
        "It controls inflation, interest rates, foreign exchange, and credit systems."
    )

def types_of_bank_accounts():
    """List different types of bank accounts in India with details."""
    return {
        "Savings Account": "For individuals to deposit savings. Offers interest and ATM card access.",
        "Current Account": "For businesses with frequent transactions. No interest but unlimited usage.",
        "Recurring Deposit": "Monthly fixed deposits for fixed period with interest.",
        "Fixed Deposit": "Lump sum deposit for fixed tenure with higher interest.",
        "Jan Dhan Account": "Zero-balance government savings account for financial inclusion."
    }

def explain_upi():
    """Describe UPI (Unified Payments Interface) and how it works in India."""
    return (
        "UPI (Unified Payments Interface) is a real-time payment system developed by NPCI. "
        "It enables inter-bank transfers instantly using a mobile number or VPA (e.g., name@upi). "
        "Users can scan QR codes, send/receive funds, and automate payments. Widely used via apps like PhonePe, GPay, BHIM, Paytm."
    )

def list_public_sector_banks():
    """Return a list of major public sector banks in India."""
    return [
        "State Bank of India (SBI)",
        "Punjab National Bank (PNB)",
        "Bank of Baroda (BOB)",
        "Canara Bank",
        "Indian Bank",
        "Union Bank of India"
    ]

def list_private_banks():
    """List private sector Indian banks."""
    return [
        "HDFC Bank",
        "ICICI Bank",
        "Axis Bank",
        "Kotak Mahindra Bank",
        "IndusInd Bank",
        "Yes Bank"
    ]

def explain_kcc():
    """Explain the Kisan Credit Card (KCC) Scheme."""
    return (
        "Kisan Credit Card (KCC) scheme provides farmers with timely access to short-term credit. "
        "They can withdraw funds to buy seeds, fertilizers, tools, etc., and repay post-harvest. "
        "The scheme helps reduce dependence on informal moneylenders."
    )

def benefits_of_jan_dhan():
    """List benefits of Pradhan Mantri Jan Dhan Yojana accounts."""
    return [
        "Zero balance savings account",
        "Free RuPay debit card",
        "Accidental insurance up to ₹2 lakh",
        "Overdraft facility",
        "Direct Benefit Transfer (DBT) for subsidies"
    ]

def digital_wallets_in_india():
    """List digital wallets and their features."""
    return {
        "Paytm": "Used for UPI, recharges, shopping, and bill payments",
        "PhonePe": "Offers UPI and direct account linking",
        "Google Pay": "Simple UPI interface, auto-bill pay",
        "Amazon Pay": "Used on Amazon purchases, cashback deals",
    }

def explain_ifsc_code():
    """What is IFSC Code and how it is used."""
    return (
        "IFSC (Indian Financial System Code) is an 11-character alphanumeric code used to identify bank branches. "
        "Used in NEFT, RTGS, IMPS transfers to ensure correct routing of funds."
    )

def atm_transaction_limit():
    """Show common ATM withdrawal limits."""
    return {
        "SBI": "₹20,000/day from basic account",
        "HDFC": "₹25,000/day from savings account",
        "Axis": "₹40,000/day for premium account",
    }

def explain_neft_rtgs_imps():
    """Explain NEFT, RTGS, and IMPS systems in India."""
    return {
        "NEFT": "Batch-based fund transfer. Settles in hourly slots.",
        "RTGS": "Real-Time Gross Settlement. For high-value transfers (₹2L+).",
        "IMPS": "Immediate Payment Service. 24x7 fast transfers using mobile or IFSC."
    }

def check_pan_linked_to_aadhaar(pan_number):
    """Simulate checking if a PAN card is linked to Aadhaar."""
    if pan_number.startswith("A") or pan_number.startswith("B"):
        return "Your PAN is linked to Aadhaar."
    else:
        return "PAN not linked to Aadhaar."

def explain_mutual_funds():
    """Briefly explain mutual funds in India."""
    return (
        "Mutual funds pool money from investors to invest in stocks, bonds, or other assets. "
        "Managed by fund managers via AMCs like SBI MF, HDFC MF, Axis MF. Returns depend on market."
    )

def types_of_insurance():
    """Types of insurance common in Indian financial planning."""
    return {
        "Life Insurance": "Pays sum assured to nominee after death.",
        "Health Insurance": "Covers medical bills and hospitalization.",
        "Vehicle Insurance": "Covers car/bike damage or theft.",
        "Term Insurance": "Pure protection plan with high cover at low premium."
    }

def describe_loan_types():
    """Types of loans offered in Indian banks."""
    return {
        "Home Loan": "To buy a house or property.",
        "Education Loan": "To study in India or abroad.",
        "Personal Loan": "Unsecured loan for emergencies.",
        "Gold Loan": "Loan against gold ornaments.",
        "Agricultural Loan": "For farmers to buy seeds, tools, or irrigation."
    }

def get_atm_charges():
    """Display typical ATM usage charges."""
    return (
        "First 5 ATM withdrawals in a month are free. After that, ₹21 per transaction. "
        "Charges may differ for non-home bank ATMs."
    )

def epfo_portal_features():
    """List features of EPFO (Employees Provident Fund Organization)."""
    return [
        "View PF balance",
        "Raise withdrawal request",
        "Download UAN card",
        "Track claim status",
        "E-Nomination"
    ]

def list_major_ipo_companies():
    """List companies that had famous IPOs in India."""
    return [
        "LIC of India",
        "Zomato",
        "Nykaa",
        "Paytm",
        "TCS",
        "IRCTC"
    ]

def explain_gst_in_india():
    """Explain GST (Goods and Services Tax)."""
    return (
        "GST is a unified indirect tax replacing multiple taxes. "
        "It applies to goods/services sold in India. Types: CGST, SGST, IGST."
    )

def rbi_interest_rate_policy():
    """Describe how RBI controls repo and reverse repo rates."""
    return (
        "RBI uses repo rate to control inflation and liquidity. "
        "If repo rate is high, loans are expensive, controlling inflation. "
        "If repo is low, borrowing becomes easier, boosting growth."
    )

def income_tax_slabs():
    """Return simplified income tax slabs."""
    return {
        "Up to ₹3L": "Nil",
        "₹3L – ₹6L": "5%",
        "₹6L – ₹9L": "10%",
        "₹9L – ₹12L": "15%",
        "₹12L – ₹15L": "20%",
        "Above ₹15L": "30%"
    }

def track_indian_stock_index():
    """Returns current indices (mock values)."""
    return {
        "Nifty 50": "20,123.00 (up 0.55%)",
        "Sensex": "67,305.21 (up 0.48%)"
    }

def ppf_account_info():
    """Describe PPF (Public Provident Fund)."""
    return (
        "PPF is a long-term savings scheme by the Government of India with 7.1% interest (as of 2025). "
        "Tenure is 15 years, with tax-free interest. Ideal for retirement."
    )

def sukanya_samriddhi_features():
    """Features of Sukanya Samriddhi Yojana for girl child."""
    return [
        "For girl child below 10 years",
        "Interest ~7.6% annually",
        "Deposit up to ₹1.5L/year",
        "Tax benefit under 80C",
        "Maturity at 21 years or marriage"
    ]

def mobile_number_update_simulation(aadhar_number):
    """Simulate mobile update for Aadhaar-linked account."""
    if len(aadhar_number) == 12:
        return "Mobile number linked successfully to Aadhaar."
    return "Invalid Aadhaar number."

def list_major_fintech_startups():
    """List Indian fintech unicorns and startups."""
    return ["Razorpay", "Groww", "Zerodha", "CRED", "BharatPe", "MobiKwik"]

def explain_credit_score():
    """Explain what credit score is and why it matters."""
    return (
        "Credit score is a 3-digit number between 300 and 900 used to evaluate your loan repayment ability. "
        "A score above 750 is considered good. Checked via CIBIL or Experian."
    )

def pmjjby_details():
    """Pradhan Mantri Jeevan Jyoti Bima Yojana insurance scheme details."""
    return {
        "Eligibility": "18–50 years",
        "Premium": "₹436/year",
        "Cover": "₹2 lakh on death",
        "Linked to": "Savings Bank Account"
    }

def apy_scheme_info():
    """Atal Pension Yojana for unorganized workers."""
    return (
        "Government-backed pension scheme for people aged 18–40. "
        "Monthly contributions provide pension up to ₹5,000 after age 60."
    )

def check_eligibility_for_pm_awaas(income, owns_home):
    """Check eligibility for PM Awas Yojana based on basic criteria."""
    if income < 600000 and not owns_home:
        return "Eligible for PMAY housing scheme."
    return "Not eligible."

def investment_options_for_students():
    """Low-risk, small-budget investment ideas for Indian students."""
    return ["Recurring deposit", "Mutual funds SIP", "Gold ETFs", "Digital gold", "NPS"]

def know_your_customer_process():
    """KYC: Know Your Customer process details."""
    return [
        "Submit PAN and Aadhaar",
        "Address proof (utility bills, rental agreement)",
        "Passport size photo",
        "Face authentication (video KYC)"
    ]

def generate_vpa(account_holder_name):
    """Create a fake UPI ID for demo purposes."""
    return f"{account_holder_name.lower()}@upi"

def describe_module():
    """Full overview of this banking_finance module."""
    return (
        "This module provides deep insight into Indian financial systems, digital banking, "
        "government schemes, and investment platforms. It simulates UPI, Aadhaar linking, credit scoring, "
        "RBI operations, tax systems, ATM networks, digital wallets, and much more. It’s built to reflect Bharat’s modern financial progress."
    )