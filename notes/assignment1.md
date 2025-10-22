Assignment 1 notes
---

**The Task:**

Setup a pipeline which builds and pushesyour container image to DockerHub or ECS

**The workflow file:**

<img width="693" height="496" alt="image" src="https://github.com/user-attachments/assets/ef5c089f-e5cd-4157-a00a-69d29f66571f" />


First I had named the workflow with something it was related which in this case is Docker Build

Next I set the trigget to workflow dispatch which essentially means a manual trigger that gets activated by the push of a button on the github actions UI.

<img width="1331" height="236" alt="image" src="https://github.com/user-attachments/assets/67beb21a-1f67-490e-88c5-3a192a3a2753" />

The Job is the set to build and is set to run on ubuntu latest 

```
jobs:
  build:
    runs-on: ubuntu-latest

```

We then run a checkout code which essentially clones the repo into the environments workspace. Without this the VM would be empty and wouldn't have the neccessary files for it to run the job

```
- name: Checkout code
  uses: actions/checkout@v2
```

Now the build docker image step is run. Here we use the pipe (|) to ch into the challenege directory, run a docker build to build the docker image. The . after build says to look in the current directory for the dockerfile
and then the -t gives the image a tag.

```
- name: Build Docker image
  run: |
    cd challenge
    docker build . -t f1him/count-app:v4
```

I then push the image to docker hub utilizing the same pipe again to run multiple commands in one run step. Here I have also added my docker token to github secrets so that this build is up to security standard. Finally a 
docker push is run to push the image to docker hub.

```
- name: push image to Docker Hub
  run: |
    docker login -u f1him -p ${{ secrets.DOCKER_TOKEN }}
    docker push f1him/count-app:v4
```

The full workflow 
---

```
(You click “Run workflow”)
        ↓
GitHub spins up Ubuntu runner
        ↓
Step 1: Clones your repo (checkout)
        ↓
Step 2: Builds Docker image (cd into /challenge)
        ↓
Step 3: Logs into Docker Hub
        ↓
Step 4: Pushes image (f1him/count-app:v4)
        ↓
✅ Pipeline completes — image is on Docker Hub
```

Improvements
---

Use a latest actions for checkoutcode instead of v2

Ensure the login is secure by doing 

```
echo "${{ secrets.DOCKER_TOKEN }}" | docker login -u f1him --password-stdin
```

For faster builds add cashing (actions/cache) or docker/build-push-action@v5

