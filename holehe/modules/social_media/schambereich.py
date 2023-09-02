from holehe.core import *

async def schambereich(email, client, out):
    name = "schambereich"
    domain = "schambereich.org"
    method = "email_check"
    frequent_rate_limit = True

    # Define the URL and headers for the POST request
    url = 'https://schambereich.org/lost-password'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://schambereich.org',
        'Connection': 'keep-alive',
        'Referer': 'https://schambereich.org/lost-password',
        'Cookie': 'popunder=1; PHPSESSID=8clrdbkv6bskamp9e63690vae3',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'DNT': '1',
        'Sec-GPC': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
        'user_lost_password[username]': email,
        'user_lost_password[_token]': 'a9851489f06b666e2882.c89kheiWJzHvEDYKi6AbC38R55S4XuGob_rdRarp9oU.Gboi54vlSgbfVV8-8pd4VBdLiPGPJJP3F9e8LMCHorZCtzzAv8ETYppzAg'
    }

    # Send the POST request to schambereich.org
    response = await client.post(url, headers=headers, data=data)

    # Check if the response contains the string 'Account wurde nicht gefunden'
    if 'Account wurde nicht gefunden' in response.text:
        out.append({
            "name": name,
            "domain": domain,
            "method": method,
            "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": False,
            "exists": False,
            "emailrecovery": None,
            "phoneNumber": None,
            "others": None
        })
    else:
        out.append({
            "name": name,
            "domain": domain,
            "method": method,
            "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": False,
            "exists": True,
            "emailrecovery": None,
            "phoneNumber": None,
            "others": None
        })
