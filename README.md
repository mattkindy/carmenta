# Carmenta: Goddess of Childbirth and Prophecy

## First Time Setup

Run

```
$ ./install.sh
```

This will install `chromedriver` and set up your `~/.bash_profile` to export the `CHROMEDRIVER` environment variable.

## Running

```
$ export FLASK_APP=root.py
$ flask run
 * Running on http://127.0.0.1:5000/
```
### Installing
1. make sure you have python, npm, and pip installed on your machine.
For this project, I used : **npm v4.6.1**, **pip v18.0**, **python v3.6.2**
2. Enter in to the directary *hello_template/templates/static/* and run the command `npm install`. This will download and install all the dependencies listed in *package.json*.
3. In the static directory, start the npm watcher to build the front end code with the command `npm run watch`
4. Create a python virtualenv(Optional)
5. Install flask with the command `$ pip install flask`
6. Install Reactjs with the command `$ npm i react react-dom --save-dev`
### Running
1. Go to the root directory and start the server with `python run.py`
2. If all is working correctly, you will be given an address http://127.0.0.1:5000/ which you can open in your favorite browser and see our application running and displaying “Hello React!”
