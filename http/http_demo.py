import base64
import http.client
import logging

from http import HTTPStatus

logging.basicConfig(level=logging.INFO)


def truncate_index(host: str, port: int, index: str, user: str = None, passwd: str = None):
    """truncate es index"""
    attempt_count = 0
    while attempt_count < 3:
        try:
            conn: http.HTTPConnection = http.client.HTTPConnection(host, port)
            headers = {'Content-Type': 'application/json'}
            if user is not None and passwd is not None:
                headers['Authorization'] = 'Basic ' + base64.encodestring(user + ':' + passwd).decode('ascii')
            conn.request(method='POST', url='/' + index + '/_delete_by_query', body=delete_body, headers=headers)
            response = conn.getresponse()
            if response.status == HTTPStatus.OK:
                logging.info('clear es index %s in server %s:%d, response: %s', index, host, port,
                             response.read().decode('utf-8'))
                break
            else:
                logging.error('clear es index failed, response code: %d, message: %s, reason: %s', response.status,
                              response.reason,
                              response.read().decode('utf-8'))
                attempt_count += 1
        except Exception as e:
            attempt_count += 1
            logging.error('clear es index %s in server %s:%d failed, response code: %s', index, host, port, e)

    else:
        logging.error('clear es index %s in server %s:%d failed, please clear it manually', index, host, port)


if __name__ == '__main__':
    # truncate_index('bjdd-igu-bce07.bjdd.baidu.com', 8200, 'schema', None, None)
    indices = ('tag', 'schemav2', 'contentv2')
    logging.info('starting clear indices %s', indices)
    print('/{index}/_delete_by_query'.format(index="aaa"))
