### 💡️ Continuous Integration and Continuous Delivery (CI/CD)

**CI/CD** represents a modern approach to agile software development. It encompasses a set of practices and tools aimed at releasing applications more frequently and efficiently, while maintaining high quality and minimizing risks.

> By embracing **CI/CD**, organizations can streamline their development processes, enabling faster and more frequent releases while ensuring stringent quality control measures.
> 
<br>

<div align="center">
    <img src="ci-cd-flow-desktop.png" width="700">
</div>

<br>

<li> <b>CI (Continuous Integration)</b>

<br>Regularly consolidates code changes back into a shared branch, often on a daily basis. The changes are consolidated and then validated through automated application builds. Multiple automated tests, typically including unit and integration tests, are performed to ensure that the changes do not introduce any issues or break the application.
<br>

<li> <b>CD (Continuous Delivery)</b>

<br>Continuous Delivery builds on Continuous Integration by automating the release process for builds that pass validation. With Continuous Delivery, code changes can be released to production with the click of a button after passing automated tests.

   -  Automated release process that can deploy code to production environments
   - Shortens the release cycle and provides faster feedback
   - Allows for more incremental updates rather than big bang releases
   - Releases still require manual approval before going live

</li>

<li> <b> Continuous Deployment </b>

Continuous Deployment takes automation one step further than Continuous Delivery. With Continuous Deployment, validated code changes are automatically released to production without any manual intervention.

  - Fully automated process from commit to production with no manual steps
  - New changes are immediately tested and deployed if they pass
  - Enables much faster release cycles
  - Requires comprehensive test automation and continuous monitoring
  - Well suited for web services and cloud infrastructure
  - Not suitable for every application - depends on comfort level

<br>

> In this project we will use **Github Actions**.  


#### 📌 Dependencies

Create a `venv` and install dependencies:

```bash
    # Create environment
    $ python3 -m venv venv  

    # Activate environment
    $ source venv/bin/activate

    # Install dependencies
    $ pip install -r requirements.txt
``` 

Configure the secrets in your repository : go to the repository site on `github / settings / Secrets and variables / Actions` and add a **new repository secrets**.

Set all the secrests :

* `AWS_ACCESS_KEY_ID`
  
* `AWS_SECRET_ACCESS_KEY`
  
* `AWS_REGION`
  
* `AWS_LAMBDA_ROLE_ARN`

Also create a `.env` file with the following:

```bash
    # .env content'
    AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXX"
    AWS_SECRET_ACCESS_KEY="aaaaaaaaaaaaaaaaaaaaaaaaaaa"
    AWS_REGION="xx-xxxx-2"
    AWS_LAMBDA_ROLE_ARN="arn:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
``` 

#### ❓️ How to use the project

File `pytest.ini` (at root) enable module importing during test running.

Check locally if the test are passing:

```bash
    # In root of the project
    pytest
```

In **Github Actions** the actions to be performed are stored in the `.github/workflows`  folder in the repository root and are represented in YAML format.

Explain the .yaml file example:

```yaml
# Provide a description for the workflow with:
name: An example of an automatic testing action

# We set the action to be run whenever there is a push on the main branch when doing:
on:
push:
    branches:
    - main

# To define a job, which is a group of steps that are executed together as part of a workflow run, we do:
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      # To bring code from the repository into the container:
      - name: Checkout code
        uses: actions/checkout@v4

      # To set up Python:
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      # To install dependencies
      - name: Install dependencies
        run: pip install -r requirements.txt

      # To run tests:
      - name: Run tests
        run: pytest

  # Define how the function will be deploy in AWS
  deploy-to-aws:
      needs: build-and-test      # If this job fail will be no deploy
      runs-on: ubuntu-latest
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        AWS_REGION: ${{ secrets.AWS_REGION }}
        AWS_LAMBDA_ROLE_ARN: ${{ secrets.AWS_LAMBDA_ROLE_ARN }}
      steps:
        # --- Omited Code ---- 
        # (Same as in build-and-test job)

```

This configuration file make that every time we push something in this repository the workflow runs and the code will be deployed.

<br>
@2024, Insper. 9° Semester,  Computer Engineering.
<br>

_Machine Learning Ops & Interviews Discipline_