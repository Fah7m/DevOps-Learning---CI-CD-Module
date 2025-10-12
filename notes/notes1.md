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

Use cases for Github actions:


