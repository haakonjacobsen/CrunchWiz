import React, { useState, useEffect, useRef } from 'react';
import logo from '../logo.svg';
import './App.css';

const App = () => {
  const [state, setState] = useState(null);
  const webSocket = useRef(null);

  useEffect(() => {
    webSocket.current = new WebSocket('ws://127.0.0.1:8888/');
    webSocket.current.onmessage = (e) => {
      setState(JSON.parse(e.data));
    };
    return () => webSocket.current.close();
  }, []);

  console.log(state);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit
          {' '}
          <code>src/App.js</code>
          {' '}
          and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
};

export default App;
