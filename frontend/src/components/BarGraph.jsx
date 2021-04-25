/* eslint react/prop-types: 0 */
import React from 'react';
import './Stickman.css';
import './MeasurementExpansion.css';
import {
  BarChart, Bar, Cell, XAxis, YAxis, Legend, Tooltip, ResponsiveContainer,
} from 'recharts';

export default function BarGraph({
  dataStats, stat, name, setMeasurment,
}) {
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
          <Bar dataKey={stat} fill="#959595" onClick={() => setMeasurment(name)}>
            {
              dataStats.map((key, index) => (
                <Cell
                  key={key}
                  fill={dataStats[index].Name === name ? '#769CFF' : '#A1A1A1'}
                />
              ))
            }
          </Bar>
          <XAxis dataKey="Name" />
          <XAxis dataKey="SelectedName" />
          <YAxis />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
