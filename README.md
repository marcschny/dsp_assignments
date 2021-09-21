# DSP HS2021 - Development Environment

This repository is the training and development environment for the course
'Einführung in Data Science mit Python', held in fall semester 2021.

You have two options to work in our standardized Data Science software stack
for this course. **Only what's running through A-Z in this stack will be graded.**
1. Set up your own environment using docker (recommended).
2. Use [https://jhub.cs.technik.fhnw.ch](https://jhub.cs.technik.fhnw.ch),
   image `sgi_dsp_hs2021`

For option 1, follow the instructions from beginning to end.  

For option 2, start your container on JHub and execute steps 3 & 4 (clone into
your container on JHub, directory `persistent`). Submitting assignments again
works the same way.


## Setting up the Development Environment 

Docker is a platform for developing and running applications and it's very
useful for developing Data Science codes in homogeneous environments as well.
We will use JupyterLab inside a Docker Container to be able to run code in a
standard python ml environment.

After setting this up you'll be able to connect to JupyterLab inside your
docker container on your local machine through your browser.


### 1. Install Docker on your computer

Depending on your operating system you have to install docker in different ways.  

You'll find detailed instructions here: https://docs.docker.com/get-docker


### 2. Pull the Docker image

Authenticate to the GitLab Docker registry with a personal access token, see
details
[here](https://docs.gitlab.com/ee/user/packages/container_registry/#authenticating-to-the-gitlab-container-registry).

Choose scope `read_registry` und `write_registry` to generate the access token.

```
# login to the FHNW GitLab docker registry first
$ docker login cr.gitlab.fhnw.ch -u <username> -p <token>

# now pull the image
$ docker pull cr.gitlab.fhnw.ch/ml/courses/dsp/dsp_hs2021:v20210917
```

### 3. Fork this repository

Fork this repository to your own user space by pressing the fork button on the
upper right.

Add `@michael.graber` and `@florian.schaerer` as a maintainer to your fork. If
you don't do this I won't see your submissions.


### 4. Clone your fork to your computer. 

For this you might wanna set up a ssh-key for your computer, see here:
https://docs.gitlab.com/ee/ssh/

In your fork on GitLab find the address with which you can clone your Repo.
Clone into your dsp directory (MY_DSP_DIR) using:

```
$ git clone MY_REPO_FORK
```


### 5. Start a dsp container on your machine

```
$ docker run -d \
    -p 8877:8888 \
    --user root \
    -v MY_DSP_DIR:/home/jovyan/work/ \
    --name=dsp_hs2021 \
    cr.gitlab.fhnw.ch/ml/courses/dsp/dsp_hs2021:v20210917 start.sh jupyter lab --LabApp.token=''
```

### 6. Check that your container is running

```
$ docker ps -a
```

### 7. Connect to your container through your browser

Enter `http://localhost:8877/lab` in your browser.


### 8. Restart

If you later on need to restart your container you can just run

```
$ docker start dsp_hs2021  
```


## Submitting assignments

You can now edit files in the clone of your fork on your local machine.
Whenever you want to upload something to your Repo on GitLab you need to
'commit' and 'push' it:

```
# commit MY_FILE
$ git commit MY_FILE -m 'my commit message'

# push all commits to the server
$ git push
```

**By pushing your commits to your personal fork on GitLab you will submit the
graded Assignments!**


If you want to fetch new assignments from the master repo do as follows:

```
# add original repo as remote upstream 
$ git remote add upstream git@gitlab.fhnw.ch:ml/courses/dsp/dsp_hs2021.git

# now whenever you want to merge the changes from the remote upstream repo, ie
the one you forked from, you can do:
$ git pull upstream master
```

.. and add some merge message in case you have to merge.

