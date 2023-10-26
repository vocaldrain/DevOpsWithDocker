import os
import sys
import subprocess

# Check if the required number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python build_and_push_docker.py <GitHub_Repo_URL> <Docker_Hub_Repo>")
    sys.exit(1)

# Extract command-line arguments
github_repo_url = sys.argv[1]
docker_hub_repo = sys.argv[2]

# Clone the GitHub repository
repo_name = github_repo_url.split("/")[-1].split(".")[0]
os.system(f"git clone {github_repo_url}")
os.chdir(repo_name)

# Build the Docker image
os.system(f"docker build -t {docker_hub_repo} .")

# Log in to Docker Hub (you need to have Docker credentials configured)
os.system("docker login")

# Push the Docker image to Docker Hub
os.system(f"docker push {docker_hub_repo}")

# Clean up - remove the local repository and image
os.chdir("..")
os.system(f"rm -rf {repo_name}")
os.system(f"docker rmi {docker_hub_repo}")

print("Docker image build and push completed.")
