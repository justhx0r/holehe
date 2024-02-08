from holehe.core import *
from holehe.localuseragent import *


async def deutschlandticket(email, client, out):
    name = "deutschlandticket.de"
    domain = "deutschlandticket.de"
    method = "register"
    frequent_rate_limit=False

    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': 'application/json',
        'Accept-Language': 'de_DE',
        'Referer': 'https://www.deutschlandticket.de/',
        'Content-Type': 'application/json',
        'Origin': 'https://deutschlandticket.de',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    response = await client.post(
        'https://deutschlandticket.de/api/v2/auth/register/check-email?email=',
        headers=headers,
        data={"email":email})
    data = response.json()
    out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rateLimit": False,
                    "exists": data["is_already_in_use"],
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
