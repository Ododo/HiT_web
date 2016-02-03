from docker import Client


DAEMON_BASE_URL='unix://var/run/docker.sock'
DAEMON_VERSION='1.18'


client = Client(base_url=DAEMON_BASE_URL,
                version=DAEMON_VERSION
				)


def create_docker(image):
	container = client.create_container(image=image, detach=True)
	client.start(container)
	return container['Id']

def get_docker_ip(docker_id):
    return client.inspect_container(docker_id)['NetworkSettings']['IPAddress']

def stop_docker(docker_id):
    client.stop(docker_id)
