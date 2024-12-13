"""Test the installation of the project.

Check that it can be run from docker
    And docker containers are running, at least for the server and trackers client

Check that the server and client are named correctly
    i.e. docker-usher_server-1 and docker-usher_tracker-1 apear in `docker ps` output

Check basic connectivity:
    1. can connect to the server
    2. server provides a "/health" endpoint

"""
import subprocess
from time import sleep

import pytest
import httpx
import docker

compose_command = ["docker-compose", "-f", "docker/docker-compose.yml"]

@pytest.fixture(scope='module')
def docker_setup():
    """Setup Docker containers for the tests."""
    client = docker.from_env()
    subprocess.run(compose_command + ["up", "-d"], check=True)
    sleep(5)
    yield
    subprocess.run(compose_command + ["down"], check=True)

def test_installation(docker_setup):
    """Test if the project installs correctly."""
    result = subprocess.run(["pip", "install", "."], capture_output=True, text=True)
    assert result.returncode == 0, f"Installation failed: {result.stderr}"

def test_app_launch(docker_setup):
    """Test that the Docker containers for the server and client apps start without errors."""
    result = subprocess.run(compose_command + ["ps"], capture_output=True, text=True)
    assert "running" in result.stdout, f"No containers are 'running'\n{result.stdout}"

def test_server_naming(docker_setup):
    """Test that the server and client are named correctly in the Docker setup."""
    client = docker.from_env()
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    assert "docker-usher_server-1" in container_names, f"server is not running: {container_names}"

def test_trackers_naming(docker_setup):
    """Test that the server and client are named correctly in the Docker setup."""
    client = docker.from_env()
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    assert "docker-usher_tracker-1" in container_names, f"tracker is not running: {container_names}"

def test_basic_connectivity(docker_setup):
    """Test that a client can connect to the server once both are running."""
    response = httpx.get("http://localhost:8000/health")
    assert response.status_code == 200, f"Client could not connect to the server. Status: {response.status_code}"

def test_health_check_endpoint(docker_setup):
    """Test the /health endpoint on the server to confirm the service is running."""
    response = httpx.get("http://localhost:8000/health")
    assert response.status_code == 200, f"Health check failed: {response.text}"
    assert response.json() == {"status": "ok"}, "Health check response is incorrect."
