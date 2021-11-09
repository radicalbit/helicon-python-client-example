import time

from helicon_publish.helicon_publish_client import HeliconPublishClient

authorization_server = "<authorization-server>"
grpc_host = "<grpc-host>"
grpc_port = 0  # "<grpc-port-as-int>"
client_id = "<client-id>"
client_secret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream-name>"

if __name__ == '__main__':
    helicon_client = HeliconPublishClient(authorization_server=authorization_server, server_host=grpc_host,
                                          server_port=grpc_port, client_id=client_id, client_secret=client_secret,
                                          tenant_name=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    helicon_client.write(stream_name, payload)

    helicon_client.close()
