# Municipal Ordinance Parsing

The goal of this project/application is to use RAG (Retrieval Augmented Generation), fine tuning and synthetic data generation to help anyone get a better understanding of the differenty ordinances for the municapality of the state that someone may reside in. It can get really complicated really quickly to understand what laws/ordinances or other codes that you have to follow in your municipality. The state of New Jersey is a great example of an abundance of legal data to comb through for this subject, as there are 500+ municipalities. 

<!-- (OLD) Midterm Video Submission:
* [Google Drive Link](https://drive.google.com/file/d/1YeIE871AmlUrumjTLenjm5BhkbxfvnD0/view?usp=sharing) - Video on Google Drive -->

## FINAL Video Submission:
* [Google Drive Link](https://drive.google.com/file/d/116LXVV1bYZ5XvWzsYO8eTaY_xLvcLZzX/view?usp=sharing) - Video on Google Drive
* NOTE: Screenshot with cURL was deleted as I would prefer the whole internet does not have too much info about my personal computer.

## FINAL Slideshow Presentation:
* [Google Drive Link](https://docs.google.com/presentation/d/1qBrrGaCCcrH6fV1ryy_E_1bE-kUHIObyHj60FC2jhj4/edit?usp=sharing) - Google Slides on Google Drive

## NJ Municipalities
![All Municipalities in NJ](/images/NJ_Municipality_Map.jpg)

## All Tasks for this Project
- [x] Set up RestAPI for project (FastAPI)
- [x] Implement RAG into chosen RestAPI
- [x] Need this application to take in user input, provide a response
- [x] Create a script that will load information into vectordb, in order for RAG to work (Chroma needs to be loaded)
- [x] Get Anything LLM running online (Use GCP???)
- [x] Get FastAPI running with Anything LLM
- [x] Download town ordnances in PDF files, load into Anything LLM

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
* Python (FastAPI, Pandas, others)
* AnythingLLM, Hugging Face (Free LLMs)
* GCP

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). (NO TAGS YET)

## Authors
* **Chris Keddell** - *Initial work* - [chris-k-njit](https://github.com/chris-k-njit)
* **Mark S.** - *Initial work* - [markszcz](https://github.com/markszcz)

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* Thanks to <a href="https://mapsontheweb.zoom-maps.com/post/127873974472/new-jersey-municipalities-by-type-by">Maps on the Web, for NJ Municipalities by Type map.</a>
* NJ Towns with PDF files of their local ordnances.
* Inspiration
* etc

## Enhancements
* Adjusting or adding new features in 2025