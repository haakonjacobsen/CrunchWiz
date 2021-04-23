/* eslint react/prop-types: 0 */
import React from 'react';
import './Stickman.css';
import './MeasurementExpansion.css';
import {
  BarChart, Bar, XAxis, YAxis, Legend, Tooltip, ResponsiveContainer,
} from 'recharts';

export default function BarGraph({ dataStats, stat }) {
  return (
    <div className="Extended-graph">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          width={150}
          height={40}
          data={dataStats}
          margin={{
            top: 5, right: 20, bottom: 5, left: 0,
          }}
        >
          <Tooltip />
          <Legend />
          <Bar dataKey={stat} fill="#8884d8" />
          <XAxis dataKey="name" />
          <YAxis />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
