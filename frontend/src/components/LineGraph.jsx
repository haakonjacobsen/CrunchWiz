/* eslint react/prop-types: 0 */
import React from 'react';
import './Stickman.css';
import './MeasurementExpansion.css';
import {
  Line, LineChart,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  ReferenceLine,
} from 'recharts';

export default function LineGraph({ graphData, time }) {
  return (
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
  );
}
