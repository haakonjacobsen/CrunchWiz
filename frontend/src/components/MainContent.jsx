import React, { useState, useEffect, useRef } from 'react';
import './MainContent.css';
import Measurement from './Measurement';
import MeasurmentExpansion from './MeasurementExpansion';

const MainContent = () => {
  const webSocket = useRef('');
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [graphData, addGraphData] = useState([]);
  const [allData, addMoreData] = useState({});

  const receiveMessage = (message) => {
    const measurement = JSON.parse(message.data)[0];
    const dataPoint = { value: measurement.value, time: measurement.time };
    addGraphData((currGraphData) => [...currGraphData, dataPoint]);
    const { name } = measurement;
    if (name in allData) {
      const value = [measurement.value];
      addMoreData((prevState) => ({
        ...prevState,
        [name]: [...[prevState.name], value],
      }));
    } else {
      const value = [measurement.value];
      addMoreData((prevState) => ({
        ...prevState,
        [name]: [value],
      }));
    }
    /*
    if (name in allData) {
      const { value } = allData[name].concat([[measurement.value, measurement.time]]);
      addMoreData({
        ...allData,
        [name]:
        value,
      });
    } else {
      const { value } = [measurement.value, measurement.time];
      addMoreData({ ...allData, [name]: [value] });
    }
    */
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
