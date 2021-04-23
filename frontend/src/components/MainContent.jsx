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
  const [loading, toggleLoading] = useState(false);
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [graphData, addMoreData] = useState({});
  const [dataStats, addStats] = useState({});
  const specialMeasurements = ['most_used_joints', 'emotion', 'anticipation'];

  function isValidIpv4Addr(ipAddress) {
    return /^(?=\d+\.\d+\.\d+\.\d+$)(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}$/.test(ipAddress);
  }

  function connectWebsocket(ipAddr, port) {
    if (isValidIpv4Addr(ipAddr) && parseInt(port, 10) >= 0 <= 65535) {
      if (`${ipAddr}:${port}` === ip) {
        setIP(null);
        toggleLoading(!loading);
        console.log(ip);
      } else {
        toggleLoading(!loading);
        setIP(`${ipAddr}:${port}`);
      }
    } else {
      setError(`${ipAddr}:${port} is not a valid IPv4 address`);
      console.log(`${ipAddr}:${port} is not a valid IPv4 address`);
    }
  }

  function handleDefaultStats(measurement, value) {
    addStats((prevState) => {
      if (Object.prototype.hasOwnProperty.call(prevState, measurement)) {
        const copy = prevState[measurement];
        if (copy.max < value) {
          copy.max = value;
        } else if (copy.min > value) {
          copy.min = value;
        }
        copy.avg = value;
        return {
          ...prevState,
          [measurement]: {
            max: copy.max, min: copy.min, avg: copy.avg,
          },
        };
      }
      return {
        ...prevState,
        [measurement]: {
          max: value, min: value, avg: value,
        },
      };
    });
  }

  function handleJointStats(measurement, value) {
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

  function handleStats(measurment, value) {
    switch (measurment) {
      case 'most_used_joints':
        console.log(measurment, value);
        handleJointStats(measurment, value);
        break;
      case 'emotion':
        console.log(measurment);
        handleJointStats(measurment, value);
        break;
      default:
        handleDefaultStats(measurment, value);
    }
  }

  function handleAdd(measurement, newValue) {
    // Check if measurement already exist in graphData, adds to array if true, creates new if false
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

  const receiveMessage = (message) => {
    try {
      const measurement = JSON.parse(message.data)[0];
      if (specialMeasurements.includes(measurement.name)) {
        const dataPoint = { value: measurement.value, time: measurement.time };
        handleAdd(measurement.name, dataPoint);
        handleStats(measurement.name, dataPoint.value);
      } else {
        const dataPoint = {
          value: parseFloat(measurement.value.toFixed(2)),
          time: measurement.time,
        };
        handleAdd(measurement.name, dataPoint);
        handleStats(measurement.name, dataPoint.value);
      }
    } catch (error) {
      console.log(error);
      setError(error);
    }
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
      { wsStatus === 3 && Object.keys(graphData).length === 0
        ? (
          <ConnectingPanel
            connectWebsocket={connectWebsocket}
            errorMsg={connectioError}
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
          />
        )
        : null}
      { wsStatus === 1 && Object.keys(graphData).length === 0
        ? <LoadingMeasurements />
        : (
          <div className="Measurements-info">
            { Object.keys(graphData).length === 0 && wsStatus === 1
              ? <LoadingMeasurements />
              : Object.keys(graphData).map((name) => (
                <Measurement
                  name={name}
                  number={graphData[name][graphData[name].length - 1].value}
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
