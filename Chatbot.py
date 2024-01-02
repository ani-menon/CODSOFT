import re

def customer_service_bot(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()

    # Define patterns for different types of queries
    password_reset_pattern = re.compile(r'\bpassword\b|\bforgot\b|\breset password\b')
    business_hours_pattern = re.compile(r'\bbusiness hours\b|\bopening hours\b')
    return_policy_pattern = re.compile(r'\breturn\b|\breturn policy\b')
    contact_support_pattern = re.compile(r'\bcontact\b|\bcustomer support\b')
    promotions_pattern = re.compile(r'\bpromotions\b|\bdiscounts\b')
    order_status_pattern = re.compile(r'\border status\b|\bwhere is my order\b')
    payment_methods_pattern = re.compile(r'\bpayment\b|\bpayment methods\b')
    update_account_pattern = re.compile(r'\bupdate\b|\baccount information\b')
    products_services_pattern = re.compile(r'\bproducts\b|\bservices\b')

    # Match user input to patterns and generate responses
    if password_reset_pattern.search(user_input_lower):
        return "To reset your password, visit our password reset page [insert link]."
    elif business_hours_pattern.search(user_input_lower):
        return "Our business hours are Monday to Friday, 9 AM to 5 PM."
    elif return_policy_pattern.search(user_input_lower):
        return "You can find information about our return policy [insert link]."
    elif contact_support_pattern.search(user_input_lower):
        return "You can contact our customer support at support@example.com or call us at +1-555-555-5555."
    elif promotions_pattern.search(user_input_lower):
        return "Check out our current promotions and discounts [insert link]."
    elif order_status_pattern.search(user_input_lower):
        return "To check the status of your order, please provide your order number."
    elif payment_methods_pattern.search(user_input_lower):
        return "We accept various payment methods, including credit cards and PayPal."
    elif update_account_pattern.search(user_input_lower):
        return "To update your account information, log in to your account and navigate to the settings page."
    elif products_services_pattern.search(user_input_lower):
        return "We offer a variety of products/services, including [brief overview]."

    # Default response for unrecognized queries
    return "I'm sorry, I didn't understand that. Please ask another question or check our FAQs."

# Example usage:
while True:
    user_input = input("Enter Query: ")
    response = customer_service_bot(user_input)
    print(response)

