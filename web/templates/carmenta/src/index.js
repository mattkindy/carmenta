import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import rootReducer from './redux/reducers'
import thunk from 'redux-thunk';
import logger from 'redux-logger'
import reportWebVitals from './reportWebVitals';
import Passage from '@passageidentity/passage-js';

const appHandle = process.env.REACT_APP_PASSAGE_APP_HANDLE
let passage = new Passage(appHandle)

// example request
passage
  .appInfo()
  .then((appInfo) => {
    console.log("App info and authentication policy: ")
    console.log(JSON.stringify(appInfo, null, 2))
  })
  .catch(e => console.error(e))

/* eslint-disable no-underscore-dangle */
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  rootReducer,
  {},
  composeEnhancers(applyMiddleware(thunk, logger))
);

const provider = <Provider store={store}><App auth={passage} /></Provider>;

ReactDOM.render(
  <React.StrictMode>
    {provider}
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
