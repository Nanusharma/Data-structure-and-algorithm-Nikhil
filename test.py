from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Download all output files to the current directory
api.kernels_output('nikhil029/s5e2-backpackprediction-challange', path='.')
