# A Simple Currency Converter

This project is a simple webs-scrapping Python-based Currency Converter (over 30 currencies).

Its UI uses `tkinter` library for the UI as displayed below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/59763234/103484755-8c39fe00-4df1-11eb-8bb6-aedf64f6caa6.png" />
</p>

The FX is cached until the next request exceeds one day. It is then fectched using webscraping on this website:
https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml

## Project structure

The App uses MVC architecture to improve readability, with driver found in `main.py`.
The Model, found in `model.py` computes the underlying currency conversions.
The View, found in `view.py` displays the results in a simple UI for Users.
The Controller, found in `controller.py` controls the intereaction between the Model and View.

## Testing

Basic Unit testing using `mock` library for the caching of webscraping is used.

## Deployment

In order to facilate managing the dependencies of this project, a Dockerfile has been built to build an image and run a Docker container for using the Currency Converter.

In order to deploy the Currency Converter, you must

- Pull the project and `cd` into the project folder.
- Run `docker build -t currency_converter .`, which builds the Docker image with all dependencies. We used a `python:3.9`, since a `python:3.9-slim-buster` does not have the required `tkinter` UI library that this project heavily uses.
- Run `docker run -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw currency_converter` in order to run this on your local Unix machine. This runs the Docker container using the display of your Unix machine.

## Notable Dependencies

Python=3.9

For Webscrapping, we used:

- `requests`
- `bs4`

For testing, we used

- `unittest` (with Mocks)
