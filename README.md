# LegalEase

The goal of this project/application is to use RAG (Retrieval Augmented Generation), fine tuning and synthetic data generation to help anyone get a better understanding of the differenty property/zoning/housing laws for the town/city of the state that someone may reside in. Whether the individual is renting or the owner of a property, it can get really complicated really quickly to understand what laws/ordinances or other codes that you have to follow in your municipality. The state of New Jersey is a great example of an abundance of legal data to comb through for this subject, as there are 500+ municipalities. 

## NJ Municipalities
![All Municipalities in NJ](/images/NJ_Municipality_Map.jpg)

## All Tasks for this Project
- [x] Set up RestAPI for project (FastAPI)
- [ ] Implement RAG into chosen RestAPI
- [ ] FastAPI, add code for accessing chroma and use logging to save the user query/input (log the query and the response to the query)
- [ ] Need this application to take in user input, provide a response
- [ ] Have applicaiton then have this create a "job", have a field to keep track of status of jobs (Jobs Created, Jobs In-Process, Jobs Complete, etc.)
- [ ] Create a script that will load information into vectordb, in order for RAG to work (Chroma needs to be loaded)
- [ ] Ensure API uses langchain / chroma in response to user inputs/prompts
- [ ] Two programs towards end of project/application (Program 1 is API, Program 2 is loading Chroma)
- [ ] Get Anything LLM running online (Use GCP???)
- [ ] Connect Hugging Face (caht models) with  Anything LLM running online (Use GCP???)
- [ ] Get FastAPI running with Anything LLM
- [ ] Download town ordnances in PDF files, load into Anything LLM

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). (NO TAGS YET)

## Authors

* **Chris Keddell** - *Initial work* - [chris-k-njit](https://github.com/chris-k-njit)

* **Mark S.** - *Initial work* - [markszcz](https://github.com/markszcz)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. (NONE AT THIS TIME, ADD ON IN FUTURE)

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thanks to <a href="https://mapsontheweb.zoom-maps.com/post/127873974472/new-jersey-municipalities-by-type-by">Maps on the Web, for NJ Municipalities by Type map.</a>
* NJ Towns with PDF files of their local ordnances.
* Inspiration
* etc
