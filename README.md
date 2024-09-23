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

#### ❓️ How to use the project

<br>
@2024, Insper. 9° Semester,  Computer Engineering.
<br>

_Machine Learning Ops & Interviews Discipline_