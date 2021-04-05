import React, { useState } from 'react';
import './ConnectingPanel.css';
import PropTypes from 'prop-types';

export default function ConnectingPanel({ setIP }) {
  const [ipPart, changeIP] = useState('0.0.0.0');
  const [portPart, changePort] = useState('1111');

  return (
    <div className="Connecting-panel">
      <h1 className="Connecting-panel-title"> Write the server IP: </h1>
      <div className="Connecting-panel-inputs">
        <input className="IP-input" type="text" placeholder="127.0.0.1" onChange={(event) => changeIP(event.target.value)} />
        <input className="Port-input" type="text" placeholder="8888" onChange={(event) => changePort(event.target.value)} />
        <button className="Connect-button" type="button" onClick={() => setIP(`${ipPart}:${portPart}`)} onKeyDown={() => setIP}> Connect </button>
      </div>
    </div>
  );
}

ConnectingPanel.defaultProps = {
  setIP: () => {},
};

ConnectingPanel.propTypes = {
  setIP: PropTypes.func,
};
