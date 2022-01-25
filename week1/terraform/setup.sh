#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="${PWD}/dtc-de-course-339320-4474c4eed421.json"

# Refresh token, and verify authentication
gcloud auth application-default login