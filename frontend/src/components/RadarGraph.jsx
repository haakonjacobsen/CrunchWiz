/* eslint react/prop-types: 0 */
import React from 'react';
import './Stickman.css';
import './MeasurementExpansion.css';
import {
  Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer,
} from 'recharts';

export default function BarGraph({ dataStats, stat }) {
  return (
    <div className="Extended-graph">
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart cx="50%" cy="50%" outerRadius="80%" data={dataStats}>
          <PolarGrid />
          <PolarAngleAxis dataKey="Name" />
          <PolarRadiusAxis />
          <Radar name="Mike" dataKey={stat} stroke="#8884d8" fill="#8884d8" fillOpacity={0.5} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}
