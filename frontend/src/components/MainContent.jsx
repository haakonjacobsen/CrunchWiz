import React, { useState, useEffect, useRef } from 'react';
import './MainContent.css';
import Measurement from './Measurement';
import MeasurmentExpansion from './MeasurementExpansion';

const MainContent = () => {
  const data = [{ name: 'No Measurment', number: 0 }];
  const webSocket = useRef('');
  const [state, setState] = useState(data);
  const [showExtended, changeExtended] = useState(false);
  const [selectedMeasurment, setMeasurment] = useState('');
  const [graphData, addGraphData] = useState([]);

  const receiveMessage = (message) => {
    const object = JSON.parse(message.data);
    setState(object);
    const dataPoint = object[Object.keys(object)[2]];
    addGraphData((currGraphData) => [...currGraphData, dataPoint]);
    console.log(dataPoint);
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
            graphData={graphData.length > 5
              ? graphData.slice(Math.max(graphData.length - 5, 1)) : graphData}
          />
        ) : <div> </div>}
      <div className="Measurements-info">
        {state.map((measurment) => (
          <Measurement
            name={measurment.name}
            number={measurment.number}
            showExtended={toggleExtended}
          />
        ))}
      </div>
    </div>
  );
};

export default MainContent;
