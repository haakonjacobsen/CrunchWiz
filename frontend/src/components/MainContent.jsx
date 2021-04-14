import React, { useState, useEffect, useRef } from 'react';
import ConnectingPanel from './ConnectingPanel';
import './MainContent.css';
import Measurement from './Measurement';
import MeasurmentExpansion from './MeasurementExpansion';
import LoadingMeasurements from './LoadingMeasurements';

const MainContent = () => {
  const renderCount = useRef(1);
  const webSocket = useRef(null);
  const [connectioError, setError] = useState('');
  const [ip, setIP] = useState(null);
  const [wsStatus, setStatus] = useState(3);
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [allData, addMoreData] = useState({});
  const [loading, toggleLoading] = useState(false);

  function isValidIpv4Addr(ipAddress) {
    return /^(?=\d+\.\d+\.\d+\.\d+$)(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}$/.test(ipAddress);
  }

  function connectWebsocket(ipAddr, port) {
    if (isValidIpv4Addr(ipAddr) && parseInt(port, 10) >= 0 <= 65535) {
      toggleLoading(!loading);
      setIP(`${ipAddr}:${port}`);
    } else {
      setError(`${ipAddr}:${port} is not a valid IPv4 address`);
      console.log(`${ipAddr}:${port} is not a valid IPv4 address`);
    }
  }

  function handleAdd(measurement, newValue) {
    // Check if measurement already exist in allData, adds to array if true, creates new if false
    addMoreData((prevState) => (Object.prototype.hasOwnProperty.call(prevState, measurement) ? {
      ...prevState,
      [measurement]: [...prevState[measurement], newValue],
    } : {
      ...prevState,
      [measurement]: [newValue],
    }));
  }

  function handleOpen() {
    setStatus(1);
    toggleLoading(!loading);
  }

  function handleError() {
    setError('Websocket error, try again');
    console.log('ERROR WHEN TRYINT OT CONNECT TO ', ip);
    toggleLoading(false);
    setIP(null);
  }
  function toggleExtended(measurment) {
    if (measurment === selectedMeasurment) {
      changeExtended(!showExtended);
    } else {
      setMeasurment(measurment);
      if (!showExtended) {
        changeExtended(!showExtended);
      }
    }
  }

  const receiveMessage = (message) => {
    const measurement = JSON.parse(message.data)[0];
    const dataPoint = { value: measurement.value.toFixed(2), time: measurement.time };
    handleAdd(measurement.name, dataPoint);
  };

  useEffect(() => {
    renderCount.current += 1;
  });

  useEffect(() => {
    if (ip !== null) {
      webSocket.current = new WebSocket(`ws://${ip}/`);
      webSocket.current.onmessage = (message) => receiveMessage(message);
      webSocket.current.onopen = () => handleOpen();
      webSocket.current.onclose = () => setStatus(3);
      webSocket.current.onerror = () => handleError();
      return () => webSocket.current.close();
    } return () => null;
  }, [ip]);

  return (
    <div className="Main-content">
      <h1>{renderCount.current}</h1>
      { wsStatus === 3 && Object.keys(allData).length === 0
        ? (
          <ConnectingPanel
            connectWebsocket={connectWebsocket}
            errorMsg={connectioError}
            isLoading={loading}
          />
        )
        : null}
      {showExtended
        ? <MeasurmentExpansion name={selectedMeasurment} graphData={allData[selectedMeasurment]} />
        : null}
      { wsStatus === 1 && Object.keys(allData).length === 0
        ? <LoadingMeasurements />
        : (
          <div className="Measurements-info">
            { Object.keys(allData).length === 0 && wsStatus === 1
              ? <LoadingMeasurements />
              : Object.keys(allData).map((name) => (
                <Measurement
                  name={name}
                  number={allData[name][allData[name].length - 1].value}
                  showExtended={toggleExtended}
                  key={name}
                />
              ))}
          </div>
        )}
    </div>
  );
};

export default MainContent;
