import json
import datetime
from urllib.request import urlopen, Request
import time
from api_keys import coinigykey, coinigysec

def delete_alerts_newer_than(coinigykey, coinigysec, newer_than, print_output=True):
    """
    Deletes all alerts created after 'newer_than'
    :param coinigykey: coinigy key
    :param coinigysec: coinigy secret
    :param newer_than: datetime object
    :return:
    """

    #get old alerts
    headers = {'Content-Type': 'application/json','X-API-KEY': coinigykey, 'X-API-SECRET': coinigysec}
    values = '{"exch_code": "BTRX"}'
    values = bytes(values, encoding='utf-8')
    request = Request('https://api.coinigy.com/api/v1/alerts', data = values, headers = headers)
    old_alerts = urlopen(request).read()
    old_alerts = old_alerts.decode("utf-8")
    old_alerts = json.loads(old_alerts)

    for alert in old_alerts['data']['open_alerts']:
        if datetime.datetime.strptime(alert['alert_added'], '%Y-%m-%d %H:%M:%S') > newer_than:
            body = '{"alert_id": ' + alert['alert_id'] + '}'
            body = bytes(body, encoding='utf-8')
            headers = {'Content-Type': 'application/json', 'X-API-KEY': coinigykey, 'X-API-SECRET': coinigysec}
            request = Request('https://api.coinigy.com/api/v1/deleteAlert', data=body, headers=headers)
            response_body = urlopen(request).read()
            if print_output:
                print(response_body)
            time.sleep(1)

if __name__ == "__main__":
    ##############VARIABLES TO SET
    from_date = datetime.datetime(year=2017, month=12, day=1, hour=23)
    ##############VARIABLES TO SET

    delete_alerts_newer_than(coinigykey, coinigysec, from_date)