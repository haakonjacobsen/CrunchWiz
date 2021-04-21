/* eslint react/prop-types: 0 */
import React, { useState } from 'react';
import './MeasurementExpansion.css';
import {
  Line, LineChart,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  ReferenceLine,
} from 'recharts';
import Indicator from './Indicator';
import MeasurmentStat from './MeasurementStat';
import Stickman from './Stickman';

export default function MeasurmentExpansion({
  name, graphData, dataStats, changeExtended, number,
}) {
  const [time, setTime] = useState(5);
  return (
    <div className="Extended-panel">
      <div className="Extended-header">
        <div className="Extended-title">
          <h3>
            {name}
          </h3>
          <div className="SVG-indicator">
            <Indicator number={number} />
          </div>
        </div>
        <button type="button" className="SVG-close" onClick={() => changeExtended(false)} onKeyDown={() => changeExtended(false)}>
          <svg width="100%" height="100%" viewBox="0 0 65 65" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M38.455 32.5532L63.7647 7.24275C65.4118 5.59641 65.4118 2.9345 63.7647 1.28816C62.1184 -0.35818 59.4565 -0.35818 57.8101 1.28816L32.4996 26.5986L7.18993 1.28816C5.54281 -0.35818 2.88168 -0.35818 1.23533 1.28816C-0.411778 2.9345 -0.411778 5.59641 1.23533 7.24275L26.545 32.5532L1.23533 57.8637C-0.411778 59.51 -0.411778 62.172 1.23533 63.8183C2.05581 64.6395 3.1346 65.0521 4.21263 65.0521C5.29066 65.0521 6.36868 64.6395 7.18993 63.8183L32.4996 38.5078L57.8101 63.8183C58.6314 64.6395 59.7094 65.0521 60.7874 65.0521C61.8654 65.0521 62.9435 64.6395 63.7647 63.8183C65.4118 62.172 65.4118 59.51 63.7647 57.8637L38.455 32.5532Z" fill="#757575" />
          </svg>
        </button>
      </div>
      <div className="Extended-main">
        <div className="Extended-stats">
          { name === 'most_used_joints'
            ? <Stickman name={graphData[graphData.length - 1].value} />
            : Object.entries(dataStats).map(([key, value]) => (
              <MeasurmentStat name={key} value={value} />
            ))}
        </div>
        <div className="Extended-graph-container">
          <div className="Extended-graph-header">
            <div className="Graph-panel">
              <button type="button" className={`Graph-panel-choice Left ${time === 5 ? 'selected' : ''}`} onClick={() => setTime(5)} onKeyDown={() => setTime(5)}>1 min</button>
              <button type="button" className={`Graph-panel-choice Center ${time === 10 ? 'selected' : ''}`} onClick={() => setTime(10)} onKeyDown={() => setTime(10)}>5 min</button>
              <button type="button" className={`Graph-panel-choice Center ${time === 20 ? 'selected' : ''}`} onClick={() => setTime(20)} onKeyDown={() => setTime(20)}>10 min</button>
              <button type="button" className={`Graph-panel-choice Right ${time === 10000 ? 'selected' : ''}`} onClick={() => setTime(10000)} onKeyDown={() => setTime(10000)}>All</button>
            </div>
            <h3>Current: 100%</h3>
          </div>
          <div className="Extended-graph">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart
                width={500}
                height={200}
                data={graphData.slice(Math.max(graphData.length - time, 1))}
                margin={{
                  top: 5, right: 20, bottom: 5, left: 0,
                }}
              >
                <XAxis dataKey="time" />
                <YAxis />
                <Line isAnimationActive={false} animationEasing="ease-in-out" strokeWidth={3} type="monotone" dataKey="value" />
                <Tooltip />
                <ReferenceLine strokeWidth={3} y={1} label="Baseline" stroke="#959595" strokeDasharray="7" />
                <ReferenceLine strokeWidth={3} y={1.1} label="High" stroke="#F6C273" strokeDasharray="7" />
                <ReferenceLine strokeWidth={3} y={0.9} label="Low" stroke="#C1E4AB" strokeDasharray="7" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
