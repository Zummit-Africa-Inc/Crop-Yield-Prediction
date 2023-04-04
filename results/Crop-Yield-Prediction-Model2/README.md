#### Deploying Crop Disease Model using FastAPI

This is a guide on how to deploy a `Crop Yield Prediction Model` using FastAPI in a Docker container.

##### Requirements

`Docker installed on your local machine`

##### Building the Docker image

1. Clone the repository into your local machine.

2. Navigate into the project directory.

3. cd into-`this-folder`

##### Build the Docker image using the following command:

`docker build -t crop-yield-prediction-model .`

The image should be built successfully if you see the output similar to the following:

`Successfully built e1d1007e8d2e`
`Successfully tagged crop-yield-prediction-model:latest`

##### Running the Docker container

Once the image has been built, run the container using the following command:

`docker run -p 8000:8000 crop-yield-prediction-model`

- This command will start a container with the name `crop-yield-prediction-model`, map port 8000 from the container to port 8000 on the host, and run the crop-disease-model image.

- You can now access the API at `http://localhost:8000/docs` in your browser or using an API testing tool like Postman.


##### Stopping the Docker container

- To stop the container, run the following command:

`docker stop crop-yield-prediction-model`

- To remove the container, run the following command:

`docker rm crop-yield-prediction-model`

##### Conclusion

You have successfully deployed a Crop Yield Prediction Model using FastAPI in a Docker container. 