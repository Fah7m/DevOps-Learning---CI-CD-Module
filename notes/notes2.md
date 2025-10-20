Matrix build and parallel testing
---

Here I have created a workflow that utilizes a matrix build and parallel testing

<img width="1041" height="757" alt="image" src="https://github.com/user-attachments/assets/bf3bbb25-77bc-4c99-86b8-99c4d7539b5e" />

So first we set the trigger to push so once a push happens, it will trigger the job. 

Next is the build job, what environment it will be executed on, the steps and the strategy.

The matrix strategy will be used to loop over these python version - it will run four times in parallel for each listed python version 

We then checkout the code and setup python inside the env we run on

Then the dependencies are installed for python - we tell it we are using bash by first adding a pipe then the commands followed by it e.g.

```
run: |
    cd chap4 - which is the folder of where the code is
    python -m pip install --upgrade pip - here is where the dependencies are then installed
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

Next we run tests against the code using pythos built in unittest framework to discover and run all tests automatically inside the chap4 folder and if any test fails the step  and job will fail 

Lastly we have the notify sucesss message which includes the python version. If all previous teps succeed then the message will dsplay.


**Errors that came back from git actions:**

First was to do with my workflow file not having correct indentation - I used the yaml extension in VScode to help with it

It first didn't allow for python version 3.10 to not be tested against and took it as 3.1 instead of 3.10 - fix was to remove it. yaml tested 3.10 as a float which means it thought it was 3.1, fix for this was to put it in quotations

```
matrix:
  python-version: ['3.8','3.9','3.10','3.11']
```

Next 3.7 was End of Life and remode from the default ubuntu-latest toolcache - either use a self hosted runner with 3.7 preinstalled or stick with 3.8


Secrets
---
Secrets are sensitive pieces of information such as API keys , passwords, or any credentials that you don't want to expose in the codebase. 

To use a secret in your workflow file you first need to

1. Go into your github repo and click on settings
<img width="484" height="98" alt="image" src="https://github.com/user-attachments/assets/37afffb9-58c3-4959-b300-ee2355209563" />

2. From there you go on the left panel and click on Secrets then actions
<img width="176" height="95" alt="image" src="https://github.com/user-attachments/assets/9fa6e931-184a-43d4-b0c1-ee367496a46a" />

3. Next you click on new repo secret and give a name and value

<img width="989" height="507" alt="image" src="https://github.com/user-attachments/assets/fc583ca3-8d37-4dd6-9c03-8c56a56649a4" />

4. From there in your workflow file you would reference it as the below
<img width="795" height="314" alt="image" src="https://github.com/user-attachments/assets/2c14f303-2ea3-41ed-a817-d5ced5251b6f" />
**So i set the name to my secret**

5. Finally when it's pushed, you will see the secret hidden
<img width="415" height="116" alt="image" src="https://github.com/user-attachments/assets/3cf3271f-7b26-488d-aecf-fe0efa5e1d02" />



Automated Testing and Linting 
---
Linting is the process of analysing code for potential errors and enforcing coding standards - basically like having a spell checker for your code making sure there are no syntax errors etc.

Benefits of this would be catching syntax errors and maintain code quality 

Tools for this would be ESLint for Java and PyLint for python.

Automated testing is running tests automatically on your codebase to ensure it works as expected 

Benefits of this would be you can catch issues early and ensure the code quality. By consistantly running tests, you can ensure the code is up to standard. 

Tools for this for Junit for Java and unittest as we used previously for python.

