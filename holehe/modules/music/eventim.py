from holehe.core import *

async def eventim(email, client, out):
    name = "eventim"
    domain = "eventim.com"
    method = "email_check"
    frequent_rate_limit = True

    # Define the URL and headers for the POST request
    url = f'https://www.eventim.com/api/customers/{email}/password?affiliate=US1'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'If-Modified-Since': '0',
        'X-XSRF-TOKEN': 'FE5D01410621E01EA99E64847BF240AD',
        'Origin': 'https://www.eventim.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.eventim.com/mycustomerdata/',
        'Cookie': 'SameSite=None; dd=1; webid=VVMxNEk1Q05LQzNLMDM5NDc0NjI2NDlOX0VO; webshop=YW1vdW50PTAmYW1vdW50X2V2aWRzPTAmY3VycmVuY3lfY29kZT1VU0QmY3VycmVuY3lfc3ltYm9sPSUyNCZkZXZpY2VfaW5mbz0wJmV2aWRzX2luX2NhcnQ9JmV2b19teWNsdWJzX21lbWJlcj0ma2V5PXZwYkFKNHJ6RXI3ZiZrcHNfdXJsPSZsYW5ndWFnZT1lbiZsb2NhbGU9ZW5_fdXMmbG9naW49MCZtZXJraXRlbXM9MCZwa2lkc19pbl9jYXJ0PSZwcmljZT0wLjAwJnByaWNlX2Zvcm1hdHRlZD0wLjAwJnJhbmRvbT0zMDY5MSZyZWZlcmVyPWh0dHBzJTNBJTJGJTJGd3d3LmV2ZW50aW0uY29tJTJGJnJlc2VydmF0aW9uX2R1cmF0aW9uPTAmdGlja2V0YW1vdW50X3ByaWNlc19wa2lkPQ==; _abck=27D1AFCE7A80EAAE74128294B5F02BB5~0~YAAQPY8UApzQYEiKAQAAhD3JSQpHFOG/azZZpjZCo+gFYar5ZV+4Wg+QrxQ9Of0aE5IbPU4CN3W37tZQfkiRAFWUXr6595g22lFAA3Ldiets7K841ENONaxOfpMgOP+/Yutwe+G4UWktPhPPfvwKdirOC2hnywCAeEumXbvo3rlKJiRZonSbWT0467dT00xqcDLzDdtwTHbCtjLX5oD6Vt5tkJnOKMM+umGpPt7cRV5amcBIW8O8MMLUFQGXYaWjCxhFth+M4kCjgQAXfmUXXStrA4vFxPwpRZqRj3LY08xUEzTQsnJrrVxq1t2O7FkM+4+TTH5K6ieXeXK/g+BKo5QOLqUn2LucoxpTVfmmRBaH4eqkRaTRUD+4NbqKjv8+DHjL/YdFVmsuvmW3zUxNQD63G//DCx4f5g==~-1~||1-CTSBpcubDk-1-10-1000-2||~1693458617; ak_bmsc=A1C7F861F56D236E28DD66BBE898BC4F~000000000000000000000000000000~YAAQPY8UApXQYEiKAQAAxy7JSRQZQSfoXr7icPf/6MUQc6h3TViDSERWCPyTQoOmw7mEZ2/gRYDWu/Zy5OOlME1qmQ0vY+LLS8P1Q4aKh5zc2TybilB8hZPXzfG2JBRf16Ze69wKXrIY/mIKze/tTrRCCZuRT7pokagJOAejgozYgE0oVgn08hLd8YSFSutHuILt5OCJaAWs1rhUbP6Y0kWj3KTK2rCuFq0dy2xUDjEW54KRLjaa3vf8vlyEuAAPnjMnrAmTgitU6qLZln/u8jpdK5+0c7Lc+2/PDmcduTcVPwkn9jHwt7hDG9H18TcTsxreBAX/sGmakcT68vh21tgx7HBKSdHDwujYwz0yUBfb972LTpj7Doz+B9Svq9QomEsxRHuv7e4M//PaTs5R4LiMgx6XRWdeLdm547/4FJTZ3A==; bm_sz=2D2AE5F2134CED42583DD35FFECEDC07~YAAQPY8UApfQYEiKAQAAxy7JSRTY2Ocl89/qGW1e3KCWA7mhbT8rKsP/a1Fg6SVn3lk8IweMcCguSyUNLKp94XM2cBL9lKeX2zjZgfJZ6vb7+/3cS3cAx1uLRDmMymkrU4sUVrJ8BusgG+ATMjhwU5HG0L8GwGU34x38S/k6ivj07Ivp088/bsBkIGQtdouCOcmUdl9pwDMsleZWFey5tUKk8ZMMHGw2/mCpBZqykI5NMtJHlU1e9wzqEqQE9hEcBbdKJlO91rs5veKbDZvKgGKypxkhtVwQfRiGJLjcMJzJqiKX~3223617~3162675; __cmpiuid=e9a9425e2ba0b4e2a6a860ee8abacbc2; __cmpcvcx36865=__s2100_s94_c24102_c24103_s23_c9953_c21289_s7_s1_s26_s2612_s135_s1104_s905_s24_s1465_s1049_s11_s2493_s2536_s34_s30_U__; __cmpcpcx36865=__1_2_3__; __cmpcvc=__s2100_s94_c24102_c24103_s23_c9953_c21289_s7_s1_s26_s2612_s135_s1104_s905_s24_s1465_s1049_s11_s2493_s2536_s34_s30_U__; __cmpcpc=__1_2_3__; __cmpiab=__264_10_506_89_21_32_25_; __cmpiabli=__264_10_506_89_21_32_25_; __cmpccpausps=1YNN; __cmpconsentx36865=BPxYLuWPxYLuWAfNhBENABAAAAAfqAHAAUABUADIAIAAsgEIAP0A; permInfo=1693301517209696640A31082023A31082023; bm_mi=CF1B81E09775735D04BED88DABCA6C95~YAAQPY8UAiPRYEiKAQAAo3XJSRQ1k6F5bn2NNaCbPdxAKgRU8rVjTNeUcs6Uq+KYVIxFlCS+fn62JZ8DYAmTjZMatCS2Bd/PhhP4LUoWv+GQl/1Wka6ewewE5jLxjuzhuWPoEnGuzDJ/qVw6aSMhI7GeTjnPrZjPRcieGMkeZtt1GRx0dwKRFF7mgbKcdb2gm3Vt0asuSaO8w6vpWSwXB9kF2Yi0UHLpY+kVNyTvTmN9hdQoTk0bEb5GKyEs8FyTHHLPa9u0jug5YmXk64uZIFnZ63mvP6YR+E5Wkii1TtSJIfFhVJPISrwl1hbtuPvyMsI2pOXLYmXGj1+WVIk=~1; bm_sv=1B174636DB66F0040AFE582BABF3C9EF~YAAQPY8UArPRYEiKAQAAkdbJSRTPHo0Zmko+JfSZMJV5hnekS9Kw/bb8GLCFm0wDMo4X6xdNpcEBmHBBBOSNoK/B6pKAw44Ft+TdkqddcK4FqMrRBfINr333jeWKr+fE0XNeEhOCOFl6lqju/9UVhSDWatv64D3vHYGhr48KwnUrwthCbX4Rm+JHTaa7kAIVe2yVg/i5iIjI/P25gT4dYR2dfBZS47BeAKOC8xK91iTpNgi5YNDfKLAAO3bxGuClJQ==~1; ADRUM_BTa=R:39|g:130af965-d8b2-46c8-bd16-8276dd68a908|n:customer1_3aa627d9-4de0-48ca-a644-db85ae91343a',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Content-Length': '0',
        'TE': 'trailers'
    }

    # Send the POST request to Eventim
    response = await client.post(url, headers=headers)

    # Check the response and add results to 'out'
    if 'Please check your inbox for an email with link to reset your password.' in response.text:
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
    elif 'Unfortunately that email address is not registered with us.' in response.text:
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
        # Handle unexpected response here
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
