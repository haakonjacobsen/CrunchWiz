import React, { useState } from 'react';
import './ConnectingPanel.css';
import PropTypes from 'prop-types';
import IpSVG from './SVG/IpSVG';
import PortSVG from './SVG/PortSVG';
import LoadingSpinnerSVG from './SVG/LoadingSpinnerSVG';

export default function ConnectingPanel({ errorMsg, isLoading, connectWebsocket }) {
  const [ipPart, changeIP] = useState('');
  const [portPart, changePort] = useState('');

  return (
    <div className="Connecting-panel Box">
      <h1 className="Connecting-panel-title"> Connect to server </h1>
      <div className="Connecting-input">
        <div className="SVG-container">
          <IpSVG />
        </div>
        <input type="text" placeholder="IP-address" onChange={(event) => changeIP(event.target.value)} />
      </div>
      <div className="Connecting-input">
        <div className="SVG-container">
          <PortSVG />
        </div>
        <input type="text" placeholder="Port number" onChange={(event) => changePort(event.target.value)} />
      </div>
      <button className="Connect-button" type="button" onClick={() => connectWebsocket(ipPart, portPart)} onKeyDown={() => connectWebsocket(ipPart, portPart)}>
        {isLoading ? 'connecting' : 'connect'}
      </button>
      {isLoading
        ? (
          <div className="SVG-loader">
            <LoadingSpinnerSVG />
          </div>
        )
        : (
          <h1 className="Error-message">
            {' '}
            {errorMsg}
            {' '}
          </h1>
        ) }
    </div>
  );
}

ConnectingPanel.defaultProps = {
  connectWebsocket: () => {},
  errorMsg: '',
  isLoading: false,
};

ConnectingPanel.propTypes = {
  connectWebsocket: PropTypes.func,
  errorMsg: PropTypes.string,
  isLoading: PropTypes.bool,
};
