import subprocess
def run_helm_command(command):
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def list_helm_charts():
    return run_helm_command("helm list")

def install_helm_chart(release_name, chart_name):
    return run_helm_command(f"helm install {release_name} {chart_name}")

def delete_helm_chart(release_name):
    return run_helm_command(f"helm delete {release_name}")

print(list_helm_charts())
print(install_helm_chart('my-release', 'bitnami/nginx'))
## print(delete_helm_chart('my-release'))


