/* eslint react/prop-types: 0 */
import React from 'react';
import './MeasurementStat.css';

export default function MeasurementStat({ name, value }) {
  return (
    <div className="Measurement-stat">
      <div className="Measurement-stat-header">
        <h2>{name}</h2>
      </div>
      <div className="Measurement-stat-content">
        <h1>{value}</h1>
      </div>
    </div>
  );
}
