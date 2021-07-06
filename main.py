#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Refreshes the k8s config, obtains the id-token, and automates the following:
# curl -X POST -H "Kube-Id-Token: <token> -d payload --resolve httpserver.npspoc.com:443:169.48.64.46 <url> --cacert <sslcertfile>
# Notice that as long as the host/ip-address pair is in /etc/hosts, --resolve is not needed, and requests does not need to deal with it

import logging
import argparse
import json
import subprocess
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='https://simple-http-server-route-default.voc-sandbox-cluster-7d4bdc08e7ddc90fa89b373d95c240eb-0001.us-east.containers.appdomain.cloud', help='url is set to (default: %(default)s)')
    parser.add_argument('--sslcertfile', default='/Users/isilval/Devt/ssl-cert/CertBundle.p7b', help='sslcertfile is set to (default: %(default)s)')
    return parser.parse_args()

if __name__ == '__main__':
    config = vars(parse_args())
    logger.info(json.dumps(config))

    headers = {'Content-Type' : 'application/json'}
    response = requests.get(config['url'], headers=headers, verify=False)

    logger.info('response code: {}, message: {}'.format(str(response.status_code), response.text))
