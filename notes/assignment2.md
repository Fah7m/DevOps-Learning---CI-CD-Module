Objective
---
To have some terraform code with errors, then to create a workflow file so that whenever it is pushed, the terraform code should be linted with because of the workflow created.

E.g. it should fail because of the errors you have in place in the terraform code and show where this has failed.

The code
---
```
name: Terraform Deploy

on: [workflow_dispatch]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Terraform
      uses: hashicorp/setup-terraform@v1

      with:
          terraform_version: 1.13.3

    - name: Terraform Init
      run: terraform init
      working-directory: ./tfcode

    - name: install tflint
      run: |
          curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
      working-directory: ./tfcode

    - name: run tflint
      run: tflint
      working-directory: ./tfcode

    - name: notify deployment success
      run: echo "Terraform linting completed successfully."
      if: success()
```

Here I built a pipeline which checks the terraform code in the directory, sets up terraform on the runner (VM), initializes terraform, installs tflint, then runs tflint and returns a message.

The tflint will check against the ./tfcode directory which is where the terraform files are stored.

I could also add 2 steps before running tflint to make sure the terraform will work 100% and these are 

Terraform fmt and Terraform Validate. The reason for this is 

```
| Tool                       | What it checks                          | Why it should come first/last                                             |
| -------------------------- | --------------------------------------- | ------------------------------------------------------------------------- |
| **`terraform fmt -check`** | Code **style / formatting**             | Ensures Terraform files are well-formed textually before deeper analysis. |
| **`terraform validate`**   | Code **structure / syntax correctness** | Ensures configuration parses correctly so TFLint doesn’t break.           |
| **`tflint`**               | **Best-practices and logic linting**    | Relies on code being both formatted and syntactically valid.              |
```

Result after running the pipeline
```
<img width="1009" height="683" alt="image" src="https://github.com/user-attachments/assets/f4b088d4-c7f0-4498-a96f-8cfbf5b1697c" />

Here we can see where the terraform code errors are and where it has failed as expected.
