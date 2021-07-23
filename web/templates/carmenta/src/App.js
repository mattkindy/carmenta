import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import StartScrapingDialog from './components/StartScrapingDialog'
import CandidateList from './components/CandidateList';

// Pretend this is the "authenticated section of the app"
const App = ({ auth }) => {
  const [loggedIn, setLoggedIn] = useState(false)

  useEffect(() => {
    console.log(JSON.stringify(auth, null, -2))
  }, [auth])

  if (!auth || !loggedIn) {
    return null
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <CandidateList />
        <StartScrapingDialog />
      </header>
    </div>
  );
}

export default App;
