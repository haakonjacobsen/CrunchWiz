import React, { useState, useEffect, useRef } from 'react';
import ConnectingPanel from './ConnectingPanel';
import './MainContent.css';
import Measurement from './Measurement';
import MeasurmentExpansion from './MeasurementExpansion';

const MainContent = () => {
  const webSocket = useRef('');
  const [ip, setIP] = useState('0.0.0.0:0000');
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [allData, addMoreData] = useState({});

  function handleAdd(measurement, newValue) {
    // Check if measurement already exist in allData and adds to array if true, creates new if false
    addMoreData((prevState) => (Object.prototype.hasOwnProperty.call(prevState, measurement) ? {
      ...prevState,
      [measurement]: [...prevState[measurement], newValue],
    } : {
      ...prevState,
      [measurement]: [newValue],
    }));
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
  function changeIP(inputIP) {
    setIP(inputIP);
  }

  const receiveMessage = (message) => {
    const measurement = JSON.parse(message.data)[0];
    const dataPoint = { value: measurement.value.toFixed(2), time: measurement.time };
    handleAdd(measurement.name, dataPoint);
    console.log(webSocket.readyState);
  };

  useEffect(() => {
    webSocket.current = new WebSocket(`ws://${ip}/`);
    webSocket.current.onmessage = (message) => receiveMessage(message);
    return () => webSocket.current.close();
  }, [ip]);

  return (
    <div className="Main-content">
      <ConnectingPanel setIP={changeIP} />
      {showExtended
        ? (
          <MeasurmentExpansion
            name={selectedMeasurment}
            graphData={allData[selectedMeasurment]}
          />
        ) : <div> </div>}
      <div className="Measurements-info">
        {Object.keys(allData).map((key) => (
          allData[key].length > 0
            ? (
              <Measurement
                name={key}
                number={allData[key][allData[key].length - 1].value}
                showExtended={toggleExtended}
              />
            ) : null
        ))}
      </div>
    </div>
  );
};

export default MainContent;
