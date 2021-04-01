import React, { useState, useEffect, useRef } from 'react';
import './MainContent.css';
import Measurement from './Measurement';
import MeasurmentExpansion from './MeasurementExpansion';

const MainContent = () => {
  const webSocket = useRef('');
  const allMeasurements = {};
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [allData, addMoreData] = useState(allMeasurements);

  function handleAdd(measurement, newValue) {
    addMoreData((prevState) => (Object.prototype.hasOwnProperty.call(prevState, measurement) ? {
      ...prevState,
      [measurement]: [...prevState[measurement], newValue],
    } : {
      ...prevState,
      [measurement]: [newValue],
    }));
  }

  const receiveMessage = (message) => {
    const measurement = JSON.parse(message.data)[0];
    const dataPoint = { value: measurement.value, time: measurement.time };
    handleAdd(measurement.name, dataPoint);
  };

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
  useEffect(() => {
    webSocket.current = new WebSocket('ws://127.0.0.1:8888/');
    webSocket.current.onmessage = (message) => receiveMessage(message);
    return () => webSocket.current.close();
  }, []);

  return (
    <div className="Main-content">
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
            ) : <div> </div>
        ))}
      </div>
    </div>
  );
};

export default MainContent;
