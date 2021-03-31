import React, { useState, useEffect, useRef } from 'react';
import './MainContent.css';
import Measurement from './Measurement';
import MeasurmentExpansion from './MeasurementExpansion';

const MainContent = () => {
  const webSocket = useRef('');
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [graphData, addGraphData] = useState([]);
  const [allData, addMoreData] = useState({ stress: [] });

  function handleAdd(measurement, newValue) {
    addMoreData((prevState) => console.log(prevState.stress));

    addMoreData((prevState) => ({
      ...prevState,
      [measurement]: [...prevState.stress, newValue],
    }));
  }

  const receiveMessage = (message) => {
    const measurement = JSON.parse(message.data)[0];
    const dataPoint = [{ value: measurement.value, time: measurement.time }];
    addGraphData((currGraphData) => [...currGraphData, dataPoint]);
    handleAdd(measurement.name, [measurement.value, measurement.time]);
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
            graphData={graphData}
          />
        ) : <div> </div>}
      <div className="Measurements-info">
        {Object.keys(allData).map((key) => (
          <Measurement
            name={key}
            number={allData[key]}
            showExtended={toggleExtended}
          />
        ))}
      </div>
    </div>
  );
};

export default MainContent;
