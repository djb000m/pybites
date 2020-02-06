#!/usr/bin/env python

## 26/11/19 - This currently does not work.
## I think this is an issue from Cisco's end.

import requests

# from requests.exceptions import HTTPError


def nxapi_show_version():
    switch_url = "https://sbx-nxos-mgmt.cisco.com"
    switchuser = "admin"
    switchpassword = "Admin_1234!"

    http_headers = {"content-type": "application/json-rpc"}
    payload = [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "show version", "version": 1},
            "id": 1,
        }
    ]

    # 1. use requests to post to the switch
    response = requests.post(
        url=switch_url,
        json=payload,
        headers=http_headers,
        auth=(switchuser, switchpassword),
        verify=False,
    )

    # version = response["result"]["body"]["kickstart_ver_str"]
    # return version
    # with requests.session() as session:
    #     session.auth = (switchuser, switchpassword)

    #     try:
    #         # run a POST request on the switch URL
    #         response = session.post(
    #             url=switch_url,
    #             data=json.dumps(payload),
    #             headers=http_headers,
    #             verify=False,
    #         )
    #         # response.raise_for_status()
    #     except HTTPError as http_err:
    #         print(f"\nHTTP error occurred: {http_err}\n")
    #         return False
    #     except TimeoutError as timeout_err:
    #         print(f"\nRequest timed out: {timeout_err}\n")
    #         return False
    #     except Exception as err:
    #         print(f"\nOther error occurred: {err}\n")
    #         return False
    #     else:
    #         # no errors... continue
    #         # 2. retrieve and return the kickstart_ver_str from the response
    #         # example response json:
    #         # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #         #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #         #                      'kickstart_ver_str': '9.2(1)',
    #         #                      ...
    #         #                      }
    #         #             }
    #         # }
    #         version = response.json()["result"]["body"]["kickstart_ver_str"]
    #         return version

    version = response.json()["result"]["body"]["kickstart_ver_str"]
    return version


if __name__ == "__main__":
    result = nxapi_show_version()
    print(result)
