import React, { useState, useEffect, useRef } from 'react';
import logo from '../logo.svg';
import './App.css';

const App = () => {
  const [state, setState] = useState(null);
  const webSocket = useRef();

  const receiveMessage = (message) => {
    // Eventually we will have multiple states which we assign to,
    // For example state for each sensor
    setState(JSON.parse(message.data));
  };

  useEffect(() => {
    webSocket.current = new WebSocket('ws://127.0.0.1:8888/');
    webSocket.current.onmessage = (message) => receiveMessage(message);
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
        <p>
          Reading from websocket:
        </p>
        <p>
          {state && state[0] && `Data from the ${state[0].device}:${state[0].data_frame[0]}`}
        </p>
      </header>
    </div>
  );
};

export default App;
