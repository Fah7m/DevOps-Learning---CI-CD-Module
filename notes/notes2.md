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
