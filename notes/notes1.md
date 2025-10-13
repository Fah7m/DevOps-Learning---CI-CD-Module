CI/CD
---
This sounds for Continous integration Continous Development 

CI- This the process of integrating code changes frequently e.g. if your team are working on different features of a project and instead of waiting for everyone to finish their part and then merge everything, CI allows you to integrate changes several times a day, more than 100 times a day actualy.

This way errors can be caught and fixed early and quickly making the whole development process much smoother.

CD- This is where continous deployment is implememnted meaning every change that passes all the stages of the production pipeline is automatically released to the users. It manes no more manual deployments as this process is fully automated.

Continous Delivery is when our code is integrated, we want to ensure it's always in a deployable state. This is where Continous Delivery comes in, this part makes sure that our software can be released reliably at any time - think of it as having a releaseready version of the product after
every stage that passes all of the testing pipeline. 

In a nutshel, CD-CD helps teams work toegether more effectively and catch errors early, also release updates quicker and safely.

<img width="1872" height="429" alt="image" src="https://github.com/user-attachments/assets/26d31af3-4abb-4797-b7f9-5d1602857639" />

<img width="1888" height="517" alt="image" src="https://github.com/user-attachments/assets/47dcf937-8a2e-4f3b-aea6-040389e70967" />


Tools for CI/CD
---
GitLab CI/CD - This integrates with your code in Gitlab and it is known for being user-friendly and has strong integration with gitlabs version control system.

Jenkins - open source and most popular, also is very power as it can almost do anything with the right plugins. However it can be quite complex.

CircleCI - Cloud based CICD tool and is known for its speed and simplicity. It integrates with Github and bitbucket allow you to builed test and deploy code very easyily. Most famous for its quick setup and ease of use.

TravisCI - Similar to circleci and is another cloud based cicd 

Github Actions - integrated directly into github which is the most common and widely used version control system. 

AWS/Azure/GCO CI/CD tools - cloud providers also have their native cicd services and each of these tools have their own strengths and might be better suited for different projects or team setups.


Role of CICD
---
In DEVOPS CICD is a fundamental part and devops cannot live without CICD.

In the image below, we have contrinous integration and within it you have code, build and test. 

In the code section that basically means deveopers write the code and commit changes frequently to the version control system such as GithUb, gitlab bitbucket. 

Next in the Build part the code is automatically built ensuring it compiles correctly and all dependencies are in place. 

Next is the automated tests, these tests are run to verify that the code has been updated and does not introduced any bugs or issues.

Now on the right side we have continous deployment, the successfully tested code is then released into a staging or production environment. Then it is deployed to a live environment make it accessible to users of the application etc.

Then once the application is operating on a live environment, this is where monitoring comes in where system performance, logs and user feedback is continously monitored

<img width="868" height="359" alt="image" src="https://github.com/user-attachments/assets/7b5498d2-182f-485c-9197-d089d26a757e" />


Github actions workflow
---
Developers write the code and make changes and then commit it.

First the commited code triggers a github actions workflow. This workflow is defined in a **YAML** file and it specifies which actions to take whena  certain event like a commit occurs. Then we have the pipeline itself and the workflow enters the CI pipeline.

Next the CI/CD pipeline happens where the first step is to build the code which involves compiling the code and resolving dependencies to ensure everything is setup correctly. 

Then we have the tests which are automated. Now these are essentially verifying that the new code doesn't break anything and any exisisting functionality. This is a crucial step for maintaing code quality and if the test pasesses the workflow carries on, but if it fails
then the process stops and developers are notified to fix any issues.

Upon a successful build and test, the code is packages - this usually means that it creates a new deployment version of the application whether it's a docker image or a compiled binary. Once it's packaged it is then deployed to a test, staging, or live environment depending
on what the company usually does.

Finally the rest is standard procedure when the changes are deployed e.g. monitoring and making sure everything is sound

**Use cases for Github actions:**

It buils and tests your code every time you push changes to the repo - you have code running unit tests on every pull request and this ensure that any new code doesn't break existing functionality and maintains the quality of your code base

After code passes all tests, github actions can automatically deploy to production or any environment - this speeds up release process and reduces manual intervention. Example would be deploying a web app to a cloud service like AWS. This can be set to happen automatically after all tests are passed

Lastly, automation can handle repetitve tasks in your workflow - An example would be managing project board automation meaning moving cards or tasks between columns on a github project board based on issues or pull requests which keeps the project board up to date without manual effort


YAML
---

YAML Ain't Markup Language is the language of devops and is a human readable data serialisation standard that is often used for configuration files.

Key value pairs in yaml is straight forward. The format works as this, the key which is the variable and the value which will be the value of the variable.

```
key: value
age: 30
```

Lists in yaml work as arrays in our programming languages e.g. a fruits list will contain fruits within it by using a semi colon followed by a space to define it

```
Fruits:
- apple
- banana
- orange
```

Finally a nested element which is applied by using indententation. 

```
server:
  name: prod-server
  ip: 192.168.1.1
  credentials:
    username: admin
    password: secret
```
<img width="617" height="532" alt="image" src="https://github.com/user-attachments/assets/3d38f1d0-8eea-4436-a4e2-acfaf7c5fb06" />


Pipelines
---

The workflow structure file is broken into parts

First we have the name which is the just the name field of the file. This could be used to simple name what this file would do.

Next we have the trigger however in this case we have "on". We have a push set to it meaning any time a pull request is created then merged, it will trigger the job or a shedule. 

Next is the job that will be run and these jobs are series of tasks that run as part of the workflow. In this scenario we have a job named build and then after that we have the steps that will be executed. 

First in this section we define which environment it runs. We also have a pipeline to run in a container if need be however by default github actions uses commonly use OSs like Ubuntu.

Each step in the job are individual tasks that run in a sequence. Each step is either a command that is run or a action. Actions are reusable pieces of code that can perform a variety of tasks. 

In the first step we have a checkout code which uses a action to checkout the code from the repository. This action pulls the latest code from the repo so the subsequent steps can work with it. 

Also, the steps can be run sequentially within a job and independent tasks run in parallel or sequential too.

There is also a marketplace for github workflows that has community created actions. Some are created by github themselves and some are other orgs like AWS etc. 

<img width="901" height="436" alt="image" src="https://github.com/user-attachments/assets/48d0052c-f144-45ef-8571-82d57f061239" />

Below is another example of a workflow file

<img width="1779" height="672" alt="image" src="https://github.com/user-attachments/assets/e7ff9b1c-7320-4105-85b8-f1cbb16ecf08" />


