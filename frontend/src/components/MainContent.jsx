import React, { useState, useEffect, useRef } from 'react';
import ConnectingPanel from './ConnectingPanel';
import './MainContent.css';
import MeasurmentExpansion from './MeasurementExpansion';
import LoadingMeasurements from './LoadingMeasurements';
import MeasurementList from './MeasurementList';

const MainContent = () => {
  // Websocket & connection
  const webSocket = useRef(null);
  const [connectionError, setError] = useState('');
  const [ip, setIP] = useState(null);
  const [wsStatus, setStatus] = useState(3);
  const [loading, toggleLoading] = useState(false);

  // Measurement data
  const [graphData, addData] = useState({});
  const [dataStats, addStats] = useState({});
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const specialMeasurements = ['Most used joints', 'Emotion', 'Anticipation', 'Mock emotion', 'Mock anticipation'];

  function isValidIpv4Addr(ipAddress) {
    return /^(?=\d+\.\d+\.\d+\.\d+$)(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}$/.test(ipAddress);
  }

  function connectWebsocket(ipAddr, port) {
    if (isValidIpv4Addr(ipAddr) && parseInt(port, 10) >= 0 <= 65535) {
      if (`${ipAddr}:${port}` === ip) {
        setIP(null);
        toggleLoading(!loading);
        setIP(`${ipAddr}:${port}`);
      } else {
        toggleLoading(!loading);
        setIP(`${ipAddr}:${port}`);
      }
    } else {
      setError(`${ipAddr}:${port} is not a valid IPv4 address`);
    }
  }

  function handleDefaultStats(measurement, value) {
    addStats((prevState) => {
      if (Object.prototype.hasOwnProperty.call(prevState, measurement)) {
        const copy = prevState[measurement];
        return {
          ...prevState,
          [measurement]: {
            Max: copy.Max < value ? value : copy.Max,
            Min: copy.Min > value ? value : copy.Min,
            Average: (copy.Average * copy.Count + value) / (copy.Count + 1),
            Count: (copy.Count + 1),
          },
        };
      }
      return {
        ...prevState,
        [measurement]: {
          Max: value, Min: value, Average: value, Count: 1,
        },
      };
    });
  }

  function handleSpecialStats(measurement, value) {
    addStats((prevState) => {
      const copy = prevState[measurement];
      if (Object.prototype.hasOwnProperty.call(prevState, measurement)) {
        if (Object.prototype.hasOwnProperty.call(copy, value)) {
          return {
            ...prevState,
            [measurement]: { ...prevState[measurement], [value]: copy[value] + 1 },
          };
        } return {
          ...prevState,
          [measurement]: { ...prevState[measurement], [value]: 1 },
        };
      }
      return {
        ...prevState,
        [measurement]: { [value]: 1 },
      };
    });
  }

  function handleAdd(measurement, newValue) {
    // Check if measurement already exist in graphData, adds to array if true, creates new if false
    addData((prevState) => (Object.prototype.hasOwnProperty.call(prevState, measurement) ? {
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
    toggleLoading(false);
    setIP(null);
    setStatus(3);
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
  function convertSnakeCase(text) {
    const copy = text.split('_').join(' ');
    return copy.charAt(0).toUpperCase() + copy.slice(1);
  }

  const receiveMessage = (message) => {
    try {
      const measurement = JSON.parse(message.data)[0];
      if (specialMeasurements.includes(convertSnakeCase(measurement.name))) {
        const dataPoint = { value: measurement.value, time: measurement.time };
        handleAdd(convertSnakeCase(measurement.name), dataPoint);
        handleSpecialStats(convertSnakeCase(measurement.name), dataPoint.value);
      } else {
        const dataPoint = {
          value: parseFloat(measurement.value.toFixed(2)),
          time: measurement.time,
        };
        handleAdd(convertSnakeCase(measurement.name), dataPoint);
        handleDefaultStats(convertSnakeCase(measurement.name), dataPoint.value);
      }
    } catch (error) {
      setError(error);
    }
  };

  useEffect(() => {
    if (ip !== null) {
      webSocket.current = new WebSocket(`ws://${ip}/`);
      webSocket.current.onmessage = (message) => receiveMessage(message);
      webSocket.current.onopen = () => handleOpen();
      webSocket.current.onclose = () => setStatus(3);
      webSocket.current.onerror = () => handleError();
      return () => webSocket.current.close();
    } console.log(Object.keys(graphData).length);
    return () => null;
  }, [ip]);

  return (
    <div className="Main-content">
      { wsStatus === 3 && Object.keys(graphData).length === 0
        ? (
          <ConnectingPanel
            connectWebsocket={connectWebsocket}
            errorMsg={connectionError}
            isLoading={loading}
          />
        )
        : null}
      {showExtended
        ? (
          <MeasurmentExpansion
            name={selectedMeasurment}
            graphData={graphData[selectedMeasurment]}
            dataStats={dataStats}
            changeExtended={changeExtended}
            number={graphData[selectedMeasurment][graphData[selectedMeasurment].length - 1].value}
            hasTextValue={specialMeasurements.includes(selectedMeasurment)}
            specialMeasurements={specialMeasurements}
            setMeasurment={setMeasurment}
          />
        )
        : null}
      { wsStatus === 1 && Object.keys(graphData).length === 0
        ? <LoadingMeasurements />
        : null}
      {wsStatus === 1 || Object.keys(graphData).length > 0
        ? (
          <MeasurementList
            graphData={graphData}
            toggleExtended={toggleExtended}
            specialMeasurements={specialMeasurements}
          />
        )
        : null}
    </div>
  );
};

export default MainContent;
