# Simple API for GCP

This repo outlines a simple toy-example of an API built with Flask in Python, containerized with Docker, and deployed to Google Cloud Platform (GCP).

Read the relevant article [here](https://medium.com/@jamescalam).

## Deploy

To create a docker image, navigate to this directory in a CLI and type:

```
docker build -t tut-api .
```

Next, deploy to GCP with:

```
gcloud builds submit --tag gcr.io/[PROJECT-ID]/tut-api
```

Finally, create a [Cloud Run service](https://console.cloud.google.com/run) using the new container.