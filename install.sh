#!/usr/bin/env bash

brew cask install chromedriver
echo 'export CHROMEDRIVER="$(which chromedriver)"' >> ~/.bash_profile
source ~/.bash_profile