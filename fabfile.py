from fabric.api import local, task


@task
def serve():
    local('jekyll --server')
